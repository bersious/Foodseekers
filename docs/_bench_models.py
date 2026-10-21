"""
So sanh chat luong cac model tren Vilao bang TASK THAT cua RMIT Hackathon 2025
Bai toan: nhi phan jailbreak/benign, ROC AUC, 10 luot noi.
Khong doan mo - chay that, luu ket qua, tinh chi phi thuc te.
"""
import json, os, time, urllib.request, urllib.error

BASE = "https://api.vilao.ai/v1"
KEY = os.environ["HERMES_MODEL_PROVIDER_API_KEY"]

MODELS = ["Minimax-M3", "gemini-3.8-flash", "claude-fable-5", "gemini-4-argon"]
PRICE = {  # (input/1M, output/1M) tu API
    "Minimax-M3": (200, 500), "gemini-3.8-flash": (400, 1600),
    "claude-fable-5": (450, 2250), "gemini-4-argon": (1800, 3000),
}

# 3 task that, lay truc tiep tu de RMIT Hackathon 2025
TASKS = [
    {
        "name": "DEBUG_BUG",
        "desc": "Viet code PyTorch fine-tune BERT binary classification, tim loi va sua. "
                "Day la code sinh ra bi sai:",
        "code": '''
model = AutoModelForSequenceClassification.from_pretrained('vinai/phobert-base', num_labels=2)
trainer = TrainingTrainer(
    model=model,
    args=TrainingArguments(output_dir='out', num_train_epochs=3,
        per_device_train_batch_size=16, eval_strategy='epoch'),
    train_dataset=train_ds,
)
trainer.train()
# ROI: trainer.evaluate() bi loi "numpy.dtype size changed"
''',
        "ask": "8 nhan 1 cau, tieng Viet, ro rang. Loi o dau? Sua nhu the nao? Bao loi giay.",
    },
    {
        "name": "AUC_STRATEGY",
        "desc": "Dataset 5000 prompt jailbreak/benign, 4000 train 1000 test, cham ROC AUC, "
                "chi duoc 10 luot noi. Chi ra 3 buoc toi uu diem theo thu tu, "
                "va noi ro buoc nao ton nhieu luot noi nhat.",
        "code": "",
        "ask": "8 nhan 1 cau, tieng Viet. Khong vong vo - sap xep theo do kiem chung.",
    },
    {
        "name": "FEATURE",
        "desc": "Chi ra 6 dac trong prompt jailbreak ma TF-IDF bo loi, "
                "va 3 feature bo sung giup mo hinh generalization tot hon tren ngon ngu it du lieu.",
        "code": "",
        "ask": "Dong y, tieng Viet, viet du dieu kien regex/toi gia cu the cho tung diem.",
    },
]

def call(model, prompt, maxtok=900):
    body = json.dumps({"model": model, "messages": [
        {"role": "user", "content": prompt}], "max_tokens": maxtok}).encode()
    req = urllib.request.Request(f"{BASE}/chat/completions", data=body, headers={
        "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            d = json.loads(r.read())
        u = d.get("usage", {})
        txt = d["choices"][0]["message"]["content"]
        return {"ok": True, "text": txt, "sec": round(time.time()-t0, 1),
                "in": u.get("prompt_tokens", 0), "out": u.get("completion_tokens", 0)}
    except urllib.error.HTTPError as e:
        return {"ok": False, "err": f"HTTP {e.code}: {e.read()[:200].decode(errors='replace')}"}
    except Exception as e:
        return {"ok": False, "err": str(e)[:200]}

out = {}
for m in MODELS:
    out[m] = {}
    print(f"\n{'='*60}\nMODEL: {m}")
    for t in TASKS:
        p = f"{t['desc']}\n{t['code']}\n\nYEU CAU: {t['ask']}"
        r = call(m, p)
        out[m][t["name"]] = r
        if r["ok"]:
            pi, po = PRICE[m]
            cost = r["in"]/1e6*pi + r["out"]/1e6*po
            print(f"  {t['name']:14} OK  {r['sec']:>5}s  in={r['in']:<5} out={r['out']:<5} ~{cost:>7.2f}d")
        else:
            print(f"  {t['name']:14} FAIL {r['err'][:90]}")

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_bench_raw.json")
json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nLUU:", path)