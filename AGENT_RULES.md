# 🤖 AGENT RULES & OPERATIONAL SPECIFICATION — TEAM FOODSEEKERS
# RMIT Hackathon 2026: Security × Generative AI × Low-Resource Languages

---

## ⚠️ MANDATORY STEP 0: IDENTITY & ROLE VERIFICATION (DO NOT SKIP!)
**CRITICAL INSTRUCTION FOR ALL AI AGENTS (Cursor, Hermes, Cline, Copilot, etc.):**
Before taking ANY action, writing ANY code, or modifying ANY file, you MUST FIRST ask the human user on this machine to identify their role:

> **"Hello! I am initialized with Team Foodseekers' project rules. Before we begin, please confirm: Who am I working with?**
> 1. **Thiện Nhân** (Team Lead / AI Integration & API Modeling)
> 2. **Văn Nhân** (Core Engineer / Kaggle Pipeline & System Integration)
> 3. **Anh Thư** (Data Analyst / Preprocessing & Metric Evaluation)
> 4. **Minh Ngọc** (System Architect / Security Adversarial Testing & Docs)
>
> *Please reply with your name or number so I can activate the correct permissions and stay within my designated workspace.*"

Once the user confirms their identity, you must STRICTLY adopt that role and NEVER touch files or branches assigned to other teammates.

---

## 1. PROJECT CONTEXT & OBJECTIVE
* **Event:** RMIT Hackathon 2026 (Transnational event across Vietnam, Australia, and Malaysia).
* **Core Themes:** 
  1. **Security:** Detecting and mitigating AI vulnerabilities (Prompt Injection, Data Poisoning, Adversarial Attacks).
  2. **Generative AI:** Leveraging and fine-tuning LLMs for accurate, grounded, and reliable outputs.
  3. **Low-Resource Languages:** Overcoming data scarcity and hallucinations in underrepresented languages.
* **Target Platform:** **Kaggle** (Hosted by SkywardAI Labs).
* **Final Deliverables:** Valid Kaggle Notebooks and properly formatted submission files (e.g., `submission.csv`). 
  - ❌ **DO NOT waste time building complex web frontends/GUIs** unless explicitly requested by the user. Everything must serve the Kaggle evaluation leaderboard.

---

## 2. TEAM ROLES & TERRITORY DIVISION (STRICT BOUNDARIES)

### Role 1: Thiện Nhân — AI Integration & Model Architect (Agent 1)
* **Designated Directory:** `/src/models/` and `/notebooks/`
* **Git Working Branch:** `dev-backend`
* **Responsibilities:**
  - Xây dựng mô hình phân loại (Baseline TF-IDF Logistic Regression, PhoBERT, DeBERTa-v3).
  - Tích hợp mô hình ngôn ngữ lớn (Vilao API, Hugging Face).
  - Ghép mô hình (Ensemble) và **là người duy nhất phụ trách nộp file lên Kaggle**.

### Role 2: Văn Nhân — Core Pipeline & Kaggle Runtime (Agent 2)
* **Designated Directory:** `/src/pipeline/` and `/notebooks/`
* **Git Working Branch:** `dev-core`
* **Responsibilities:**
  - Dựng notebook huấn luyện hoàn chỉnh, tối ưu tài nguyên GPU trên Kaggle.
  - Xử lý xung đột thư viện, đảm bảo code chạy trơn tru từ đầu đến cuối không bị văng lỗi.
  - Tự động hóa quá trình xuất dự đoán và kiểm tra tính toàn vẹn của file nộp bài.

### Role 3: Anh Thư — Data Preprocessing & Feature Engineering (Agent 3)
* **Designated Directory:** `/src/features/` and `/data/`
* **Git Working Branch:** `dev-data`
* **Responsibilities:**
  - Tiền xử lý dữ liệu văn bản đa ngữ và xử lý ngôn ngữ ít tài nguyên (Low-Resource Languages).
  - Tách từ tiếng Việt (`underthesea`), loại bỏ dấu chuẩn (`unicodedata`), phát hiện ngôn ngữ (`langdetect`).
  - Trích xuất các đặc trưng bề mặt, ký tự đặc biệt, cấu trúc câu lệnh tấn công (Jailbreak markers).

### Role 4: Minh Ngọc — System Architecture & Adversarial Robustness (Agent 4)
* **Designated Directory:** `/src/attacks/` and `/docs/`
* **Git Working Branch:** `dev-system`
* **Responsibilities:**
  - Xây dựng các kịch bản và câu lệnh tấn công đối kháng (Prompt Injection, Red Teaming).
  - Biên soạn sơ đồ kiến trúc hệ thống, tài liệu kỹ thuật và slide thuyết trình.
  - Theo dõi nhật ký nộp bài tại `/submissions/README.md`.

---

## 3. STRICT GUARDRAILS (THE 5 COMMANDMENTS)

1. **NEVER COMMIT DIRECTLY TO `main`:**
   - Always create and work in your designated feature branch (`dev-backend`, `dev-core`, `dev-data`, `dev-system`).
   - Only the designated human gatekeeper merges code into `main` after verification.

