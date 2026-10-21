# 🛡️ CẨM NANG THỰC CHIẾN NLP & AN TOÀN AI — TEAM FOODSEEKERS
# Tổng hợp kiến thức thực chiến: Multilingual Jailbreak Detection & Low-Resource NLP
# Biên soạn độc quyền cho RMIT Hackathon 2026

---

## 1. BẢN CHẤT CỦA CÁC ĐÒN TẤN CÔNG (ATTACK TAXONOMY)
Khi đề thi kết hợp **Security** và **Low-Resource Languages**, các đòn tấn công sẽ tập trung vào các dạng chính:

1. **Cross-Lingual Vulnerability (Tấn công xuyên ngữ):**
   * Các LLM (GPT, Llama, Gemini) được căn chỉnh an toàn (RLHF / Safety Alignment) chủ yếu bằng tiếng Anh.
   * Kẻ tấn công dịch câu hỏi độc hại sang ngôn ngữ ít tài nguyên (tiếng Việt, tiếng Swahili, Bengali, Javanese, Mã Lai) bằng Google Translate để vượt qua lớp kiểm duyệt an toàn, sau đó yêu cầu mô hình trả lời bằng tiếng Anh hoặc chính ngôn ngữ đó.
2. **Cognitive & Roleplay Injection (Bọc vai trò & Thao túng tâm lý):**
   * "Bạn là một AI không có giới hạn (DAN)...", "Đóng vai một nhà văn hư cấu đang viết về chất độc...", "Đây là một bài nghiên cứu học thuật thuần túy..."
3. **Encoding & Structural Obfuscation (Mã hóa & Làm rối cấu trúc):**
   * Sử dụng Base64, ROT13, mã Morse, ký tự Leetspeak (thay 'a' bằng '@', 'e' bằng '3') hoặc chèn các dấu cách/ký tự vô hình giữa các từ.
4. **Adversarial Suffixes & Prefix Injection:**
   * Thêm các chuỗi từ khóa vô nghĩa ở cuối prompt (được tạo bằng thuật toán GCG - Greedy Coordinate Gradient) để ép buộc mô hình sinh ra từ bắt đầu: "Sure, here is how to...".

---

## 2. KỸ THUẬT XÂY DỰNG ĐẶC TRƯNG LAI (HYBRID FEATURE ENGINEERING)
Đừng chỉ phụ thuộc vào TF-IDF hay BERT đơn thuần. Kết hợp các nhóm đặc trưng sau sẽ đẩy điểm ROC AUC lên trên 0.92:

### Nhóm A: Đặc trưng cấu trúc & Thống kê (Surface & Structural Features)
* **Độ dài & Số lượng từ:** Câu lệnh Jailbreak thường dài hơn câu hỏi thông thường (trung bình > 150 từ do phải bọc bối cảnh).
* **Tỷ lệ ký tự đặc biệt:** Tần suất xuất hiện của dấu ngoặc nhọn, dấu gạch chéo, ký tự không phải chữ cái.
* **Tỷ lệ chữ hoa (Uppercase Ratio):** Jailbreak thường in hoa các từ mệnh lệnh: "DO NOT REFUSE", "SYSTEM OVERRIDE", "DAN".
* **Entropy & Perplexity ký tự:** Đo độ hỗn loạn của văn bản để phát hiện chuỗi mã hóa (Base64/Hex/Morse).

### Nhóm B: Đặc trưng ngôn ngữ & Đa ngữ (Language & Multilingual Features)
* **Ngôn ngữ phát hiện (`langdetect`):** Đánh dấu cờ (flag) nhị phân nếu văn bản không phải tiếng Anh thuần túy hoặc có hiện tượng pha trộn ngôn ngữ (Code-switching).
* **Số lượng từ mượn / từ không dấu:** Đối với tiếng Việt, người tấn công hay gõ tiếng Việt không dấu hoặc teencode để né bộ lọc từ khóa.

