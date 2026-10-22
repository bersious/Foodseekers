# 🍽️ Foodseekers — RMIT Hackathon 2026

[![Built with TideCloak](https://tide.org/badges/built-with-tidecloak.svg)](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked)

Dự án tham gia cuộc thi lập trình quốc tế **RMIT Hackathon 2026** (Việt Nam — Úc — Malaysia) bởi đội thi **Foodseekers** đến từ Trường Đại học Công nghệ Thông tin (UIT), ĐHQG-HCM.

---

## 🌐 Trải nghiệm Trực tuyến (Live Production Portal)

Toàn bộ hệ thống sản phẩm đã được triển khai trực tiếp trên môi trường đám mây:

* ⚡ **Cổng Điều Hướng Trung Tâm:** [https://bersious.io.vn/rmit](https://bersious.io.vn/rmit)
* 🎧 **Cổng 01 · Két Sắt Nghệ Sĩ:** [https://bersious.io.vn/rmit/1](https://bersious.io.vn/rmit/1) *(Tải tệp, phân quyền, kiểm âm, tạo profile)*
* 🎙️ **Cổng 02 · Phòng Nghe Thử Bảo Mật:** [https://bersious.io.vn/rmit/2](https://bersious.io.vn/rmit/2) *(Chọn nghệ sĩ, xin quyền, nghe in-memory, chống tải về, watermark)*
* ⚠️ **Cổng 03 · Trình Giám Sát S3 (Oblivious Proxy):** [https://bersious.io.vn/rmit/3](https://bersious.io.vn/rmit/3) *(Bảng SOC giám sát mã hóa thời gian thực, mô phỏng tấn công root)*

> **Thông tin xác thực kiểm thử:**  
> Mật khẩu đăng nhập mặc định cho tất cả tài khoản là `123`.  
> *Nghệ sĩ mẫu:* `alice_artist`, `endy_producer` (hoặc tự tạo nghệ sĩ mới).  
> *Người nghe mẫu:* `minh_mastering`, `thu_producer`, `lan_soundcheck`, `nhânn` (hoặc tự tạo danh tính mới).

---

## 🏆 THỬ THÁCH 2: DỰ ÁN "UNRELEASED" (Tide × RMIT 2026)

### Project Overview
**UNRELEASED** là studio cộng tác và nghe thử tác phẩm âm nhạc / video trước ngày phát hành áp dụng mô hình bảo mật **Zero-Trust & Zero-Custody**, tích hợp công nghệ **TideCloak** và cơ chế **Emergent Authority (Quyền hạn tự sinh)**. Nền tảng triệt tiêu hoàn toàn chìa khóa chủ (Master Key) trên máy chủ lưu trữ, bảo vệ nghệ sĩ tuyệt đối khỏi nguy cơ bị nhân viên đám mây lạm quyền hoặc hacker đánh cắp bản thu master.

Built with [TideCloak](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked).

### 1. Vision & Originality
Trong ngành công nghiệp âm nhạc, những vụ rò rỉ album chưa phát hành (pre-release leak) gây thiệt hại hàng triệu USD cho các nghệ sĩ lớn. Nguyên nhân cốt lõi là các nền tảng lưu trữ hiện nay (Dropbox, Google Drive, Box, Byta) đều hoạt động theo mô hình ủy thác chìa khóa: quản trị viên máy chủ hoặc quản trị viên cơ sở dữ liệu luôn nắm giữ chìa khóa giải mã master. Chúng tôi đề xuất **UNRELEASED**: một không gian chia sẻ tác phẩm sáng tạo mà **không cần trao quyền kiểm soát cho bất kỳ bên thứ ba nào**. Chìa khóa giải mã không bao giờ tồn tại ở dạng tĩnh trên máy chủ — nó chỉ tự sinh ra trong một phần nghìn giây trên bộ nhớ RAM của đúng người nghe được cấp phép.

### 2. Trust Constraint Insight
Rào cản lòng tin hiện nay buộc các nhà sản xuất và nghệ sĩ phải dùng những biện pháp tiêu cực: không dám gửi bản thu chất lượng cao, chần chừ hợp tác từ xa, hoặc phải bay trực tiếp đến phòng thu để nghe demo. Khi loại bỏ nỗi sợ bị lạm quyền máy chủ và lộ dữ liệu, các nghệ sĩ độc lập có thể tự tin gửi bản master 24-bit FLAC không nén cho các kỹ sư hòa âm, giám đốc âm nhạc hay đài phát thanh trên toàn thế giới để thẩm định tức thì.

### 3. Value & Impact
* **Nghệ sĩ & Hãng đĩa:** Kiểm soát 100% bản quyền tác phẩm. Thu hồi quyền nghe của đối tác chỉ trong 0.069ms.
* **Kỹ sư âm thanh & Giám tuyển:** Trải nghiệm nghe thử âm thanh gốc trong bộ nhớ mà không cần tải file về ổ đĩa, loại bỏ gánh nặng pháp lý về việc vô tình làm lộ file demo.

### 4. Why TideCloak Matters
Các hệ thống đăng nhập thông thường (OAuth2, Keycloak, JWT thông thường) chỉ kiểm tra tài khoản rồi trao token tải file về. Khi máy chủ đám mây bị xâm nhập, kẻ tấn công có thể tải toàn bộ bucket S3 và giải mã ngoại tuyến. **TideCloak mang lại sự khác biệt quyết định:**
* **Emergent Authority:** Quyền hạn giải mã chỉ sinh ra khi có sự đồng thuận từ các node phân tán (Quorum Consensus).
* **Oblivious Proxy:** Máy chủ lưu trữ đóng vai trò người chuyển thư vô can — máy chủ chỉ lưu khối nhị phân mã hóa (`.enc`), không hề có chìa khóa master.
* **Tự hủy tức thì:** Khi nghệ sĩ bấm thu hồi quyền, các node Quorum hủy phiên trong chưa đầy 1ms, không token cũ hay bộ nhớ cache nào có thể tái tạo lại chìa khóa.

### 5. Prototype & Storytelling
Nguyên mẫu trực tuyến hôm nay chứng minh trọn vẹn 5 tính năng cốt lõi:
1. **Quản lý đa nghệ sĩ:** Nghệ sĩ tạo hồ sơ mới, tải nhạc/video lên và phân quyền đích danh cho từng danh tính phi tập trung (DID).
2. **Xin quyền tương tác hai chiều:** Người nghe gửi đơn xin quyền trực tiếp ➔ Nghệ sĩ duyệt trên Trang 1 ➔ Bài hát tự động mở khóa trên Trang 2 theo thời gian thực qua Cloud Database Upstash Redis.
3. **Chế độ tự hủy sau 1 lần nghe (Single-Play):** Quyền giải mã tự động thu hồi vĩnh viễn ngay khi bài hát phát xong.
4. **Giới hạn thời lượng nghe thử (10s / 15s / 30s / 60s):** Nghệ sĩ có thể giới hạn chỉ cho nghe đoạn teaser đầu. Trình phát tự động ngắt âm thanh khi chạm mốc thời gian.
5. **Chống tải về & Chống thu âm ngoài loa:** Khóa thuộc tính `nodownload`, cấm chuột phải, kết hợp tính năng chèn **Watermark tiếng vịt kêu định kỳ** hoặc **Giọng đọc AI bản quyền** đè lên nhạc mỗi 9 giây, làm vô hiệu hóa hoàn toàn ý đồ dùng điện thoại kề loa để thu âm lậu.
6. **Mô phỏng tấn công Root Admin:** Tại Trang 3, người dùng kích hoạt thử nghiệm hacker chiếm quyền root S3 để giải mã ➔ Hệ thống Quorum từ chối 403, rò rỉ dữ liệu = 0 bytes!

---

## 🛠️ Kiến trúc Kỹ thuật (Technical Architecture)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                      1. CLIENT INTERFACE TIER                           │
│  /rmit/1 (Artist Sovereign Vault)  │  /rmit/2 (Reviewer In-Memory Room) │
│  - Client-side AES-256-GCM Encrypt │  - In-Memory Web Audio API Playback│
│  - Entitlement Policy Management   │  - Anti-Download & Watermark Engine│
└────────────────────────────────────┬────────────────────────────────────┘
                                     │ Encrypted Stream / JIT Session Request
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   2. OBLIVIOUS PROXY & API TIER                         │
│   src/backend/server.js (Node.js)  │  api/rmit-vault.ts (Serverless)    │
│   - Host holds 0 Master Keys       │  - Realtime Quorum Policy Engine   │
│   - Pure Encrypted Binary Storage  │  - Upstash Redis Cloud Database    │
│   - Vercel Blob High-Speed Media CDN for Audio/Video Streaming          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │ Identity & Policy Attestation
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                  3. TIDE FABRIC QUORUM (CONSENSUS)                      │
│   src/sdk/tidecloak/emergent_authority.js & crypto_engine.js            │
│   - Decentralized Consensus Nodes (Zero Single Point of Compromise)     │
│   - Ephemeral JIT Key Emergence (Synthesized only in caller's RAM)      │
│   - Instant Revocation & Single-Play Self-Destruction in 0.069ms        │
└─────────────────────────────────────────────────────────────────────────┘
```

### Các Module Cốt Lõi Trong Kho Lưu Trữ

* `prototype/`: Giao diện ứng dụng hoàn chỉnh chia thành 3 cổng (`/rmit`, `/rmit/1`, `/rmit/2`, `/rmit/3`).
* `api/rmit-vault.ts`: API điều phối phân quyền và cơ sở dữ liệu thời gian thực kết nối Upstash Redis.
* `api/upload-media.ts`: API nạp tệp media lên máy chủ CDN Vercel Blob tốc độ cao.
* `src/sdk/tidecloak/emergent_authority.js`: Thuật toán phân quyền Quorum và sinh khóa Just-In-Time.
* `src/sdk/tidecloak/crypto_engine.js`: Động cơ mật mã học mã hóa AES-256-GCM.
* `src/backend/server.js`: Máy chủ Oblivious Proxy mẫu chạy trên cổng 4000.
* `src/security/`: Bộ kịch bản kiểm thử bảo mật đối kháng và kiểm thử tích hợp đầu-cuối (Pass 100%).

---

## 📊 THỬ THÁCH 1: PHÂN LOẠI CÂU LỆNH TẤN CÔNG ĐỐI KHÁNG (Kaggle)

Song song với Thử thách 2, đội ngũ Foodseekers tham gia bảng đấu Kaggle chính thức của RMIT:

* **Bài toán:** Phân loại 3 nhãn an toàn AI đa ngôn ngữ (`BENIGN`, `JAILBREAK`, `PROMPT_INJECTION`) trên 4 ngôn ngữ (Anh, Pháp, Ý, Bồ Đào Nha).
* **Chỉ số đo lường:** Macro-averaged F1 Score.
* **Chiến lược:** Xây dựng Pipeline Ensemble đa tầng kết hợp trích xuất đặc trưng N-gram văn bản, ký tự, one-hot ngôn ngữ, regex an ninh cùng các mô hình Transformer tối ưu (XLM-RoBERTa, DeBERTa-v3).
* **Kết quả đạt được:**
  * Baseline ban đầu: `0.9028`
  * Tối ưu hóa lượt 2: `0.9175`
  * Bứt phá lượt 3: `0.9508` (Top Leaderboard).

---

## 👥 Đội ngũ Thành viên & Phân công

| STT | Thành viên | GitHub | Nhánh làm việc | Vai trò chính |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Nguyễn Thành Thiện Nhân** | `bersious` | `dev-backend` | **Team Lead & AI Integration:** Quản lý dự án, kiến trúc hệ thống, tích hợp mô hình AI, kết nối Vercel & nộp bài Kaggle. |
| **2** | **Nguyễn Văn Nhân** | `NguyenNhan1107` | `dev-core` | **Core Engineer:** Xây dựng logic code chính, GPU runner, tối ưu pipeline Kaggle. |
| **3** | **Trần Nguyễn Anh Thư** | `tuna184` | `dev-data` | **Data Analyst:** Tiền xử lý dữ liệu ngôn ngữ, đánh giá ma trận nhầm lẫn, định dạng tệp nộp bài. |
| **4** | **Trần Minh Ngọc** | `tranminhngoc171-bot` | `dev-system` | **System Architecture & Security:** Thiết kế luồng bảo mật đối kháng, kiểm thử kịch bản exploit, hoàn thiện tài liệu. |

---

## 💻 Hướng Dẫn Cài Đặt Cục Bộ (Local Setup)

### 1. Khởi chạy ứng dụng mẫu (Prototype):
Chỉ cần mở trực tiếp tệp `prototype/index.html` (hoặc `prototype/1/index.html`, `prototype/2/index.html`, `prototype/3/index.html`) bằng bất kỳ trình duyệt web hiện đại nào (Chrome, Edge, Firefox, Safari).

### 2. Khởi chạy máy chủ Oblivious Proxy:
```bash
cd Foodseekers
npm install
node src/backend/server.js
# Máy chủ lắng nghe tại http://localhost:4000
```

### 3. Chạy bộ kiểm thử an ninh tự động:
```bash
# Kiểm thử mô phỏng tấn công root admin
node src/security/exploit_simulation.js

# Kiểm thử tích hợp phân quyền đầu-cuối
node src/security/e2e_integration_test.js
```

---

**Team Foodseekers — Đại học Công nghệ Thông tin (UIT) — RMIT Hackathon 2026** 🚀
