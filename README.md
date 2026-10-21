# 🍽️ Foodseekers — RMIT Hackathon 2026

**Team Foodseekers** — Đại học Công nghệ Thông tin (UIT), ĐHQG-HCM — tham gia cuộc thi lập trình quốc tế **RMIT Hackathon 2026**.

---

## 🎯 Chủ đề cuộc thi

**Security × Generative AI × Low-Resource Languages**

| Trụ cột | Mô tả |
| :--- | :--- |
| **Security** | Phòng chống lỗ hổng trong hệ thống AI: prompt injection, data poisoning, adversarial input. |
| **Generative AI** | Tận dụng và tinh chỉnh LLM: tăng độ chính xác, độ tin cậy, khả năng có căn cứ. |
| **Low-Resource Languages** | Giảm sai sót của AI trên các ngôn ngữ thiếu dữ liệu huấn luyện. |

---

## 👥 Đội hình & Phân công

| # | Thành viên | GitHub | Nhánh | Vai trò |
| :---: | :--- | :--- | :--- | :--- |
| 1 | **Nguyễn Thành Thiện Nhân** | `bersious` | `dev-backend` | **Team Lead & AI Integration** — tích hợp mô hình AI, prompt engineering, API & nộp bài Kaggle. |
| 2 | **Nguyễn Văn Nhân** | `NguyenNhan1107` | `dev-core` | **Core Engineer** — pipeline trên Kaggle, GPU runner, xử lý lỗi kỹ thuật. |
| 3 | **Trần Nguyễn Anh Thư** | `tuna184` | `dev-data` | **Data Analyst** — tiền xử lý văn bản, đo lường độ chính xác, định dạng file nộp bài. |
| 4 | **Trần Minh Ngọc** | *(gửi username cho Lead)* | `dev-system` | **System Architecture** — thiết kế kiến trúc, kịch bản kiểm thử bảo mật đối kháng, tài liệu & báo cáo. |

---

## 🏗️ Kiến trúc thư mục

```text
Foodseekers/
├── README.md            # Tài liệu tổng quan dự án
├── AGENT_RULES.md       # Quy tắc bắt buộc cho Agent và con người
├── .cursorrules         # Quy tắc ngắn cho Cursor / Cline AI
├── TEAM_CHAT.md         # Kênh chat nội bộ cập nhật tiến độ liên tục
├── CODE_INDEX.md        # Sổ tay tra cứu module và hàm dùng chung
├── requirements.txt     # Danh sách thư viện Python
├── .gitignore           # File cấm đẩy lên Git (.env, key, data nặng)
│
├── submissions/         # (Lead) Nơi lưu các file submission.csv & sổ log điểm
│   └── README.md        # Bảng theo dõi 10 lượt nộp Kaggle (CV vs LB)
├── notebooks/           # (Core) Notebook huấn luyện trên Kaggle GPU
├── data/                # (Data) Dữ liệu thô và dữ liệu sạch (train/test)
├── docs/                # Tài liệu chiến lược, đề thi các năm, báo cáo kỹ thuật
│   ├── STRATEGY.md      # Phân tích chiến lược thi bám sát đề 2025
│   ├── DEADLINES.md     # Mốc thời gian chi tiết 2 ngày thi (22-23/10)
│   └── rmit-de-quac-2024-2025.md # Dữ liệu tổng hợp đề thi thực tế
│
└── src/                 # Mã nguồn chia theo dòng dữ liệu (Pipeline)
    ├── features/        # (Data) Tiền xử lý, bỏ dấu, tách từ, trích xuất đặc trưng
    ├── models/          # (Lead) Baseline, PhoBERT, DeBERTa, Ensemble
    ├── pipeline/        # (Core) Pipeline huấn luyện đầu cuối & xuất dự đoán
    └── attacks/         # (System) Mẫu câu lệnh tấn công đối kháng (Red Teaming)
```

---

## 🤝 Quy trình làm việc

### Chuẩn bị trước khi code
1. `git pull origin main` để đồng bộ.
2. Đọc **5 dòng cuối** của `TEAM_CHAT.md` để nắm tiến độ đồng đội.
3. Tra cứu `CODE_INDEX.md` để tái sử dụng module đã có, tránh trùng lặp.

### Trong khi code
4. Chỉ làm việc trong **thư mục** đã được phân công.
5. **Cấm** ghi API key, token hay mật khẩu vào code — phải dùng biến môi trường hoặc file `.env` (đã có trong `.gitignore`).
6. Thêm thư viện mới → bổ sung tên + phiên bản vào `requirements.txt`.

### Sau khi hoàn thành
7. Thêm **1 dòng báo cáo tiếng Việt** vào cuối `TEAM_CHAT.md` (định dạng: `[Agent X - Tên] (HH:MM): ...`).
8. Thêm **1 dòng mô tả** vào `CODE_INDEX.md` nếu xây dựng module/hàm mới.
9. `git add . && git commit -m "..." && git push origin dev-<tên>`.
10. **Cấm tuyệt đối** push trực tiếp lên `main`.

---

## 🛠️ Công nghệ sử dụng

| Lớp | Công nghệ |
| :--- | :--- |
| Ngôn ngữ | Python 3.10+ |
| Nền tảng thi | **Kaggle** (do SkywardAI Labs tổ chức) |
| AI / ML | `transformers`, `torch`, `datasets`, `accelerate`, `scikit-learn` |
| Dữ liệu | `pandas`, `numpy`, `underthesea` (xử lý tiếng Việt) |
| Hỗ trợ thi | Cursor (API Vilao), Git/GitHub, Jupyter Notebook |

---

## 📖 Tài liệu chi tiết

| File | Mục đích |
| :--- | :--- |
| [`AGENT_RULES.md`](./AGENT_RULES.md) | Quy tắc lãnh thổ, bảo mật key, giao tiếp giữa các Agent. |
| [`.cursorrules`](./.cursorrules) | Phiên bản ngắn cho Cursor AI. |
| [`TEAM_CHAT.md`](./TEAM_CHAT.md) | Nhật ký báo cáo & bàn giao giữa 4 Agent. |
| [`CODE_INDEX.md`](./CODE_INDEX.md) | Tra cứu hàm/module đã có sẵn. |

---

<div align="center">

**Team Foodseekers** · UIT · Vietnam

</div>
