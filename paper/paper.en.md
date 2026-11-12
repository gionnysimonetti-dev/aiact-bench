---
title: "Confident Even When Wrong"
subtitle: "Three AI assistants tested on 30 questions about the EU AI Act, the Digital Omnibus and Italian law 132/2025: correctness, declared confidence and the reliability of LLM graders"
author: "Giovanni Simonetti (ORCID 0009-0008-7543-6737)"
date: "Technical report, version 0.1, November 2026. Italian version archived at Zenodo, DOI 10.5281/zenodo.24139406"
abstract: |
  A small Italian business that asks an AI assistant about a rule of the EU AI Act gets an answer, a source and, if it asks, a confidence percentage. This report measures what each of the three is worth. We asked Claude, ChatGPT and Gemini, in their default web versions with web search on, 30 questions that can be checked against the official text (deadlines, prohibited practices, obligations and penalties, Italian law 132/2025, questions with a false premise), 10 of which concern provisions amended by Regulation (EU) 2026/1744 (the "Digital Omnibus"), asking for a short answer, the legal source and a confidence from 0 to 100. The 90 answers were anonymised, shuffled and graded blind by three different assistants, with the majority vote as final grade. Fully correct answers are 28 of 30 for Claude (93%, 95% interval 79-98%), 22 for ChatGPT (73%, 56-86%) and 14 for Gemini (47%, 30-64%). No assistant gives a fully wrong answer, but many answers are partial: missing new dates, omitted exceptions, wrong sources, the superseded wording of Article 4. ChatGPT and Gemini declare a mean confidence of 99 out of 100 on correct and partial answers alike, 26 and 52 points above their accuracy; Claude declares 88 on average, close to its 93%. For none of the three does confidence separate a complete answer from an incomplete one. Two local models without web search answer 7 of 30 questions correctly and cite legal provisions that do not exist. Among the LLM graders, ChatGPT and Claude agree strongly (kappa 0.76) while Gemini rates almost everything correct (kappa 0.08-0.12 with the others). The sample is small and the difference between Claude and ChatGPT is not statistically significant. Dataset, answers, grades and code are public.
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

# 1. Introduction

Since 2 February 2025 a business that uses artificial intelligence must comply with the prohibitions of Article 5 of the AI Act [1] and take care of the AI literacy of its staff. Since 10 October 2025 Italy has added law 132/2025 [3], and since 23 October 2026 Legislative Decree 179/2026 [4] gives the national authorities AgID and ACN the power to impose penalties. In between, on 27 July 2026, Regulation (EU) 2026/1744 [2], the "Digital Omnibus", entered into force: it moved the obligations on high-risk systems to 2 December 2027 and 2 August 2028, rewrote Article 4 and added new prohibitions to Article 5.

A small business without a legal department, facing this framework, more and more often does the simplest thing: it asks an AI assistant. It gets a well-written answer, almost always with a source and, if it asks, with a confidence percentage. This report measures how far each of the three can be relied on, in November 2026, with the tools that business would actually use.

There are three research questions:

- **Correctness.** Are the answers right, complete and based on the law in force, especially where the Omnibus changed the text?
- **Confidence.** Does the confidence declared by the assistant help the user know when to trust it?
- **Grading.** If AI assistants are used to grade other assistants, are their grades reliable?

The contributions are a dataset of 30 questions with the verbatim legal text and a link to the official source, the 90 complete answers of the three assistants, a blind grading by three graders with a measure of their agreement, and a first measure of the gap between declared confidence and correctness on an Italian regulatory task.

# 2. Related work

**Reliability of AI tools on legal questions.** Dahl and co-authors [5] documented high rates of hallucination by general-purpose models on questions about US case law; Magesh and co-authors [6] showed that legal research tools with document retrieval also err in a relevant share of answers. LegalBench [7] measures legal reasoning on structured tasks. These works concern US law and models or versions of a given moment; here the task is European and Italian AI regulation, recently amended, and the assistants are the ones a user opens in the browser.

**Confidence and calibration.** A model is well calibrated when, among the answers given with 80% confidence, about 80% are correct [8]. Kadavath and co-authors [9] showed that language models partly know what they know; Xiong and co-authors [10] observed that confidence expressed in words tends to be high and uninformative. Earlier work by the author [15] measured how poorly the confidence of small models separates right from wrong answers in a classification task.

