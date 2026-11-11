# AI Act bench: sicuri anche quando sbagliano

Quanto ci si può fidare di un assistente AI su una domanda di conformità all'AI Act? Abbiamo posto 30 domande verificabili sul testo ufficiale a Claude, ChatGPT e Gemini nelle versioni web di default, chiedendo una risposta breve, la fonte e una confidenza da 0 a 100. Le domande riguardano l'AI Act come modificato dall'Omnibus digitale (reg. UE 2026/1744) e la legge italiana 132/2025. Le 90 risposte sono state anonimizzate, mescolate e valutate alla cieca da tre assistenti diversi.

| Assistente | Pienamente corrette | Parziali | Errate | Confidenza media dichiarata |
|:--|--:|--:|--:|--:|
| Claude | 28/30 (93%) | 2 | 0 | 88 |
| ChatGPT | 22/30 (73%) | 8 | 0 | 99 |
| Gemini | 14/30 (47%) | 16 | 0 | 99 |
| Qwen2.5 3B, locale senza ricerca web | 7/30 | 4 | 19 | — |

- ChatGPT e Gemini dichiarano 99 su 100 sia sulle risposte corrette sia su quelle incomplete. Per nessuno dei tre assistenti la confidenza indica quale risposta verificare.
- Le risposte parziali omettono soprattutto date nuove, eccezioni e soggetto obbligato, citano la norma sbagliata o descrivono il testo superato dell'articolo 4.
- Fra i valutatori automatici, ChatGPT e Claude concordano fortemente (kappa 0,76); Gemini segna come corrette quasi tutte le risposte (kappa 0,08–0,12 con gli altri).
- Con 30 domande la differenza fra Claude e ChatGPT non è statisticamente significativa (McNemar p = 0,11).

DOI: [10.5281/zenodo.24139406](https://doi.org/10.5281/zenodo.24139406)

Rapporto completo: [paper/paper.pdf](paper/paper.pdf) (sorgente [paper/paper.md](paper/paper.md)). Riepilogo in foglio di calcolo: [risultati_v0.xlsx](risultati_v0.xlsx).

## English summary

We asked Claude, ChatGPT and Gemini (default web versions, web search on) 30 questions on the EU AI Act as amended by the 2026 Digital Omnibus and on Italian AI law 132/2025, each verifiable against the official text. Graded blind by three different assistants (majority vote): Claude 28/30 fully correct, ChatGPT 22/30, Gemini 14/30; no answer was fully wrong, many were partial. ChatGPT and Gemini declared a mean confidence of 99 on correct and partial answers alike. The report is in Italian with an English abstract.

## Contenuto

| Cartella | Cosa contiene |
|:--|:--|
| `dataset/` | Le 30 domande con risposta attesa, elementi chiave, citazione letterale della norma e link alla fonte ufficiale |
| `risposte/web/` | Prompt, domande e risposte complete di Claude, ChatGPT e Gemini |
| `risposte/locali/` | Risposte dei modelli locali Qwen2.5 1.5B e 3B |
| `valutazioni/` | File anonimizzato, prompt del valutatore, voti di ogni valutatore, chiave di anonimizzazione, voti finali, revisione iniziale scartata |
| `analisi/` | `analizza.py` ricalcola ogni numero del rapporto; `run_local.py` esegue i modelli locali |
| `paper/` | Rapporto tecnico e figura |

Per ricalcolare i risultati:

```
cd analisi
python analizza.py
```

## Metodo in breve

1. Ogni domanda è posta una volta, in una conversazione nuova, con lo stesso prompt (Claude in incognito, ChatGPT in chat temporanea, Gemini in chat standard; 10-11 novembre 2026).
2. Le risposte sono ripulite di ciò che identifica l'assistente e della confidenza, etichettate A/B/C con ordine casuale per domanda.
3. ChatGPT, Claude e Gemini valutano le 90 risposte alla cieca: C corretta, P parziale, E errata. Il voto finale è di maggioranza.
4. Perplexity valuta le stesse risposte conoscendo il nome dell'assistente, come confronto.

## Limiti

Trenta domande, una sola esecuzione per assistente, impostazioni di default, valutatori automatici senza revisione giuridica. L'autore non è un giurista: le risposte attese si limitano a ciò che si legge nel testo e ognuna è verificabile sul link indicato. Lo studio è stato svolto con l'aiuto di Claude, che è anche uno degli assistenti valutati; i dettagli sono nella sezione 7 del rapporto.

## Segnalare un errore

Se una risposta attesa è sbagliata o superata, apri una issue indicando la domanda e il testo normativo. Le correzioni saranno registrate con una nuova versione del dataset.

## Autore e licenza

Giovanni Simonetti, ORCID [0009-0008-7543-6737](https://orcid.org/0009-0008-7543-6737), [LinkedIn](https://www.linkedin.com/in/giovanni-simonetti-247374211/).

Dati, risposte e rapporto: CC BY 4.0. Codice: MIT. Le risposte degli assistenti sono riportate integralmente a fini di ricerca.
