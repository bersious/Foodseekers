"""
Pipeline tối ưu cho RMIT Hackathon 2026 — Multilingual Prompt-Attack Classification.
Bài toán: phân loại 3 lớp (BENIGN / JAILBREAK / PROMPT_INJECTION) trên 4 ngôn ngữ (pt/fr/it/en).
Thang đo: Macro-averaged F1.

Chiến thuật (chạy được trên CPU, không cần GPU):
1. TF-IDF lai (word 1-2 gram + char_wb 2-5 gram) -> bắt tốt hình thái đa ngữ (diacritics pt/fr/it).
2. Đặc trưng ngữ nghĩa đa ngữ (regex injection/jailbreak theo từng ngôn ngữ) từ skill.
3. LogisticRegression(class_weight='balanced') xử lý mất cân bằng (BENIGN 62% / JAILBREAK 31% / PROMPT_INJECTION 7%).
4. Đánh giá nội bộ 5-Fold Stratified CV theo Macro F1 (fit TF-IDF chỉ trên fold train -> chống rò rỉ).
5. Tinh chỉnh hệ số nhân xác suất cho lớp hiếm PROMPT_INJECTION (grid search trên OOF) để tối đa Macro F1.
6. Xuất submission.csv đúng chuẩn id,label (6.000 dòng).
"""

import os
import re
import sys
import argparse
import numpy as np
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold

LABELS = ["BENIGN", "JAILBREAK", "PROMPT_INJECTION"]
LABEL2ID = {l: i for i, l in enumerate(LABELS)}
ID2LABEL = {i: l for l, i in LABEL2ID.items()}

# --- Regex đặc trưng ngữ nghĩa đa ngữ (theo skill multilingual-prompt-attack) ---
INJECTION_PATTERNS = re.compile(
    r"(ignore\s+(all\s+)?previous|disregard\s+(the\s+)?system|system\s+override|forget\s+(the\s+)?(system|rules)"
    r"|ignorez\s+les\s+instructions|oubliez\s+toutes\s+les|nouvelle\s+instruction"
    r"|ignore\s+todas\s+as\s+instru|esque\u00e7a\s+as\s+regras|novo\s+comando|desconsidere\s+o\s+prompt"
    r"|ignora\s+tutte\s+le\s+istruzioni|dimentica\s+le\s+regole|nuova\s+istruzione|sovrascrivi\s+il\s+sistema"
    r"|repeat\s+the\s+system\s+prompt|verbatim)",
    re.IGNORECASE,
)
JAILBREAK_PATTERNS = re.compile(
    r"(you\s+are\s+now\s+DAN|developer\s+mode|pretend\s+you\s+are|act\s+as\s+an?\s+unrestricted|fictional\s+story"
    r"|vous\s+\u00eates\s+maintenant\s+DAN|mode\s+d\u00e9veloppeur|agissez\s+en\s+tant\s+que|histoire\s+fictive"
    r"|voc\u00ea\s+agora\s+\u00e9\s+DAN|modo\s+desenvolvedor|finja\s+que\s+voc\u00ea|cen\u00e1rio\s+hipot\u00e9tico"
    r"|ora\s+sei\s+DAN|modalit\u00e0\s+sviluppatore|fai\s+finta\s+di\s+essere|scenario\s+ipotetico"
    r"|jailbreak|unrestricted|without\s+any\s+restrictions)",
    re.IGNORECASE,
)
DELIMITER_PATTERNS = re.compile(r"(###\s*system|\[INST\]|<\|.*?\|>|```json|<system>|\{\{.*?\}\})", re.IGNORECASE)


def extract_semantic_features(texts):
    rows = []
    for t in texts:
        t = str(t) if t is not None else ""
        low = t.lower()
        n = len(t) + 1e-5
        rows.append([
            len(t),
            len(t.split()),
            sum(c.isupper() for c in t) / n,
            sum((not c.isalnum() and not c.isspace()) for c in t) / n,
            1 if INJECTION_PATTERNS.search(t) else 0,
            1 if JAILBREAK_PATTERNS.search(t) else 0,
            1 if DELIMITER_PATTERNS.search(t) else 0,
        ])
    return np.array(rows, dtype=np.float32)