**Assistants as graders.** Using a language model as a judge is now common practice [11], with known biases including a preference for its own answers [12]. For this reason the answers were anonymised and shuffled, and each assistant also graded its own answers without knowing it.

# 3. Method

## 3.1 The questions

The dataset contains 30 questions in Italian, written as the owner of a small business would ask them, in five groups: deadlines (7), prohibited practices (5), obligations, risk classification and penalties (10), law 132/2025 (4), questions with a false premise (4). The false-premise questions contain an error that the answer must correct: an AI literacy certification that the law does not require, a deadline superseded by the Omnibus, a letter of Article 5 that does not exist, a wrong national authority.

Each question has an expected answer, the key elements the answer must contain, the verbatim text of the provision and a link to the text on EUR-Lex or Normattiva. The author is not a lawyer and the dataset has not had an independent legal review: for this reason only questions whose answer can be read in the text, without interpretation, were admitted, and every expected answer can be checked by anyone at the link given. Reports of errors are welcome and will be recorded publicly.

## 3.2 The assistants and the collection

We queried Claude (claude.ai, incognito mode, default model Opus 5.5 with medium effort), ChatGPT (chatgpt.com, temporary chat, default model with "Instant" effort) and Gemini (gemini.google.com, standard chat, default model), all with web search on as the user finds them. Each question was asked in a new conversation, on 10 November 2026 for Gemini and on 11 November 2026 for the other two, with the same prompt, here translated from Italian:

> Answer as a consultant to a small Italian business, in Italian, briefly (at most 5 sentences). At the end write two separate lines: SOURCE: <act and article you rely on> and CONFIDENCE: <number from 0 to 100, how sure you are that the answer is correct>.

Each question was asked once per assistant. As a reference without web search, the same questions were put to two local open-weight models, Qwen2.5 with 1.5 and 3 billion parameters (Q4_K_M quantisation, llama.cpp, temperature 0), on a PC with no graphics card.

## 3.3 Grading

Each answer receives one of three grades. **C (correct)**: right verdict consistent with the text in force, key elements present, relevant source. **P (partial)**: right verdict but with a key element missing, a wrong source, contradictory statements or the description of a superseded text. **E (wrong)**: wrong verdict, false premise accepted or non-existent provision cited.

The 90 web answers were stripped of everything that identified the assistant (recurring greetings, source links, footers) and of the declared confidence, labelled A, B and C in a random order different for each question, and given to ChatGPT, Claude and Gemini to grade in new conversations, with the reference legal text and the instruction not to search the web. The final grade is the majority vote; in no case were the three grades all different. One correction was applied by hand: an answer graded "wrong" for calling "(ba)" the letter that the Italian text numbers "b bis)" was brought back to "partial", since "(ba)" is the numbering of the English version of the same regulation (the answer remains contradictory for other reasons). Perplexity graded the same answers knowing the name of the assistant; its grades are reported for comparison and do not enter the final grade.

The local models were graded by a single reviewer on the same scale, also recording non-existent or irrelevant legal references.

## 3.4 Measures

For each assistant we report the share of fully correct answers with the 95% Wilson interval [14], the mean declared confidence and its gap from correctness, the ability of confidence to separate correct answers from the others (area under the ROC curve, where 0.5 is chance) and the Brier score. Differences between assistants, which answer the same questions, are tested with the exact McNemar test. Agreement between graders is measured with Cohen's kappa [13].

# 4. Results

## 4.1 Correctness

| Assistant | Correct | Partial | Wrong | % correct (95% CI) | Mean confidence |
|:--|--:|--:|--:|:--|--:|
| Claude | 28 | 2 | 0 | 93% (79-98%) | 88 |
| ChatGPT | 22 | 8 | 0 | 73% (56-86%) | 99 |
| Gemini | 14 | 16 | 0 | 47% (30-64%) | 99 |
| Qwen2.5 3B local | 7 | 4 | 19 | 23% | - |
| Qwen2.5 1.5B local | 7 | 2 | 21 | 23% | - |

Table: Results by assistant. Web assistants: majority vote of three blind graders. Local models: one reviewer.

