# 📋 SỔ NHẬT KÝ NỘP BÀI KAGGLE — RMIT HACKATHON 2026
# RÀNG BUỘC: CHỈ CÓ TỐI ĐA 6 LƯỢT NỘP (6 SUBMISSIONS ONLY)
# Metric: Macro-averaged F1 Score

---

| Lượt | Thời gian | Mô hình & Kỹ thuật | Điểm CV nội bộ (Macro F1) | Điểm Public LB (Kaggle) | Người nộp | Ghi chú & Đánh giá |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **01** | 10:15 22/10 | Baseline TF-IDF (35k n-grams) + Logistic Regression (Balanced + Threshold 1.25) | **0.9028** | **0.91000** | Thiện Nhân | Hoàn thành Warm-up Challenge 1, thông luồng định dạng 6.000 dòng test |
| **02** | 11:00 22/10 | Ensemble N-gram đa tầng (Word 1-3, Char_wb 3-4, 70k feats) + Security Regex + Language Encoding + Logistic Regression (C=3.5 balanced) + Probability Threshold Multiplier ($w=[1.0, 0.85, 1.45]$) (`submission_Foodseekers_092.csv`) | **0.9202** | **0.91750** 🚀 | Thiện Nhân | Nhảy vọt lên 0.91750 Public LB; cải thiện vượt bậc độ nhạy nhãn hiếm PROMPT_INJECTION (F1=0.901) |
| **03** | 12:46 22/10 | **XLM-RoBERTa base** (fine-tune 3 epoch, weighted CE loss, threshold tuning lớp hiếm) — Colab T4 GPU, notebook `UIT_SGS_Foodseekers_C1` | *(val holdout 10%)* | **0.95082** 🔥 | Thiện Nhân | Nhảy vọt từ 0.91750 → **0.95082** nhờ mô hình Transformer đa ngữ. File: `submission.csv`. Xác suất lưu tại `xlmr_test_proba.npy` để ensemble Lượt 5. |
| **04** | Chiều 22/10 | XLM-RoBERTa large (Kaggle GPU) | *chờ điền* | *chờ điền* | Cả đội | Đẩy trần biểu diễn ngữ nghĩa sâu |
| **05** | Chiều 22/10 | Ensemble lai mềm (Soft Voting: Transformer + Feature-Union + Post-Processing) | *chờ điền* | *chờ điền* | Thiện Nhân | Kết hợp thế mạnh của cả 2 hướng tiếp cận |
| **06** | 17:30 22/10 | Lượt chốt cuối cùng | *chờ điền* | *chờ điền* | Thiện Nhân | Bản chốt điểm cao nhất trước giờ đóng cổng 18:00 |

---

### Định dạng file nộp bài chuẩn (6.000 dòng test):
```csv
id,label
t000006,BENIGN
t000007,PROMPT_INJECTION
t000008,JAILBREAK
```
* Cột `id`: Giữ nguyên vẹn mã số từ `test.csv`.
* Cột `label`: Đúng 1 trong 3 chuỗi: `BENIGN`, `JAILBREAK`, `PROMPT_INJECTION`.
