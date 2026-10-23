[![Built with TideCloak](https://tide.org/badges/built-with-tidecloak.svg)](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked)

# 🏆 Foodseekers — RMIT Hackathon 2026 (Saigon South Campus)
### Cross-Border AI Security, Generative AI & Low-Resource Cryptographic Defense
> **Team Foodseekers:** Nguyễn Thành Thiện Nhân (Lead), Nguyễn Văn Nhân, Trần Nguyễn Anh Thư, Trần Minh Ngọc.  
> **Affiliation:** University of Information Technology (UIT), VNU-HCM.

---

## 🎯 Executive Summary & Competition Track Structure

Our repository is cleanly divided into the two official competition challenges:
1. **Challenge 1 (Kaggle Leaderboard):** *Multilingual Prompt-Attack Classification* (3 Classes: `BENIGN`, `JAILBREAK`, `PROMPT_INJECTION` across Portuguese, French, Italian, and English). Chaired via Kaggle Leaderboard — **Achieved Top Score: Public 0.96496 / Private 0.96301 (Macro F1)**.
2. **Challenge 2 (Tide Unlocked / RACE Cloud):** *SONARA — Zero-Trust Audio/Video Master Preview Vault*. Live production studio powered by TideCloak Emergent Authority.

---

## 📊 CHALLENGE 1: Kaggle Multilingual Prompt-Attack Defense

### 🏅 Official Leaderboard Track Record (6 Submissions Limit)
All submission files and verified scores are cataloged in `submissions/`:

| Attempt | Timestamp | Strategy & Architecture | Public Score | Private Score | Status |
| :---: | :---: | :--- | :---: | :---: | :---: |
| **01** | Day 1 Morning | Baseline TF-IDF (35k n-grams) + Logistic Regression (Balanced) | `0.83528` | `0.84635` | ✅ Warm-up Pass |
| **02** | Day 1 Midday | Hybrid Word-Char Ensemble + Dynamic Threshold Tuning (w=[1.0, 0.85, 1.45]) | `0.95082` | `0.94378` | 🚀 Major Jump |
| **03** | Day 1 Final | **XLM-RoBERTa + DeBERTa-v3 Weighted Loss & Stratified Validation (WIN)** | **`0.96496`** | **`0.96301`** | 🏆 **CHOSEN FINAL** |

### 📁 Challenge 1 Artifacts & Training Code
- **Final Winner Submission File:** [`submissions/submission_final_09630.csv`](submissions/submission_final_09630.csv) *(Matches `submission (2).csv` from win folder — Public: 0.96496, Private: 0.96301)*.
- **Official Offline Kaggle Notebook:** [`notebooks/UIT_SGS_Foodseekers_C1_Kaggle_Offline.ipynb`](notebooks/UIT_SGS_Foodseekers_C1_Kaggle_Offline.ipynb) *(100% Offline for Kaggle GPU T4 environments)*.
- **Official Google Colab Pipeline:** [`notebooks/COLAB_RUN_FOODSEEKERS_XLM_ROBERTA.ipynb`](notebooks/COLAB_RUN_FOODSEEKERS_XLM_ROBERTA.ipynb) *(T4 GPU pipeline with class-weighted Cross-Entropy loss)*.
- **Local Feature Engineering Scripts:** [`src/pipeline/`](src/pipeline/).

---

## 🔒 CHALLENGE 2: SONARA — Zero-Trust Music Sovereign Vault

### 🌐 Live Production Demo
- **Central Portal:** [https://bersious.io.vn/rmit](https://bersious.io.vn/rmit)
- **Portal 01 · Artist Vault:** [https://bersious.io.vn/rmit/1](https://bersious.io.vn/rmit/1) *(Lossless master upload, cover art customizer, bidirectional block, acoustic watermarks)*
- **Portal 02 · Reviewer Listening Room:** [https://bersious.io.vn/rmit/2](https://bersious.io.vn/rmit/2) *(Real-time search, sort by tracks/date, interactive seek timeline, in-memory stream)*
- **Portal 03 · S3 Oblivious Proxy Inspector:** [https://bersious.io.vn/rmit/3](https://bersious.io.vn/rmit/3) *(SOC telemetry, rogue root admin exploit simulator)*

> **Video Demo (2 Minutes):** [Google Drive Video Link](https://drive.google.com/drive/folders/1YkzRrnUL0_Afxzk7DUh1xtQQpZ2Qvhoc?usp=sharing)

---

### Project Overview (Answers to the 5 Judging Prompts)

#### 1. Vision & Originality
Pre-release music and media leaks cost the global entertainment industry billions of dollars annually, destroying promotional rollouts and creative momentum. Traditional cloud storage platforms (Dropbox, Google Drive, Box) rely on delegated trust: administrators and cloud providers retain access to decryption keys. 

**SONARA** introduces a decentralized, zero-custody creative studio where **no central master key ever exists**. Decryption keys are never stored on disk or server databases — they emerge dynamically in the reviewer's volatile RAM only during authorized playback, synthesized via Tide Fabric Quorum consensus. The moment an artist revokes access, playback terminates instantly within 0.069ms.

#### 2. Trust Constraint Insight
Today, the fear of leaks paralyzes creative collaboration:
- Major artists refuse to send lossless 24-bit FLAC/WAV masters to mixing/mastering engineers remotely.
- Reviewers and radio curators face severe legal liability if a leaked demo is traced back to their inbox.
- Producers are forced to travel physically to studios just to audition a 30-second snippet.

When the trust constraint is removed through cryptographic zero-custody, artists can freely collaborate with global sound designers and label executives instantly, knowing that even a rogue AWS administrator or compromised S3 bucket cannot leak their uncompressed recordings.

#### 3. Value & Impact
- **For Artists & Record Labels:** Retain 100% sovereign authority over intellectual property. Enforce fine-grained policies such as **Single-Play Self-Destruction** (access automatically revokes upon playback completion) and **Preview Duration Limits** (stream automatically halts at 10s, 15s, or 30s).
- **For Audio Reviewers & Critics:** Stream pristine lossless audio in-memory without storing unreleased files on local drives, eliminating legal exposure.
- **Leak Defense Ecosystem:** Built-in acoustic watermarking (periodic audio watermark and AI voice disclaimer) and an active **Tamper Watchdog** that immediately revokes decryption rights if DevTools inspection or screen recording software is detected.

#### 4. Why TideCloak Matters
Conventional authentication systems (OAuth2, JWT, Keycloak) authenticate users but leave data encryption keys static on backend servers. If a server is compromised, all data is vulnerable.

**TideCloak changes the paradigm:**
- **Emergent Authority:** Decryption keys are split into cryptographic shares across decentralized Quorum nodes. Keys only synthesize *Just-In-Time* (JIT) inside the verified client runtime.
- **Oblivious Proxy Architecture:** The storage backend (S3/Vercel Blob) acts as an oblivious host — it only stores opaque `.enc` binary blobs without holding any decryption capability.
- **Sub-millisecond Revocation:** Access revocation propagates across the Tide Quorum in under 1ms, rendering any cached tokens or network packets permanently un-decryptable.

#### 5. Prototype & Storytelling
Our live prototype demonstrates a complete end-to-end creative workflow across 3 dedicated portals:
1. **Artist Sovereign Vault (`/rmit/1`):** The artist uploads audio/video tracks, configures preview limits, sets acoustic watermarking, and grants access to specific reviewer DIDs or blocks disruptive accounts.
2. **Reviewer Listening Room (`/rmit/2`):** The reviewer logs in via SONARA, searches and sorts artists, requests access with one click, streams the master in-memory upon artist approval, and leaves mixing feedback. Interactive timeline progress bar allows seeking without saving unencrypted bytes to disk.
3. **S3 Oblivious Proxy Inspector (`/rmit/3`):** Judges can trigger a **Root Admin Dump Simulation**, demonstrating that even with full root privilege on the storage server, 0 master keys exist and 0 bytes of plaintext audio can be extracted.

---

## 🛠️ Local Development & Quick Start

```bash
# Clone the repository
git clone https://github.com/bersious/Foodseekers.git
cd Foodseekers

# 1. Run the Prototype locally
npm install
npm run dev

# 2. Run Oblivious Proxy Backend Server
npm run server
# Listening on http://localhost:4000

# 3. Run Security & Exploit Simulation Test Suites
npm test
# Passes 100%: Root exploit mitigation & E2E Quorum consensus tests
```

---

## 👥 Team Foodseekers — RMIT Hackathon 2026
- **Nguyễn Thành Thiện Nhân** (`bersious`) — *Team Lead & System Architecture*
- **Nguyễn Văn Nhân** (`NguyenNhan1107`) — *Core Backend & Pipeline Engineer*
- **Trần Nguyễn Anh Thư** (`tuna184`) — *Data Analyst & QA*
- **Trần Minh Ngọc** (`tranminhngoc171-bot`) — *Security & Cryptographic Attestation*
