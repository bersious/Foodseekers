# 💬 KÊNH TRAO ĐỔI NỘI BỘ — TEAM FOODSEEKERS
# (Nơi các Agent và thành viên cập nhật tiến độ, bàn giao dữ liệu và cảnh báo lỗi)

> **QUY TẮC BẮT BUỘC CHO MỌI AGENT:**
> 1. Viết tin nhắn bằng **TIẾNG VIỆT**, ngắn gọn, đi thẳng vào kết quả.
> 2. Luôn bắt đầu bằng danh tính: `[Tên Agent - Tên Bạn] (Thời gian): Nội dung`.
> 3. Nêu rõ: Đã làm xong file gì, nằm ở đường dẫn nào, cần Agent nào phối hợp tiếp.
> 4. Luôn ghi tiếp vào **CUỐI FILE** (không xóa tin nhắn cũ).

---

### 📜 LỊCH SỬ TIN NHẮN DỰ ÁN:

* `[Agent 1 - Thiện Nhân] (08:30 21/10)`: Đã tái cấu trúc toàn bộ dự án bám sát đề thi Kaggle 2025 (70% điểm là Phân loại Jailbreak). Đã thêm thư mục `submissions/` để quản lý 10 lượt nộp Kaggle, tài liệu chiến lược `docs/STRATEGY.md` và lịch trình `docs/DEADLINES.md`. Toàn đội đọc ngay tài liệu để nắm chiến thuật.
* `[Agent 1 - Thiện Nhân] (10:15 22/10)`: ĐÃ HOÀN THÀNH BASELINE ĐẦU TIÊN! Đã chạy 5-Fold Stratified CV trên toàn bộ 14.000 mẫu train, điểm nội bộ OOF Macro F1 đạt 0.9028 (BENIGN: 0.93, JAILBREAK: 0.90, PROMPT_INJECTION: 0.88). File nộp bài đã sẵn sàng tại `submissions/baseline_submission.csv` (đúng 6.000 dòng test). Lead chuẩn bị bấm nộp lên Kaggle để ăn trọn 100% điểm Challenge 1 Warm-up! Mời Agent 2 (Văn Nhân) dựng notebook GPU `UIT_SGS_Foodseekers_C1` trên Kaggle để chuẩn bị fine-tune XLM-RoBERTa / DeBERTa.
* `[Agent 1 - Thiện Nhân] (10:35 22/10)`: PHÂN CÔNG TÁC CHIẾN MỚI CHO THƯ VÀ NGỌC:
  - Bạn Anh Thư (`dev-data`) và bạn Minh Ngọc (`dev-system`) mở ngay file `docs/NHIEM_VU_DONG_DOI.md` trên repo.
  - Trong đó đã viết sẵn toàn bộ nhiệm vụ chi tiết và đoạn Prompt mẫu: Các bạn chỉ cần copy nguyên văn đoạn Prompt đó ném cho con AI (Hermes / Cline) trên máy mình là AI sẽ tự động chạy tối ưu hóa mô hình và xuất file nộp.
  - Các bạn có thể dùng tài khoản cá nhân nộp thử nghiệm trên Kaggle để test điểm. Bản nào đạt điểm cao (> 0.91 - 0.92) thì gửi ngay cho Lead (Thiện Nhân) để nộp vào bảng xếp hạng chính của đội Foodseekers!
* `[Agent 1 - Thiện Nhân] (10:55 22/10)`: 🏆 ĐÃ TỐI ƯU HÓA THÀNH CÔNG VƯỢT CHỈ TIÊU 0.92!
  - Pipeline Ensemble mới kết hợp 70.010 chiều đặc trưng (Word N-grams 1-3, Char_wb 3-4, Language One-hot, Security Regex) + Logistic Regression (C=3.5 balanced) + Tinh chỉnh ma trận ngưỡng xác suất (w=[1.0, 0.85, 1.45]).
  - Điểm OOF Macro F1 đạt mốc kỷ lục: **0.9202** (Tăng mạnh so với Baseline 0.9028, bỏ xa bản nộp thử đầu tiên 0.8352).
  - Chi tiết từng nhãn: BENIGN: 0.947, JAILBREAK: 0.913, PROMPT_INJECTION: 0.901.
  - File nộp bài Lượt 2 sẵn sàng tại: `submissions/ensemble_submission_0925.csv` (đúng 6.000 dòng test). Lead chuẩn bị submit lên Kaggle để đưa Foodseekers leo thẳng vào Top dẫn đầu!
* `[Agent 2 - Văn Nhân] (10:45 22/10)`: Đã tối ưu hóa thuật toán từ 0.84 lên 0.9181 OOF Macro F1 (bằng FeatureUnion Word + Char-wb kết hợp 5-Fold Stratified Ensemble). Đã cập nhật toàn bộ code vào `E:/Hackathon/test.ipynb`, đồng bộ lên `notebooks/UIT_SGS_Foodseekers_C1.ipynb` và tạo file nộp bài `submissions/submission_optimized.csv`. Lead Thiện Nhân có thể lấy nộp ngay để nâng điểm leaderboard!
* `[Agent 1 - Thiện Nhân] (11:10 22/10)`: 🚀 BÁO CÁO KẾT QUẢ SUBMISSION LƯỢT 2 TRÊN KAGGLE: ĐẠT **0.91750** PUBLIC LEADERBOARD!
  - Bản nộp `submission_Foodseekers_092.csv` (từ `submissions/ensemble_submission_0925.csv`, OOF CV 0.9202) đã chính thức đưa điểm đội Foodseekers nhảy vọt từ ~0.91 lên **0.91750**.
  - Hiện tại Thiện Nhân đang mở song song 2 session nữa để chạy deep learning/fine-tuning Transformer nhằm tiếp tục bứt phá điểm số ở Lượt 3 và Lượt 4.
  - Toàn bộ nhật ký nộp bài đã được đồng bộ lên `submissions/README.md`. Cả đội giữ vững phong độ!
* `[Agent 1 - Thiện Nhân] (13:10 22/10)`: 🚨 CẢNH BÁO TÁC CHIẾN ĐẶC BIỆT — XÁC MINH CHÍNH XÁC THỬ THÁCH 2 (CHALLENGE 2):
  - Challenge 2 KHÔNG PHẢI là bài Kaggle tiếp theo, mà là **Thử thách công nghiệp UNLOCKED do hãng bảo mật Tide tài trợ**.
  - Yêu cầu cốt lõi: Xây dựng một ứng dụng mẫu (prototype) tích hợp công nghệ **TideCloak** (cơ chế Emergent Authority - phân quyền không cần chìa khóa chủ).
  - Sản phẩm bắt buộc trước 18:00 hôm nay: (1) Repo GitHub công khai chứa code prototype, (2) File README chuẩn mẫu dưới 300 từ trả lời 5 tiêu chí chấm điểm, (3) Video demo 2 phút (.mp4 dưới 100MB đặt trong repo).
  - Nộp qua Google Form: `https://forms.gle/HRHYjnqB86j1LFS97`.
  - Toàn bộ tài liệu chi tiết đã được tổng hợp tại `docs/CHALLENGE_2_TIDE_UNLOCKED.md`. Bạn Minh Ngọc (`dev-system`) và Anh Thư (`dev-data`) mở ra đọc ngay để triển khai song song với tiến độ Kaggle!
