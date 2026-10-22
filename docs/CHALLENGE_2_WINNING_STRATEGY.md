# 🏆 CHIẾN LƯỢC GIẬT GIẢI THỬ THÁCH 2: DỰ ÁN "UNRELEASED"
# Tên sản phẩm: UNRELEASED — Zero-Trust Creative Preview Studio
# Chủ đề lựa chọn: Ý tưởng số 5 (Creative work & Collaboration) trong danh mục Tide Unlocked
# Đơn vị dự thi: Team Foodseekers (UIT) — RMIT Hackathon 2026

---

## 🎯 1. TẠI SAO LỰA CHỌN "UNRELEASED" LÀ BƯỚC ĐI CHIẾN LƯỢC VƯỢT TRỘI?

Đội Foodseekers chuyển hướng sang **Ý tưởng số 5: UNRELEASED** vì những lý do mang tính quyết định:
1. **Tránh bão trùng lặp đề tài:** Đa số các đội thi hackathon đều chọn Y tế (Care Passport) hoặc Bầu cử. Việc chọn đề tài Âm nhạc & Tác phẩm sáng tạo giúp đội mình **hoàn toàn khác biệt, nổi bật ngay lập tức** trong mắt ban giám khảo.
2. **Nỗi đau thực tế hàng trăm triệu đô:** Trong ngành công nghiệp âm nhạc và điện ảnh, việc các bản thu âm demo, album chưa phát hành (như của các nghệ sĩ lớn) bị tuồn ra ngoài (leak) trước ngày ra mắt gây thiệt hại khổng lồ và phá hỏng toàn bộ chiến dịch truyền thông.
3. **Nút thắt niềm tin (Trust Bottleneck):** Các nghệ sĩ, nhà sản xuất âm nhạc rất cần gửi bản mix demo cho kỹ sư âm thanh hoặc ca sĩ hát phụ nghe thử, nhưng không bao giờ dám tin tưởng Dropbox, Google Drive hay SoundCloud Private vì người quản trị máy chủ lưu trữ hoặc nhân viên nội bộ luôn có chìa khóa chủ để tải và nghe lén file gốc.
4. **Điểm sáng tuyệt đối của TideCloak:** UNRELEASED chứng minh rằng **máy chủ lưu trữ đám mây chỉ là một người trung chuyển vô can (Oblivious Proxy)**. File nhạc được mã hóa đầu cuối, và chỉ người nghe được cấp quyền mới có thể giải mã luồng âm thanh trong tích tắc để nghe thử. Không ai có thể tải file lậu hay mở trộm!

---

## 📄 2. BẢN NHÁP README CHUẨN MẪU (DƯỚI 300 TỪ - TIẾNG ANH THEO BAREM CHẤM)

Đoạn văn này được viết chuẩn xác theo 5 tiêu chí của ban giám khảo, sẵn sàng đặt vào đầu file `README.md`:

```markdown
[![Built with TideCloak](https://tide.org/badges/built-with-tidecloak.svg)](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked)

## Project overview

**UNRELEASED** is a zero-trust creative collaboration studio empowering musicians and creators to share unreleased masters with external collaborators without cloud storage custody or leak risks.

Built with [TideCloak](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked).

### 1. Vision & originality
UNRELEASED transforms pre-release creative collaboration. Rather than trusting centralized cloud drives with multimillion-dollar unreleased album masters, UNRELEASED provides a cryptographically isolated preview studio where artists share fine-grained listening entitlements without surrendering master file access to the hosting platform.

### 2. Trust constraint insight
Today, creative pre-releases are crippled by leak anxieties: sharing unmastered demos with session musicians, mixing engineers, or A&R reviewers forces artists to deposit plaintext audio into services (Dropbox, SoundCloud Private) where platform administrators and leaked storage buckets hold universal decryption keys. This trust bottleneck causes costly delays, NDAs, and devastating pre-release leaks.

### 3. Value & impact
Independent artists, record labels, and sound engineers can now collaborate seamlessly across continents. Creatives maintain sovereign control over intellectual property, eliminating unauthorized leaks and preserving multimillion-dollar launch campaigns, while collaborators enjoy friction-free, secure streaming previews.

### 4. Why TideCloak matters
Conventional cloud platforms use server-side RBAC where storage operators retain master decryption capabilities. UNRELEASED integrates TideCloak's **Emergent Authority**: audio assets remain unbreakable ciphertext in cloud buckets. Decryption keys never exist on our servers—they emerge just-in-time strictly within the authorized reviewer's browser memory. When an artist revokes access, playback terminates immediately at the cryptographic quorum layer.

### 5. Prototype & storytelling
Our prototype demonstrates a live zero-trust review workflow:
1. Artist Alice manages her upcoming album vault with 3 encrypted masters.
2. She grants Track 1 listening entitlement to Reviewer Minh.
3. Minh authenticates via TideCloak BYOiD and streams Track 1 seamlessly, while Tracks 2 & 3 remain cryptographically inaccessible.
4. The Cloud Storage Operator attempts root decryption from the S3 bucket and is denied (zero master keys exist).
5. Alice revokes Minh's access: active streaming stops instantly.
```

