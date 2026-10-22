# 📑 CODE & MODULE INDEX — TEAM FOODSEEKERS
# (Bảng tra cứu các hàm, module và dữ liệu đã sẵn sàng để tái sử dụng)

> **QUY TẮC BẮT BUỘC CHO 4 AGENT:**
> 1. Khi bạn viết xong một script, hàm xử lý hoặc tạo ra file dữ liệu mới: **BẮT BUỘC cập nhật 1 dòng vào bảng dưới đây**.
> 2. Trước khi viết bất kỳ hàm mới nào: **ĐỌC BẢNG NÀY TRƯỚC** để xem đồng đội đã viết chưa, tránh viết trùng lặp hoặc chồng chéo code.
> 3. Mô tả rõ: Đường dẫn file, Đầu vào (Input), Đầu ra (Output) và cách gọi mẫu.

---

## 📦 Danh Sách Module & Tài Nguyên Dự Án

| Thời gian | Tác giả | Đường dẫn file | Input nhận vào | Output trả về | Chức năng chính |
| :---: | :---: | :--- | :--- | :--- | :--- |
| *Khởi tạo* | *Hệ thống* | `/TEAM_CHAT.md` | Tin nhắn cập nhật | Lịch sử trao đổi | Kênh chat nội bộ giữa 4 Agent |
| *Khởi tạo* | *Hệ thống* | `/requirements.txt` | Tên thư viện Python | Môi trường ảo `.venv` | Quản lý phụ thuộc dự án |
| 13:20 22/10 | Thiện Nhân | `/docs/CHALLENGE_2_TIDE_UNLOCKED.md` | Đề bài & tiêu chí | Cẩm nang Thử thách 2 | Tổng quan Thử thách UNLOCKED của Tide, link Google Form và quy định nộp bài |
| 13:25 22/10 | Thiện Nhân | `/docs/CHALLENGE_2_DEEP_RESEARCH.md` | Tài liệu Tide | Báo cáo nghiên cứu | Nghiên cứu sâu về Emergent Authority, Oblivious Proxy, Raziel MCP và các cạm bẫy |
| 13:30 22/10 | Thiện Nhân | `/docs/CHALLENGE_2_WINNING_STRATEGY.md` | Barem giám khảo | Chiến lược giật giải | Đề án CareVault, kịch bản video demo 2 phút chi tiết từng giây, bản nháp README 300 từ |
| 13:35 22/10 | Thiện Nhân | `/docs/CHALLENGE_2_AGENT_PLAYBOOK.md` | Phân công nhóm | Kế hoạch 4 tiếng | Phân chia công việc giữa 4 Agent theo từng khung giờ trước 17:30 |
| 13:40 22/10 | Thiện Nhân | `/prototype/index.html` | Thao tác người dùng | Giao diện web tương tác | Ứng dụng mẫu UNRELEASED hoàn chỉnh với Web Audio synth và so sánh kiến trúc |
| 13:45 22/10 | Thiện Nhân | `/src/sdk/tidecloak/crypto_engine.js` | Plaintext & 32B Key | Ciphertext AES-GCM | Bộ mã hóa đầu cuối E2EE AES-256-GCM với IV ngẫu nhiên |
| 13:48 22/10 | Thiện Nhân | `/src/sdk/tidecloak/emergent_authority.js` | Policy & Session Nonce | Khóa giải mã RAM | Mô phỏng Tide Fabric Quorum đánh giá chính sách và sinh khóa Just-in-Time |
| 13:50 22/10 | Thiện Nhân | `/src/backend/server.js` | HTTP Requests | JSON API & Auth tokens | Máy chủ Oblivious Proxy Node.js độc lập không giữ Master Key |
| 13:52 22/10 | Thiện Nhân | `/src/security/exploit_simulation.js` | Kịch bản tấn công | Kết quả kiểm thử | Bộ kiểm thử tự động xác thực miễn nhiễm trước tấn công của Admin máy chủ |
| 13:55 22/10 | Thiện Nhân | `/data/mock_assets/album_manifest.json` | Metadata bài hát | JSON Manifest | Siêu dữ liệu chuẩn FLAC/WAV cho album demo "MIDNIGHT CIPHER" |

*(Khi viết xong module mới, Agent hãy thêm một dòng vào cuối bảng trên và commit đẩy lên nhánh của mình)*
