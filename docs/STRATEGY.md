# 🎯 CHIẾN LƯỢC TÁC CHIẾN CHÍNH THỨC — RMIT HACKATHON 2026
# Đề bài: Multilingual Prompt-Attack Classification (Kaggle)

---

## 1. THÔNG SỐ VÀNG CỦA ĐỀ THI
* **Nhiệm vụ:** Phân loại 3 nhãn: `BENIGN` (62%), `JAILBREAK` (31%), `PROMPT_INJECTION` (7%).
* **Ngôn ngữ:** Tiếng Bồ Đào Nha (`pt`), Pháp (`fr`), Ý (`it`), Anh (`en`).
* **Metric:** **Macro-averaged F1 Score**.
  - ⚠️ `PROMPT_INJECTION` chỉ chiếm 7% nhưng mang giá trị 33.3% tổng điểm! Nếu dự đoán yếu lớp này thì điểm F1 sẽ bị kéo sụt nghiêm trọng.
* **Số lượt nộp:** **CHỈ CÓ ĐÚNG 6 LƯỢT NỘP (6 ATTEMPTS)**.
* **Tên Kaggle Notebook:** `UIT_SGS_Foodseekers_C1`.
* **Hạn nộp:** 18:00 ngày 22/10/2026.

---

## 2. PHÂN BỔ 6 LƯỢT NỘP KAGGLE (CỰC KỲ TIẾT KIỆM & HIỆU QUẢ)
1. **Lượt 1 (09:45 - 10:30):** Nộp ngay mô hình Baseline TF-IDF + Logistic Regression (có `class_weight='balanced'`).
   - *Mục tiêu:* Ăn trọn điểm Challenge 1 (chỉ cần 1 lượt nộp hợp lệ là nhận điểm hoàn thành), kiểm tra thông luồng format CSV (`id,label`).
2. **Lượt 2 (11:30 - 12:00):** Nộp mô hình `protectai/deberta-v3-base-prompt-injection-v2`.
   - *Mục tiêu:* Mô hình này vốn đã được pretrain về an toàn AI và prompt injection, sẽ nhận diện cực tốt nhãn `PROMPT_INJECTION` 7%.
3. **Lượt 3 (13:30 - 14:15):** Nộp mô hình `FacebookAI/xlm-roberta-base`.
   - *Mục tiêu:* Mô hình đa ngữ kinh điển, xử lý xuất sắc các ngôn ngữ Romance (pt, fr, it).
4. **Lượt 4 (15:00 - 15:45):** Nộp mô hình `FacebookAI/xlm-roberta-large` (Huấn luyện trên Kaggle GPU P100/T4).
   - *Mục tiêu:* Nâng trần độ chính xác của Encoder lớn nhất.
5. **Lượt 5 (16:30 - 17:00):** Ensemble (Ghép xác suất giữa DeBERTa Safety + XLM-RoBERTa + Threshold Tuning nhãn hiếm).
6. **Lượt 6 (17:15 - 17:45):** Bản chốt điểm cao nhất trước giờ đóng cổng 18:00.

---

## 3. DANH SÁCH 10 MÔ HÌNH HỢP LỆ (APPROVED BACKBONES)
1. `distilbert/distilbert-base-multilingual-cased` (Baseline nhanh)
2. `jhu-clsp/mmBERT-small`
3. `jhu-clsp/mmBERT-base`
4. `FacebookAI/xlm-roberta-base` (Khuyến nghị 1)
5. `FacebookAI/xlm-roberta-large` (Khuyến nghị 2 - Mạnh nhất)
6. `google/rembert`
7. `protectai/deberta-v3-base-prompt-injection-v2` (Khuyến nghị 3 - Chuyên trị Prompt Injection)
8. `patronus-studio/wolf-defender-prompt-injection`
9. `ibm-granite/granite-3.3-2b-instruct`
10. `mistralai/Mistral-7B-Instruct-v0.3`
