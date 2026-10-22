# 🏆 CHIẾN LƯỢC GIẬT GIẢI THỬ THÁCH 2: DỰ ÁN "CAREVAULT"
# Tên sản phẩm: CareVault — Cross-Hospital Patient-Governed Health Passport
# Đơn vị dự thi: Team Foodseekers (UIT) — RMIT Hackathon 2026

---

## 🎯 1. LỰA CHỌN Ý TƯỞNG CHIẾN LƯỢC: TẠI SAO LẠI LÀ CAREVAULT?

Ban tổ chức gợi ý 12 chủ đề, trong đó chủ đề **Care Passport (Hồ sơ y tế tự chủ)** là ý tưởng mạnh mẽ nhất để giành điểm tuyệt đối vì:
1. **Đánh trúng nỗi đau thực tế lớn nhất:** Các vụ rò rỉ dữ liệu y tế chấn động (như Medibank làm lộ hàng triệu hồ sơ bệnh án) cho thấy việc các bệnh viện lưu trữ bản rõ hồ sơ người bệnh trong một máy chủ trung tâm là quả bom nổ chậm.
2. **Sự bế tắc của niềm tin (Trust Bottleneck):** Bệnh nhân rất muốn chia sẻ hồ sơ chụp MRI hay kết quả xét nghiệm nhạy cảm từ Bệnh viện A sang Bác sĩ chuyên khoa tại Bệnh viện B để xin ý kiến hội chẩn, nhưng sợ hồ sơ của mình bị nhân viên IT của bệnh viện sao chép hoặc bị bán cho công ty bảo hiểm.
3. **Sự khác biệt rõ nét của TideCloak:** Với TideCloak, **bệnh nhân là người duy nhất nắm quyền cấp hoặc hủy quyền giải mã**. Kể cả quản trị viên hệ thống của CareVault cũng chỉ thấy chuỗi mã hóa và không bao giờ đọc được bệnh án.

---

## 📄 2. BẢN NHÁP README CHUẨN MẪU (DƯỚI 300 TỪ - TIẾNG ANH THEO BAREM CHẤM)

Đoạn văn này được viết chuẩn xác theo 5 tiêu chí của ban giám khảo, sẵn sàng đặt vào đầu file `README.md`:

```markdown
[![Built with TideCloak](https://tide.org/badges/built-with-tidecloak.svg)](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked)

## Project overview

**CareVault** is a patient-governed health record passport enabling patients to share sensitive diagnostic records across independent healthcare providers without central authority custody.

Built with [TideCloak](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked).

### 1. Vision & originality
CareVault reimagines cross-provider healthcare collaboration. Instead of forcing patients to surrender complete medical histories to centralized hospital databases, CareVault enables fine-grained, self-sovereign record sharing directly between patients and specialized clinicians across different institutions.

### 2. Trust constraint insight
Today, collaborative healthcare is paralyzed by trust bottlenecks: sharing records across clinics exposes patients to catastrophic database breaches (like Medibank) and rogue administrator snooping. Providers cannot safely cross-collaborate because custody creates enormous regulatory liability. Removing unilateral administrative control enables seamless global second opinions without data exposure risk.

### 3. Value & impact
Patients gain absolute dignity and control over their most vulnerable data (mental health, oncology, genomics). Clinicians receive instantaneous, cryptographically verified referrals without waiting weeks for administrative bureaucracy. Hospitals eliminate multimillion-dollar data breach liabilities because their servers store zero master decryption keys.

### 4. Why TideCloak matters
Traditional IAM systems (Auth0, standard Keycloak) rely on centralized database permissions where database administrators retain "god-mode" decryption capabilities. CareVault integrates TideCloak's **Emergent Authority**: decryption keys are never stored anywhere—they emerge just-in-time only when the patient's active consent policy and the clinician's verified identity align. When consent is revoked, decryption becomes mathematically impossible even for the server operator.

### 5. Prototype & storytelling
Our prototype demonstrates an end-to-end patient referral:
1. Patient Alice uploads an encrypted MRI scan and grants temporary diagnostic access to Dr. Minh.
2. Dr. Minh authenticates via TideCloak and successfully decrypts the medical imagery.
3. System Admin attempts to view the record and is cryptographically denied (oblivious proxy).
4. Alice revokes consent: subsequent decryption requests from Dr. Minh are instantly rejected by Tide's quorum.
```

