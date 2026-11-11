---
title: "Sicuri anche quando sbagliano"
subtitle: "Tre assistenti AI alla prova di 30 domande su AI Act, Omnibus digitale e legge 132/2025. Correttezza, confidenza dichiarata e affidabilità dei valutatori automatici"
author: "Giovanni Simonetti (ORCID 0009-0008-7543-6737)"
date: "Rapporto tecnico, bozza 0.1, novembre 2026"
lang: it
abstract: |
  Una piccola impresa italiana che oggi chiede a un assistente AI una regola dell'AI Act riceve una risposta, una fonte e, se la chiede, una percentuale di sicurezza. Questo rapporto misura quanto valgono le tre cose. Abbiamo posto 30 domande verificabili sul testo ufficiale (scadenze, pratiche vietate, obblighi e sanzioni, legge 132/2025, domande con premessa falsa), 10 delle quali toccano disposizioni modificate dal regolamento (UE) 2026/1744 ("Omnibus digitale"), a Claude, ChatGPT e Gemini nelle versioni web di default, con ricerca web attiva, chiedendo una risposta breve, la fonte e una confidenza da 0 a 100. Le 90 risposte sono state anonimizzate, mescolate e valutate alla cieca da tre assistenti diversi; il voto finale è quello di maggioranza. Le risposte pienamente corrette sono 28 su 30 per Claude (93%, intervallo al 95% 79–98%), 22 per ChatGPT (73%, 56–86%) e 14 per Gemini (47%, 30–64%); nessun assistente dà risposte del tutto errate, ma molte sono parziali: date nuove mancanti, eccezioni omesse, fonti sbagliate, testo superato dell'articolo 4. ChatGPT e Gemini dichiarano una confidenza media di 99 su 100 sia sulle risposte corrette sia su quelle parziali, con uno scarto rispetto alla correttezza di +26 e +52 punti; Claude dichiara in media 88, vicino al suo 93%. Per nessuno dei tre la confidenza distingue la singola risposta giusta da quella incompleta. Due modelli locali senza ricerca web rispondono correttamente a 7 domande su 30 e inventano riferimenti normativi. Fra i valutatori automatici, ChatGPT e Claude concordano fortemente (kappa 0,76) mentre Gemini segna come corretto quasi tutto (kappa 0,08–0,12 con gli altri). Il campione è piccolo e la differenza fra Claude e ChatGPT non è statisticamente significativa; dataset, risposte, voti e codice sono pubblici.
geometry: margin=2.4cm
fontsize: 10.5pt
linestretch: 1.08
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
header-includes:
  - \usepackage{booktabs}
  - \setlength{\parskip}{0.45em}
  - \setlength{\parindent}{0pt}
---

# Abstract (English)

We asked Claude, ChatGPT and Gemini (default web versions, web search on) 30 questions on the EU AI Act as amended by the 2026 Digital Omnibus (Reg. (EU) 2026/1744) and on Italian AI law 132/2025, each verifiable against the official text and requiring a short answer, a legal source and a 0–100 confidence. The 90 answers were anonymised, shuffled and graded blind by three different assistants (majority vote). Fully correct answers: Claude 28/30 (93%, 95% CI 79–98%), ChatGPT 22/30 (73%, 56–86%), Gemini 14/30 (47%, 30–64%); no answer was fully wrong, many were partial (missing new dates or exceptions, wrong sources, superseded wording). ChatGPT and Gemini declared a mean confidence of 99 on correct and partial answers alike (overconfidence of +26 and +52 points); Claude declared 88. For none of the three did confidence separate correct from incomplete answers. Two local models without web search got 7/30 right and invented legal references. Among LLM graders, ChatGPT and Claude agreed strongly (kappa 0.76) while Gemini rated almost everything correct (kappa 0.08–0.12). The sample is small and the Claude–ChatGPT difference is not statistically significant. Data, answers, grades and code are public.

# 1. Introduzione

