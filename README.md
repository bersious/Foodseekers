[![Built with TideCloak](https://tide.org/badges/built-with-tidecloak.svg)](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked)

# SONARA — Zero-Trust Audio/Video Preview Vault

## Project overview

_SONARA is a zero-trust creative pre-release preview vault that eliminates cloud master keys using TideCloak Emergent Authority, allowing artists to share sonara masters with reviewers without risk of server-side leaks._

Built with [TideCloak](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked).

---

### 🌐 Live Production Demo

- **Central Portal:** [https://bersious.io.vn/rmit](https://bersious.io.vn/rmit)
- **Portal 01 · Artist Vault:** [https://bersious.io.vn/rmit/1](https://bersious.io.vn/rmit/1) *(Upload masters, manage DID access, configure preview limits & audio watermarks)*
- **Portal 02 · Reviewer Listening Room (SONARA):** [https://bersious.io.vn/rmit/2](https://bersious.io.vn/rmit/2) *(Browse artists, request access, in-memory stream, leave feedback, tamper protection)*
- **Portal 03 · S3 Oblivious Proxy Inspector:** [https://bersious.io.vn/rmit/3](https://bersious.io.vn/rmit/3) *(Real-time SOC monitoring, root exploit simulation with 0 master keys)*

> **Credentials for Testing:** All demo accounts use password `123`.  
> - *Sample Artists:* `alice_artist`, `endy_producer` (or create a new artist profile).  
> - *Sample Reviewers:* `minh_mastering`, `thu_producer`, `lan_soundcheck`, `nhânn` (or register a new identity).

---

### 1. Vision & originality

Pre-release music and video leaks cost artists and record labels millions of dollars annually, destroying promotional rollouts and creative momentum. Traditional cloud storage platforms (Dropbox, Google Drive, Box) rely on delegated trust: administrators and cloud providers retain access to decryption keys. 

**SONARA** introduces a decentralized, zero-custody creative studio where **no central master key ever exists**. Decryption keys are never stored on disk or server databases — they emerge dynamically in the reviewer's volatile RAM only during authorized playback, synthesized via Tide Fabric Quorum consensus. The moment an artist revokes access, playback terminates instantly within 0.069ms.

### 2. Trust constraint insight

Today, the fear of leaks paralyzes creative collaboration:
- Major artists refuse to send lossless 24-bit FLAC/WAV masters to mixing/mastering engineers remotely.
- Reviewers and radio curators face severe legal liability if a leaked demo is traced back to their inbox.
- Producers are forced to travel physically to studios just to audition a 30-second snippet.

When the trust constraint is removed through cryptographic zero-custody, artists can freely collaborate with global sound designers and label executives instantly, knowing that even a rogue AWS administrator or compromised S3 bucket cannot leak their uncompressed recordings.

### 3. Value & impact

- **For Artists & Record Labels:** Retain 100% sovereign authority over intellectual property. Enforce fine-grained policies such as **Single-Play Self-Destruction** (access automatically revokes upon playback completion) and **Preview Duration Limits** (stream automatically halts at 10s, 15s, or 30s).
- **For Audio Reviewers & Critics:** Stream pristine lossless audio in-memory without storing sonara files on local drives, eliminating legal exposure.
- **Leak Defense Ecosystem:** Built-in acoustic watermarking (periodic audio watermark and AI voice disclaimer) and an active **Tamper Watchdog** that immediately revokes decryption rights if DevTools inspection or screen recording software is detected.

### 4. Why TideCloak matters

Conventional authentication systems (OAuth2, JWT, Keycloak) authenticate users but leave data encryption keys static on backend servers. If a server is compromised, all data is vulnerable.

**TideCloak changes the paradigm:**
- **Emergent Authority:** Decryption keys are split into cryptographic shares across decentralized Quorum nodes. Keys only synthesize *Just-In-Time* (JIT) inside the verified client runtime.
- **Oblivious Proxy Architecture:** The storage backend (S3/Vercel Blob) acts as an oblivious host — it only stores opaque `.enc` binary blobs without holding any decryption capability.
- **Sub-millisecond Revocation:** Access revocation propagates across the Tide Quorum in under 1ms, rendering any cached tokens or network packets permanently un-decryptable.

### 5. Prototype & storytelling

Our live prototype demonstrates a complete end-to-end creative workflow across 3 dedicated portals:

1. **Artist Sovereign Vault (`/rmit/1`):** The artist uploads audio/video tracks, configures a 15-second teaser limit, enables periodic acoustic watermarking, and grants access to specific reviewer DIDs.
2. **Reviewer Listening Room (`/rmit/2`):** The reviewer logs in via SONARA, browses the artist's discography, requests access with one click, streams the master in-memory upon artist approval, and leaves mixing feedback. If DevTools or screen capture is triggered, access is revoked automatically.
3. **S3 Oblivious Proxy Inspector (`/rmit/3`):** Judges can trigger a **Root Admin Dump Simulation**, demonstrating that even with full root privilege on the storage server, 0 master keys exist and 0 bytes of plaintext audio can be extracted.

---

## Setup

```bash
# Clone the repository
git clone https://github.com/bersious/Foodseekers.git
cd Foodseekers

# 1. Run the Prototype locally
# Simply open prototype/index.html (or prototype/1, prototype/2, prototype/3) in any modern web browser
# Or serve via Node / Vite:
npm install
npm run dev

# 2. Run Oblivious Proxy Backend Server
npm run server
# Listening on http://localhost:4000

# 3. Run Security & Exploit Simulation Test Suites
npm test
# Passes 100%: Root exploit mitigation & E2E Quorum consensus tests
```
VIDEO : https://drive.google.com/drive/folders/1YkzRrnUL0_Afxzk7DUh1xtQQpZ2Qvhoc?usp=sharing
---

## 👥 Team Foodseekers — RMIT Hackathon 2026

- **Nguyễn Thành Thiện Nhân** (`bersious`) — *Team Lead & System Architecture*
- **Nguyễn Văn Nhân** (`NguyenNhan1107`) — *Core Backend & Pipeline Engineer*
- **Trần Nguyễn Anh Thư** (`tuna184`) — *Data Analyst & QA*
- **Trần Minh Ngọc** (`tranminhngoc171-bot`) — *Security & Cryptographic Attestation*

---

## 📊 Challenge 1: Multilingual Adversarial Prompt-Attack Classification (Kaggle)

Our team also achieved **Macro-F1 0.9508** on the RMIT Kaggle Challenge 1 leaderboard using an ensemble of multilingual Transformers (XLM-RoBERTa & DeBERTa-v3) with adversarial safety regularization. See `notebooks/` for details.