def build_features(train_texts, test_texts):
    """Fit vectorizers trên train, transform train+test. Trả về ma trận sparse đã ghép."""
    word_vec = TfidfVectorizer(ngram_range=(1, 2), max_features=20000, sublinear_tf=True, min_df=3)
    char_vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4), max_features=20000, sublinear_tf=True, min_df=3)

    Xw_tr = word_vec.fit_transform(train_texts)
    Xw_te = word_vec.transform(test_texts)
    Xc_tr = char_vec.fit_transform(train_texts)
    Xc_te = char_vec.transform(test_texts)

    sem_tr = csr_matrix(extract_semantic_features(train_texts))
    sem_te = csr_matrix(extract_semantic_features(test_texts))

    X_tr = hstack([Xw_tr, Xc_tr, sem_tr]).tocsr()
    X_te = hstack([Xw_te, Xc_te, sem_te]).tocsr()
    return X_tr, X_te


def tune_rare_multiplier(oof_proba, y_true):
    """Grid search hệ số nhân xác suất lớp hiếm PROMPT_INJECTION trên OOF để tối đa Macro F1."""
    best_m, best_f1 = 1.0, -1.0
    for m in np.arange(1.0, 1.61, 0.05):
        adj = oof_proba.copy()
        adj[:, LABEL2ID["PROMPT_INJECTION"]] *= m
        pred = adj.argmax(axis=1)
        f1 = f1_score(y_true, pred, average="macro")
        if f1 > best_f1:
            best_f1, best_m = f1, m
    return best_m, best_f1


def run(train_path, test_path, out_path):
    print("=" * 64)
    print("RMIT HACKATHON 2026 — PIPELINE TỐI ƯU (Macro F1, 3 lớp, đa ngữ)")
    print("=" * 64)

    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    print(f"[+] Train: {train.shape} | Test: {test.shape}")

    train["text"] = train["text"].fillna("").astype(str)
    test["text"] = test["text"].fillna("").astype(str)
    y = train["label"].map(LABEL2ID).values
    print("[+] Phân bố nhãn:", {ID2LABEL[i]: int((y == i).sum()) for i in range(3)})

    # --- 5-Fold Stratified CV (fit lại vectorizer mỗi fold để chống rò rỉ) ---
    print("\n[*] Chạy 5-Fold Stratified CV (Macro F1)...")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    oof = np.zeros((len(train), 3))
    fold_f1 = []
    for k, (tr_idx, va_idx) in enumerate(skf.split(train, y)):
        Xk_tr, Xk_va = build_features(
            train["text"].iloc[tr_idx].tolist(),
            train["text"].iloc[va_idx].tolist(),
        )
        clf = LogisticRegression(C=2.0, max_iter=1000, class_weight="balanced", solver="lbfgs")
        clf.fit(Xk_tr, y[tr_idx])
        p = clf.predict_proba(Xk_va)
        oof[va_idx] = p
        f1 = f1_score(y[va_idx], p.argmax(1), average="macro")
        fold_f1.append(f1)
        print(f"  - Fold {k + 1}: Macro F1 = {f1:.4f}")

    cv_raw = f1_score(y, oof.argmax(1), average="macro")
    mult, cv_tuned = tune_rare_multiplier(oof, y)
    print("=" * 64)
    print(f"[=] OOF Macro F1 (argmax thô):            {cv_raw:.4f}")
    print(f"[=] Hệ số nhân lớp hiếm tốt nhất:         x{mult:.2f}")
    print(f"[=] OOF Macro F1 (sau tinh chỉnh ngưỡng): {cv_tuned:.4f}")
    print("=" * 64)

    # --- Train toàn bộ train, dự đoán test ---
    print("\n[*] Train toàn bộ dữ liệu & dự đoán test...")
    X_tr, X_te = build_features(train["text"].tolist(), test["text"].tolist())
    clf = LogisticRegression(C=2.0, max_iter=1000, class_weight="balanced", solver="lbfgs")
    clf.fit(X_tr, y)
    proba = clf.predict_proba(X_te)
    proba[:, LABEL2ID["PROMPT_INJECTION"]] *= mult
    pred = proba.argmax(1)

    sub = pd.DataFrame({"id": test["id"], "label": [ID2LABEL[i] for i in pred]})

    # --- Kiểm tra toàn vẹn file nộp ---
    assert sub.shape[0] == test.shape[0], "Sai số dòng submission!"
    assert sub["label"].isin(LABELS).all(), "Có nhãn lạ ngoài 3 lớp cho phép!"
    assert sub["label"].isna().sum() == 0, "Có nhãn rỗng!"

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    sub.to_csv(out_path, index=False)
    print(f"[OK] Đã lưu submission: {out_path}")
    print("[i] Phân bố dự đoán:", sub["label"].value_counts().to_dict())
    return cv_tuned, mult, sub


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--train", default="data/train.csv")
    ap.add_argument("--test", default="data/test.csv")
    ap.add_argument("--out", default="submissions/submission.csv")
    a = ap.parse_args()
    run(a.train, a.test, a.out)
