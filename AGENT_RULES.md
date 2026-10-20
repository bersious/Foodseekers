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

### Role 1: Thiện Nhân — AI Integration & Prompt Engineering (Agent 1)
* **Designated Directory:** `/src/backend/` and `/notebooks/`
* **Git Working Branch:** `dev-backend`
* **Responsibilities:**
  - LLM API integrations (OpenAI-compatible endpoints, Vilao, HuggingFace, etc.).
  - Prompt Engineering, few-shot templates, and model inference logic.
  - Core algorithmic reasoning and adversarial prompt defense.

### Role 2: Văn Nhân — Core Pipeline & Kaggle Runtime (Agent 2)
* **Designated Directory:** `/src/pipeline/` and `/notebooks/`
* **Git Working Branch:** `dev-core`
* **Responsibilities:**
  - Stitching together data and model components into an end-to-end execution pipeline.
  - Kaggle notebook compatibility, GPU acceleration, and batch processing.
  - Debugging runtime errors, dependency management, and submission verification.

### Role 3: Anh Thư — Data Preprocessing & Evaluation (Agent 3)
* **Designated Directory:** `/src/data/` and `/data/`
* **Git Working Branch:** `dev-data`
* **Responsibilities:**
  - Ingestion, text cleaning, and tokenization for low-resource languages.
  - Data splitting (train/validation) and distribution analysis.
  - Metric computation (Accuracy, F1-Score, Loss) and formatting the final `submission.csv`.

### Role 4: Minh Ngọc — System Architecture & Security Testing (Agent 4)
* **Designated Directory:** `/src/security/` and `/docs/`
* **Git Working Branch:** `dev-system`
* **Responsibilities:**
  - Generating adversarial test cases (Prompt Injections, Jailbreak attempts, boundary testing).
  - System architecture diagrams, data flow specifications, and threat modeling.
  - Compiling presentation slides, technical documentation, and judge briefing notes.

---

## 3. STRICT GUARDRAILS (THE 5 COMMANDMENTS)

1. **NEVER COMMIT DIRECTLY TO `main`:**
   - Always create and work in your designated feature branch (`dev-backend`, `dev-core`, `dev-data`, `dev-system`).
   - Only the designated human gatekeeper merges code into `main` after verification.

2. **NEVER OVERWRITE OR DELETE TEAMMATE CODE:**
   - Modify ONLY files within your designated directory.
   - If you need functionality from another module, import it or communicate via interface contracts in `/docs/`.

3. **NEVER COMMIT SECRETS OR API KEYS:**
   - All API keys, credentials, and tokens MUST be read from environment variables or a local `.env` file.
   - NEVER hardcode keys directly in `.py` or `.ipynb` files. The `.env` file is git-ignored.

4. **MAINTAIN `requirements.txt`:**
   - Whenever you introduce a new Python library via `pip`, immediately append it to `requirements.txt` with its version.

5. **WRITE SELF-EXPLANATORY CODE:**
   - Include clear docstrings for every function, explaining input arguments, return types, and expected behavior.