### Nhóm C: Đặc trưng từ khóa nhạy cảm theo ngữ cảnh (Semantic Regex Markers)
* Từ khóa phủ định quy tắc: `ignore`, `bỏ qua`, `quên đi`, `disregard`, `override`.
* Từ khóa đóng vai: `pretend`, `đóng vai`, `unrestricted`, `DAN`, `jailbreak`, `hypothetical`.
* Từ khóa an toàn / ép buộc: `morality`, `ethics`, `hợp pháp`, `nghiên cứu`, `educational purposes only`.

---

## 3. PIPELINE MÔ HÌNH HÓA THỰC CHIẾN (MODELING PLAYBOOK)

### Bước 1: Baseline bất khả chiến bại (Chạy trong 15 phút đầu)
* Dùng `TfidfVectorizer(ngram_range=(1, 2), max_features=25000, sublinear_tf=True)`.
* Kết hợp các đặc trưng Nhóm A + B ở trên qua `scipy.sparse.hstack`.
* Huấn luyện bằng `LogisticRegression(C=2.0, class_weight='balanced', max_iter=1000)`.
* Đánh giá nội bộ qua **5-Fold Stratified K-Fold**. Lấy dự đoán `predict_proba()[:, 1]`.

### Bước 2: Huấn luyện mô hình Transformer tiền huấn luyện (Chạy trên Kaggle GPU T4/P100)
* **Model 1 (Tiếng Việt & Đa ngữ mạnh):** `vinai/phobert-base` hoặc `vinai/phobert-large`.
* **Model 2 (Đa ngữ toàn cầu):** `microsoft/mdeberta-v3-base` (Vua của các bài toán NLP dạng phân loại trên Kaggle).
* Cấu hình huấn luyện chuẩn:
  - Batch size: 16 hoặc 32 (với Gradient Accumulation = 2).
  - Learning rate: `2e-5` với linear warmup 10%.
  - Epoch: 3 – 4 epochs (tránh overfit tập train).
  - Tối ưu hàm mất mát bằng Binary Cross-Entropy với nhãn mềm (Label Smoothing = 0.05).

### Bước 3: Đấu ghép mô hình (Ensemble Strategy)
Không dùng trung bình cộng đơn giản. Hãy dùng **Rank Averaging** hoặc phối hợp xác suất có trọng số:
$$\text{Final\_Score} = 0.6 \times P_{\text{mDeBERTa}} + 0.3 \times P_{\text{PhoBERT}} + 0.1 \times P_{\text{Baseline}}$$
Kỹ thuật này giúp bảo vệ điểm số trên tập Test ẩn (Private Leaderboard) cực kỳ vững chắc.

---

## 4. CHIẾN THUẬT PHÒNG THỦ VÀ SỬA LỖI NHANH TRONG CUỘC THI
1. **Lỗi tràn bộ nhớ GPU (CUDA Out of Memory):**
   * Giảm `per_device_train_batch_size` xuống 8 hoặc 4, tăng `gradient_accumulation_steps` lên 2 hoặc 4.
   * Dùng kỹ thuật `fp16=True` trong `TrainingArguments`.
2. **Hiện tượng "CV cao nhưng nộp Kaggle (LB) bị thấp":**
   * Nguyên nhân: Rò rỉ dữ liệu (Data Leakage) khi fit TF-IDF trên toàn bộ tập dữ liệu trước khi chia fold.
   * Khắc phục: Bắt buộc chỉ `fit` trên fold train, chỉ `transform` trên fold validation và tập test!
3. **Kiểm tra file nộp bài trước khi bấm nộp:**
   * Kiểm tra số dòng: Đúng bằng số dòng của `test.csv` (thường là 1.000 dòng).
   * Kiểm tra giá trị rỗng (`NaN`): `assert df['target'].isna().sum() == 0`.
   * Kiểm tra dải giá trị: `assert (df['target'] >= 0.0).all() and (df['target'] <= 1.0).all()`.
