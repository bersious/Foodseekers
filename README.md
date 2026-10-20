# 🍽️ Foodseekers — RMIT Hackathon 2026

Dự án tham gia cuộc thi **RMIT Hackathon 2026** (Tổ chức đồng thời tại Việt Nam, Úc và Malaysia) bởi đội thi **Foodseekers** đến từ Trường Đại học Công nghệ Thông tin - ĐHQG-HCM (UIT).

---

## 🎯 Chủ đề cuộc thi (Themes)
**Security × Generative AI × Low-Resource Languages**
* **Security:** Phòng chống các lỗ hổng bảo mật trong hệ thống AI (Prompt Injection, Data Poisoning, Adversarial Attacks).
* **Generative AI:** Tận dụng và tinh chỉnh các mô hình ngôn ngữ lớn (LLMs), tối ưu độ chính xác, độ tin cậy và kiểm chứng dữ liệu.
* **Low-Resource Languages:** Giải quyết thách thức cho các ngôn ngữ ít tài nguyên số hóa, hạn chế ảo giác (hallucination) và nâng cao tính an toàn.

---

## 👥 Đội ngũ thành viên & Phân công nhiệm vụ

| STT | Thành viên | Chuyên ngành | Vai trò chính trong dự án |
| :---: | :--- | :--- | :--- |
| **1** | **Nguyễn Thành Thiện Nhân** | Trí tuệ nhân tạo (TTNT) | **Team Lead & AI Integration:** Tích hợp mô hình AI, Prompt Engineering, kết nối API và điều phối kỹ thuật. |
| **2** | **Nguyễn Văn Nhân** | Khoa học máy tính (KHMT) | **Core Engineer & Pipeline:** Xây dựng logic code chính, ráp nối pipeline dữ liệu/mô hình, quản lý môi trường và xử lý lỗi kỹ thuật. |
| **3** | **Nguyễn Trần Anh Thư** | Khoa học dữ liệu (KHDL) | **Data Analyst & Evaluation:** Phân tích và làm sạch dữ liệu (Data Preprocessing), theo dõi các chỉ số đánh giá (Metrics) và định dạng file nộp bài Kaggle. |
| **4** | **Trần Minh Ngọc** | Hệ thống thông tin (HTTT) | **System Architecture & Security Testing:** Thiết kế kiến trúc luồng hệ thống, xây dựng các kịch bản kiểm thử bảo mật đối kháng và hoàn thiện tài liệu, báo cáo. |

---

## 📂 Cấu trúc thư mục (Repository Structure)

```text
Foodseekers/
├── README.md                 # Giới thiệu dự án và phân công nhóm
├── PROJECT_RULES.md          # Quy ước kỹ thuật và phân chia nhánh làm việc
├── requirements.txt          # Danh sách thư viện Python cần thiết
├── data/                     # Thư mục chứa dữ liệu mẫu hoặc mô tả dữ liệu
├── notebooks/                # Các notebook thử nghiệm trên Kaggle / Colab
├── src/                      # Mã nguồn chính của dự án
│   ├── backend/              # Mã nguồn xử lý mô hình, API và logic giải thuật
│   ├── data_processing/      # Script làm sạch và tiền xử lý dữ liệu
│   └── security_tests/       # Kịch bản kiểm thử bảo mật (Prompt Injection / Adversarial)
└── docs/                     # Tài liệu thiết kế hệ thống, sơ đồ kiến trúc và báo cáo
```

---

## 🛠️ Quy ước làm việc Git (Git Collaboration Rules)

1. **Nhánh chính (`main`):** Chỉ chứa các phiên bản ổn định đã được kiểm thử, dùng để nộp bài hoặc chạy bản phát hành cuối.
2. **Nhánh chức năng (`feature branches`):** Mỗi thành viên/vai trò làm việc trên nhánh riêng, ví dụ:
   - `dev-backend`: Dành cho module xử lý mô hình và API.
   - `dev-data`: Dành cho module làm sạch dữ liệu.
   - `dev-system`: Dành cho tài liệu và kịch bản kiểm thử hệ thống.
3. **Quy trình gộp code:** Tạo Pull Request (PR) hoặc trao đổi trước khi gộp vào nhánh `main` để tránh xung đột mã nguồn (*merge conflicts*).

---

## 📌 Công nghệ sử dụng (Tech Stack)
* **Ngôn ngữ:** Python 3.10+
* **Nền tảng thi đấu:** Kaggle (SkywardAI Labs)
* **Thư viện AI/ML:** `transformers`, `torch`, `datasets`, `scikit-learn`, `pandas`, `numpy`
* **Công cụ hỗ trợ:** Hermes Agent, Git/GitHub, VS Code
