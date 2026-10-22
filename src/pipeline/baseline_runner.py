"""
Pipeline Baseline chính thức cho RMIT HACKATHON 2026.
Nhiệm vụ: Multilingual 3-Class Prompt-Attack Classification (BENIGN, JAILBREAK, PROMPT_INJECTION)
Đánh giá: Macro-averaged F1 Score
Định dạng nộp bài: id,label (CSV 6,000 dòng)
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, classification_report
from sklearn.model_selection import StratifiedKFold

CLASSES = ["BENIGN", "JAILBREAK", "PROMPT_INJECTION"]
LABEL2ID = {c: i for i, c in enumerate(CLASSES)}
ID2LABEL = {i: c for i, c in enumerate(CLASSES)}

def run_multilingual_baseline(train_path: str = "data/train.csv", 
                              test_path: str = "data/test.csv", 
                              output_path: str = "submissions/baseline_submission.csv"):
    print("=" * 65)
    print("🚀 BẮT ĐẦU CHẠY BASELINE MULTILINGUAL PROMPT-ATTACK CLASSIFICATION")
    print("=" * 65)

    if not os.path.exists(train_path) or not os.path.exists(test_path):
        print(f"[!] Chưa tìm thấy file dữ liệu ({train_path} hoặc {test_path}).")
        return None, None

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    print(f"[+] Dữ liệu train: {train_df.shape[0]} dòng")
    print(f"[+] Dữ liệu test: {test_df.shape[0]} dòng")

    if "language" in train_df.columns:
        print("[i] Phân phối ngôn ngữ tập train:")
        print(train_df["language"].value_counts(normalize=True).round(3).to_dict())

    y_train = train_df["label"].map(LABEL2ID).values
    print("[i] Phân phối nhãn tập train:")
    for c, count in train_df["label"].value_counts().items():
        print(f"  - {c:<18}: {count} ({count/len(train_df):.1%})")

    print("\n[*] Đang véc-tơ hóa văn bản (TF-IDF sublinear, max_features=35000)...")
    tfidf = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=35000,
        sublinear_tf=True,
        min_df=2
    )
    X_train = tfidf.fit_transform(train_df["text"].fillna("").astype(str))
    X_test = tfidf.transform(test_df["text"].fillna("").astype(str))

    print("\n[*] Chạy 5-Fold Stratified Cross-Validation (Đo Macro F1)...")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    oof_preds = np.zeros(len(train_df), dtype=int)
    test_probs = np.zeros((len(test_df), 3))

    fold_scores = []
    for fold, (train_idx, val_idx) in enumerate(skf.split(X_train, y_train)):
        X_tr, y_tr = X_train[train_idx], y_train[train_idx]
        X_va, y_val = X_train[val_idx], y_train[val_idx]

        model = LogisticRegression(
            C=2.0, 
            max_iter=1000, 
            class_weight="balanced", 
            random_state=42
        )
        model.fit(X_tr, y_tr)

        val_pred = model.predict(X_va)
        oof_preds[val_idx] = val_pred

        score = f1_score(y_val, val_pred, average="macro")
        fold_scores.append(score)
        print(f"  - Fold {fold + 1} Macro F1: {score:.4f}")

        test_probs += model.predict_proba(X_test) / skf.n_splits

    overall_macro_f1 = f1_score(y_train, oof_preds, average="macro")
    print("=" * 65)
    print(f"🏆 ĐIỂM ĐÁNH GIÁ NỘI BỘ TOÀN CỤC (OOF MACRO F1): {overall_macro_f1:.4f}")
    print("=" * 65)
    print("\n[i] Báo cáo chi tiết từng lớp nhãn:")
    print(classification_report(y_train, oof_preds, target_names=CLASSES))

    # Áp dụng threshold tuning cho nhãn hiếm PROMPT_INJECTION (class 2)
    # Nhân hệ số 1.25 cho xác suất của class 2 để tối ưu hóa Macro F1
    tuned_test_probs = test_probs.copy()
    tuned_test_probs[:, 2] *= 1.25
    test_pred_ids = np.argmax(tuned_test_probs, axis=1)
    test_pred_labels = [ID2LABEL[i] for i in test_pred_ids]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    id_col = "id" if "id" in test_df.columns else "Id"
    submission_df = pd.DataFrame({
        "id": test_df[id_col],
        "label": test_pred_labels
    })
    submission_df.to_csv(output_path, index=False)
    print(f"[✅] Đã lưu file nộp bài hợp lệ tại: {output_path}")
    print(f"[+] Tổng số dòng nộp: {len(submission_df)} (yêu cầu đúng 6.000 dòng)")
    print(f"[i] Xem trước 5 dòng đầu file nộp:\n{submission_df.head()}")

    print("\n[i] Phân phối nhãn dự đoán trên tập test:")
    print(submission_df["label"].value_counts(normalize=True).round(3).to_dict())

    return overall_macro_f1, output_path

if __name__ == "__main__":
    run_multilingual_baseline()
