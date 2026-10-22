import time
import numpy as np
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier, RidgeClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import f1_score, classification_report
from sklearn.model_selection import StratifiedKFold

CLASSES = ["BENIGN", "JAILBREAK", "PROMPT_INJECTION"]
LABEL2ID = {c: i for i, c in enumerate(CLASSES)}
ID2LABEL = {i: c for i, c in enumerate(CLASSES)}

train_df = pd.read_csv("data/train.csv")
y_train = train_df["label"].map(LABEL2ID).values

# Word TF-IDF 1-3 grams + Char TF-IDF with smaller limit (char_wb 3-4, max 25000)
print("[*] Building Word + Char TF-IDF...")
word_vec = TfidfVectorizer(ngram_range=(1, 3), max_features=45000, sublinear_tf=True, min_df=2)
char_vec = TfidfVectorizer(ngram_range=(3, 4), analyzer="char_wb", max_features=25000, sublinear_tf=True, min_df=5)

X_word = word_vec.fit_transform(train_df["text"].fillna("").astype(str))
X_char = char_vec.fit_transform(train_df["text"].fillna("").astype(str))
lang_dummies = pd.get_dummies(train_df["language"], prefix="lang").astype(float)

X_full = hstack([X_word, X_char, csr_matrix(lang_dummies.values)]).tocsr()
print(f"X_full shape: {X_full.shape}")

# 5-fold CV with 2 distinct models (LogisticRegression + Calibrated SGD)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
oof_probs_lr = np.zeros((len(train_df), 3))
oof_probs_sgd = np.zeros((len(train_df), 3))

for fold, (train_idx, val_idx) in enumerate(skf.split(X_full, y_train)):
    X_tr, y_tr = X_full[train_idx], y_train[train_idx]
    X_va, y_val = X_full[val_idx], y_train[val_idx]
    
    # 1. Logistic Regression
    clf_lr = LogisticRegression(C=3.5, max_iter=1000, class_weight="balanced", random_state=42)
    clf_lr.fit(X_tr, y_tr)
    oof_probs_lr[val_idx] = clf_lr.predict_proba(X_va)
    
    # 2. SGD with modified_huber loss (smooth hinge, outputs probabilities, very fast max-margin)
    clf_sgd = SGDClassifier(loss="modified_huber", alpha=1e-5, max_iter=1000, class_weight="balanced", random_state=42)
    clf_sgd.fit(X_tr, y_tr)
    oof_probs_sgd[val_idx] = clf_sgd.predict_proba(X_va)

# Evaluate individual
score_lr = f1_score(y_train, np.argmax(oof_probs_lr, axis=1), average="macro")
score_sgd = f1_score(y_train, np.argmax(oof_probs_sgd, axis=1), average="macro")
print(f"OOF LR: {score_lr:.4f} | OOF SGD: {score_sgd:.4f}")

# Blend ensemble
oof_blend = 0.6 * oof_probs_lr + 0.4 * oof_probs_sgd
raw_blend_score = f1_score(y_train, np.argmax(oof_blend, axis=1), average="macro")
print(f"OOF Blend (Raw Argmax): {raw_blend_score:.4f}")

# Threshold tuning on blend
best_f1 = raw_blend_score
best_w = (1.0, 1.0, 1.0)
for w1 in np.linspace(0.9, 1.2, 7):
    for w2 in np.linspace(1.0, 1.6, 13):
        w = np.array([1.0, w1, w2])
        preds = np.argmax(oof_blend * w, axis=1)
        f1 = f1_score(y_train, preds, average="macro")
        if f1 > best_f1:
            best_f1 = f1
            best_w = (1.0, w1, w2)

print(f"🏆 OOF Blend + Threshold Tuning: {best_f1:.4f} (Weights={best_w})")
print(classification_report(y_train, np.argmax(oof_blend * np.array(best_w), axis=1), target_names=CLASSES))