None of the answers of the three web assistants is fully wrong, and all of them know that the Omnibus exists and which main dates it changed. The difference lies in completeness. Gemini's partial answers mostly omit key elements (the new date of application, the exception for medical or safety reasons on emotion recognition, the exception for fraud detection in creditworthiness assessment) or base a right answer on the wrong rule: in three cases they cite the GDPR or the professional code of conduct where the rule is in the AI Act or in law 132/2025. Claude's two partial answers concern the date of the new Article 5 prohibitions and the paragraph cited from law 132/2025.

Claude is clearly ahead of Gemini (15 questions where only Claude is correct, 1 the other way round, p < 0.001), and ChatGPT is ahead of Gemini (10 against 2, p = 0.04). The difference between Claude and ChatGPT (8 against 2) is not statistically significant with 30 questions (p = 0.11).

The two local models without web search do not know the Omnibus, get almost all deadlines wrong, reject none of the four false premises and cite non-existent or irrelevant articles (11 times for the 3-billion model), sometimes declaring a confidence of 95-100 on wrong answers. The gap with the web assistants depends largely on web search: on rules that changed a few months ago, a model without access to the updated text cannot answer well.

## 4.2 Confidence

![Mean declared confidence and share of fully correct answers by assistant.](fig1_confidence_vs_correctness.pdf){width=78%}

ChatGPT and Gemini declare a confidence between 95 and 100 on all 30 answers. On correct answers their mean confidence is 99.0 and 99.1; on partial ones 98.9 and 98.8. The gap between mean confidence and correctness is +26 points for ChatGPT and +52 for Gemini, and the Brier score is 0.26 and 0.52. Claude declares between 80 and 95, 88 on average, close to its 93% of correct answers (Brier 0.07).

For none of the three, however, does the confidence of a single answer show whether that answer is complete: the area under the ROC curve is 0.57 for ChatGPT and 0.55 for Gemini, close to chance. For Claude the figure cannot be interpreted, because only two answers are not correct (they receive confidence 95 and 85). In practice, the confidence declared by Claude is a reasonable estimate of its average accuracy, while that of ChatGPT and Gemini is not; but none of the three tells the user which answer to stop and check.

## 4.3 The amended law

Ten questions concern provisions amended by the Omnibus. On these the fully correct answers are 9 for Claude, 6 for ChatGPT and 3 for Gemini; on the other twenty, 19, 16 and 11. The difficulties concentrate where the text changed without a date making it obvious. The clearest example is Article 4. Before the Omnibus it required measures "to ensure, to their best extent, a sufficient level of AI literacy"; the amended text asks for measures to support the development of AI literacy and states that the obligation does not impose a specific level. ChatGPT describes Article 4 with the superseded text in at least four answers, including the one where it answers "Yes" to the question whether a sufficient level must be ensured for every employee, and then adds at the end that the new text does not impose any level. Claude also uses the superseded wording in one answer (on the deployer role), while in two others it describes the new text correctly.

A second example is the new prohibition on realistic intimate images generated without consent, applicable from 2 December 2026. ChatGPT first answers that the app is not prohibited by the AI Act, then adds an "important correction" and concludes that it is; Gemini presents it as already applicable, without the date. Both, then, reach the updated information, but integrate it into the answer in an incomplete or contradictory way.

## 4.4 False premises

All three assistants reject, at least in substance, the false premises on AI literacy certification, on letter (i) of Article 5 and on the Italian data protection authority as the AI authority. On the premise that the Annex III obligations start on 2 August 2026, Claude and ChatGPT correct it with the new date of 2 December 2027; Gemini acknowledges that the deadlines were "postponed" without saying until when, and gives 2 August 2026 as the deadline for other obligations. Fully correct answers on the four false premises are 4 for Claude, 2 for ChatGPT and 1 for Gemini: the others reject the premise but with a missing element or with the superseded text of Article 4.

## 4.5 The graders

| Pair of graders | Agreement | Kappa |
|:--|--:|--:|
| ChatGPT - Claude (blind) | 89% | 0.76 |
| ChatGPT - Perplexity (with names) | 81% | 0.60 |
| Claude - Perplexity (with names) | 79% | 0.55 |
| ChatGPT - Gemini (blind) | 67% | 0.12 |
| Gemini - Claude (blind) | 67% | 0.08 |
| Gemini - Perplexity | 63% | 0.10 |

Table: Agreement between graders on the 90 answers (grades C/P/E).

