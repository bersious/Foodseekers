# 📋 SỔ NHẬT KÝ NỘP BÀI KAGGLE — RMIT HACKATHON 2026
# RÀNG BUỘC: CHỈ CÓ TỐI ĐA 6 LƯỢT NỘP (6 SUBMISSIONS ONLY)
# Metric: Macro-averaged F1 Score

---

| Lượt | Thời gian | Mô hình & Kỹ thuật | Điểm CV nội bộ (Macro F1) | Điểm Public LB (Kaggle) | Người nộp | Ghi chú & Đánh giá |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **01** | 10:15 22/10 | Baseline TF-IDF (35k n-grams) + Logistic Regression (Balanced + Threshold 1.25) | **0.9028** | *đang nộp* | Thiện Nhân | Ăn điểm Challenge 1, 6.000 dòng chuẩn format id,label |
| **02** | Sáng 22/10 | DeBERTa v3 Prompt Injection v2 | *chờ điền* | *chờ điền* | Thiện Nhân | Chuyên biệt hóa nhãn 7% PROMPT_INJECTION |
| **03** | Trưa 22/10 | XLM-RoBERTa base (Multilingual) | *chờ điền* | *chờ điền* | Thiện Nhân | Đánh giá năng lực đa ngữ pt/fr/it/en |
| **04** | Chiều 22/10 | XLM-RoBERTa large (Kaggle GPU) | *chờ điền* | *chờ điền* | Thiện Nhân | Mô hình sâu mạnh nhất |
| **05** | Chiều 22/10 | Ensemble (XLM-RoBERTa + DeBERTa) | *chờ điền* | *chờ điền* | Thiện Nhân | Ghép xác suất đa mô hình |
| **06** | 17:30 | Lượt chốt cuối cùng | *chờ điền* | *chờ điền* | Thiện Nhân | Bản chốt điểm cao nhất trước 18:00 |

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