Dal 2 febbraio 2025 un'impresa che usa l'intelligenza artificiale deve rispettare i divieti dell'articolo 5 dell'AI Act [1] e occuparsi dell'alfabetizzazione del personale. Dal 10 ottobre 2025 in Italia si aggiunge la legge 132/2025 [3], e dal 23 ottobre 2026 il decreto legislativo 179/2026 [4] assegna ad AgID e ACN i poteri sanzionatori. In mezzo, il 27 luglio 2026, è entrato in vigore il regolamento (UE) 2026/1744 [2], l'"Omnibus digitale", che ha spostato al 2 dicembre 2027 e al 2 agosto 2028 gli obblighi sui sistemi ad alto rischio, ha riscritto l'articolo 4 e ha aggiunto nuovi divieti all'articolo 5.

Una piccola impresa senza un ufficio legale, davanti a questo quadro, fa sempre più spesso la cosa più semplice: chiede a un assistente AI. Riceve una risposta ben scritta, quasi sempre con una fonte e, se la chiede, con una percentuale di sicurezza. Questo rapporto misura quanto si può fare affidamento su ciascuna delle tre cose, a novembre 2026, con gli strumenti che quella impresa userebbe davvero.

Le domande di ricerca sono tre:

- **Correttezza.** Le risposte sono giuste, complete e fondate sulla norma vigente, in particolare dove l'Omnibus ha cambiato il testo?
- **Confidenza.** La sicurezza dichiarata dall'assistente aiuta l'utente a capire quando fidarsi?
- **Valutazione.** Se si usano assistenti AI per valutare altri assistenti, i giudizi sono affidabili?

I contributi sono un dataset di 30 domande con citazione letterale della norma e link alla fonte ufficiale, le 90 risposte complete dei tre assistenti, una valutazione alla cieca con tre valutatori e la misura del loro accordo, e una prima misura della distanza fra confidenza dichiarata e correttezza su un compito normativo italiano.

# 2. Lavori correlati

**Affidabilità degli strumenti AI in ambito giuridico.** Dahl e coautori [5] hanno documentato tassi elevati di allucinazione dei modelli generalisti su domande di giurisprudenza statunitense; Magesh e coautori [6] hanno mostrato che anche strumenti di ricerca giuridica con recupero di documenti producono errori in una quota rilevante delle risposte. LegalBench [7] misura il ragionamento giuridico su compiti strutturati. Questi lavori riguardano il diritto statunitense e modelli o versioni di un momento preciso; qui il compito è la normativa europea e italiana sull'AI, appena modificata, e gli assistenti sono quelli che un utente usa dal browser.

**Confidenza e calibrazione.** Un modello è ben calibrato quando, fra le risposte date con confidenza dell'80%, circa l'80% è corretto [8]. Kadavath e coautori [9] hanno mostrato che i modelli linguistici sanno in parte riconoscere ciò che sanno; Xiong e coautori [10] hanno osservato che la confidenza espressa a parole tende a essere alta e poco informativa. Un lavoro precedente dell'autore [15] ha misurato quanto male la fiducia dei modelli piccoli separi le risposte giuste da quelle sbagliate in un compito di classificazione.

**Assistenti come valutatori.** Usare un modello linguistico come giudice è ormai una pratica diffusa [11], con distorsioni note fra cui la preferenza per le proprie risposte [12]. Per questo le risposte sono state anonimizzate e mescolate, e ogni assistente ha valutato anche le proprie senza saperlo.

# 3. Metodo

## 3.1 Le domande

Il dataset contiene 30 domande in italiano, scritte come le porrebbe il titolare di una piccola impresa, in cinque famiglie: scadenze (7), pratiche vietate (5), obblighi, classificazione del rischio e sanzioni (10), legge 132/2025 (4), domande con premessa falsa (4). Le domande con premessa falsa contengono un errore che la risposta deve correggere: una certificazione dell'alfabetizzazione che la norma non prevede, una scadenza superata dall'Omnibus, una lettera dell'articolo 5 che non esiste, un'autorità nazionale sbagliata.

Ogni domanda ha una risposta attesa, gli elementi chiave che la risposta deve contenere, la citazione letterale della disposizione e il link al testo su EUR-Lex o Normattiva. L'autore non è un giurista e il dataset non ha avuto una validazione legale indipendente: per questo sono state ammesse solo domande la cui risposta si legge nel testo, senza interpretazione, e ogni risposta attesa è verificabile da chiunque sul link indicato. Le segnalazioni di errori sono benvenute e verranno registrate pubblicamente.

