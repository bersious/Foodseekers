# 📋 SỔ TAY TÁC CHIẾN AGENT: TRIỂN KHAI DỰ ÁN "UNRELEASED" (13:30 – 17:30)
# Mục tiêu: Đội Foodseekers hoàn thành ứng dụng mẫu, video demo 2 phút và nộp Google Form trước 17:30

---

## 👥 PHÂN CÔNG TÁC CHIẾN 4 THÀNH VIÊN CHO DỰ ÁN "UNRELEASED"

| Thành viên | Nhánh | Nhiệm vụ chính | Sản phẩm đầu ra |
| :--- | :--- | :--- | :--- |
| **Thiện Nhân** (Lead) | `dev-backend` | Điều phối tổng, khớp kịch bản quay video demo 2 phút trên tệp `prototype/index.html`, kiểm tra file MP4 dưới 100MB và điền biểu mẫu nộp bài Google Form. | File video `demo/unreleased-demo.mp4` & Hoàn tất nộp form trước 17:30. |
| **Minh Ngọc** | `dev-system` | Mở và kiểm tra giao diện ứng dụng mẫu `prototype/index.html` (thử nghiệm luồng chuyển đổi giữa 3 vai trò: Artist, Reviewer, Cloud Admin; kiểm tra sóng âm và cơ chế thu hồi quyền). | Giao diện chạy mượt mà, sẵn sàng bấm quay màn hình. |
| **Anh Thư** | `dev-data` | Kiểm tra lại đoạn văn giới thiệu tiếng Anh dưới 300 từ trong `docs/CHALLENGE_2_WINNING_STRATEGY.md`, đảm bảo chuẩn barem 5 tiêu chí của ban giám khảo. | Nội dung README tiếng Anh hoàn hảo. |
| **Văn Nhân** | `dev-core` | Giữ vững mặt trận Kaggle (Challenge 1), theo dõi notebook Colab chạy xong thì tải file dự đoán nộp Lượt 4 & 5 để bảo vệ thứ hạng top. | File nộp bài Kaggle Lượt 4 & 5. |

---

## 🕒 TIẾN ĐỘ THỰC HIỆN THEO TỪNG KHUNG GIỜ (HẠN CHÓT 18:00)

* **13:30 – 14:15:** Minh Ngọc và Thiện Nhân mở tệp `prototype/index.html` trên trình duyệt Chrome/Edge, tập bấm thử theo kịch bản:
  1. Ở tab Artist: xem 3 bài hát, bấm cấp quyền Bài 1 cho Reviewer Minh.
  2. Ở tab Reviewer: bấm nút phát nhạc giải mã (Waveform nhấp nhô), xem 2 bài kia bị khóa.
  3. Ở tab Admin: xem bảng S3 Bucket chỉ lưu mã hóa, bấm thử nút ép giải mã ➔ bị báo lỗi từ chối.
  4. Ở tab Artist: bấm nút "Revoke Minh's Access" ➔ sang tab Reviewer thấy nhạc dừng và báo lỗi đỏ.
* **14:15 – 15:30:** Thiện Nhân bật phần mềm quay màn hình (`Win + Alt + R` trên Windows), thao tác đúng 120 giây theo kịch bản trong `docs/CHALLENGE_2_WINNING_STRATEGY.md`.
* **15:30 – 16:30:** Lưu video thành file `.mp4`, kiểm tra dung lượng (nếu lớn hơn 100MB thì nén lại), lưu vào thư mục `demo/unreleased-demo.mp4` trong repo.
* **16:30 – 17:15:** Cập nhật đoạn giới thiệu README tiếng Anh vào file `README.md` chính, commit và push lên GitHub.
* **17:15 – 17:30:** Điền link kho lưu trữ GitHub vào Google Form: `https://forms.gle/HRHYjnqB86j1LFS97`. Hoàn thành nộp bài an toàn trước giờ đóng cổng 18:00!
