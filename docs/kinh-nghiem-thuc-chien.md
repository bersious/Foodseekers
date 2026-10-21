# 🏆 KINH NGHIỆM THỰC CHIẾN XƯƠNG MÁU — RMIT HACKATHON
# Đúc kết từ các đội vô địch (4Knights, Deadline-Haters, dahp) & Bài học thực tế

---

## 1. KINH NGHIỆM PHẦN CỨNG & HẠ TẦNG TẠI HỘI TRƯỜNG (SAIGON SOUTH)
1. **Mạng Wifi tại hội trường chắc chắn sẽ nghẽn:**
   * Hơn 100 đội (400–500 người) cùng lúc tải model (Hugging Face nặng hàng trăm MB đến GB) sẽ khiến Wifi bị nghẽn (throttling/timeout).
   * **Giải pháp của đội mình:** Chuẩn bị sẵn 4G/phát hotspot dự phòng. Môi trường `.venv` trên máy cậu đã cài đủ 23 thư viện từ đêm nay, sáng mai không cần tốn băng thông tải thêm gì nữa!
2. **Kaggle GPU Quota (Hạn mức 30 giờ GPU/tuần):**
   * Đừng để cả 4 người cùng bấm Train trên 1 tài khoản Kaggle.
   * **Phân chia:** Mỗi bạn dùng tài khoản Kaggle cá nhân của mình để chạy thử nghiệm các nhánh nhỏ (Fold riêng), chỉ gửi file dự đoán hoặc code tốt nhất cho Lead (Thiện Nhân) ghép lại.

---

## 2. KINH NGHIỆM TÁC CHIẾN KAGGLE (TRÁNH CẠN 10 LƯỢT NỘP)
1. **Lỗi "Ảo tưởng điểm số" (Overfitting Public Leaderboard):**
   * Tập test của Kaggle thường chia làm 2 phần: **Public LB** (chấm trên ~30% test, hiển thị ngay) và **Private LB** (chấm trên 70% còn lại, chỉ mở khi hết giờ để trao giải).
   * Rất nhiều đội thấy điểm Public cao vút (0.98) do overfit từ khóa, nhưng khi đóng thi điểm Private rơi tự do xuống 0.70.
   * **Nguyên tắc vàng:** Luôn tin vào điểm **Cross-Validation (CV) 5-Fold nội bộ**. Nếu CV tăng thì mới nộp. Nếu CV giảm mà Public LB tăng thì đó là bẫy học vẹt!
2. **Kỹ thuật Ensemble (Ghép mô hình) — Bí quyết của các đội Top 1:**
   * Đừng bao giờ nộp một mô hình duy nhất. Hãy ghép:
     - 1 Mô hình TF-IDF + Logistic Regression (Bắt từ khóa cực nhạy)
     - 1 Mô hình Transformer PhoBERT / DeBERTa (Hiểu ngữ cảnh sâu)
   * Lấy trung bình xác suất có trọng số của cả 2. Độ ổn định sẽ vô địch.

---

## 3. KINH NGHIỆM ĐỐI MẶT VỚI BAN GIÁM KHẢO (PRESENTATION & JUDGING)
Ban giám khảo RMIT gồm các chuyên gia bảo mật từ **NAB, Tide, Katalon, RMIT RACE**:
1. **Họ không chỉ nhìn vào điểm số trên màn hình:**
   * Giám khảo luôn hỏi: *"Tại sao mô hình của bạn đưa ra quyết định đó? Làm sao bạn chứng minh mô hình không bị lừa khi gặp một ngôn ngữ lạ hoàn toàn?"*
2. **Cách trả lời ăn điểm tuyệt đối:**
   * Trình bày rõ ràng: Đội em xây dựng **bộ đặc trưng lai (Hybrid Features)** gồm cả cấu trúc ngữ pháp, đo lường độ hỗn loạn (Entropy), và kết hợp với mô hình ngôn ngữ sâu.
   * Chỉ ra rõ ràng các trường hợp biên (Edge Cases): *"Đây là cách bọn em phát hiện khi kẻ tấn công trộn tiếng Anh với tiếng Việt không dấu (Code-Switching)..."*
3. **Sự chuyên nghiệp trong Repo GitHub:**
   * Ban giám khảo sẽ chấm điểm cả phong cách kỹ thuật (Engineering Standards): Repo sạch sẽ, có `README.md`, có sổ tay `submissions/`, có lịch trình `DEADLINES.md` — đây là điểm cộng cực lớn giúp đội mình nổi bật so với các nhóm làm tự phát!

---

## 4. CHIẾN THUẬT PHÂN BỔ NĂNG LƯỢNG CHO 4 THÀNH VIÊN
* **Sáng (09:00 - 12:00):** Ăn chắc 20% điểm Warm-up, dựng xong khung xương, kiểm tra dữ liệu.
* **Đầu giờ chiều (13:30 - 16:00):** Giai đoạn bứt phá điểm số mạnh nhất (Train GPU, Feature Engineering).
* **Cuối chiều (16:30 - 17:30):** Dừng thêm tính năng mới, tập trung ghép mô hình (Ensemble), kiểm tra định dạng file nộp và đồng bộ Git. Tránh code ẩu phút chót gây lỗi crash toàn hệ thống.
