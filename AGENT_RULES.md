# 🤖 HERMES AGENT OPERATIONAL SPECIFICATION — TEAM FOODSEEKERS
# RMIT Hackathon 2026: Security × Generative AI × Low-Resource Languages
# Nhiệm vụ chính thức: Multilingual Prompt-Attack Classification (Kaggle)

---

## 🎯 1. ĐỀ THI CHÍNH THỨC ĐÃ CÔNG BỐ (OFFICIAL CHALLENGE SPECS)
- **Tên cuộc thi:** RMIT HACKATHON 2026 (Nền tảng: Kaggle & RMIT RACE Cloud).
- **Bài toán:** **Phân loại 3 nhãn câu lệnh tấn công đa ngữ (Multilingual 3-Class Classification)**.
  - Ngôn ngữ trong dữ liệu: **Tiếng Bồ Đào Nha (pt), Tiếng Pháp (fr), Tiếng Ý (it) và Tiếng Anh (en)**.
  - 3 Nhãn phân loại:
    1. `BENIGN` (62% tập train): Yêu cầu bình thường, an toàn của người dùng.
    2. `JAILBREAK` (31% tập train): Nỗ lực thao túng để AI phá vỡ quy tắc an toàn.
    3. `PROMPT_INJECTION` (7% tập train — Nhãn hiếm!): Nỗ lực chiếm quyền điều khiển chỉ dẫn hệ thống của mô hình.
- **Thang đo đánh giá (Evaluation Metric):** **Macro-averaged F1 Score**.
  - *Cực kỳ quan trọng:* Macro F1 tính trọng số trung bình ngang nhau (33.3%) cho cả 3 nhãn. Nhãn hiếm `PROMPT_INJECTION` chỉ chiếm 7% nhưng quyết định 1/3 điểm số toàn bài! Bắt buộc phải xử lý mất cân bằng lớp (class weights / focal loss / threshold tuning).
  - Dự đoán toàn bộ `BENIGN` chỉ đạt ~0.26 điểm. Điểm tối đa là 1.0.
- **Tập dữ liệu:**
  - `train.csv`: 14.000 dòng (`id`, `text`, `language`, `label`).
  - `test.csv`: 6.000 dòng (`id`, `text`, `language`).
  - `sample_submission.csv`: 6.000 dòng (`id`, `label`).
- **Quy cách file nộp bài (`submission.csv`):**
  - Gồm đúng 2 cột: `id` và `label`.
  - Cột `label` là chuỗi văn bản: `BENIGN`, `JAILBREAK` hoặc `PROMPT_INJECTION`.
- **RÀNG BUỘC SỐNG CÒN:** **CHỈ CÓ ĐÚNG 6 LƯỢT NỘP KAGGLE (6 SUBMISSIONS ONLY)**.
- **Quy tắc đặt tên Kaggle Notebook:**
  - Bắt buộc theo định dạng: `<university>_<campus>_<team>_C1`
  - Tên chuẩn của đội mình: `UIT_SGS_Foodseekers_C1`
- **Thời gian kết thúc:** **ĐÚNG 18:00 HÔM NAY (22/10/2026)**.

---

## 📦 2. DANH SÁCH MÔ HÌNH ĐƯỢC PHÉP SỬ DỤNG (APPROVED MODELS ONLY)
Ban tổ chức quy định giải pháp BẮT BUỘC xây dựng trên 1 trong các mô hình nguồn mở sau (không dùng backbone ngoài):
1. `distilbert/distilbert-base-multilingual-cased` (Encoder - Baseline nhanh nhất)
2. `jhu-clsp/mmBERT-small` (Encoder - Nhẹ, đa ngữ)
3. `jhu-clsp/mmBERT-base` (Encoder - Đa ngữ mạnh)
4. `FacebookAI/xlm-roberta-base` (Encoder - Rất mạnh về tiếng pt/fr/it/en)
5. `FacebookAI/xlm-roberta-large` (Encoder - Mô hình mạnh nhất, cần VRAM GPU lớn)
6. `google/rembert` (Encoder - Đa ngữ, dùng batch size 8)
7. `protectai/deberta-v3-base-prompt-injection-v2` (Được huấn luyện sẵn về an toàn AI & Prompt Injection - RẤT TIỀM NĂNG)
8. `patronus-studio/wolf-defender-prompt-injection` (Được huấn luyện sẵn về phát hiện tấn công)
9. `ibm-granite/granite-3.3-2b-instruct` (LLM nhỏ - Fine-tune / LoRA)
10. `mistralai/Mistral-7B-Instruct-v0.3` (LLM lớn - Fine-tune / LoRA)

---

## 👥 3. PHÂN VAI TÁC CHIẾN ĐỘI FOODSEEKERS
Cả 4 máy chạy Hermes Agent phối hợp trên cùng một chuỗi dữ liệu (Pipeline):
* **Thiện Nhân (`dev-backend`):** Team Lead — Xây dựng mô hình (Baseline, RoBERTa/DeBERTa), quản lý và bấm nộp bài Kaggle (duy nhất giữ quyền nộp để bảo toàn 6 lượt nộp).
* **Văn Nhân (`dev-core`):** Core Engineer — Tạo notebook Kaggle `UIT_SGS_Foodseekers_C1`, bật GPU T4/P100, fine-tune mô hình Transformers và xuất file dự đoán.
* **Anh Thư (`dev-data`):** Data Analyst — Phân tích dữ liệu 4 thứ tiếng (pt, fr, it, en), trích xuất đặc trưng câu lệnh tấn công, xử lý mất cân bằng lớp (7% `PROMPT_INJECTION`).
* **Minh Ngọc (`dev-system`):** System Architect — Báo cáo kỹ thuật, tài liệu giải pháp, hỗ trợ kiểm thử đối kháng và ghi nhật ký lượt nộp.

---

## 🛡️ 4. NGUYÊN TẮC KỸ THUẬT & AN TOÀN HỆ THỐNG
1. **Làm việc trên nhánh riêng:** Chỉ commit và push vào nhánh `dev-*` của mình. Duy nhất Team Lead mới gộp vào `main`.
2. **Tuyệt đối không lưu API Key vào code:** Dùng biến môi trường hoặc file `.env`.
3. **Phối hợp liên thư mục linh hoạt:** Được quyền gọi và sửa chéo code trong `src/`, hoàn thành module mới thì ghi 1 dòng ngắn gọn vào `TEAM_CHAT.md`.
4. **Chiến thuật 6 lượt nộp:**
   - **Lượt 1 (Warm-up):** Nộp Baseline ngay trong 30–45 phút đầu để ăn trọn điểm Challenge 1 và kiểm tra thông luồng.
   - **Lượt 2 - 3:** Nộp mô hình `xlm-roberta-base` hoặc `deberta-v3-base-prompt-injection-v2`.
   - **Lượt 4 - 5:** Nộp mô hình `xlm-roberta-large` hoặc Ensemble kết hợp xử lý cân bằng lớp.
   - **Lượt 6:** Bản chốt an toàn trước 17:30.
