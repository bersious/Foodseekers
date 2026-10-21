# 🎯 CHIẾN LƯỢC TÁC CHIẾN — TEAM FOODSEEKERS
# Phân tích từ dữ liệu RMIT Hackathon 2024 - 2025 & Định hướng 2026

---

## 1. BẢN CHẤT CUỘC THI & TRỌNG TÂM ĐIỂM SỐ
Qua phân tích đề thi thực tế năm 2025 trên Kaggle (tổ chức bởi SkywardAI Labs):
* **70% tổng điểm** nằm ở bài toán **Phân loại nhị phân phát hiện Jailbreak (Challenge 1 & 2)**.
* **Thang đo:** Đánh giá bằng **ROC AUC** trên tập dữ liệu (5.000 prompt: 4.000 train, 1.000 test).
* **Ràng buộc sống còn:** Toàn bộ cuộc thi **CHỈ CÓ 10 LƯỢT NỘP KAGGLE**. Mỗi lượt nộp phải có mục đích đo đạc rõ ràng, tuyệt đối không nộp hú họa.
* **Trục mới năm 2026 (Low-Resource Languages):** Đề thi kết hợp ngôn ngữ ít tài nguyên vào an toàn AI. Các câu lệnh tấn công có thể được dịch sang tiếng Việt, tiếng Mã Lai, hoặc trộn ngôn ngữ để vượt bộ lọc an toàn. Mô hình chỉ học tiếng Anh sẽ thất bại.

---

## 2. QUY TRÌNH PHÁT TRIỂN THEO DÒNG DỮ LIỆU (PIPELINE)
Không chia rẽ nhóm theo các ngách rời rạc. Cả 4 thành viên cùng vận hành một chuỗi dữ liệu thống nhất:

```text
[Dữ liệu thô train.csv]
       │
       ▼
 1. TIỀN XỬ LÝ & ĐẶC TRƯNG (src/features/)
    ├── Chuẩn hóa tiếng Việt/đa ngữ, giải mã Base64, Leetspeak
    └── Trích xuất độ dài, ký tự đặc biệt, regex từ khóa nguy hiểm
       │
       ▼
 2. XÂY DỰNG MÔ HÌNH (src/models/)
    ├── Baseline: TF-IDF + Logistic Regression / LightGBM (Chắc chắn có điểm)
    └── Advanced: Fine-tune PhoBERT / DeBERTa-v3 / Multilingual-BERT
       │
       ▼
 3. TÍCH HỢP ĐẦU CUỐI (src/pipeline/)
    ├── Đánh giá nội bộ qua 5-Fold Stratified Cross-Validation (CV)
    └── Xuất file dự đoán xác suất (0.0 đến 1.0)
       │
       ▼
 4. BẢNG NỘP BÀI (submissions/)
    └── Lưu file CSV, ghi nhật ký điểm CV so với điểm Leaderboard (LB)
```

---

## 3. CHIẾN LƯỢC DÙNG 10 LƯỢT NỘP KAGGLE
* **Lượt 1 (Mở khóa 20% điểm Warm-up):** Nộp ngay mô hình cơ sở TF-IDF + Logistic Regression để đảm bảo có điểm hợp lệ đầu tiên và đo độ lệch giữa điểm nội bộ (CV) và bảng xếp hạng (LB).
* **Lượt 2 - 4 (Tối ưu tiền xử lý & Feature Engineering):** Thử nghiệm làm sạch văn bản đa ngữ, bổ sung đặc trưng regex và độ phức tạp câu.
* **Lượt 5 - 7 (Mô hình Transformer tiền huấn luyện):** Fine-tune PhoBERT hoặc Multilingual BERT.
* **Lượt 8 - 9 (Ensemble / Ghép mô hình):** Kết hợp xác suất từ mô hình Transformer và mô hình cây (LightGBM).
* **Lượt 10 (Dự phòng khẩn cấp):** Bản chốt trước 17:00 ngày cuối.

---

## 4. BỘ CÔNG CỤ & MODEL GỢI Ý
* **Tiền xử lý tiếng Việt:** Sử dụng `underthesea` (tách từ), `unicodedata` loại bỏ dấu chuẩn, `langdetect` phân loại ngôn ngữ.
* **Mô hình khuyến nghị:** `vinai/phobert-base`, `microsoft/mdeberta-v3-base`.
* **Trợ lý lập trình tại chỗ:** Cài extension **Cline** trên VS Code, trỏ API Vilao (`https://api.vilao.ai/v1`), dùng model `gemini-3.8-flash` hoặc `Minimax-M3` để tiết kiệm và chính xác.
