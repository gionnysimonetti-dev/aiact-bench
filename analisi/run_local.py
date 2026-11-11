import json, sys, time
from llama_cpp import Llama
model_path, tag = sys.argv[1], sys.argv[2]
rows=json.load(open('../dataset/dataset_v0.json'))
SYS=("Sei un consulente che risponde a una piccola impresa italiana su AI Act (regolamento UE 2024/1689) e normativa italiana sull'intelligenza artificiale. "
     "Rispondi in italiano, in modo breve (massimo 5 frasi). Alla fine scrivi due righe separate:\n"
     "FONTE: <atto e articolo su cui ti basi>\nCONFIDENZA: <numero da 0 a 100, quanto sei sicuro che la risposta sia corretta>")
llm=Llama(model_path=model_path, n_ctx=2048, n_threads=2, verbose=False, seed=1)
out=open(f'../risposte/locali/{tag}.jsonl','w')
for r in rows:
    t=time.time()
    res=llm.create_chat_completion(messages=[{"role":"system","content":SYS},{"role":"user","content":r['domanda']}], max_tokens=260, temperature=0)
    ans=res['choices'][0]['message']['content']
    out.write(json.dumps({"id":r['id'],"model":tag,"answer":ans,"secs":round(time.time()-t,1)},ensure_ascii=False)+"\n"); out.flush()
    print(r['id'], round(time.time()-t,1), flush=True)