---

## 🎬 3. KỊCH BẢN QUAY VIDEO DEMO 2 PHÚT (CHÍNH XÁC TỪNG GIÂY)

* **Tệp đầu ra:** `.mp4`, dung lượng `< 100 MB`, lưu trong thư mục `demo/`.
* **Thời lượng:** Đúng 120 giây (2 phút).

| Thời gian | Cảnh hiển thị trên màn hình | Lời thuyết minh (Voiceover tiếng Anh / phụ đề) |
| :---: | :--- | :--- |
| **0:00 – 0:25**<br>*(25s)* | **Màn hình mở đầu:** Logo UNRELEASED & Bối cảnh ngành âm nhạc.<br>Hình ảnh bài toán rò rỉ nhạc trước ngày ra mắt (album leaks). | *"Welcome to UNLOCKED Challenge 2. In the creative industry, unreleased music is worth millions, but pre-release collaboration is broken. When artists share demos via Dropbox or SoundCloud, platform admins and compromised servers have full access to the audio, leading to devastating leaks."* |
| **0:25 – 0:50**<br>*(25s)* | **Giao diện Artist Alice:** Mở album "MIDNIGHT CIPHER". Thấy 3 bài: Track 1, Track 2, Track 3. Bấm cấp quyền bài 1 cho Reviewer Minh. | *"With UNRELEASED built on TideCloak, trust is no longer a bottleneck. Artist Alice uploads 3 unreleased tracks. She invites mixing engineer Minh to review ONLY Track 1. Tracks 2 and 3 remain strictly locked. Crucially, our servers store zero master keys."* |
| **0:50 – 1:15**<br>*(25s)* | **Giao diện Reviewer Minh:** Bấm nút *"Play Decrypted Stream"*. Thanh sóng âm (Waveform) nhấp nhô sống động, đồng hồ chạy nhạc. Bấm vào bài 2 & 3 thì hiện "Access Denied". | *"Minh logs in through TideCloak BYOiD. Tide's decentralized quorum verifies Alice's policy and Minh's credential. Authority emerges just-in-time, streaming decrypted audio directly in Minh's browser. Meanwhile, unauthorized tracks remain completely unreadable."* |
| **1:15 – 1:40**<br>*(25s)* | **Giao diện Cloud Host Admin:** Mở bảng lưu trữ S3 Bucket. Toàn bộ file nhạc chỉ là chuỗi byte mã hóa loằng ngoằng. Bấm nút *"Attempt Root Master Decryption / Leak"* ➔ Bị báo lỗi đỏ: `ERROR: Unilateral master key does not exist`. | *"Now, look at the Cloud Infrastructure view. Even if a rogue employee or hacker breaches our AWS S3 bucket, they find only ciphertext. Because TideCloak eliminates unilateral authority, our server is an oblivious proxy—incapable of leaking the artist's audio."* |
| **1:40 – 1:55**<br>*(15s)* | **Giao diện Artist Alice:** Alice bấm *"Revoke Minh's Access"*. Chuyển sang màn hình Minh: Nhạc lập tức dừng lại, hiện thông báo đỏ `Error 403: EntitlementRevoked`. | *"Finally, review session over. Alice clicks Revoke Access. Minh's stream cuts off immediately as Tide's quorum ceases key emergence. Alice retains sovereign control over her art."* |
| **1:55 – 2:00**<br>*(5s)* | **Logo UNRELEASED & RMIT Hackathon 2026.** | *"UNRELEASED proves what becomes possible when trust is no longer a bottleneck. Built with TideCloak for RMIT Hackathon 2026. Thank you!"* |
