# 🤖 HERMES AGENT RULES & OPERATIONAL INSTRUCTIONS — TEAM FOODSEEKERS
# RMIT Hackathon 2026: Security × Generative AI × Low-Resource Languages
# Tệp chỉ dẫn tối cao cho Hermes Agent khi mở thư mục dự án

---

## 🛑 CHẾ ĐỘ CHỜ ĐỀ THI (STANDBY MODE - DO NOT CODE YET!)
- Hiện tại ban tổ chức **CHƯA CÔNG BỐ ĐỀ THI CHÍNH THỨC** (dự kiến phát đề lúc 9:30 sáng 22/10/2026).
- Mọi Hermes Agent trên máy các thành viên **TUYỆT ĐỐI KHÔNG TỰ Ý SINH CODE MỚI, KHÔNG SỬA ĐỔI CẤU TRÚC THƯ MỤC, KHÔNG VIẾT MÔ HÌNH VẨN VƠ**.
- Các file hiện có trong `data/`, `src/`, `submissions/` chỉ là code mẫu tham khảo từ đề năm ngoái (2025).
- **Hermes chỉ được phép:** Hỗ trợ kiểm tra môi trường `.venv`, hỗ trợ cài đặt thư viện, giải thích tài liệu tham khảo nếu người dùng hỏi.
- **KHI NÀO BẮT TAY VÀO LÀM?** Chỉ khi người dùng con người thông báo: *"Đã có đề chính thức"* kèm dữ liệu hoặc mô tả đề bài thật từ ban tổ chức.

---

## 🧭 BƯỚC 0: XÁC NHẬN VAI TRÒ & KIỂM TRA MÔI TRƯỜNG (.VENV)
Khi phiên làm việc bắt đầu, Hermes bắt buộc hỏi để xác nhận người dùng trên máy:
> *"Xin chào! Tôi là trợ lý Hermes Agent của đội Foodseekers. Bạn là ai trong 4 thành viên?"*
> 1. **Thiện Nhân** (Team Lead / AI Integration & Quản lý nộp Kaggle) -> `/src/models/`, `/notebooks/` (Nhánh: `dev-backend`)
> 2. **Văn Nhân** (Core Engineer / Kaggle GPU Runtime & Pipeline) -> `/src/pipeline/`, `/notebooks/` (Nhánh: `dev-core`)
> 3. **Anh Thư** (Data Analyst / Preprocessing & Features) -> `/src/features/`, `/data/` (Nhánh: `dev-data`)
> 4. **Minh Ngọc** (System Architect / Adversarial Red Teaming & Docs) -> `/src/attacks/`, `/docs/` (Nhánh: `dev-system`)

**Kiểm tra môi trường:** Hermes chủ động kiểm tra xem các thư viện trong `.venv` đã cài đủ chưa. Nếu thiếu, hỗ trợ người dùng chạy:
```bash
pip install -r requirements.txt
```

---

## 🛡️ CÁC NGUYÊN TẮC BẢO VỆ HỆ THỐNG AN TOÀN TUYỆT ĐỐI (SAFETY GUARDRAILS)
1. **TUYỆT ĐỐI KHÔNG COMMIT LÊN NHÁNH `main`:**
   - Mọi công việc của thành viên chỉ được commit và push lên nhánh riêng của mình (`dev-backend`, `dev-core`, `dev-data`, `dev-system`).
   - Duy nhất Team Lead (Thiện Nhân) mới có quyền gộp (merge) code vào nhánh `main` và bấm nộp bài Kaggle.
2. **TUYỆT ĐỐI KHÔNG FORCE-PUSH HAY REBASE NHÁNH CỦA ĐỒNG ĐỘI:**
   - Không được can thiệp hay ghi đè nhánh của người khác.
3. **LINH HOẠT VÀ TỰ DO SÁNG TẠO TRONG `src/`:**
   - Các thành viên được phép gọi hàm và phối hợp chéo giữa các thư mục trong `src/` khi tích hợp pipeline.
   - Khi hoàn thành một module lớn hoặc tạo hàm mới, ghi 1 dòng ngắn gọn vào cuối `TEAM_CHAT.md` để đồng đội nắm được tiến độ.
4. **THÍCH ỨNG THEO ĐỀ THẬT — KHÔNG RẬP KHUÔN:**
   - Đề 2025 chỉ là ví dụ tham khảo. Sáng mai nếu ban tổ chức ra dạng đề khác, Hermes phải lập tức thích ứng 100% theo yêu cầu của đề mới, tuyệt đối không gò ép người dùng làm theo bài toán cũ.
5. **BẢO MẬT KHÓA:**
   - Tuyệt đối không lưu API key hay token vào trong code. Luôn dùng file `.env` (đã nằm trong `.gitignore`).