## 3.2 Gli assistenti e la raccolta

Sono stati interrogati Claude (claude.ai, modalità incognito, modello di default Opus 5.5 con impegno medio), ChatGPT (chatgpt.com, chat temporanea, modello di default con impegno "Instant") e Gemini (gemini.google.com, chat standard, modello di default), tutti con la ricerca web attiva come l'utente li trova. Ogni domanda è stata posta in una conversazione nuova, il 10 novembre 2026 per Gemini e l'11 novembre 2026 per gli altri due, con lo stesso prompt:

> Rispondi come consulente a una piccola impresa italiana, in italiano, in modo breve (massimo 5 frasi). Alla fine scrivi due righe separate: FONTE: <atto e articolo su cui ti basi> e CONFIDENZA: <numero da 0 a 100, quanto sei sicuro che la risposta sia corretta>.

Ogni domanda è stata posta una sola volta per assistente. Come termine di confronto senza ricerca web, le stesse domande sono state poste a due modelli locali a pesi aperti, Qwen2.5 da 1,5 e 3 miliardi di parametri (quantizzazione Q4_K_M, llama.cpp, temperatura 0), su un PC senza scheda grafica.

## 3.3 La valutazione

Ogni risposta riceve uno di tre voti. **C (corretta)**: verdetto giusto e coerente con il testo vigente, elementi chiave presenti, fonte pertinente. **P (parziale)**: verdetto giusto ma con un elemento chiave mancante, una fonte sbagliata, affermazioni contraddittorie o la descrizione di un testo superato. **E (errata)**: verdetto sbagliato, premessa falsa accettata o norma inesistente citata.

Le 90 risposte web sono state ripulite di tutto ciò che identificava l'assistente (saluti ricorrenti, collegamenti alle fonti, note a piè di risposta) e della confidenza dichiarata, etichettate A, B e C con un ordine casuale diverso per ogni domanda, e date da valutare a ChatGPT, Claude e Gemini in conversazioni nuove, con il testo normativo di riferimento e l'istruzione di non cercare sul web. Il voto finale è quello di maggioranza; in nessun caso i tre voti sono stati tutti diversi. Una sola correzione è stata applicata a mano: una risposta penalizzata come "errata" per aver chiamato "ba)" la lettera che il testo italiano chiama "b bis)", che è la numerazione della versione inglese dello stesso regolamento, è stata riportata a "parziale" (la risposta resta contraddittoria per altri motivi). Perplexity ha valutato le stesse risposte conoscendo il nome dell'assistente; il suo giudizio è riportato come confronto e non entra nel voto finale.

I modelli locali sono stati valutati da un solo revisore con la stessa scala, segnando anche i riferimenti normativi inesistenti o non pertinenti.

## 3.4 Le misure

Per ogni assistente riportiamo la quota di risposte pienamente corrette con l'intervallo di Wilson al 95% [14], la confidenza media dichiarata e il suo scarto dalla correttezza, la capacità della confidenza di separare le risposte corrette dalle altre (area sotto la curva ROC, dove 0,5 equivale al caso) e il punteggio di Brier. Le differenze fra assistenti, che rispondono alle stesse domande, sono verificate con il test esatto di McNemar. L'accordo fra valutatori è misurato con il kappa di Cohen [13].

# 4. Risultati

## 4.1 Correttezza

| Assistente | Corrette | Parziali | Errate | % corrette (IC 95%) | Confidenza media |
|:--|--:|--:|--:|:--|--:|
| Claude | 28 | 2 | 0 | 93% (79–98%) | 88 |
| ChatGPT | 22 | 8 | 0 | 73% (56–86%) | 99 |
| Gemini | 14 | 16 | 0 | 47% (30–64%) | 99 |
| Qwen2.5 3B locale | 7 | 4 | 19 | 23% | — |
| Qwen2.5 1.5B locale | 7 | 2 | 21 | 23% | — |

Table: Risultati per assistente. Assistenti web: voto di maggioranza di tre valutatori alla cieca. Modelli locali: un revisore.

