import time
import re
import numpy as np
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, classification_report
from sklearn.model_selection import StratifiedKFold

CLASSES = ["BENIGN", "JAILBREAK", "PROMPT_INJECTION"]
LABEL2ID = {c: i for i, c in enumerate(CLASSES)}
ID2LABEL = {i: c for i, c in enumerate(CLASSES)}

train_df = pd.read_csv("data/train.csv")
y_train = train_df["label"].map(LABEL2ID).values

t0 = time.time()
# Word TF-IDF with 1, 2, 3 grams (fast and rich)
print("[*] TF-IDF Word (1, 2, 3)...")
word_tfidf = TfidfVectorizer(
    ngram_range=(1, 3),
    max_features=50000,
    sublinear_tf=True,
    min_df=2
)
X_train = word_tfidf.fit_transform(train_df["text"].fillna("").astype(str))
print(f"Done in {time.time() - t0:.1f}s, shape: {X_train.shape}")

# Add Language One-hot
lang_dummies = pd.get_dummies(train_df["language"], prefix="lang").astype(float)
X_train_full = hstack([X_train, csr_matrix(lang_dummies.values)]).tocsr()

# 5-fold CV
print("[*] 5-Fold Stratified CV...")
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
oof_probs = np.zeros((len(train_df), 3))

for fold, (train_idx, val_idx) in enumerate(skf.split(X_train_full, y_train)):
    X_tr, y_tr = X_train_full[train_idx], y_train[train_idx]
    X_va, y_val = X_train_full[val_idx], y_train[val_idx]
    
    # Logistic Regression with C=3.5
    clf = LogisticRegression(C=3.5, max_iter=1000, class_weight="balanced", random_state=42)
    clf.fit(X_tr, y_tr)
    oof_probs[val_idx] = clf.predict_proba(X_va)

raw_preds = np.argmax(oof_probs, axis=1)
raw_macro_f1 = f1_score(y_train, raw_preds, average="macro")
print(f"OOF Macro F1 (raw argmax): {raw_macro_f1:.4f}")

# Threshold grid search
best_f1 = raw_macro_f1
best_w = (1.0, 1.0, 1.0)
for w1 in np.linspace(0.9, 1.2, 7):
    for w2 in np.linspace(1.0, 1.5, 11):
        w = np.array([1.0, w1, w2])
        preds = np.argmax(oof_probs * w, axis=1)
        f1 = f1_score(y_train, preds, average="macro")
        if f1 > best_f1:
            best_f1 = f1
            best_w = (1.0, w1, w2)

print(f"OOF Macro F1 (Tuned threshold w={best_w}): {best_f1:.4f}")
print(classification_report(y_train, np.argmax(oof_probs * np.array(best_w), axis=1), target_names=CLASSES))
