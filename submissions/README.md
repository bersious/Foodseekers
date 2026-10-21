# 📋 SỔ NHẬT KÝ NỘP BÀI KAGGLE (TỐI ĐA 10 LƯỢT NỘP)
# Quy tắc: Điểm đánh giá nội bộ (CV) tăng thì mới được nộp lên Kaggle (LB).

---

| Lượt | Thời gian | Mô tả mô hình & kỹ thuật | Điểm CV nội bộ (ROC AUC) | Điểm Public LB (Kaggle) | Người nộp | Ghi chú & Bài học |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **01** | Ngày 1 | TF-IDF (1-2 gram) + Logistic Regression (C=1.0) | *chờ điền* | *chờ điền* | Thiện Nhân | Ăn 20% điểm Warm-up C1, đo độ lệch CV-LB |
| **02** | Ngày 1 | Thêm đặc trưng độ dài, regex từ khóa cấm, strip accents | *chờ điền* | *chờ điền* | Thiện Nhân | Kiểm tra hiệu quả của tiền xử lý văn bản |
| **03** | Ngày 1 | LightGBM trên bộ đặc trưng trích xuất | *chờ điền* | *chờ điền* | Thiện Nhân | Thử nghiệm mô hình dạng cây |
| **04** | Ngày 1 | PhoBERT base (fine-tune 3 epochs trên Kaggle GPU) | *chờ điền* | *chờ điền* | Thiện Nhân | Mô hình biểu diễn ngữ cảnh tiếng Việt |
| **05** | Ngày 1 | Multilingual BERT / DeBERTa-v3 đa ngữ | *chờ điền* | *chờ điền* | Thiện Nhân | Xử lý low-resource và chuyển ngữ |
| **06** | Ngày 1 | Ensemble (50% PhoBERT + 50% TF-IDF Logistic Regression) | *chờ điền* | *chờ điền* | Thiện Nhân | Kết hợp xác suất |
| **07** | Ngày 1 | Chốt ngày 1 | *chờ điền* | *chờ điền* | Thiện Nhân | Phiên bản tốt nhất ngày 1 |
| **08** | Ngày 2 | Tối ưu ngưỡng cắt xác suất hoặc lọc nhiễu | *chờ điền* | *chờ điền* | Thiện Nhân | Thử nghiệm sáng ngày 2 |
| **09** | Ngày 2 | Ensemble cuối cùng | *chờ điền* | *chờ điền* | Thiện Nhân | Phiên bản hoàn thiện |
| **10** | Ngày 2 | Lượt chốt an toàn cuối cùng | *chờ điền* | *chờ điền* | Thiện Nhân | Dự phòng khẩn cấp trước 11:15 |

---

### Định dạng file nộp hợp lệ:
File `submission.csv` bắt buộc gồm đúng 2 cột:
```csv
id,target
1,0.72
2,0.13
3,0.55
```
* Cột `id`: Định danh mẫu kiểm thử (nguyên vẹn theo `test.csv`).
* Cột `target`: Xác suất dự đoán mẫu là độc hại / jailbreak (số thực từ `0.0` đến `1.0`).
