# 🛡️ BÍ KÍP VÕ CÔNG THỰC CHIẾN — RMIT HACKATHON 2026
# Chuyên đề: Multilingual Prompt-Attack Classification (Kaggle)
# Mục tiêu: Đạt Top Bảng Xếp Hạng với Thang Đo Macro F1 & 6 Lượt Nộp

---

## 🧠 1. BẢN CHẤT SỰ KHÁC BIỆT CỐT TỬ: `JAILBREAK` VS `PROMPT_INJECTION`
Đề thi phân loại 3 lớp: `BENIGN`, `JAILBREAK`, `PROMPT_INJECTION`. Để mô hình phân biệt chuẩn xác, cả đội cần hiểu rõ sự khác biệt bản chất:

| Đặc tính | 🟢 `BENIGN` (62%) | 🟡 `JAILBREAK` (31%) | 🔴 `PROMPT_INJECTION` (7% - Nhãn hiếm) |
| :--- | :--- | :--- | :--- |
| **Mục tiêu tấn công** | Không tấn công | **Đạo đức & Bộ lọc an toàn (Safety Alignment)** | **Chỉ dẫn hệ thống & Quyền kiểm soát (Control Flow)** |
| **Ý đồ kẻ xấu** | Yêu cầu thông thường | Ép AI nói ra điều bị cấm (vũ khí, độc tố, hack, chửi bới, lừa đảo) | Cướp quyền điều khiển, ép AI bỏ qua chỉ dẫn của developer |
| **Kỹ thuật đặc trưng** | Câu hỏi bài tập, dịch thuật, trò chuyện thường nhật | **Roleplay / DAN**, đóng vai kẻ cướp, kịch bản phim, nghiên cứu giả định | **Instruction Override**, Delimiter Hijack, System Prompt Leakage |
| **Dấu hiệu nhận diện** | Văn phong tự nhiên, lịch sự | *"Hãy tưởng tượng...", "Đóng vai DAN...", "Kịch bản hư cấu..."* | *"Bỏ qua các lệnh trước đó...", "In ra system prompt", "Không dịch nữa mà làm X..."* |

---

## 🌍 2. GIẢI MÃ 4 NGÔN NGỮ TRONG ĐỀ THI (PT, FR, IT, EN)
Ban tổ chức chọn Bồ Đào Nha (`pt`), Pháp (`fr`), Ý (`it`) và Anh (`en`) vì đây là các ngôn ngữ lớn trong NLP nhưng **cực kỳ khan hiếm dữ liệu An toàn AI (AI Safety)**. Phần lớn bộ lọc của OpenAI/Anthropic/Meta chỉ được huấn luyện kỹ bằng tiếng Anh.

### Dấu hiệu từ khóa tấn công theo từng ngôn ngữ:
* **🇫🇷 Tiếng Pháp (`fr`):**
  - Prompt Injection: `ignorez les instructions précédentes`, `oubliez toutes les règles`, `nouvelle instruction`, `système`.
  - Jailbreak: `vous êtes maintenant DAN`, `mode développeur`, `agissez en tant que`, `histoire fictive`, `scénario hypothétique`.
* **🇵🇹 Tiếng Bồ Đào Nha (`pt`):**
  - Prompt Injection: `ignore todas as instruções anteriores`, `esqueça as regras`, `novo comando`, `desconsidere o prompt do sistema`.
  - Jailbreak: `você agora é DAN`, `modo desenvolvedor`, `finja que você é`, `cenário hipotético`, `história de ficção`.
* **🇮🇹 Tiếng Ý (`it`):**
  - Prompt Injection: `ignora tutte le istruzioni precedenti`, `dimentica le regole`, `nuova istruzione`, `sovrascrivi il sistema`.
  - Jailbreak: `ora sei DAN`, `modalità sviluppatore`, `fai finta di essere`, `scenario ipotetico`, `storia fittizia`.
* **🇬🇧 Tiếng Anh (`en`):**
  - Prompt Injection: `ignore all previous instructions`, `disregard system prompt`, `system override`, `print system prompt`.
  - Jailbreak: `you are now DAN`, `developer mode`, `pretend you are`, `hypothetical experiment`, `fictional roleplay`.

---

