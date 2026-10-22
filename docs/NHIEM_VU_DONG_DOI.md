# 🎯 BẢNG GIAO VIỆC & PROMPT TÁC CHIẾN CHO ANH THƯ & MINH NGỌC
# Đội Foodseekers — RMIT Hackathon 2026 (Chủ đề: Multilingual Prompt-Attack Classification)
# Hướng dẫn: Các bạn chỉ cần copy nguyên văn đoạn Prompt bên dưới, dán vào con AI (Hermes / Cline) trên máy mình là AI sẽ tự động làm việc!

---

## 🌸 1. NHIỆM VỤ DÀNH CHO BẠN ANH THƯ (Nhánh `dev-data`)
* **Vai trò:** Data Analyst & Feature Engineering.
* **Mục tiêu chính:** 
  - Phân tích và làm sạch dữ liệu văn bản 4 thứ tiếng: Bồ Đào Nha (`pt`), Pháp (`fr`), Ý (`it`), Anh (`en`).
  - Xây dựng bộ đặc trưng từ khóa để bắt thật nhạy nhãn hiếm 7% `PROMPT_INJECTION` (đây là nhãn quyết định 1/3 tổng điểm vì thi bằng Macro F1).
  - Chạy thử nghiệm mô hình đặc trưng trên máy để tìm ra điểm CV > 0.91, xuất file CSV dự đoán gửi cho Lead (Thiện Nhân).

### 📋 PROMPT ANH THƯ COPY DÁN CHO CON AI TRÊN MÁY MÌNH:
```text
Tôi là Trần Nguyễn Anh Thư (nhánh dev-data), phụ trách Data Analyst của đội Foodseekers thi RMIT Hackathon 2026.
Nhiệm vụ của bạn:
1. Đọc file `data/train.csv` và `data/test.csv`. Phân tích phân phối của 3 nhãn (BENIGN 62%, JAILBREAK 31%, PROMPT_INJECTION 7%) trên 4 ngôn ngữ (pt, fr, it, en).
2. Xây dựng bộ từ khóa đặc trưng cho từng thứ tiếng:
   - Từ khóa Prompt Injection (lệnh cướp quyền điều khiển, bỏ qua system prompt):
     + Pháp (fr): "ignorez les instructions précédentes", "oubliez les règles", "système", "nouvelle instruction".
     + Bồ Đào Nha (pt): "ignore todas as instruções anteriores", "esqueça as regras", "desconsidere o prompt".
     + Ý (it): "ignora tutte le istruzioni precedenti", "dimentica le regole", "nuova istruzione".
     + Anh (en): "ignore all previous instructions", "disregard system prompt", "system override".
   - Từ khóa Jailbreak (thao túng đạo đức, đóng vai DAN):
     + DAN, roleplay, hypothetical, kịch bản hư cấu, mode développeur, modo desenvolvedor.
3. Thử nghiệm kết hợp TF-IDF N-grams (1-3) với bộ đặc trưng từ khóa và mô hình Logistic Regression (hoặc LightGBM) có class_weight='balanced'.
4. Đánh giá bằng 5-Fold Stratified Cross-Validation với thang đo Macro F1.
5. Khi tìm được điểm Macro F1 > 0.91, hãy xuất file dự đoán ra `submissions/thu_feature_submission.csv` (đúng 6.000 dòng test, gồm 2 cột id,label) và báo cáo lại kết quả cho tôi!
```

---