ChatGPT and Claude, grading blind, agree on 80 answers out of 90, and Perplexity, which knew the names, is close to both. Gemini as a grader marks 83 answers out of 90 as correct and almost never detects wrong sources, missing exceptions or superseded text; its agreement with the others, corrected for chance, is almost nil. On the answers written by Gemini, ChatGPT and Claude as graders give 13 and 12 correct answers, Perplexity 13, Gemini 26. Gemini is lenient with the other assistants too, so this figure alone does not show a preference for its own answers, which in any case it did not recognise as its own.

The ranking of the assistants is the same with each of the three mutually consistent graders taken alone, with one exception: Perplexity, which knew the names, puts ChatGPT (22) slightly ahead of Claude (21). The majority vote reduces the weight of a lenient grader but does not remove it: where ChatGPT and Claude as graders disagreed, Gemini decided (10 answers, one of which was corrected by hand as described in section 3.3).

# 5. What it means for users of these tools

For a small business that uses an AI assistant to find its way through the AI Act, these results suggest three practical habits.

- **Use an assistant with web search and always ask for the source.** Without access to the updated text, answers on recently amended rules are largely wrong, and the cited source is the only way to check them.
- **Do not use the confidence percentage to decide whether to check.** A confidence of 99 does not separate the complete answer from the one missing a date or an exception.
- **Check dates, exceptions and the obliged party in particular.** They are the elements that partial answers omit most often, and they decide what to do and when.

For those who build automated evaluations, the lesson is that a single assistant used as a judge can be very lenient without anything signalling it; measuring agreement between several graders on a shared sample is a cheap check that reveals it.

# 6. Limits and what would count against these results

- **The sample is small.** Thirty questions are enough to separate Claude and ChatGPT from Gemini, not Claude from ChatGPT. The 95% intervals are wide.
- **One run per assistant.** Web assistants are not deterministic and change over time; asking the same questions on another day may give different answers. The results describe the assistants in mid-November 2026.
- **Default settings.** We used the model and effort the user finds on opening the assistant (for ChatGPT, "Instant" effort). More expensive models or reasoning settings may do better.
- **The questions were written by the author, who is not a lawyer.** Choosing questions verifiable on the text reduces the risk of wrong expected answers but does not remove it, and the dataset does not cover interpretive cases, which are the hardest.
- **The graders are AI assistants.** The majority vote also depends on an unreliable grader, and no lawyer reviewed the grades.
- **The questions and answers are in Italian.** Results may differ in other languages.
- **Gemini was queried in a standard chat and one day earlier** than the other two.

These results would be contradicted by a repetition, on more questions or on more days, in which ChatGPT and Gemini declared distinct confidences on correct and partial answers, or in which an independent legal review changed a relevant share of the majority grades.

# 7. Conflict of interest, role of AI tools and data availability

The author has no financial relationship with Anthropic, OpenAI, Google or Perplexity. The study was designed, run and written with the help of Claude (Anthropic), which is also one of the assistants evaluated and the one with the best result. To reduce this risk the answers were graded blind by three different assistants; the first grading, done by Claude in the same working session, was more lenient with all assistants, Gemini included, and was discarded. With ChatGPT as the only grader the ranking stays the same (Claude 26, ChatGPT 20, Gemini 13 correct answers).

Dataset, prompts, complete answers of all models, anonymised files, anonymisation key, grades of every grader and analysis code are published in the repository https://github.com/gionnysimonetti-dev/aiact-bench and archived at Zenodo with DOI 10.5281/zenodo.24139406, together with the Italian version of this report. Reports of errors in the expected answers are welcome and will be recorded publicly with the corrected version of the dataset.

# References

[1] Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act).

[2] Regulation (EU) 2026/1744 of 8 July 2026 ("Digital Omnibus on AI"), OJ EU of 24 July 2026, in force from 27 July 2026. CELEX 32026R1744.

[3] Italian Law of 23 September 2025, no. 132, Provisions and delegations to the Government on artificial intelligence.

[4] Italian Legislative Decree of 7 October 2026, no. 179, Alignment of national legislation with Regulation (EU) 2024/1689, Official Gazette no. 234 of 8 October 2026.

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

[15] G. Simonetti. History Before Models: labelled history, small language models and cascades for request classification on local hardware. Technical report, 2026. DOI 10.5281/zenodo.23313670.