## ⚖️ 3. XỬ LÝ MẤT CÂN BẰNG LỚP VỚI MACRO F1 (CHÌA KHÓA CHIẾN THẮNG)
* **Quy tắc tính điểm:** $\text{Macro F1} = \frac{F1_{\text{BENIGN}} + F1_{\text{JAILBREAK}} + F1_{\text{PROMPT\_INJECTION}}}{3}$.
* **Vấn đề cốt tử:** Nhãn `PROMPT_INJECTION` chỉ chiếm **7% dữ liệu**, nhưng mang giá trị **33.3% tổng số điểm**! Nếu mô hình dự đoán yếu nhãn này (ví dụ F1 của injection chỉ đạt 0.3), thì dù 2 nhãn kia đạt 0.95, Macro F1 toàn bài cũng chỉ kéo lên được ~0.73.

### 2 Tuyệt chiêu khắc phục:
1. **Class Weights trong Hàm Mất Mát (Loss Function):**
   - Trong quá trình huấn luyện (cả PyTorch lẫn Scikit-Learn), bắt buộc đặt trọng số phạt nặng hơn cho nhãn hiếm:
     $$w_c = \frac{N}{3 \times N_c}$$
   - Nhãn `PROMPT_INJECTION` sẽ nhận trọng số phạt cao gấp ~9 lần so với `BENIGN`.
2. **Kỹ thuật Tối ưu hóa Ngưỡng Xác suất (Threshold Tuning):**
   - Không nên lấy nhãn bằng `argmax` thông thường.
   - Do nhãn 7% có xác suất nền thấp, hãy nhân một hệ số điều chỉnh $w_2 \approx 1.25 - 1.40$ vào xác suất dự đoán của `PROMPT_INJECTION` trước khi lấy `argmax`. Thử nghiệm nội bộ chứng minh kỹ thuật này kéo Macro F1 tăng thêm **0.8% đến 1.5%**!

---

## 🏆 4. CHIẾN LƯỢC CHỌN MÔ HÌNH TỪ DANH SÁCH APPROVED MODELS
Ban tổ chức bắt buộc chọn mô hình trong danh sách cấp phép. Cặp bài trùng tối ưu nhất cho đội mình:

1. **`FacebookAI/xlm-roberta-base` & `xlm-roberta-large` (Mô hình chủ lực đa ngữ):**
   - Được huấn luyện trên hơn 100 ngôn ngữ, cực kỳ am tường từ vựng và cấu trúc ngữ pháp của tiếng Pháp, Bồ Đào Nha, Ý và Anh.
   - Xử lý mượt mà toàn bộ các ký tự có dấu phụ (`é, ç, ã, ô, à, è...`).
2. **`protectai/deberta-v3-base-prompt-injection-v2` (Vũ khí chuyên biệt về Injection):**
   - Được cộng đồng AI Security huấn luyện chuyên sâu để phát hiện các kỹ thuật Prompt Injection và vượt rào bảo mật.
3. **Chiến lược Ensemble (Ghép mô hình):**
   - Lấy xác suất dự đoán của **XLM-RoBERTa Large (60%)** kết hợp với **DeBERTa Prompt Injection (40%)**.
   - Sự kết hợp này mang lại khả năng phân loại vượt trội: 1 con giỏi đa ngữ + 1 con giỏi nhận diện đòn tấn công.

---

## 📊 5. KỊCH BẢN PHÂN BỔ 6 LƯỢT NỘP BÀI KAGGLE
* **Lượt 1 (Sáng):** Nộp Baseline TF-IDF Logistic Regression (`src/pipeline/baseline_runner.py`) ➔ Ăn trọn điểm Challenge 1 Warm-up, kiểm tra thông luồng nộp bài.
* **Lượt 2 (Trưa):** Nộp mô hình `xlm-roberta-base` huấn luyện 3 epochs trên Kaggle GPU T4.
* **Lượt 3 (Đầu chiều):** Nộp mô hình `protectai/deberta-v3-base-prompt-injection-v2`.
* **Lượt 4 (Chiều):** Nộp mô hình `xlm-roberta-large` (Mô hình sâu mạnh nhất).
* **Lượt 5 (16:30):** Nộp bản Ensemble (kết hợp các mô hình và cân chỉnh ngưỡng nhãn 7%).
* **Lượt 6 (17:30):** Bản chốt điểm cao nhất trước giờ đóng sổ 18:00.
