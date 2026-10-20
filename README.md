# 🍽️ Foodseekers — RMIT Hackathon 2026

Dự án tham gia cuộc thi **RMIT Hackathon 2026** (tổ chức đồng thời tại Việt Nam, Úc và Malaysia) bởi đội thi **Foodseekers** đến từ Trường ĐH Công nghệ Thông tin - ĐHQG-HCM (UIT).

---

## 🎯 Chủ đề cuộc thi (Themes)
**Security × Generative AI × Low-Resource Languages**
* **Security:** Phòng chống các lỗ hổng bảo mật trong hệ thống AI (Prompt Injection, Data Poisoning, Adversarial Attacks).
* **Generative AI:** Tận dụng và tinh chỉnh các mô hình ngôn ngữ lớn (LLMs), tối ưu độ chính xác, độ tin cậy và kiểm chứng dữ liệu.
* **Low-Resource Languages:** Giải quyết thách thức cho các ngôn ngữ ít tài nguyên số hóa, hạn chế ảo giác (hallucination) và nâng cao tính an toàn.

---

## 👥 Đội ngũ thành viên & Phân công nhiệm vụ

| STT | Thành viên | GitHub | Nhánh làm việc | Vai trò chính trong dự án |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Nguyễn Thành Thiện Nhân** (`bersious`) | `bersious` | `dev-backend` | **Team Lead & AI Integration:** Tích hợp mô hình AI, Prompt Engineering, kết nối API, quản lý Kaggle & nộp bài. |
| **2** | **Nguyễn Văn Nhân** | `NguyenNhan1107` | `dev-core` | **Core Engineer & Pipeline:** Xây dựng logic code chính, ráp nối pipeline trên Kaggle, xử lý lỗi kỹ thuật. |
| **3** | **Trần Nguyễn Anh Thư** | *(gửi username cho Team Lead)* | `dev-data` | **Data Analyst & Evaluation:** Phân tích, làm sạch dữ liệu văn bản, định dạng file nộp bài Kaggle. |
| **4** | **Trần Minh Ngọc** | *(gửi username cho Team Lead)* | `dev-system` | **System Architecture & Security Testing:** Thiết kế luồng hệ thống, kịch bản kiểm thử bảo mật đối kháng, hoàn thiện tài liệu. |

> **Ghi chú:** Hai bạn 3 và 4 nhắn username GitHub qua Zalo cho Nhân là Nhân add vào repo trong 5 phút.

---

## 📂 Cấu trúc thư mục (Repository Structure)

```text
Foodseekers/
├── README.md                 # Giới thiệu dự án và phân công nhóm (file này)
├── AGENT_RULES.md            # Quy tắc bắt buộc cho cả con người lẫn AI Agent
├── .cursorrules              # Quy tắc ngắn dành cho Cursor AI
├── TEAM_CHAT.md              # Kênh chat nội bộ giữa 4 Agent (status, handoff, báo lỗi)
├── CODE_INDEX.md             # Sổ tay tra cứu các module/hàm/dữ liệu đã có sẵn
├── requirements.txt          # Danh sách thư viện Python
├── .gitignore                # File cấm đẩy lên Git (key, dataset nặng, ...)
├── data/                     # (dev-data) tiền xử lý dữ liệu
├── notebooks/                # (dev-core) notebook Kaggle
├── src/
│   ├── backend/              # (dev-backend) Mô hình AI, API, prompt template
│   ├── pipeline/             # (dev-core) Pipeline chạy trên Kaggle
│   └── security/             # (dev-system) Kịch bản kiểm thử bảo mật
└── docs/                     # (dev-system) Báo cáo, sơ đồ kiến trúc
```

---

## 🛠️ Quy ước làm việc Git (Git Collaboration Rules)

1. **Nhánh chính (`main`):** Chỉ chứa bản ổn định. **Cấm push trực tiếp vào `main`.**
2. **Nhánh chức năng (`dev-*`):** Mỗi thành viên làm việc trên nhánh riêng (xem bảng thành viên ở trên).
   * `dev-backend`: Mô hình AI, API, prompt template (Thiện Nhân)
   * `dev-core`: Pipeline Kaggle, GPU runner (Văn Nhân)
   * `dev-data`: Data preprocessing, metrics (Anh Thư)
   * `dev-system`: System architecture, security test, docs (Minh Ngọc)
3. **Trước khi viết code:** Đọc `TEAM_CHAT.md` (5 dòng cuối) + `CODE_INDEX.md` để biết đồng đội đang làm gì, tránh trùng.
4. **Sau khi viết xong:** Ghi 1 dòng vào cuối `TEAM_CHAT.md` + thêm 1 dòng vào `CODE_INDEX.md` (nếu viết hàm mới), rồi commit và push lên nhánh của mình.
5. **Trước hạn chót 17h30 (22/10):** Commit bản cuối lên nhánh, thông báo Team Lead để gộp vào `main` rồi nộp lên Kaggle.

---

## 📌 Công nghệ sử dụng (Tech Stack)
* **Ngôn ngữ:** Python 3.10+
* **Nền tảng thi đấu:** Kaggle (SkywardAI Labs)
* **Thư viện AI/ML:** `transformers`, `torch`, `datasets`, `scikit-learn`, `pandas`, `numpy`, `underthesea`
* **Công cụ hỗ trợ:** Cursor (API Vilao), Hermes Agent, Git/GitHub

---

## 🕒 Lịch trình thi (Hackathon Schedule)

| Ngày | Giờ | Hoạt động |
| :---: | :---: | :--- |
| 22/10 | 8:15 – 9:00 | Check-in cả đội tại Canopy, Tòa nhà 2 |
| 22/10 | 9:30 | Ban tổ chức mở đề + briefing |
| 22/10 | 10:00 – 18:00 | Làm bài trên Kaggle |
| 22/10 | **18:00** | **Hạn chót nộp bài** |
| 23/10 | 10:00 – 13:30 | Lễ trao giải |

**Foodseekers — UIT — RMIT Hackathon 2026** 🚀
