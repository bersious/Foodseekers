# RMIT Hackathon — Đề các năm trước & Suy đoán đề 2026

**Nghiên cứu:** 21/10/2026 · **Nguồn chính:** rmit-hackathon.com, kaggle.com (đọc trực tiếp bằng trình duyệt), rmit.edu.vn, github, huggingface, arxiv

---

## 1. RMIT Hackathon 2025 — "GenAI & Cyber Security" (năm gần nhất, quan trọng nhất)

**Kaggle:** https://www.kaggle.com/competitions/rmit-hackathon-2025
**Thời gian:** 19–20/10/2025 · **Tham gia:** 421 entrants · 318 người · 110 đội · 612 submissions
**Tag:** Binary Classification · NLP · AI · **Metric: ROC AUC**
**Quy mô:** 600+ người, 165 đội, 30 trường (VN + Melbourne). Hơn gấp đôi năm 2024.

### 4 phần thi & tỉ trọng điểm

| Phần | Tên | % | Nội dung |
|---|---|---|---|
| 1 | Fundamentals (warm-up) | **20%** | Dựng môi trường Kaggle, TF-IDF + Logistic Regression, thử DistilBERT/BERT. **Nộp 1 submission hợp lệ = tự động có 20 điểm.** |
| 2 | Protector Model | **50%** | Nhị phân jailbreak vs benign, tối đa hóa ROC AUC. Đây là phần cạnh tranh thật. |
| 3 | Vibe Coding — Play to Impact | **15%** | Làm game web 2D bằng LLM về vấn đề xã hội VN/AU. Chấm thủ công 5 tiêu chí. |
| 4 | The Attacker | **15%** | Đóng vai Red Team, tự tạo prompt jailbreak. Nộp file PKL. Chấm bằng Jailbreak Benchmark Tool. |

→ **70% điểm nằm ở Challenge 1+2 (cùng một bài Kaggle).** Đó là lý do năm nay cũng tập trung Kaggle.

### Challenge 1+2 — Jailbreak Detection (chi tiết)

**Nhiệm vụ:** dự đoán xác suất một prompt là jailbreak (không an toàn) hay benign (an toàn).

**Dataset:**
- Tổng: **5.000** prompt
- Train: **4.000** / Test: **1.000** (nhãn ẩn)
- Cột: `id`, `text`, `label`
- Files: `train.csv`, `test.csv`, `sample_submission.csv` — 3.65 MB, CC BY-NC-SA 4.0

**Format nộp (CSV):**
```csv
id,target
1,0.72
2,0.13
3,0.55
```

**Ràng buộc quan trọng:**
- ⚠️ **Chỉ có 10 lượt nộp.** Phải thử nghiệm cẩn thận, mỗi lượt phải có ý đồ.
- Dùng bất kỳ công cụ, model, framework nào — từ ML truyền thống đến fine-tune LLM.
- Hướng được gợi ý: HuggingFace Transformers, scikit-learn, ensemble, prompt-aware features.
- Yêu cầu nhấn mạnh: **"robust generalization — not just leaderboard overfitting"**

**Đặc tả tên notebook:** `<campus>_<team>_C<challenge>` với `<challenge> ∈ {2,4}`
→ Ví dụ: `SGS_a_C2`, `Hanoi_beautiful_C2`, `MEL_sunny_C4`
→ Campus chỉ dùng chữ cái; team dùng chữ/số/_/-

### Challenge 4 — The Attacker (chi tiết)

- Tạo **5 prompt jailbreak** tự thân.
- Nộp file **PKL** (pickle) chứa list/DataFrame với 3 field bắt buộc:
  - `prompt` — prompt jailbreak tự soạn
  - `result` — phản hồi của model
  - `result_code` — HTTP status (vd 400 = bị chặn)
- Chấm bằng **Jailbreak Benchmark Tool**: chất lượng prompt · hiệu quả vượt safety · đúng format PKL
- Ví dụ tham chiếu: `https://www.kaggle.com/code/aisuko/hanoi-beautiful-c4`

### Challenge 3 — Game web (chi tiết)

