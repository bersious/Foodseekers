# 🔬 NGHIÊN CỨU TOÀN DIỆN VỀ TIDECLOAK & EMERGENT AUTHORITY
# Dự án: Thử thách 2 (Challenge 2) — UNLOCKED Hackathon (Tide × RMIT 2026)
# Biên soạn: Đội Foodseekers (UIT)

---

## 📌 1. NGUYÊN LÝ CỐT LÕI: TẠI SAO BẢO MẬT TRUYỀN THỐNG THẤT BẠI?

### 1.1. Nút thắt lòng tin (The Trust Bottleneck)
Trong kiến trúc phần mềm truyền thống (Web2 và hầu hết ứng dụng đám mây hiện nay):
* Dữ liệu nhạy cảm của người dùng (bệnh án, tài chính, danh tính) được lưu trữ trên cơ sở dữ liệu.
* Để phân quyền cho người này xem, người kia không xem, hệ thống dùng các mô hình kiểm soát truy cập như RBAC (Role-Based Access Control) hoặc ABAC (Attribute-Based Access Control).
* **Điểm chí tử:** Dù có phân quyền phức tạp đến đâu, **luôn tồn tại một thực thể nắm giữ quyền lực tối cao (God-Mode / Master Key)**:
  1. Người quản trị cơ sở dữ liệu (DB Admin) có thể dump toàn bộ dữ liệu dạng bản rõ.
  2. Nhà cung cấp dịch vụ đám mây (AWS, Azure, GCP) có quyền truy cập vật lý và hạ tầng.
  3. Khóa bí mật (Secret Key / Master Key) được lưu trong biến môi trường hoặc Vault trung tâm.
* Khi kẻ tấn công (hoặc AI độc hại) dùng kỹ thuật xã hội (Social Engineering) để lừa nhân viên, hoặc khai thác một lỗ hổng phần mềm duy nhất, **toàn bộ kho báu (Crown Jewels) sẽ bị phơi bày**.

### 1.2. Sự thất bại của việc "Thêm tường lửa và vá lỗi"
Nghiên cứu của Tide chỉ ra rằng:
* Kẻ tấn công chỉ cần **1 sai sót duy nhất** trong hàng triệu dòng code để đột nhập.
* Các nhóm tin tặc khét tiếng (như Lapsus$) đã xâm nhập Microsoft, Nvidia, Okta, Uber không phải nhờ bẻ khóa thuật toán mã hóa, mà bằng cách tấn công vào con người nắm giữ chìa khóa chủ.
* Trong kỷ nguyên **AI Agent & Vibe Coding**, mã nguồn được tạo ra với tốc độ chóng mặt, kéo theo số lượng lỗ hổng tăng hơn 300%. Việc dùng AI để đi vá từng lỗ hổng là một thế bế tắc vô tận.

---

## ⚡ 2. CÔNG NGHỆ CỐT LÕI CỦA TIDE: EMERGENT AUTHORITY (QUYỀN HẠN TỰ SINH)

### 2.1. Định nghĩa "Quyền hạn tự sinh"
> **"Authority for an action, with no master key to keep."**  
> (Quyền hạn thực hiện hành động xuất hiện mà không cần bất kỳ ai phải nắm giữ chìa khóa chủ).

Thay vì lưu giữ chìa khóa giải mã trong một két sắt trung tâm:
1. Năng lực mật mã được phân tán trên một mạng lưới các nút độc lập (Tide Cybersecurity Fabric) bằng kỹ thuật mật mã ngưỡng (Threshold Cryptography).
2. **Không một nút đơn lẻ, không một quản trị viên, không một máy chủ ứng dụng nào sở hữu đầy đủ quyền hạn để giải mã dữ liệu một mình.**
3. Quyền hạn giải mã dữ liệu **chỉ tự động hình thành (emerge) trong một khoảnh khắc duy nhất (Just-in-Time)** khi 3 yếu tố hội tụ đầy đủ:
   * **Danh tính (Identity):** Đúng người dùng được ủy quyền.
   * **Chính sách (Policy):** Quy tắc cho phép truy cập đang có hiệu lực.
   * **Sự đồng thuận (Approvals):** Chủ sở hữu dữ liệu đã ký xác nhận chia sẻ.