Nessuna risposta dei tre assistenti web è del tutto sbagliata, e tutti conoscono l'esistenza dell'Omnibus e le sue date principali. La differenza sta nella completezza. Le risposte parziali di Gemini omettono soprattutto elementi chiave (la nuova data di applicazione, l'eccezione per motivi medici o di sicurezza sul riconoscimento delle emozioni, l'eccezione per l'individuazione delle frodi nel merito creditizio) o fondano una risposta giusta sulla norma sbagliata: in tre casi citano il GDPR o il codice deontologico dove la regola sta nell'AI Act o nella legge 132/2025. Le due risposte parziali di Claude riguardano la data dei nuovi divieti dell'articolo 5 e il comma citato della legge 132/2025.

Claude è davanti a Gemini in modo netto (15 domande in cui solo Claude è corretto, 1 al contrario, p < 0,001), e ChatGPT è davanti a Gemini (10 contro 2, p = 0,04). La differenza fra Claude e ChatGPT (8 contro 2) non è statisticamente significativa con 30 domande (p = 0,11).

I due modelli locali senza ricerca web non conoscono l'Omnibus, sbagliano quasi tutte le scadenze, non respingono nessuna delle quattro premesse false e citano articoli inesistenti o non pertinenti (11 volte il modello da 3 miliardi), dichiarando talvolta una confidenza di 95–100 su risposte errate. Il divario con gli assistenti web dipende in buona parte dalla ricerca sul web: su norme cambiate da pochi mesi, un modello senza accesso al testo aggiornato non può rispondere bene.

## 4.2 Confidenza

![Confidenza media dichiarata e quota di risposte pienamente corrette per assistente.](fig1_confidenza_vs_correttezza.pdf){width=78%}

ChatGPT e Gemini dichiarano una confidenza fra 95 e 100 su tutte le 30 risposte. Sulle risposte corrette la loro confidenza media è 99,0 e 99,1; su quelle parziali 98,9 e 98,8. Lo scarto fra confidenza media e correttezza è di +26 punti per ChatGPT e +52 per Gemini, e il punteggio di Brier è 0,26 e 0,52. Claude dichiara fra 80 e 95, in media 88, vicino al suo 93% di risposte corrette (Brier 0,07).

Per nessuno dei tre, però, la confidenza della singola risposta indica se quella risposta è completa: l'area sotto la curva ROC è 0,57 per ChatGPT e 0,55 per Gemini, vicina al caso. Per Claude il dato non è interpretabile, perché le risposte non corrette sono solo due (e ricevono confidenza 95 e 85). In pratica, la confidenza dichiarata da Claude è una stima ragionevole della sua accuratezza media, mentre quella di ChatGPT e Gemini non lo è; ma nessuna delle tre dice all'utente su quale risposta fermarsi a verificare.

## 4.3 La norma cambiata

Dieci domande riguardano disposizioni modificate dall'Omnibus. Su queste le risposte pienamente corrette sono 9 per Claude, 6 per ChatGPT e 3 per Gemini; sulle altre venti, 19, 16 e 11. Le difficoltà si concentrano dove il testo è cambiato senza che una data lo renda evidente. L'esempio più chiaro è l'articolo 4. Prima dell'Omnibus chiedeva di adottare misure "per garantire nella misura del possibile un livello sufficiente di alfabetizzazione"; oggi chiede di adottare misure "volte a sostenere lo sviluppo dell'alfabetizzazione" e precisa che l'obbligo non impone un livello specifico. ChatGPT descrive l'articolo 4 con il testo superato in almeno quattro risposte, compresa quella in cui risponde "Sì" alla domanda se debba garantire un livello sufficiente a ogni dipendente, per poi aggiungere in fondo che il nuovo testo non impone alcun livello. Anche Claude usa la formula superata in una risposta (sulla qualifica di deployer), mentre in altre due descrive correttamente il nuovo testo.

Un secondo esempio è il nuovo divieto sulle immagini intime realistiche generate senza consenso, applicabile dal 2 dicembre 2026. ChatGPT risponde prima che l'app non è vietata dall'AI Act, poi aggiunge una "rettifica importante" e conclude che lo è; Gemini lo dà come già applicabile, senza la data. Entrambi, quindi, sono raggiunti dall'informazione aggiornata, ma la integrano nella risposta in modo incompleto o contraddittorio.

## 4.4 Premesse false

Tutti e tre gli assistenti respingono, almeno nella sostanza, le premesse false sulla certificazione dell'alfabetizzazione, sulla lettera i) dell'articolo 5 e sul Garante privacy come autorità per l'IA. Sulla premessa che gli obblighi dell'allegato III scattino il 2 agosto 2026, Claude e ChatGPT correggono con la nuova data del 2 dicembre 2027; Gemini riconosce che le scadenze sono state "differite" senza dire quando, e indica il 2 agosto 2026 come scadenza per altri obblighi. Le risposte pienamente corrette sulle quattro premesse false sono 4 per Claude, 2 per ChatGPT e 1 per Gemini: le altre respingono la premessa ma con un elemento mancante o con il testo superato dell'articolo 4.

## 4.5 I valutatori

| Coppia di valutatori | Accordo | Kappa |
|:--|--:|--:|
| ChatGPT – Claude (alla cieca) | 89% | 0,76 |
| ChatGPT – Perplexity (con i nomi) | 81% | 0,60 |
| Claude – Perplexity (con i nomi) | 79% | 0,55 |
| ChatGPT – Gemini (alla cieca) | 67% | 0,12 |
| Gemini – Claude (alla cieca) | 67% | 0,08 |
| Gemini – Perplexity | 63% | 0,10 |

Table: Accordo fra valutatori sulle 90 risposte (voto C/P/E).

ChatGPT e Claude, alla cieca, concordano su 80 risposte su 90, e Perplexity, che conosceva i nomi, è vicino a entrambi. Gemini come valutatore segna "corretta" 83 risposte su 90 e non rileva quasi mai fonti sbagliate, eccezioni mancanti o testo superato; il suo accordo con gli altri, corretto per il caso, è quasi nullo. Sulle risposte scritte da Gemini, ChatGPT e Claude come valutatori danno 13 e 12 risposte corrette, Perplexity 13, Gemini 26. Gemini è indulgente anche con gli altri assistenti, quindi questo dato da solo non dimostra una preferenza per le proprie risposte, che in ogni caso non riconosceva come proprie.

L'ordine fra gli assistenti è lo stesso con ciascuno dei tre valutatori coerenti fra loro preso da solo, con una eccezione: Perplexity, che conosceva i nomi, mette ChatGPT (22) leggermente davanti a Claude (21). Il voto di maggioranza attenua il peso di un valutatore indulgente, ma non lo elimina: dove ChatGPT e Claude come valutatori non concordavano, a decidere è stato Gemini (10 risposte, una delle quali corretta a mano come descritto nella sezione 3.3).

# 5. Che cosa significa per chi usa questi strumenti

Per una piccola impresa che usa un assistente AI per orientarsi sull'AI Act, questi risultati suggeriscono tre comportamenti pratici.

- **Usare un assistente con ricerca web e chiedere sempre la fonte.** Senza accesso al testo aggiornato le risposte su norme appena modificate sono in gran parte sbagliate, e la fonte citata è l'unico modo per verificarle.
- **Non usare la percentuale di sicurezza per decidere se verificare.** Una confidenza di 99 non separa la risposta completa da quella a cui manca una data o un'eccezione.
- **Controllare in particolare date, eccezioni e soggetto obbligato.** Sono gli elementi che le risposte parziali omettono più spesso, e sono quelli che decidono che cosa fare e quando.

Per chi costruisce valutazioni automatiche, la lezione è che un singolo assistente usato come giudice può essere molto indulgente senza che nulla lo segnali; misurare l'accordo fra più valutatori su un campione condiviso è un controllo economico che lo rivela.

# 6. Limiti e che cosa smentirebbe questi risultati

- **Il campione è piccolo.** Trenta domande bastano a distinguere Claude e ChatGPT da Gemini, non Claude da ChatGPT. Gli intervalli al 95% sono larghi.
- **Una sola esecuzione per assistente.** Gli assistenti web non sono deterministici e cambiano nel tempo; ripetere le stesse domande in un altro giorno può dare risposte diverse. I risultati descrivono gli assistenti a metà novembre 2026.
- **Impostazioni di default.** Sono stati usati il modello e l'impegno che l'utente trova all'apertura (per ChatGPT l'impegno "Instant"). Modelli o impostazioni di ragionamento più costosi possono comportarsi meglio.
- **Le domande sono dell'autore, che non è un giurista.** La scelta di domande verificabili sul testo riduce il rischio di risposte attese sbagliate, ma non lo elimina, e il dataset non copre i casi interpretativi, che sono quelli più difficili.
- **I valutatori sono assistenti AI.** Il voto di maggioranza dipende anche da un valutatore poco affidabile, e nessun giurista ha rivisto i voti.
- **Gemini è stato interrogato in una chat standard e un giorno prima** degli altri due.

