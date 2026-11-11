"""Ricalcola tutti i numeri del rapporto a partire dai file del repository.

Uso: python analizza.py   (dalla cartella analisi/)
"""
import csv, json, math, re, itertools
from collections import Counter
from math import comb

IDS = [f"Q{i:02d}" for i in range(1, 31)]
ASSISTENTI = ["claude", "chatgpt", "gemini"]
VALUTATORI_CIECHI = ["chatgpt_cieca", "claude_cieca", "gemini_cieca"]
TUTTI_VALUTATORI = VALUTATORI_CIECHI + ["perplexity_nominativa"]
# Unica correzione manuale: "ba)" e la numerazione inglese di "b bis)" (sezione 3.3 del rapporto)
CORREZIONI = {"Q11-A": "P"}

chiave = json.load(open("../valutazioni/chiave_anonimizzazione.json"))
dataset = {r["id"]: r for r in json.load(open("../dataset/dataset_v0.json"))}
risposte = {m: json.load(open(f"../risposte/web/{m}.json"))["answers"] for m in ASSISTENTI}
voti = {n: {r["item"]: r["voto"] for r in csv.DictReader(open(f"../valutazioni/valutatore_{n}.csv", encoding="utf-8-sig"), delimiter=";") if r.get("item")}
        for n in TUTTI_VALUTATORI}


def confidenza(testo):
    m = re.search(r"CONFIDENZA:?\s*\**\s*(\d+)", testo, re.I)
    return int(m.group(1)) if m else None


def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def auroc(pos, neg):
    if not pos or not neg:
        return float("nan")
    return sum((p > q) + 0.5 * (p == q) for p in pos for q in neg) / (len(pos) * len(neg))


def kappa(a, b):
    po = sum(a[i] == b[i] for i in chiave) / len(chiave)
    ca, cb = Counter(a[i] for i in chiave), Counter(b[i] for i in chiave)
    pe = sum(ca[k] * cb[k] for k in "CPE") / len(chiave) ** 2
    return po, (po - pe) / (1 - pe)


def mcnemar(f, a, b):
    x = sum(f[a][k] == "C" and f[b][k] != "C" for k in IDS)
    y = sum(f[a][k] != "C" and f[b][k] == "C" for k in IDS)
    n = x + y
    p = min(1.0, 2 * sum(comb(n, i) for i in range(min(x, y) + 1)) / 2 ** n) if n else 1.0
    return x, y, p


# Voto finale: maggioranza dei tre valutatori alla cieca
finale = {m: {} for m in ASSISTENTI}
for item, ass in chiave.items():
    c = Counter(voti[n][item] for n in VALUTATORI_CIECHI).most_common(1)[0]
    assert c[1] >= 2, f"nessuna maggioranza per {item}"
    finale[ass][item[:3]] = CORREZIONI.get(item, c[0])

print("Risultati (voto di maggioranza)")
for m in ASSISTENTI:
    v = [finale[m][k] for k in IDS]
    conf = [confidenza(risposte[m][k]) for k in IDS]
    y = [x == "C" for x in v]
    k = sum(y); lo, hi = wilson(k, 30)
    pos = [c for c, yi in zip(conf, y) if yi]; neg = [c for c, yi in zip(conf, y) if not yi]
    brier = sum((c / 100 - yi) ** 2 for c, yi in zip(conf, y)) / 30
    print(f"  {m:8} C={v.count('C'):2} P={v.count('P'):2} E={v.count('E')}  "
          f"corrette {k/30:.0%} [{lo:.0%}-{hi:.0%}]  confidenza media {sum(conf)/30:.1f}  "
          f"scarto {sum(conf)/30 - k/30*100:+.1f}  AUROC {auroc(pos, neg):.2f}  Brier {brier:.3f}")

omnibus = [k for k in IDS if dataset[k]["modificato_omnibus"] == "si"]
print("Domande modificate dall'Omnibus (10) / altre (20):",
      {m: (sum(finale[m][k] == "C" for k in omnibus), sum(finale[m][k] == "C" for k in IDS if k not in omnibus)) for m in ASSISTENTI})
print("Premesse false pienamente corrette:", {m: sum(finale[m][k] == "C" for k in ["Q27", "Q28", "Q29", "Q30"]) for m in ASSISTENTI})

print("McNemar (solo il primo corretto, solo il secondo corretto, p):")
for a, b in [("claude", "chatgpt"), ("chatgpt", "gemini"), ("claude", "gemini")]:
    print(f"  {a} vs {b}: {mcnemar(finale, a, b)}")

print("Voti per valutatore (C/P/E):")
for n in TUTTI_VALUTATORI:
    c = {m: Counter() for m in ASSISTENTI}
    for item, v in voti[n].items():
        c[chiave[item]][v] += 1
    print(f"  {n:22}", {m: f"{c[m]['C']}/{c[m]['P']}/{c[m]['E']}" for m in ASSISTENTI})

print("Accordo fra valutatori:")
for a, b in itertools.combinations(TUTTI_VALUTATORI, 2):
    po, k = kappa(voti[a], voti[b])
    print(f"  {a} vs {b}: accordo {po:.0%}, kappa {k:.2f}")