### 2.2. Khái niệm Máy chủ vô can (Oblivious Proxy)
* Máy chủ ứng dụng của bạn đóng vai trò là một "người trung chuyển vô can" (Oblivious Proxy).
* Máy chủ **không lưu khóa giải mã, không nhìn thấy dữ liệu dạng rõ**.
* Dù máy chủ của bạn có bị tin tặc chiếm quyền điều khiển hoàn toàn (Full RCE), tin tặc cũng **chỉ thu về các khối dữ liệu đã mã hóa vô nghĩa**, vì máy chủ không có chìa khóa để mở!

---

## 🛡️ 3. TIDECLOAK LÀ GÌ?

* **TideCloak** là hệ thống quản lý danh tính và quyền truy cập (IAM) tương thích hoàn toàn với chuẩn mã nguồn mở **Keycloak** (hệ thống IAM cấp doanh nghiệp của RedHat).
* TideCloak tích hợp sẵn công nghệ Emergent Authority vào các luồng chuẩn OIDC (OpenID Connect) và OAuth 2.0.
* **Các tính năng đột phá của TideCloak:**
  1. **BYOiD (Bring Your Own Identity):** Người dùng tự kiểm soát danh tính giống như ví số, không ai có thể mạo danh, không lưu trữ mật khẩu tập trung.
  2. **Ủy quyền bất biến (Tamper-proof Authorization):** Mọi sự phê duyệt đều được niêm phong bằng chữ ký mật mã không thể giả mạo.
  3. **Quản trị đa đồng thuận (Quorum Enforced Governance):** Xóa bỏ tài khoản "siêu admin" (God-mode). Mọi thay đổi chính sách quan trọng bắt buộc phải có sự đồng thuận từ nhiều bên.
  4. **Mã hóa đầu cuối niêm phong miễn nhiễm (Immunity-Sealed E2EE):** Ràng buộc phiên làm việc với khóa riêng trên thiết bị người dùng.

---

## 🤖 4. GIAO THỨC RAZIEL MCP SERVER (AI CODING AGENT INTEGRATION)

Tide phát triển một máy chủ MCP chuyên dụng tên là **Raziel**:
* **Địa chỉ MCP Server:** `https://mcp.tide.org/mcp`
* **Nhiệm vụ của Raziel:**
  1. Đọc và phân tích "bán kính tổn thương" (Blast Radius Scan) của dự án.
  2. Cung cấp cẩm nang triển khai chuẩn (Verified Playbooks) cho Next.js, Express, React.
  3. Ngăn chặn AI Agent tự suy diễn mã nguồn bảo mật sai lầm (Anti-patterns).
* **Các công cụ chính của Raziel MCP:**
  * `tide_choose_playbook`: Đề xuất kịch bản tích hợp phù hợp nhất.
  * `tide_choose_scenario`: Khớp yêu cầu dự án với 5 kiến trúc tham chiếu mẫu (ví dụ: Password Manager, Encrypted Chat, Governance Panel).
  * `tide_canon`: Đọc các bất biến bảo mật bắt buộc phải tuân thủ.

---

## 🚨 5. CÁC CẠM BẪY CHÍ TỬ CẦN TRÁNH TRONG BÀI THI (CRITICAL PITFALLS)

Dựa trên hướng dẫn chính thức và tiêu chí đánh giá của ban giám khảo:

1. **❌ Tuyệt đối không làm một ứng dụng đăng nhập thông thường (Ordinary Login Demo):**
   * *Sai lầm:* Người dùng đăng nhập bằng TideCloak, sau đó hệ thống đọc dữ liệu từ SQL và hiển thị ra màn hình.
   * *Nhận xét của giám khảo:* "Nếu ứng dụng của bạn hoạt động y hệt với đăng nhập Auth0 hay Keycloak thông thường, bạn sẽ bị điểm thấp."
2. **❌ Không làm dashboard quản trị bảo mật chung chung (Generic Security Tool):**
   * Ứng dụng phải phục vụ một nhu cầu thực tế của con người (y tế, giáo dục, tài chính cá nhân, bất động sản).
3. **✅ Điểm mấu chốt bắt buộc phải trình diễn (The Magic Moment):**
   * Phải cho thấy: Khi người dùng **rút lại quyền đồng thuận (Revoke Consent)**, thì **kể cả người quản trị hệ thống cũng ngay lập tức bị từ chối giải mã dữ liệu**.
   * Phải giải thích được: Vì sao nếu không có TideCloak thì mô hình này không bao giờ dám triển khai ngoài đời thật.