Yêu cầu cấu trúc thư mục nộp **rất nghiêm ngặt** — đây là bài học để nhớ cho 2026:
```
game_submission/
├── README.md
├── project_report.pdf      # giới thiệu, chủ đề, impact, tech stack, cơ chế, reflection
├── youtube_link.txt        # CHỈ URL, video ≤7 phút, có voice-over
├── prompts/                # phải nộp TẤT CẢ prompt đã dùng
│   ├── concept_prompts.txt
│   ├── asset_generation_prompts.txt
│   ├── code_generation_prompts.txt
│   └── refinement_prompts.txt
├── game_app/
│   ├── index.html          # Welcome/Menu/Play
│   └── ...
└── screenshots/            # TỐI ĐA 5 ảnh, tên phải đúng
    ├── menu_screen.png
    ├── play_screen1..3.png
    └── results_screen.png
```
- Chỉ HTML/CSS/JS, **front-end thuần, không backend, không cài đặt thêm**.
- Ít nhất 2 màn hình: Menu + Play.
- Repo phải **public** và truy cập không cần đăng nhập.
- Template tham chiếu: https://github.com/TomHuynhSG/MyTeamName_Sample_Game_Project_Hackathon
- Tiêu chí chấm: Relevance & Impact · Creativity & Originality · Gameplay & UX · Technical Execution · Documentation & Reflection
- ⚠️ Lưu ý thực tế: nộp video YouTube sớm (HD/4K mất tới 1 giờ xử lý).

### Kết quả 2025
- **4Knights** (4 sinh viên năm 2 Cybersecurity, RMIT **Hanoi**) — **giải nhất**
- HeinoTee — nhiều hackathon, nhấn mạnh "created an impactful system that worked like a real IT team"
- Lưu ý: đội thắng là **sinh viên năm 2**, đúng bậc của đội Foodseekers.

---

## 2. RMIT Hackathon 2024 — kỳ đầu tiên

**Thời gian:** 8–10/11/2024 · Melbourne + Saigon South + Hanoi
**Quy mô:** 270+ người · 10 trường (RMIT, Melbourne, HUST, UET, HCMUS, HCMUT…)

### 4 challenge
1. Deploy API giống OpenAI trên **Amazon EC2**
2. Mã hóa / giải mã bằng Python
3. Fine-tune mô hình cho **nhị phân phân loại web traffic**
4. *(bất ngờ)* Test độ bền LLM qua **biến đổi ngôn ngữ học** (linguistic modifications)

- Đánh giá bằng **kết hợp AI chấm + xác minh thủ công**.
- **Không challenge nào là bắt buộc** — làm càng nhiều càng tốt điểm.
- Kết quả: PetKulLeon (Melbourne) nhất; Deadline-Haters á nhất; tại TP.HCM có `dahp` và `fintechbois`.

### Bài học rút ra
- **2024: hạ tầng + bảo mật.** 2025: **NLP + jailbreak detection + LLM red-teaming**. 2026: thêm **low-resource languages**.
- Xu hướng dồn dập về **phân loại văn bản bằng mô hình ngôn ngữ**, không phải triển khai hệ thống.

---

## 3. RMIT Hackathon 2026 — thông tin đã biết

**Lịch chính thức:**
- **22/10/2026 (thứ Năm): 8h–18h**
- **23/10/2026 (thứ Sáu): 8h–12h**

**Địa điểm (chọn 1):**
- RMIT Saigon South — 702 Nguyễn Văn Linh, TP.HCM ← *đội Foodseekers chọn chỗ này*
- RMIT Melbourne — B091.01.001, 110 Victoria St, Carlton VIC 3053
- RMIT Hanoi — Handi Resco, 521 Kim Mạ, Giảng Võ, Hà Nội
- Taylor's University Lakeside — Subang Jaya, Selangor, Malaysia

**Format (chưa đổi nhiều từ 2025):**
- **1 warm-up + 2 challenge**
- Ngôn ngữ: **tiếng Anh**
- Nền tảng: **Kaggle**, do **SkywardAI Labs** tổ chức
- ⚠️ **"Specific challenge details will be revealed on the hackathon day"** — đề chưa công bố
- Mỗi đội **4 người**, **bắt buộc cùng ở một cơ sở**, không online/khác cơ sở
- Miễn phí · Giải thưởng tổng **tới 100 triệu đồng**

**Đối tác 2026:** Tide (Industry Challenge Sponsor — bảo mật zero-knowledge) · DesignLive/Compnow · Katalon · Orange Logic Vietnam · Taylor's

### Thay đổi so với 2025
| | 2025 | 2026 |
|---|---|---|
| Chủ đề | GenAI & Cyber Security | + **Low-Resource Languages** |
| Số challenge | 4 (2 chung + 2 riêng) | **1 warm-up + 2 challenge** |
| Cơ sở | Melbourne + VN | + **Malaysia** |
| Tổng điểm Kaggle | 70% | nhiều khả năng **≥70%** |

---

## 4. Suy đoán đề 2026 (mức độ tin cậy: trung bình-cao)

**Pattern ổn định qua 2 năm:** phần lớn điểm nằm ở **một bài Kaggle phân loại nhị phân văn bản**, chấm **ROC AUC**, nộp CSV.

