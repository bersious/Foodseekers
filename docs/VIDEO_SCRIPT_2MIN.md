# 🎬 KỊCH BẢN THUYẾT MINH VIDEO DEMO 2 PHÚT (120 GIÂY)
## DỰ ÁN: SONARA. — KÉT SẮT ÂM NHẠC ZERO-TRUST (TIDECLOAK)
**Đội thi:** Foodseekers — Trường Đại học Công nghệ Thông tin (UIT), ĐHQG-HCM  
**Cuộc thi:** RMIT Hackathon 2026 — Challenge 2 (Tide UNLOCKED)

---

### ⏱️ PHÂN BỔ THỜI GIAN CHUẨN (TỔNG: 120 GIÂY)

| Phân đoạn | Thời lượng | Màn hình quay | Nội dung chính |
| :--- | :---: | :--- | :--- |
| **Phần 1: Giới thiệu & Nỗi đau** | `00:00 - 00:25` (25s) | Slide mở đầu hoặc Trang chủ `/rmit` | Nạn lộ bài hát trước ngày ra mắt & Thất bại của Google Drive / Dropbox |
| **Phần 2: Cổng Nghệ Sĩ** | `00:25 - 00:55` (30s) | Trang `/rmit/1` | Tải bài hát master, đặt giới hạn 15s, bật watermark tiếng vịt |
| **Phần 3: Cổng Người Nghe** | `00:55 - 01:25` (30s) | Trang `/rmit/2` | Xin quyền 1-click, nghe in-memory, visualizer, chống can thiệp |
| **Phần 4: Mô phỏng Hacker S3** | `01:25 - 01:45` (20s) | Trang `/rmit/3` | Kích hoạt Root Admin dump S3 ➔ 0 Master Key, 0 byte rò rỉ |
| **Phần 5: Kết luận & Giá trị** | `01:45 - 02:00` (15s) | Màn hình tổng hợp & Logo SONARA | Tuyên ngôn Zero-Custody & Chào kết |

---

### 🎙️ LỜI THOẠI CHI TIẾT THEO TỪNG GIÂY (DÀNH CHO BẠN THUYẾT MINH)

> **Mẹo cho bạn nói:** Nói với giọng tự tin, dứt khoát, nhịp điệu vừa phải (khoảng 130 - 140 từ/phút), không cần nói quá nhanh. Bật phím `R` trên web để ẩn con trỏ chuột khi chuyển cảnh.

---

#### 🎬 PHẦN 1: MỞ ĐẦU & BÀI TOÁN LỘ BẢN THU (00:00 - 00:25)
* **Hình ảnh trên video:** Mở đầu bằng Cổng trung tâm `https://bersious.io.vn/rmit` với Logo SONARA phát sáng.
* **Lời đọc:**
  > *"Xin chào Ban giám khảo! Chúng em là đội thi Foodseekers đến từ Đại học Công nghệ Thông tin UIT.  
  > Trong ngành công nghiệp âm nhạc, những vụ rò rỉ album chưa phát hành gây thiệt hại hàng triệu đô la cho các nghệ sĩ. Nguyên nhân là vì các nền tảng đám mây hiện nay như Google Drive hay Dropbox đều nắm giữ chìa khóa chủ của dữ liệu.  
  > Để giải quyết triệt để rào cản lòng tin này, chúng em phát triển **SONARA.** — Két sắt âm nhạc Zero-Trust đầu tiên ứng dụng công nghệ **TideCloak** và cơ chế **Emergent Authority**."*

---

#### 🎬 PHẦN 2: CỔNG NGHỆ SĨ — QUYỀN LỰC TỐI THƯỢNG (00:25 - 00:55)
* **Hình ảnh trên video:** Chuyển sang Cổng 1 (`/rmit/1`). Quay cảnh đăng nhập tài khoản nghệ sĩ `alice_artist`, kéo thả file nhạc lên, chỉnh giới hạn `15 giây đầu` và gạt bật `Watermark tiếng vịt kêu`.
* **Lời đọc:**
  > *"Đầu tiên là **Cổng Nghệ Sĩ**. Tại đây, toàn bộ tác phẩm âm nhạc được mã hóa trực tiếp tại trình duyệt bằng thuật toán AES-256-GCM trước khi đẩy lên đám mây.  
  > Điểm đặc biệt: Nghệ sĩ nắm quyền kiểm soát tuyệt đối: có thể cấu hình giới hạn chỉ cho nghe thử **15 giây đầu**, cấp quyền **Nghe một lần tự hủy**, và kích hoạt **Watermark âm thanh tiếng vịt kêu** định kỳ mỗi 9 giây để vô hiệu hóa hoàn toàn hành vi đưa điện thoại lại gần loa thu âm lậu!"*

