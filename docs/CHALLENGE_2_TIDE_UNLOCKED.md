# 🔓 THỬ THÁCH 2: UNLOCKED HACKATHON (TIDE × RMIT 2026)
# Đơn vị tài trợ thử thách công nghiệp: Hãng công nghệ bảo mật Tide
# Hạn chót nộp bài: 18:00 ngày 22/10/2026 (Giờ Việt Nam)

---

## 🎯 1. BẢN CHẤT THỬ THÁCH 2 LÀ GÌ?

**Tóm tắt cốt lõi trong một câu:**  
Thử thách 2 yêu cầu xây dựng một ứng dụng mẫu (prototype) giải quyết một bài toán thực tế mà trước đây bị bế tắc do "nỗi sợ bị lạm quyền hoặc lộ dữ liệu", bằng cách tích hợp công nghệ **TideCloak** và cơ chế **Emergent Authority (Quyền hạn tự sinh)**.

### ❓ Vì sao lại cần TideCloak?
* **Mô hình truyền thống:** Dữ liệu luôn cần một "người quản trị tối cao" (Admin), một máy chủ trung tâm hoặc một AI nắm giữ chìa khóa chủ (Master Key). Khi người này bị hack, bị tha hóa hoặc bị ép buộc, toàn bộ dữ liệu người dùng sẽ sụp đổ.
* **Mô hình TideCloak:** **Không một ai giữ chìa khóa chủ.** Quyền hạn để mở khóa dữ liệu chỉ tự sinh ra (emerge) khi có sự đồng thuận từ các bên độc lập theo đúng quy tắc thiết lập sẵn. Kể cả quản trị viên hệ thống hay máy chủ đám mây cũng không thể đơn phương xem trộm hay thay đổi dữ liệu.

---

## 📦 2. YÊU CẦU NỘP BÀI (HẠN CHÓT 18:00 HÔM NAY)