**Suy đoán khả dĩ nhất — Jailbreak detection đa ngôn ngữ:**
- Ngữ cảnh: nghiên cứu của Brown (Deng & colleagues) chứng minh **chỉ cần dịch prompt độc hại sang ngôn ngữ low-resource là vượt được bộ lọc an toàn của LLM**, tỉ lệ thành công tăng mạnh. Kết hợp với MultiJail (ICLR 2024) — phân loại an toàn theo ngôn ngữ, xếp **Vietnamese = high-resource**, **Bengali/Swahili/Javanese = low-resource**.
- Nghĩa là: đề 2026 nhiều khả năng cho prompt **nhiều ngôn ngữ** và yêu cầu phân loại jailbreak/benign **xuyên ngôn ngữ**.
- Hệ quả: mô hình tiếng Anh đơn thuần sẽ **tụt điểm mạnh** trên nhóm low-resource.

**Dạng đề khả dĩ khác:** đo độ chính xác của LLM trên ngôn ngữ thiếu dữ liệu (dịch thuật, tóm tắt, phân loại), hoặc phát hiện prompt injection có chèn ngôn ngữ lạ.

---

## 5. Tài nguyên nên chuẩn bị trước (đề chưa biết nhưng nhiều khả năng dùng)

### Dữ liệu jailbreak mở
| Nguồn | Mô tả |
|---|---|
| **MultiJail** — `DAMO-NLP-SG/multilingual-safety-for-LLMs` | 315 prompt EN dịch thủ công sang 9 ngôn ngữ (zh/it/vi cao; ar/ko/th trung bình; bn/sw/jv thấp). Framework Self-Defence. ICLR 2024. |
| **centrepourlasecuriteia/jailbreak-dataset** (HF) | **6.406 dòng, 35 kỹ thuật**, 720 prompt gốc × 35 biến thể. Có nhóm riêng **`low_resource_language` (6 kỹ thuật, 646 dòng)** — trùng khớp chủ đề 2026 nhất. Kỹ thuật: Adversarial Suffixes, ASCII Art, Cognitive & Psychological, DAP, Encoding/Cyphering, FSH, Structural Obfuscation, TokenBreak. Cần xin access. |
| **Brown University** (Deng et al.) | Bài "Low-Resource Languages Jailbreak GPT-4", có PDF công khai. Nhãn 3 loại: BYPASS / REJECT / UNCLEAR. |
| Kaggle 2025 dataset | 5.000 prompt jailbreak/benign, CC BY-NC-SA 4.0. Cùng cấu trúc rất có thể được tái dùng. |

### Mô hình tiếng Việt nên biết
- `vinai/phobert-base`, `vinai/bartpho-xlm-r-large`
- `BAAI/bge-m3` (đa ngôn ngữ, retrieval tốt)
- `sentence-transformers` để so khớp ngữ nghĩa đa ngôn ngữ
- `underthesea` — đã cài & test chạy OK trên Python 3.14 của máy Lead

### Kỹ thuật thường thắng ở bài nhị phân văn bản
1. TF-IDF + Logistic Regression (baseline chắc chắn có điểm)
2. Fine-tune BERT/RoBERTa/phobert (điểm tốt)
3. Ensemble nhiều seed + threshold tuning
4. Xử lý **mất cân bằng ngôn ngữ** — đây là chỗ 2026 nhiều khả năng ra đề
5. Tăng dữ liệu: dịch ngược, tạo synthetic bằng LLM (hướng nghiên cứu EACL 2026 chính là: dùng LLM sinh dữ liệu cho low-resource)

---

## 6. Sai lầm cần tránh (rút từ lịch sử thi)

- ❌ Không cài cả 4 máy trước lúc thi — dành thời gian đó cho việc thật
- ❌ Không xây web/GUI phức tạp — mọi thứ phải phục vụ bảng xếp hạng Kaggle
- ❌ Không đổi tool giữa chừng — giờ học tool mới lúc 8h sáng là tự tạo thảm hoạ
- ❌ Không dùng hết 10 lượt nộp một cách mù quáng
- ❌ Overfit leaderboard — đề 2025 nhấn mạnh generalization
- ❌ Quên nộp prompts/ + README + report khi bài yêu cầu tài liệu
- ❌ Để video YouTube chưa xử lý xong vào phút cuối
- ⚠️ Chỉ 1 người nộp Kaggle (Lead) — tránh trùng submission & tranh quyền

---

## 7. Việc cần làm ngay (deadline 22/10 8h)

1. Sửa Deadline Safety Net trong `AGENT_RULES.md`: hiện ghi 22/10 18:00 nhưng thực tế **22/10 8h–18h + 23/10 8h–12h**
2. Ghi file này vào repo làm tài liệu chung (docs/)
3. Chốt model dùng trong thi: `Minimax-M3` (rẻ nhất, 200/500 đ) cho phần code dài; `gemini-4-argon` khi bí
4. Quyết định tool cho 3 bạn: **Cline** (VS Code, miễn phí, OpenAI Compatible) — KHÔNG dùng Cursor vì gói free đã chặn BYOK