Questi risultati sarebbero smentiti da una ripetizione, su più domande o in più giorni, in cui ChatGPT e Gemini dichiarassero confidenze distinte su risposte corrette e parziali, oppure in cui una revisione giuridica indipendente cambiasse una parte rilevante dei voti di maggioranza.

# 7. Conflitto di interessi, ruolo degli strumenti AI e disponibilità dei dati

L'autore non ha rapporti economici con Anthropic, OpenAI, Google o Perplexity. Lo studio è stato progettato, eseguito e scritto con l'aiuto di Claude (Anthropic), che è anche uno degli assistenti valutati e quello con il risultato migliore. Per ridurre questo rischio le risposte sono state valutate alla cieca da tre assistenti diversi; la prima valutazione, fatta da Claude nella stessa sessione di lavoro, era più indulgente con tutti, Gemini compreso, ed è stata scartata. Con ChatGPT come unico valutatore l'ordine resta lo stesso (Claude 26, ChatGPT 20, Gemini 13 risposte corrette).

Dataset, prompt, risposte complete di tutti i modelli, file anonimizzati, chiave di anonimizzazione, voti di ogni valutatore e codice di analisi sono pubblicati nel repository del progetto. Le segnalazioni di errori nelle risposte attese sono benvenute e saranno registrate pubblicamente con la versione corretta del dataset.

