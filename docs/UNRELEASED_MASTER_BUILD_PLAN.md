# 🏗️ BẢN THIẾT KẾ KIẾN TRÚC & KẾ HOẠCH TRIỂN KHAI PHẦN MỀM "UNRELEASED"
# Dự án: UNRELEASED — Zero-Trust Creative Audio Preview Studio (Tide × RMIT 2026)
# Phân công: 4 Nhánh Git / 4 Subagents độc lập trên kho lưu trữ `Foodseekers`

---

## 🏛️ 1. TỔNG QUAN KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

Hệ thống UNRELEASED được chia thành **4 tầng mô đun độc lập (Separation of Concerns)**:

```text
                        ┌────────────────────────────────────────┐
                        │          CLIENT STUDIO UI              │
                        │    (Next.js / Web Audio API)           │
                        └───────────────┬────────────────────────┘
                                        │ (1) Client-side E2EE & Playback
                                        ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    TIDECLOAK & EMERGENT AUTHORITY                      │
│   - BYOiD Identity (OIDC Token)                                        │
│   - Decentralized Quorum Nodes (Fabric Verification)                   │
│   - Just-In-Time Ephemeral Decryption in RAM                           │
└───────────────────────────────────────┬────────────────────────────────┘
                                        │ (2) Scoped Token Validation
                                        ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   OBLIVIOUS PROXY BACKEND SERVER                       │
│   - Node.js / Express API                                              │
│   - Raw Encrypted Audio Chunk Storage (Mock S3 Bucket)                 │
│   - ZERO Master Keys Stored in DB / Environment                        │
└───────────────────────────────────────┬────────────────────────────────┘
                                        │ (3) Automated Verification
                                        ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   SECURITY & EXPLOIT TEST SUITE                        │
│   - Rogue Admin S3 Dump Exploit Test (Must Fail)                       │
│   - Instant Revocation Latency Benchmark (< 50ms)                      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 👥 2. KẾ HOẠCH PHÂN CHIA NHÁNH GIT & NHIỆM VỤ SUBAGENT

Toàn bộ quá trình code được chia thành 4 nhánh song song, mỗi nhánh giải quyết triệt để một tầng chức năng:

### 🌿 Nhánh 1: `dev-core` (Phụ trách: Văn Nhân / Subagent Core)
* **Thư mục làm việc:** `src/sdk/tidecloak/`
* **Nhiệm vụ:**
  1. `crypto_engine.js`: Viết module mã hóa đầu cuối bằng chuẩn Web Crypto API (AES-256-GCM, 12-byte IV ngẫu nhiên).
  2. `emergent_authority.js`: Viết module mô phỏng nút đồng thuận Tide Quorum:
     - Hàm `evaluateEntitlement(artistPolicy, userToken, trackId)`: Kiểm tra chính sách và quyền truy cập.
     - Hàm `generateEphemeralKey(sessionId)`: Khóa giải mã sinh ra tạm thời trong bộ nhớ RAM, tự hủy sau khi kết thúc phiên.
     - Hàm `revokeEntitlement(trackId, collaboratorId)`: Ngắt quyền tức thì, từ chối mọi yêu cầu giải mã tiếp theo.
* **Đầu ra:** Thư viện SDK hoàn chỉnh có thể import vào cả giao diện lẫn kịch bản kiểm thử.

---

### 🌿 Nhánh 2: `dev-backend` (Phụ trách: Thiện Nhân - Lead / Subagent Backend)
* **Thư mục làm việc:** `src/backend/` & `prototype/`
* **Nhiệm vụ:**
  1. `server.js`: Xây dựng máy chủ API trung chuyển vô can (Oblivious Proxy):
     - `GET /api/tracks`: Trả về danh sách bài hát và trạng thái chính sách.
     - `POST /api/tracks/share`: Cập nhật chính sách ủy quyền nghe thử cho cộng tác viên.
     - `POST /api/tracks/revoke`: Hủy quyền nghe thử tức thì.
     - `GET /api/storage/raw-chunks`: Endpoint giả lập kho lưu trữ S3, chỉ trả về các khối byte mã hóa.
     - `POST /api/admin/dump-master`: Mô phỏng hành vi tấn công của quản trị viên hệ thống ➔ Bắt buộc ném lỗi `500 UNAUTHORIZED: Oblivious proxy holds zero master keys`.
  2. Đồng bộ giao diện `prototype/index.html` gọi API thực tế của máy chủ.
* **Đầu ra:** Máy chủ backend chạy độc lập trên cổng 4000 và kết nối thông suốt với giao diện.

---

### 🌿 Nhánh 3: `dev-system` (Phụ trách: Minh Ngọc / Subagent System & Security)
* **Thư mục làm việc:** `src/security/` & `docs/`
* **Nhiệm vụ:**
  1. `exploit_simulation.js`: Kịch bản kiểm thử bảo mật tự động:
     - Kịch bản 1 (The Compromised Admin Attack): Giả lập tài khoản root dump dữ liệu từ S3 và cố gắng giải mã mà không có sự đồng thuận từ Tide Quorum ➔ Khẳng định thất bại 100%.
     - Kịch bản 2 (Revocation Latency Benchmark): Đo thời gian từ lúc nghệ sĩ bấm Revoke đến lúc yêu cầu giải mã bị từ chối (mục tiêu: < 50 mili-giây).
  2. `docs/SYSTEM_ARCHITECTURE_REPORT.md`: Soạn thảo tài liệu báo cáo kiến trúc hệ thống chuẩn chỉnh kèm sơ đồ luồng dữ liệu cho ban giám khảo RMIT.
* **Đầu ra:** Báo cáo kiểm thử bảo mật pass 100% và file PDF/Markdown kiến trúc hệ thống.

---

### 🌿 Nhánh 4: `dev-data` (Phụ trách: Anh Thư / Subagent Data & Compliance)
* **Thư mục làm việc:** `data/mock_assets/` & `README.md`
* **Nhiệm vụ:**
  1. `data/mock_assets/album_manifest.json`: Tạo siêu dữ liệu hoàn chỉnh cho album mẫu "MIDNIGHT CIPHER" (3 bài: Master Track, Vocal Stems, Collab Beat; kèm thời lượng, tần số lấy mẫu 48kHz, hash mã hóa SHA-256).
  2. Hoàn thiện file `README.md` chính của kho lưu trữ, dán đúng bản nháp 5 tiêu chí dưới 300 từ tiếng Anh để sẵn sàng nộp bài.
* **Đầu ra:** Bộ tài sản dữ liệu mẫu sống động và file README hoàn hảo.

---

## ⏱️ 3. LỘ TRÌNH THỰC HIỆN THEO CHẶNG (SPRINT ROADMAP TRƯỚC 18:00)

* **Chặng 1 (13:45 – 14:45):** Triển khai đồng loạt 4 nhánh (Core, Backend, Security, Data).
* **Chặng 2 (14:45 – 15:15):** Chạy kiểm thử tự động, gộp (Merge) 4 nhánh vào nhánh `main`.
* **Chặng 3 (15:15 – 16:15):** Chạy ứng dụng hoàn chỉnh, quay video demo 2 phút kèm âm thanh thật.
* **Chặng 4 (16:15 – 17:15):** Đẩy video MP4 lên GitHub, kiểm tra dung lượng < 100MB và điền Google Form.
* **17:30:** Chốt hạ bài nộp an toàn tuyệt đối trước hạn chót 18:00!