2. **CROSS-DIRECTORY COLLABORATION WITH AUDIT TRAIL:**
   - Members are permitted to modify code across `/src/` subdirectories when integrating pipelines or fixing bugs.
   - **MANDATORY AUDIT:** Immediately after touching another member's code, you MUST append 1 line to `TEAM_CHAT.md` stating clearly: *Which file was modified, what was changed, and why*.

3. **NEVER COMMIT SECRETS OR API KEYS:**
   - All API keys, credentials, and tokens MUST be read from environment variables or a local `.env` file.
   - NEVER hardcode keys directly in `.py` or `.ipynb` files. The `.env` file is git-ignored.

4. **MAINTAIN `requirements.txt`:**
   - Whenever you introduce a new Python library via `pip`, immediately append it to `requirements.txt` with its version.

5. **WRITE SELF-EXPLANATORY CODE & TAKE NOTES:**
   - Include clear docstrings for every function, explaining input arguments, return types, and expected behavior.
   - **MANDATORY NOTE-TAKING & INDEXING (`CODE_INDEX.md`):** Whenever you build a reusable module, data processor, or inference script, you MUST register it with a 1-line entry in `/CODE_INDEX.md` (specifying input, output, and usage).
   - **BEFORE WRITING A FUNCTION:** Check `/CODE_INDEX.md` to see if another agent has already built it. Never duplicate code.
   - If your module is complex, place a mini `README.md` inside your directory (e.g., `/src/data/README.md`) explaining how other agents should consume your outputs.

---

## 4. AGENT-TO-AGENT COMMUNICATION PROTOCOL (`TEAM_CHAT.md`)
To maintain seamless cross-machine synchronization without network sockets, all 4 agents will communicate via **`TEAM_CHAT.md`** (Blackboard Pattern).

### Rule for Reading:
* **BEFORE starting any new task**, run `git pull origin main` (or pull your branch) and **READ the last 5 messages in `TEAM_CHAT.md`**.
* This ensures you know what data or models have just been released by teammates.

### Rule for Writing:
* **AFTER completing any major task, script, or dataset**, you MUST APPEND a 1-2 sentence status message to the bottom of `TEAM_CHAT.md` in **VIETNAMESE**:
  - Format: `* [Agent X - Tên Bạn] (HH:MM): [Nội dung đã làm, file ở đâu, cần ai làm gì tiếp]`
  - Example: `* [Agent 3 - Anh Thư] (10:30): Đã tiền xử lý xong tập train, lưu tại /data/clean_train.csv. Mời Agent 2 vào lấy train.`
  - Example: `* [Agent 1 - Thiện Nhân] (11:00): Đã dựng xong hàm gọi API LLM tại /src/backend/model.py. Đầu ra nhãn 0/1.`
* Commit and push this update so other agents receive the notification!

---

## 5. MERGE PROTOCOL & DEADLINE MANAGEMENT

### Who Merges to `main`
* **ONLY the Team Lead (Thiện Nhân / `bersious`)** merges branches into `main`.
* Other agents MUST NOT merge, MUST NOT force-push, MUST NOT rebase other people's branches.
* If your work is done, push your branch and post a line in `TEAM_CHAT.md`. The Lead will handle the merge.

### Deadline Safety Net (22 – 23/10/2026)
| Day / Time | Target / Action |
| :---: | :--- |
| **Day 1: 09:00 - 10:30** | Baseline TF-IDF + Logistic Regression completed & **Submitted Submission 1** (Unlock 20% Challenge 1 Warm-up marks). |
| **Day 1: 16:00** | Working transformer/feature-rich pipeline committed and tested on GPU. |
| **Day 1: 17:30** | Day 1 best predictions submitted (Submissions 4 - 6). Main branch synchronized. |
| **Day 1: 18:00** | **END OF DAY 1 HACKATHON.** |
| **Day 2: 09:00 - 10:30** | Model ensemble, probability threshold tuning, final submissions (Submissions 8 - 9). |
| **Day 2: 10:45 - 11:15** | Final verification, **Submission 10** logged in `submissions/README.md`. |
| **Day 2: 12:00** | **HARD DEADLINE — COMPETITION CLOSES.** |

### Rules Modification Policy
* **Documentation** (`README.md`, `CODE_INDEX.md`, `TEAM_CHAT.md`): anyone may edit freely.
* **Rules & Structure** (`AGENT_RULES.md`, `.cursorrules`, `.gitignore`, `requirements.txt`, directory layout): **ask the Team Lead first.** Do not modify unilaterally.

---

## 6. ENVIRONMENT & DEPENDENCY NOTES

* **Python version:** The team standard is **Python 3.10–3.13**. Some packages (notably `underthesea` / `sklearn-crfsuite` / `python-crfsuite`) do not have wheels for Python 3.14 and may fail to build. If `pip install -r requirements.txt` fails on `sklearn-crfsuite`, downgrade to Python 3.12 and re-create the venv.
* **Virtual environment:** Always work inside `.venv` (already git-ignored). Never `pip install` into the global Python.
* **Heavy packages:** `torch` is ~120 MB. Start the install early and let it run in the background while you do other work.
* **Git identity:** Run `git config user.name` / `git config user.email` (repo-local, never `--global`) and confirm it is YOUR identity before your first commit.
* **Kaggle:** Only the Team Lead needs Kaggle credentials (`kaggle.json`). Everyone else delivers code via GitHub.