# Riferimenti

[1] Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale (regolamento sull'intelligenza artificiale).

[2] Regolamento (UE) 2026/1744 dell'8 luglio 2026 ("Omnibus digitale sull'IA"), GU UE del 24 luglio 2026, in vigore dal 27 luglio 2026. CELEX 32026R1744.

[3] Legge 23 settembre 2025, n. 132, Disposizioni e deleghe al Governo in materia di intelligenza artificiale.

[4] Decreto legislativo 7 ottobre 2026, n. 179, Adeguamento della normativa nazionale alle disposizioni del regolamento (UE) 2024/1689, GU n. 234 dell'8 ottobre 2026.

[5] M. Dahl, V. Magesh, M. Suzgun, D. E. Ho. Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models. Journal of Legal Analysis, 2024.

[6] V. Magesh, F. Surani, M. Dahl, M. Suzgun, C. D. Manning, D. E. Ho. Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. 2024.

[7] N. Guha et al. LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models. NeurIPS Datasets and Benchmarks, 2023.

[8] C. Guo, G. Pleiss, Y. Sun, K. Q. Weinberger. On Calibration of Modern Neural Networks. ICML, 2017.

[9] S. Kadavath et al. Language Models (Mostly) Know What They Know. 2022.

[10] M. Xiong et al. Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs. ICLR, 2024.

[11] L. Zheng et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. NeurIPS Datasets and Benchmarks, 2023.

[12] A. Panickssery, S. R. Bowman, S. Feng. LLM Evaluators Recognize and Favor Their Own Generations. NeurIPS, 2024.

[13] J. Cohen. A Coefficient of Agreement for Nominal Scales. Educational and Psychological Measurement, 1960.

[14] E. B. Wilson. Probable Inference, the Law of Succession, and Statistical Inference. Journal of the American Statistical Association, 1927.

[15] G. Simonetti. Lo storico prima dei modelli: storico etichettato, piccoli modelli linguistici e cascate per classificare le richieste su hardware locale. Rapporto tecnico, 2026. DOI 10.5281/zenodo.23313670.