## 🌺 2. NHIỆM VỤ DÀNH CHO BẠN MINH NGỌC (Nhánh `dev-system`)
* **Vai trò:** System Architect & Transformer Modeling.
* **Mục tiêu chính:**
  - Lên Kaggle Notebook (hoặc chạy local nếu máy có GPU), tận dụng các mô hình trong danh sách cấp phép (Approved Models) của ban tổ chức.
  - Trọng tâm thử nghiệm 2 mô hình mạnh nhất:
    1. `protectai/deberta-v3-base-prompt-injection-v2`: Mô hình được huấn luyện sẵn chuyên trị Prompt Injection.
    2. `FacebookAI/xlm-roberta-base`: Mô hình đa ngữ kinh điển cực mạnh về tiếng Pháp, Bồ Đào Nha, Ý.
  - Chạy thử nghiệm nộp bài trên tài khoản Kaggle của Ngọc để test điểm Public Leaderboard. Nếu đạt điểm cao (> 0.92), gửi file CSV về cho Lead (Thiện Nhân) gộp vào bản chính.
  - Chuẩn bị khung báo cáo kỹ thuật và slide tóm tắt giải pháp cho ban giám khảo.

### 📋 PROMPT MINH NGỌC COPY DÁN CHO CON AI TRÊN MÁY MÌNH:
```text
Tôi là Trần Minh Ngọc (nhánh dev-system), phụ trách System Architect & Transformer Modeling của đội Foodseekers thi RMIT Hackathon 2026.
Nhiệm vụ của bạn:
1. Đọc kỹ file `docs/rmit-2026-multilingual-playbook.md` để nắm rõ danh sách mô hình được ban tổ chức cho phép (Approved Models) và thang đo Macro F1.
2. Xây dựng một script huấn luyện hoặc Kaggle Notebook (đặt tên `UIT_SGS_Foodseekers_C1`) để fine-tune mô hình Transformers:
   - Ưu tiên 1: `protectai/deberta-v3-base-prompt-injection-v2` (chuyên trị Prompt Injection).
   - Ưu tiên 2: `FacebookAI/xlm-roberta-base` (chuyên trị đa ngữ 4 thứ tiếng pt/fr/it/en).
3. Thiết lập hàm Loss có trọng số cân bằng lớp (Class Weights) để phạt nặng lỗi sai ở nhãn 7% PROMPT_INJECTION.
4. Xuất file dự đoán trên tập `data/test.csv` thành file CSV đúng chuẩn (gồm 2 cột id,label, đúng 6.000 dòng test).
5. Hướng dẫn tôi cách chạy thử và nộp thử trên Kaggle để kiểm tra điểm Leaderboard thực tế. Nếu điểm > 0.92, tôi sẽ gửi file này cho Team Lead (Thiện Nhân) nộp vào bảng xếp hạng chính của đội.
6. Soạn thảo sẵn khung báo cáo kỹ thuật (System Architecture Report) giải thích lý do đội chọn kiến trúc lai và cách xử lý ngôn ngữ đa ngữ để nộp cho ban giám khảo.
```

---

## 🔄 3. QUY TRÌNH PHỐI HỢP VỚI TEAM LEAD (THIỆN NHÂN)
1. **Thư và Ngọc chạy thử nghiệm độc lập trên nhánh của mình:**
   - Thư làm việc trên nhánh `dev-data`.
   - Ngọc làm việc trên nhánh `dev-system`.
2. **Nộp thử nghiệm:**
   - Các bạn có thể dùng tài khoản Kaggle cá nhân của mình để nộp thử nghiệm file CSV mà con AI trên máy các bạn vừa tạo ra để xem điểm số thực tế trên Public Leaderboard là bao nhiêu.
3. **Chuyển giao kết quả tốt nhất:**
   - Khi chạy ra file có điểm cao, các bạn chỉ cần:
     1. Push file code và file CSV dự đoán lên nhánh Git của mình.
     2. Nhắn 1 câu vào nhóm Zalo hoặc file `TEAM_CHAT.md`: *"Nhân ơi tao chạy ra bản điểm [X] rồi nè, file nằm ở [đường dẫn], mày lấy nộp vào team chính nha!"*.
   - Lead Thiện Nhân sẽ kiểm tra tính hợp lệ và bấm nộp chính thức cho đội `Foodseekers`!
