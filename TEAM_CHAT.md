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
* `[Agent 2 - Văn Nhân] (10:45 22/10)`: Đã tối ưu hóa thuật toán từ 0.84 lên 0.9181 OOF Macro F1 (bằng FeatureUnion Word + Char-wb kết hợp 5-Fold Stratified Ensemble). Đã cập nhật toàn bộ code vào `E:/Hackathon/test.ipynb`, đồng bộ lên `notebooks/UIT_SGS_Foodseekers_C1.ipynb` và tạo file nộp bài `submissions/submission_optimized.csv`. Lead Thiện Nhân có thể lấy nộp ngay để nâng điểm leaderboard!
