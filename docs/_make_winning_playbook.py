with open(r"C:\Users\nguye\Foodseekers\docs\UNRELEASED_TIDE_RESEARCH_AND_WINNING_PLAYBOOK.md", "w", encoding="utf-8") as f:
    f.write("""# 🎧 TỔNG HỢP NGHIÊN CỨU CHUYÊN SÂU & CHIẾN LƯỢC TỐI ƯU GIẬT GIẢI
# DỰ ÁN: UNRELEASED — ZERO-TRUST AUDIO PREVIEW STUDIO
# Đơn vị: Team Foodseekers (UIT) — RMIT Hackathon 2026 (Challenge 2: Tide Unlocked)

---

## 📌 1. BỐI CẢNH THỰC TẾ & NỖI ĐAU THỊ TRƯỜNG (MARKET RESEARCH)

### 1.1. Thảm họa rò rỉ âm nhạc trước ngày phát hành (Pre-release Music Leaks)
* Trong ngành công nghiệp âm nhạc toàn cầu, các bản thu âm demo, vocal stems và album chưa phát hành có giá trị thương mại hàng triệu USD.
* Hàng loạt vụ rò rỉ chấn động (như album của Taylor Swift, Frank Ocean, Kendrick Lamar, Dua Lipa hay tại Việt Nam là các bản thu nháp của Sơn Tùng M-TP, Hứa Kim Tuyền) đều xuất phát từ cùng một lỗ hổng: **nghệ sĩ gửi file nghe thử cho nhạc sĩ phối khí, kỹ sư mastering hoặc ban biên tập đĩa hát qua các dịch vụ lưu trữ đám mây thông thường**.

### 1.2. Tại sao các nền tảng hiện nay (Byta, DISCO, Dropbox, SoundCloud Private) đều thất bại?
* Các nền tảng chuyên nghiệp cho ngành nhạc hiện nay (như Byta.com, DISCO.ac) giải quyết bài toán bằng cách: **Gắn dấu bản quyền âm thanh (Watermarking)** hoặc **Tạo đường link riêng tư (Private Link)**.
* **Lỗ hổng chí mạng:** Các nền tảng này vẫn là hệ thống ủy thác tập trung (Custodial Architecture). Toàn bộ file nhạc gốc dạng FLAC/WAV không nén được lưu trữ trên các thùng chứa đám mây (AWS S3 / Google Cloud Storage).
  1. Người quản trị cơ sở dữ liệu (Database Admin) hoặc quản trị viên hạ tầng đám mây luôn có quyền đọc và tải toàn bộ file gốc.
  2. Khi tài khoản nhân viên nội bộ bị mua chuộc hoặc lộ khóa API đám mây, tin tặc sẽ tải sạch toàn bộ album trước khi nghệ sĩ kịp nhận ra.
  3. Đóng dấu bản quyền (Watermarking) chỉ có tác dụng điều tra xem ai làm lộ **sau khi bài hát đã bị tung lên mạng**, chứ **hoàn toàn không thể ngăn chặn hành vi rò rỉ ban đầu**.

---

## ⚡ 2. ĐỘT PHÁ CỦA UNRELEASED KHI TÍCH HỢP TIDECLOAK

UNRELEASED thay đổi hoàn toàn kiến trúc bảo mật của việc chia sẻ âm nhạc:

| Đặc tính kỹ thuật | Nền tảng hiện có (Dropbox, Byta, DISCO) | UNRELEASED tích hợp TideCloak |
| :--- | :--- | :--- |
| **Vị trí lưu chìa khóa chủ** | Lưu trên máy chủ, database hoặc AWS KMS | **HOÀN TOÀN KHÔNG TỒN TẠI** (Zero Master Key) |
| **Vai trò của máy chủ lưu trữ** | Nắm toàn quyền đọc và giải mã file gốc | **Người trung chuyển vô can (Oblivious Proxy)** |
| **Cơ chế nghe thử (Preview)** | Tải cả file audio về bộ nhớ đệm máy tính | Giải mã trực tiếp trên RAM qua Web Audio API |
| **Quyền truy cập của Admin** | Có thể tải và nghe trộm mọi bài hát | Mở ra chỉ thấy chuỗi mã hóa vô nghĩa, bị chặn giải mã |
| **Độ trễ khi thu hồi quyền** | Phải đợi xóa token hoặc file đã bị tải về máy | **Cắt đứt tức thì** (Mạng lưới Tide Quorum ngừng sinh khóa) |

---

## 🎯 3. BÍ QUYẾT TỐI ƯU HÓA 5 TIÊU CHÍ CHẤM ĐIỂM ĐỂ GIÀNH GIẢI CAO NHẤT

Ban giám khảo Tide và RMIT chấm điểm dựa trên 5 tiêu chí rõ ràng (tổng 100 điểm):

### 1. Tầm nhìn & Tính độc bản (Vision & Originality — 25 điểm)
* **Điểm nhấn:** Không đi theo lối mòn y tế hay biểu quyết học đường mà chọn đề tài bản quyền tác phẩm sáng tạo — ngành công nghiệp đang bị tàn phá nặng nề bởi các vụ leak nhạc trên Telegram, Reddit.

### 2. Thấu hiểu rào cản lòng tin (Trust Constraint Insight — 20 điểm)
* **Điểm nhấn:** Chỉ rõ lý do vì sao sự hợp tác âm nhạc bị đình trệ: Nghệ sĩ độc lập không thể tự tin thuê các kỹ sư hòa âm quốc tế vì sợ bị đánh cắp bản quyền; các hãng đĩa phải bắt ký hợp đồng bảo mật (NDA) rườm rà nhưng vẫn không ngăn được rò rỉ từ nhân viên IT.

### 3. Giá trị & Tác động xã hội (Value & Impact — 20 điểm)
* **Điểm nhấn:** Mang lại chủ quyền dữ liệu tuyệt đối cho người sáng tạo nội dung. Nghệ sĩ có thể gửi bài nghe thử xuyên biên giới với quyền kiểm soát từng bài hát riêng lẻ mà không bị phụ thuộc vào sự trung thực của các nền tảng trung gian.

### 4. Vai trò cốt lõi của TideCloak (Why TideCloak Matters — 20 điểm)
* **Đây là tiêu chí quyết định!** Hướng dẫn của Tide ghi rõ: *"Nếu ứng dụng của bạn làm được y hệt với phân quyền thông thường, bạn sẽ bị điểm thấp"*.
* Đội mình giải thích thuyết phục: Trong phân quyền thông thường, máy chủ backend vẫn giữ file hoặc master key. Chỉ có **Emergent Authority** của Tide mới biến máy chủ thành Oblivious Proxy, đảm bảo kể cả khi máy chủ bị hack hay admin bị tha hóa thì kẻ xấu cũng không thu được một giây âm thanh nào.

### 5. Trình diễn nguyên mẫu & Kể chuyện (Prototype & Storytelling — 15 điểm)
* **Điểm nhấn trong video demo 2 phút:**
  1. Giao diện trực quan, chuyên nghiệp với dải sóng âm nhấp nhô.
  2. Phát âm thanh thật sinh động thông qua Web Audio API.
  3. Bằng chứng trực tiếp: Chuyển sang màn hình Admin bấm nút rò rỉ dữ liệu ➔ Bị hệ thống Tide từ chối ngay trước mắt giám khảo.
  4. Bấm nút thu hồi quyền ➔ Luồng âm thanh lập tức bị ngắt.

---

## 🎬 4. KỊCH BẢN THOẠI TIẾNG ANH CHUẨN XÁC CHO VIDEO 2 PHÚT

*(Có thể đọc trực tiếp khi quay màn hình hoặc gắn phụ đề vào video)*

* **0:00 – 0:25:**  
  *"Welcome to UNLOCKED Challenge 2. In the music industry, unreleased demos and album masters represent millions of dollars in creative investment. Yet, creative collaboration is paralyzed by leak anxiety. Platforms like Dropbox, SoundCloud Private, or Byta store plaintext audio in centralized cloud buckets where storage administrators or rogue employees hold universal master keys, leading to catastrophic pre-release leaks."*
* **0:25 – 0:50:**  
  *"UNRELEASED solves this using TideCloak Emergent Authority. Artist Alice uploads her upcoming album 'MIDNIGHT CIPHER'. She shares Track 1 with mixing engineer Minh, while keeping Tracks 2 and 3 strictly private. Crucially, our cloud storage holds zero master keys—all tracks remain unbreakable ciphertext."*
* **0:50 – 1:15:**  
  *"Minh authenticates via TideCloak BYOiD. Tide's decentralized quorum verifies Alice's active policy and Minh's credential. Authority emerges just-in-time, allowing Minh to stream decrypted audio directly in memory via Web Audio API. Minh cannot access unauthorized tracks, and no audio file is ever cached to disk."*
* **1:15 – 1:40:**  
  *"Now, observe our Cloud Storage Inspector. Even if a rogue system administrator or an external attacker breaches our AWS S3 storage, they see only encrypted ciphertext. When an admin attempts a root master decryption, Tide's quorum immediately rejects the request because the server is an oblivious proxy without unilateral authority."*
* **1:40 – 2:00:**  
  *"Finally, Alice revokes Minh's access with one click. Minh's stream terminates instantly as Tide's quorum ceases key emergence. UNRELEASED demonstrates what becomes possible when trust is no longer the bottleneck. Built with TideCloak for RMIT Hackathon 2026. Thank you!"*
""")
print("Created UNRELEASED_TIDE_RESEARCH_AND_WINNING_PLAYBOOK.md successfully!")