Ban tổ chức yêu cầu nộp liên kết kho lưu trữ GitHub thông qua biểu mẫu:  
🔗 **Google Form nộp bài:** [https://forms.gle/HRHYjnqB86j1LFS97](https://forms.gle/HRHYjnqB86j1LFS97)

Trong kho lưu trữ GitHub (chế độ Public) bắt buộc phải có **2 thành phần**:

### 1. Mã nguồn ứng dụng mẫu (Working Prototype)
* Có tích hợp thư viện hoặc dịch vụ của TideCloak.
* Có thể dùng dữ liệu giả lập (mock data / synthetic data), không cần sản phẩm hoàn chỉnh mà chỉ cần một kịch bản tương tác minh chứng tính khả thi.

### 2. Video trình diễn 2 phút (Demo Video)
* Định dạng: `.mp4`.
* Dung lượng: **Dưới 100 MB** (giới hạn tệp của GitHub).
* Đặt trực tiếp trong thư mục gốc hoặc thư mục quy định của kho GitHub.
* Cấu trúc gợi ý 4 phần trong 2 phút:
  1. **Khả năng mới (The possibility):** Ứng dụng này sinh ra để làm gì?
  2. **Rào cản lòng tin (The constraint):** Vấn đề bảo mật / tin tưởng nào đang khiến ý tưởng này bế tắc trong đời thực?
  3. **Nguyên mẫu chạy thực tế (The prototype):** Quay màn hình ứng dụng hoạt động và vai trò của TideCloak.
  4. **Giá trị thay đổi (What changes):** Người dùng nhận được lợi ích gì khi không còn nguy cơ bị lạm quyền?

---

## ⚖️ 3. TIÊU CHÍ CHẤM ĐIỂM CỦA BAN GIÁM KHẢO (100%)

| Tiêu chí | Tỷ trọng | Nội dung trọng tâm |
| :--- | :---: | :--- |
| **1. Vision & Originality** | **25%** | Tầm nhìn mới mẻ, tham vọng và ý tưởng độc đáo, giải quyết một vấn đề chưa ai dám làm. |
| **2. Trust Constraint Insight** | **20%** | Chỉ ra rõ ràng nỗi sợ mất dữ liệu, sự lạm quyền của quản trị viên đang cản trở điều gì trong thực tế. |
| **3. Value & Impact** | **20%** | Mang lại giá trị có ý nghĩa cho cá nhân, tổ chức hoặc xã hội. |
| **4. Why TideCloak Matters** | **20%** | Chứng minh được vì sao phải dùng TideCloak thì ý tưởng mới khả thi (nếu dùng đăng nhập thông thường mà làm được y hệt thì sẽ bị điểm thấp). |
| **5. Prototype & Storytelling** | **15%** | Video và tài liệu mạch lạc, dễ hiểu, cho thấy được tương tác then chốt đang hoạt động. |

---

## 📝 4. MẪU README BẮT BUỘC (DƯỚI 300 TỪ)

Đặt đoạn văn này ở ngay đầu file `README.md` của kho lưu trữ:

```markdown
[![Built with TideCloak](https://tide.org/badges/built-with-tidecloak.svg)](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked)

## Project overview

_Mô tả một câu ngắn gọn về ứng dụng của bạn._

Built with [TideCloak](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked).

### 1. Vision & originality
<!-- Bạn đề xuất sản phẩm, dịch vụ hoặc cách làm việc mới nào? Điều gì khiến ý tưởng của bạn khác biệt? -->

### 2. Trust constraint insight
<!-- Hiện nay điều gì đang gặp rủi ro hoặc bất khả thi do sự cản trở của niềm tin và bảo mật? Khi loại bỏ rào cản đó, điều gì sẽ trở nên khả thi? -->

### 3. Value & impact
<!-- Ai sẽ hưởng lợi và công việc/cuộc sống của họ được cải thiện như thế nào? Nêu ví dụ thực tế. -->

### 4. Why TideCloak matters
<!-- Ứng dụng tích hợp TideCloak như thế nào để hiện thực hóa ý tưởng? Giải thích tại sao đăng nhập thông thường không thể đáp ứng được. -->

### 5. Prototype & storytelling
<!-- Nguyên mẫu hôm nay chứng minh được điều gì? Điểm tương tác then chốt nào ban giám khảo cần chú ý xem trong video? -->

## Setup

<!-- Hướng dẫn chi tiết các bước cài đặt và chạy ứng dụng cục bộ. -->
```

---

## 💡 5. CÁC Ý TƯỞNG TIÊU BIỂU TỪ BAN TỔ CHỨC (INSPIRATION)

1. **Hồ sơ y tế tự chủ (Care Passport):** Bệnh nhân tự chọn chia sẻ hồ sơ bệnh án cho đúng bác sĩ khám bệnh. Bác sĩ chuyên khoa này không xem được bệnh án của chuyên khoa khác, và nền tảng bệnh viện không lưu giữ bản rõ.
2. **Kho đồng thuận nghiên cứu (Research Consent Vault):** Tình nguyện viên cung cấp dữ liệu nghiên cứu nhạy cảm. Khi rút quyền đồng thuận, hệ thống lập tức khóa vĩnh viễn quyền giải mã của viện nghiên cứu mà không phụ thuộc vào quản trị viên máy chủ.
3. **Hồ sơ thuê nhà bảo mật (Rental Application Passport):** Người thuê nhà chứng minh thu nhập và tài chính với chủ nhà nhưng không để lại bản sao căn cước hoặc sao kê ngân hàng trong hòm thư của công ty môi giới.
4. **Chấm thi / Đánh giá hồ sơ mù (Blind Portfolio Review):** Giám khảo chấm điểm bài thi trước khi biết danh tính thí sinh. Dữ liệu danh tính chỉ được tự động giải mã khi đạt đến vòng phỏng vấn theo đúng tiến trình.

---

## 🛠️ 6. HƯỚNG DẪN KỸ THUẬT TRIỂN KHAI NHANH

### Cách nhanh nhất: Dùng TideCloak Quickstart Next.js
1. Khởi chạy máy chủ TideCloak qua Docker (hoặc dùng tài khoản có sẵn):
```bash
docker run --name mytidecloak -d -p 8080:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=password tideorg/tidecloak-dev:latest
```
2. Khởi tạo dự án Next.js tích hợp sẵn TideCloak:
```bash
npm init @tidecloak/nextjs@latest my-tide-app
```
3. Chạy giao diện cục bộ:
```bash
cd my-tide-app
npm install
npm run dev
```

### Kết nối AI Agent qua giao thức MCP:
* Máy chủ MCP chính thức: `https://mcp.tide.org/mcp`
* Hỗ trợ sẵn trên Cursor, Claude Code, VS Code để tự động hóa việc gọi tài liệu và viết code tích hợp.