---

#### 🎬 PHẦN 3: CỔNG NGƯỜI NGHE — GIẢI MÃ IN-MEMORY & CHỐNG CAN THIỆP (00:55 - 01:25)
* **Hình ảnh trên video:** Chuyển sang Cổng 2 (`/rmit/2`). Người nghe bấm chọn nghệ sĩ Alice Nguyễn, bấm `Xin quyền nghe`, quay lại Cổng 1 bấm `Duyệt`, rồi quay lại Cổng 2 bấm `Phát ngay`. Visualizer 60fps nhảy sóng và đĩa xoay.
* **Lời đọc:**
  > *"Tiếp theo là **Cổng Người Nghe SONARA**. Người nghe chọn nghệ sĩ và gửi yêu cầu truy cập chỉ bằng một click. Ngay khi nghệ sĩ duyệt, chính sách ủy quyền Quorum lập tức có hiệu lực qua Cloud Database thời gian thực.  
  > Nhạc được giải mã tức thì trong bộ nhớ RAM — tuyệt đối **không thể tải về máy**. Đến đúng giây thứ 15, luồng phát tự động ngắt. Nếu người nghe cố tình mở DevTools hoặc chuyển sang phần mềm quay quét màn hình, hệ thống **Tamper Watchdog** sẽ lập tức thu hồi quyền truy cập vĩnh viễn!"*

---

#### 🎬 PHẦN 4: HẠ TẦNG S3 OBLIVIOUS PROXY — ZERO-CUSTODY (01:25 - 01:45)
* **Hình ảnh trên video:** Chuyển sang Cổng 3 (`/rmit/3`). Bấm nút đỏ `Thực thi kịch bản Root Admin giải mã trộm`. Màn hình Terminal quét chữ chạy từng dòng log.
* **Lời đọc:**
  > *"Nhưng điều gì xảy ra nếu máy chủ đám mây bị tấn công? Tại **Cổng Giám Sát S3**, chúng em mô phỏng kịch bản kẻ tấn công chiếm toàn quyền Root của hạ tầng.  
  > Kết quả: Server hoạt động như một người chuyển thư vô can — **0 chìa khóa master tồn tại trên máy chủ**. Khi hacker cố gắng giải mã, mạng lưới Tide Fabric Quorum từ chối yêu cầu ngay lập tức. Dữ liệu rò rỉ bằng đúng 0 byte!"*

---

#### 🎬 PHẦN 5: TỔNG KẾT & KẾT THÚC (01:45 - 02:00)
* **Hình ảnh trên video:** Quay lại màn hình chính của SONARA và hiện thông tin đội thi Foodseekers UIT.
* **Lời đọc:**
  > *"Với SONARA và TideCloak, nghệ sĩ có thể tự tin chia sẻ những bản thu master đắt giá nhất cho đối tác toàn cầu mà không còn nỗi sợ bị rò rỉ.  
  > Đây là minh chứng cho sức mạnh của bảo mật không ủy thác. Cảm ơn Ban giám khảo đã lắng nghe!"*

---

### 💡 3 LƯU Ý SỐNG CÒN KHI QUAY:
1. **Mở sẵn 2 tab cạnh nhau:** Một tab Cổng 1 (Nghệ sĩ) và một tab Cổng 2 (Người nghe) để khi bấm "Xin quyền" ➔ chuyển tab bấm "Duyệt" ➔ chuyển lại nghe nhạc diễn ra trong vòng 5 giây rất mượt.
2. **Âm thanh:** Nhớ bật loa vừa phải để video thu được tiếng nhạc và 1 tiếng vịt kêu ngắn (khoảng giây thứ 45 - 50) để ban giám khảo thấy tính năng watermark hoạt động thật!
3. **Phím tắt:** Nhấn phím **`R`** để ẩn chuột nếu muốn khung hình sạch sẽ, nhấn **`ESC`** để hiện lại chuột khi cần click.