---

## 🎬 3. KỊCH BẢN QUAY VIDEO DEMO 2 PHÚT (CHÍNH XÁC TỪNG GIÂY)

* **Quy định:** Tệp `.mp4`, dung lượng `< 100 MB`, lưu trong repo.
* **Thời lượng:** Đúng 120 giây (2 phút).

| Thời gian | Cảnh hiển thị trên màn hình | Lời thuyết minh (Voiceover tiếng Anh / phụ đề) |
| :---: | :--- | :--- |
| **0:00 – 0:25**<br>*(25s)* | **Slide / Tiêu đề:** CareVault — Powered by TideCloak.<br>Màn hình minh họa bài toán Medibank và nỗi lo rò rỉ dữ liệu y tế. | *"Welcome to CareVault. In modern healthcare, sharing medical records across hospitals is broken. Centralized databases create massive targets for ransomware, and database admins possess dangerous god-mode access to our most private health records."* |
| **0:25 – 0:45**<br>*(20s)* | **Giao diện Patient Alice:** Bệnh nhân đăng nhập bằng TideCloak BYOiD, tải lên hồ sơ bệnh án nhạy cảm (Encrypted MRI). Chọn Bác sĩ Minh và bấm *"Grant Diagnostic Access"*. | *"With CareVault built on TideCloak, trust is no longer a bottleneck. Alice encrypts her sensitive MRI scan. She selects Dr. Minh for a second opinion and grants scoped access. Crucially, no master key exists in our cloud."* |
| **0:45 – 1:10**<br>*(25s)* | **Giao diện Dr. Minh:** Bác sĩ Minh đăng nhập. Bấm vào hồ sơ của Alice: Hệ thống gọi TideCloak Emergent Authority và giải mã thành công bệnh án. | *"Dr. Minh logs in from another hospital. TideCloak's decentralized nodes verify Alice's active policy and Dr. Minh's identity. Authority emerges just-in-time, allowing Dr. Minh to view and diagnose the record seamlessly."* |
| **1:10 – 1:35**<br>*(25s)* | **Giao diện System Admin / Database View:** Đăng nhập với quyền Admin cao nhất. Mở bảng bệnh án: Toàn bộ hiển thị `[CIPHERTEXT - NO UNILATERAL ACCESS]`. Bấm giải mã: Bị từ chối. | *"Now, look at the System Administrator screen. Even with root database access, the admin sees only ciphertext. Because TideCloak removes unilateral authority, an internal breach or compromised admin yields zero stolen health data."* |
| **1:35 – 1:50**<br>*(15s)* | **Giao diện Patient Alice:** Alice bấm *"Revoke Access"*. Quay lại màn hình Bác sĩ Minh bấm F5: Bị báo lỗi truy cập bị từ chối ngay lập tức. | *"Finally, Alice finishes her treatment and clicks Revoke Consent. Dr. Minh refreshes: access is instantly terminated at the cryptographic quorum layer. Alice remains the sole master of her health data."* |
| **1:50 – 2:00**<br>*(10s)* | **Logo TideCloak & RMIT Hackathon:** Tổng kết thông điệp. | *"CareVault proves what becomes possible when trust is no longer the bottleneck. Built with TideCloak for RMIT Hackathon 2026. Thank you!"* |

---

## 📊 4. DANH MỤC KIỂM TRA ĐẢM BẢO CHIẾN THẮNG (WINNING CHECKLIST)

- [x] Đã chọn bài toán đời thực có tính thuyết phục cao (Healthcare Privacy).
- [x] Đã chứng minh rõ ràng: Hệ thống thông thường (Auth0, PostgreSQL RBAC) có lỗ hổng Admin God-mode, còn TideCloak thì triệt tiêu hoàn toàn chìa khóa chủ.
- [x] Có tương tác thực tế: Bệnh nhân cấp quyền -> Bác sĩ xem được -> Admin không xem được -> Bệnh nhân hủy quyền -> Bác sĩ bị chặn.
- [x] README đúng mẫu quy định, dưới 300 từ tiếng Anh, trả lời đủ 5 câu hỏi.
- [x] Video demo đúng 2 phút, định dạng `.mp4`, dưới 100 MB.
- [x] Nộp trước 17:30 (trước hạn chót 18:00) qua Google Form chính thức.
