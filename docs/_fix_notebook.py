import json

nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🛡️ RMIT HACKATHON 2026 — UIT_SGS_Foodseekers_C1\n",
    "### Multilingual Prompt-Attack Classification (BENIGN, JAILBREAK, PROMPT_INJECTION)\n",
    "### Model: Fine-tuned `FacebookAI/xlm-roberta-base` with Class-Weighted Loss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import gc\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import torch\n",
    "import torch.nn as nn\n",
    "from torch.optim import AdamW\n",
    "from torch.utils.data import Dataset, DataLoader\n",
    "from transformers import AutoTokenizer, AutoModelForSequenceClassification, get_linear_schedule_with_warmup\n",
    "from sklearn.model_selection import StratifiedKFold\n",
    "from sklearn.metrics import f1_score, classification_report\n",
    "from tqdm.auto import tqdm\n",
    "\n",
    "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n",
    "print(f'Device: {device}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "MODEL_NAME = 'FacebookAI/xlm-roberta-base'\n",
    "BATCH_SIZE = 16\n",
    "MAX_LEN = 256\n",
    "EPOCHS = 3\n",
    "LR = 2e-5\n",
    "SEED = 42\n",
    "\n",
    "CLASSES = ['BENIGN', 'JAILBREAK', 'PROMPT_INJECTION']\n",
    "LABEL2ID = {c: i for i, c in enumerate(CLASSES)}\n",
    "ID2LABEL = {i: c for i, c in enumerate(CLASSES)}\n",
    "\n",
    "DATA_DIR = '/kaggle/input/rmit-hackathon-2026'\n",
    "if not os.path.exists(DATA_DIR):\n",
    "    for root, dirs, files in os.walk('/kaggle/input'):\n",
    "        if 'train.csv' in files:\n",
    "            DATA_DIR = root\n",
    "            break\n",
    "\n",
    "train_df = pd.read_csv(f'{DATA_DIR}/train.csv')\n",
    "test_df = pd.read_csv(f'{DATA_DIR}/test.csv')\n",
    "train_df['target'] = train_df['label'].map(LABEL2ID)\n",
    "\n",
    "class_counts = train_df['label'].value_counts()[CLASSES].values\n",
    "class_weights = len(train_df) / (len(CLASSES) * class_counts)\n",
    "weights_tensor = torch.tensor(class_weights, dtype=torch.float).to(device)\n",
    "print('Class weights:', weights_tensor)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)\n",
    "\n",
    "class PromptAttackDataset(Dataset):\n",
    "    def __init__(self, texts, labels=None, tokenizer=None, max_len=256):\n",
    "        self.texts = texts\n",
    "        self.labels = labels\n",
    "        self.tokenizer = tokenizer\n",
    "        self.max_len = max_len\n",
    "    def __len__(self):\n",
    "        return len(self.texts)\n",
    "    def __getitem__(self, idx):\n",
    "        text = str(self.texts[idx])\n",
    "        enc = self.tokenizer(text, truncation=True, max_length=self.max_len, padding='max_length', return_tensors='pt')\n",
    "        item = {'input_ids': enc['input_ids'].squeeze(0), 'attention_mask': enc['attention_mask'].squeeze(0)}\n",
    "        if self.labels is not None:\n",
    "            item['label'] = torch.tensor(self.labels[idx], dtype=torch.long)\n",
    "        return item\n",
    "\n",
    "skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)\n",
    "train_idx, val_idx = next(skf.split(train_df, train_df['target']))\n",
    "df_tr, df_va = train_df.iloc[train_idx].reset_index(drop=True), train_df.iloc[val_idx].reset_index(drop=True)\n",
    "\n",
    "train_loader = DataLoader(PromptAttackDataset(df_tr['text'].values, df_tr['target'].values, tokenizer, MAX_LEN), batch_size=BATCH_SIZE, shuffle=True)\n",
    "val_loader = DataLoader(PromptAttackDataset(df_va['text'].values, df_va['target'].values, tokenizer, MAX_LEN), batch_size=BATCH_SIZE, shuffle=False)\n",
    "test_loader = DataLoader(PromptAttackDataset(test_df['text'].values, None, tokenizer, MAX_LEN), batch_size=BATCH_SIZE, shuffle=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=3, id2label=ID2LABEL, label2id=LABEL2ID).to(device)\n",
    "criterion = nn.CrossEntropyLoss(weight=weights_tensor)\n",
    "optimizer = AdamW(model.parameters(), lr=LR, weight_decay=0.01)\n",
    "total_steps = len(train_loader) * EPOCHS\n",
    "scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=int(total_steps * 0.1), num_training_steps=total_steps)\n",
    "\n",
    "best_macro_f1 = 0.0\n",
    "for epoch in range(EPOCHS):\n",
    "    model.train()\n",
    "    for batch in tqdm(train_loader, desc=f'Epoch {epoch+1} Train'):\n",
    "        optimizer.zero_grad()\n",
    "        out = model(input_ids=batch['input_ids'].to(device), attention_mask=batch['attention_mask'].to(device))\n",
    "        loss = criterion(out.logits, batch['label'].to(device))\n",
    "        loss.backward()\n",
    "        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)\n",
    "        optimizer.step()\n",
    "        scheduler.step()\n",
    "    \n",
    "    model.eval()\n",
    "    preds, trues = [], []\n",
    "    with torch.no_grad():\n",
    "        for batch in val_loader:\n",
    "            out = model(input_ids=batch['input_ids'].to(device), attention_mask=batch['attention_mask'].to(device))\n",
    "            p = torch.argmax(out.logits, dim=1).cpu().numpy()\n",
    "            preds.extend(p)\n",
    "            trues.extend(batch['label'].numpy())\n",
    "    \n",
    "    score = f1_score(trues, preds, average='macro')\n",
    "    print(f'Epoch {epoch+1} Macro F1: {score:.4f}')\n",
    "    if score > best_macro_f1:\n",
    "        best_macro_f1 = score\n",
    "        torch.save(model.state_dict(), 'best_model.pt')\n",
    "print(f'Best Validation Macro F1: {best_macro_f1:.4f}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.load_state_dict(torch.load('best_model.pt'))\n",
    "model.eval()\n",
    "test_preds = []\n",
    "with torch.no_grad():\n",
    "    for batch in tqdm(test_loader, desc='Predicting Test'):\n",
    "        out = model(input_ids=batch['input_ids'].to(device), attention_mask=batch['attention_mask'].to(device))\n",
    "        p = torch.argmax(out.logits, dim=1).cpu().numpy()\n",
    "        test_preds.extend(p)\n",
    "\n",
    "id_col = 'id' if 'id' in test_df.columns else 'Id'\n",
    "sub = pd.DataFrame({'id': test_df[id_col], 'label': [ID2LABEL[i] for i in test_preds]})\n",
    "sub.to_csv('submission.csv', index=False)\n",
    "print('Finished submission.csv! Rows:', len(sub))\n",
    "print(sub['label'].value_counts())\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.10.0"}
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open(r"C:\Users\nguye\Desktop\UIT_SGS_Foodseekers_C1.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

with open(r"C:\Users\nguye\Foodseekers\notebooks\UIT_SGS_Foodseekers_C1.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("FIXED AND SAVED NOTEBOOK!")
