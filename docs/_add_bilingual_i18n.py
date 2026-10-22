import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

I18N_CSS = r"""
/* ==================== I18N LANGUAGE SWITCHER ==================== */
.lang-switcher{
  display:inline-flex;align-items:center;background:var(--surface-2);
  border:1px solid var(--line);border-radius:999px;padding:2px;gap:2px;
}
.lang-btn{
  background:transparent;border:none;color:var(--muted);font-family:inherit;
  font-size:11px;font-weight:700;padding:4px 9px;border-radius:999px;cursor:pointer;
  transition:all .18s var(--ease-out);letter-spacing:.04em;
}
.lang-btn:hover{color:var(--fg)}
.lang-btn.active{
  background:var(--accent);color:#0a0b0e;box-shadow:0 0 10px rgba(184,243,107,0.3);
}
"""

I18N_JS = r"""
/* ==================== I18N CORE ENGINE (DEFAULT: EN) ==================== */
(function(){
  if(window.__i18nReady) return;
  window.__i18nReady = true;

  // Từ điển đa ngôn ngữ toàn diện
  const DICT = {
    // Topbar & Common
    "Nghệ Sĩ / Studio Két Sắt Mật Mã": { en: "Artist / Cryptographic Sovereign Vault", vi: "Nghệ Sĩ / Studio Két Sắt Mật Mã" },
    "Phòng nghe thử riêng tư · TideCloak BYOiD": { en: "Private Review Room · TideCloak BYOiD", vi: "Phòng nghe thử riêng tư · TideCloak BYOiD" },
    "Hạ Tầng Lưu Trữ Đám Mây S3 (Oblivious Proxy)": { en: "S3 Cloud Storage Infrastructure (Oblivious Proxy)", vi: "Hạ Tầng Lưu Trữ Đám Mây S3 (Oblivious Proxy)" },
    "Zero-Trust Media Vault": { en: "Zero-Trust Media Vault", vi: "Két Sắt Media Zero-Trust" },
    "Cloud Database Synced": { en: "Cloud Database Synced", vi: "Đã Đồng Bộ Đám Mây" },
    "Zero-Custody Enforced": { en: "Zero-Custody Enforced", vi: "Thực Thi Không-Ủy-Thác" },
    "Đăng xuất": { en: "Sign Out", vi: "Đăng xuất" },

    // Page 1: Artist
    "Đăng Nhập Nghệ Sĩ": { en: "Artist Sign In", vi: "Đăng Nhập Nghệ Sĩ" },
    "Tạo Profile Mới": { en: "Create New Profile", vi: "Tạo Profile Mới" },
    "Nhập tên đăng nhập và mật khẩu để mở két sắt tác phẩm": { en: "Enter your username and password to unlock your master vault", vi: "Nhập tên đăng nhập và mật khẩu để mở két sắt tác phẩm" },
    "Tên Đăng Nhập": { en: "Username", vi: "Tên Đăng Nhập" },
    "Mật Khẩu": { en: "Password", vi: "Mật Khẩu" },
    "Đăng Nhập": { en: "Sign In", vi: "Đăng Nhập" },
    "Khởi Tạo Profile Nghệ Sĩ Mới": { en: "Create New Artist Profile", vi: "Khởi Tạo Profile Nghệ Sĩ Mới" },
    "Đăng ký nghệ danh và tạo két sắt lưu trữ tác phẩm riêng": { en: "Register your artist pseudonym and initialize a private sovereign vault", vi: "Đăng ký nghệ danh và tạo két sắt lưu trữ tác phẩm riêng" },
    "Tên Nghệ Sĩ / Nghệ Danh": { en: "Artist / Stage Name", vi: "Tên Nghệ Sĩ / Nghệ Danh" },
    "Dòng Nhạc Sở Trường": { en: "Musical Genre", vi: "Dòng Nhạc Sở Trường" },
    "Mật Khẩu Khởi Tạo": { en: "Initial Password", vi: "Mật Khẩu Khởi Tạo" },
    "Tạo hồ sơ và đăng nhập": { en: "Create Profile & Sign In", vi: "Tạo hồ sơ và đăng nhập" },
    "Tài khoản:": { en: "Account:", vi: "Tài khoản:" },
    "KÉT SẮT RIÊNG TƯ ĐANG KHÓA CHẶT": { en: "PRIVATE VAULT CRYPTOGRAPHICALLY LOCKED", vi: "KÉT SẮT RIÊNG TƯ ĐANG KHÓA CHẶT" },
    "Chuyển sang tài khoản khác": { en: "Switch Account", vi: "Chuyển sang tài khoản khác" },
    "Két Sắt Tác Phẩm Master": { en: "Master Track Sovereign Vault", vi: "Két Sắt Tác Phẩm Master" },
    "Mã hóa đầu cuối client-side · Ủy quyền Quorum cho từng người nghe": { en: "Client-side E2EE · Quorum Emergent Entitlements per Reviewer", vi: "Mã hóa đầu cuối client-side · Ủy quyền Quorum cho từng người nghe" },
    "Tự động duyệt xin quyền: ": { en: "Auto-approve access requests: ", vi: "Tự động duyệt xin quyền: " },
    "Kéo thả hoặc nhấp để tải lên tệp âm thanh / video master": { en: "Drag & drop or click to upload lossless audio / video master files", vi: "Kéo thả hoặc nhấp để tải lên tệp âm thanh / video master" },
    "Hỗ trợ MP3, WAV, FLAC, AAC, MP4, WEBM": { en: "Supports MP3, WAV, FLAC, AAC, MP4, WEBM", vi: "Hỗ trợ MP3, WAV, FLAC, AAC, MP4, WEBM" },
    "DANH SÁCH TÁC PHẨM TRONG KÉT SẮT": { en: "TRACKS SEALED IN VAULT", vi: "DANH SÁCH TÁC PHẨM TRONG KÉT SẮT" },
    "ĐƠN XIN QUYỀN TRUY CẬP TỪ NGƯỜI NGHE": { en: "ACCESS PERMISSION REQUESTS", vi: "ĐƠN XIN QUYỀN TRUY CẬP TỪ NGƯỜI NGHE" },
    "Chưa cấp quyền cho bất kỳ ai": { en: "No reviewers authorized yet", vi: "Chưa cấp quyền cho bất kỳ ai" },
    "Thu hồi": { en: "Revoke", vi: "Thu hồi" },
    "Xóa Tác Phẩm": { en: "Delete Track", vi: "Xóa Tác Phẩm" },
    "TRÌNH PHÁT ÂM THANH MASTER": { en: "LOSSLESS AUDIO MASTER PLAYER", vi: "TRÌNH PHÁT ÂM THANH MASTER" },
    "TRÌNH PHÁT VIDEO MASTER": { en: "MASTER VIDEO PLAYER", vi: "TRÌNH PHÁT VIDEO MASTER" },
    "Tự động thu hồi khi phát hiện can thiệp:": { en: "Auto-revoke upon tamper detection:", vi: "Tự động thu hồi khi phát hiện can thiệp:" },
    "Đang bật bảo vệ chống can thiệp và ghi âm lậu": { en: "Active: Anti-tamper & unauthorized capture defense", vi: "Đang bật bảo vệ chống can thiệp và ghi âm lậu" },
    "Đang tắt": { en: "Disabled", vi: "Đang tắt" },
    "Chống thu âm ngoài loa:": { en: "Acoustic Watermark Defense:", vi: "Chống thu âm ngoài loa:" },
    "Không chèn watermark": { en: "No acoustic watermark", vi: "Không chèn watermark" },
    "Chèn tiếng vịt kêu định kỳ": { en: "Periodic Duck Quack watermark", vi: "Chèn tiếng vịt kêu định kỳ" },
    "Giọng nói AI đọc cảnh báo bản quyền": { en: "Periodic AI Voice Copyright Disclaimer", vi: "Giọng nói AI đọc cảnh báo bản quyền" },
    "Giới hạn thời gian nghe thử:": { en: "Preview Duration Limit:", vi: "Giới hạn thời gian nghe thử:" },
    "Toàn bộ bài hát": { en: "Full Track Duration", vi: "Toàn bộ bài hát" },
    "10 giây đầu": { en: "First 10 seconds", vi: "10 giây đầu" },
    "15 giây đầu": { en: "First 15 seconds", vi: "15 giây đầu" },
    "30 giây đầu": { en: "First 30 seconds", vi: "30 giây đầu" },
    "60 giây đầu": { en: "First 60 seconds", vi: "60 giây đầu" },
    "DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:": { en: "IDENTITIES CURRENTLY AUTHORIZED TO DECRYPT:", vi: "DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:" },
    "Chỉ nghe 1 lần": { en: "Single-Play Self-Destruct", vi: "Chỉ nghe 1 lần" },
    "Cấp quyền truy cập": { en: "Grant Decryption Entitlement", vi: "Cấp quyền truy cập" },
    "GÓP Ý & BÌNH LUẬN TỪ NGƯỜI NGHE:": { en: "FEEDBACK & REVIEWS FROM LISTENERS:", vi: "GÓP Ý & BÌNH LUẬN TỪ NGƯỜI NGHE:" },
    "Duyệt Cấp Quyền": { en: "Approve & Grant", vi: "Duyệt Cấp Quyền" },
    "Từ Chối": { en: "Deny", vi: "Từ Chối" },

    // Page 2: SONARA Listener
    "KHO LƯU TRỮ ÂM NHẠC BẢO MẬT": { en: "ZERO-TRUST SECURE AUDIO REPOSITORY", vi: "KHO LƯU TRỮ ÂM NHẠC BẢO MẬT" },
    "Thư viện âm nhạc bảo mật": { en: "Zero-Trust Reviewer Listening Room", vi: "Thư viện âm nhạc bảo mật" },
    "Nghe thử in-memory không qua trung gian · Thu hồi quyền truy cập tức thì": { en: "Direct in-memory decrypted streaming · Sub-millisecond instant revocation", vi: "Nghe thử in-memory không qua trung gian · Thu hồi quyền truy cập tức thì" },
    "CHỌN NGHỆ SĨ ĐỂ XEM DANH MỤC:": { en: "SELECT ARTIST DISCOGRAPHY:", vi: "CHỌN NGHỆ SĨ ĐỂ XEM DANH MỤC:" },
    "Tất cả nghệ sĩ": { en: "All Artists", vi: "Tất cả nghệ sĩ" },
    "Đang phát in-memory:": { en: "Streaming In-Memory:", vi: "Đang phát in-memory:" },
    "Đã cấp quyền": { en: "Authorized", vi: "Đã cấp quyền" },
    "Đang chờ duyệt": { en: "Pending Approval", vi: "Đang chờ duyệt" },
    "Chưa cấp quyền": { en: "Locked (No Access)", vi: "Chưa cấp quyền" },
    "Phát ngay": { en: "Play Master", vi: "Phát ngay" },
    "Xin quyền nghe": { en: "Request Access", vi: "Xin quyền nghe" },
    "Góp ý & Đánh giá gửi tới Nghệ Sĩ": { en: "Audition Feedback & Notes for Artist", vi: "Góp ý & Đánh giá gửi tới Nghệ Sĩ" },
    "Gửi góp ý": { en: "Submit Feedback", vi: "Gửi góp ý" },
    "BẢNG NHẬT KÝ ĐÁNH GIÁ QUYỀN HẠN TIDECLOAK": { en: "TIDECLOAK SECURITY & AUDIT TELEMETRY", vi: "BẢNG NHẬT KÝ ĐÁNH GIÁ QUYỀN HẠN TIDECLOAK" },

    // Page 3: S3 Inspector
    "Trình Giám Sát Hạ Tầng Đám Mây S3": { en: "S3 Cloud Infrastructure Security Monitor", vi: "Trình Giám Sát Hạ Tầng Đám Mây S3" },
    "Mô phỏng góc nhìn của Kẻ xâm nhập hoặc Quản trị viên máy chủ nắm quyền Root AWS": { en: "Simulating an adversary or rogue server administrator with AWS Root credentials", vi: "Mô phỏng góc nhìn của Kẻ xâm nhập hoặc Quản trị viên máy chủ nắm quyền Root AWS" },
    "Mạng Quorum Độc Lập": { en: "Decentralized Quorum Nodes", vi: "Mạng Quorum Độc Lập" },
    "Chìa Khóa Chủ Lưu Trên Server": { en: "Master Keys on Server", vi: "Chìa Khóa Chủ Lưu Trên Server" },
    "Khối Nhị Phân Mã Hóa S3": { en: "Encrypted S3 Binary Blobs", vi: "Khối Nhị Phân Mã Hóa S3" },
    "Rủi Ro Rò Rỉ Nội Bộ": { en: "Insider Leak Vulnerability", vi: "Rủi Ro Rò Rỉ Nội Bộ" },
    "Thực thi kịch bản Root Admin giải mã trộm": { en: "Simulate Root Admin Unauthorized Decryption Exploit", vi: "Thực thi kịch bản Root Admin giải mã trộm" },
    "Các Tệp Tin Nhị Phân Trong S3:": { en: "Encrypted Objects in S3 Bucket:", vi: "Các Tệp Tin Nhị Phân Trong S3:" },
    "Đối Tượng S3": { en: "S3 Object", vi: "Đối Tượng S3" },
    "Nghệ Sĩ": { en: "Artist", vi: "Nghệ Sĩ" },
    "Mã Băm Nhị Phân": { en: "Binary Hash (SHA-256)", vi: "Mã Băm Nhị Phân" },
    "Chìa Khóa Trên Server": { en: "Key On Storage Server", vi: "Chìa Khóa Trên Server" },
    "Chính Sách Quorum": { en: "Quorum Entitlement Policy", vi: "Chính Sách Quorum" },

    // Portal Index
    "Kiến trúc Két Sắt Mật Mã Âm Nhạc Không-Chìa-Khóa-Chủ": { en: "Zero-Master-Key Cryptographic Music Vault Architecture", vi: "Kiến trúc Két Sắt Mật Mã Âm Nhạc Không-Chìa-Khóa-Chủ" },
    "CỔNG 01 · KÉT SẮT NGHỆ SĨ": { en: "PORTAL 01 · ARTIST VAULT", vi: "CỔNG 01 · KÉT SẮT NGHỆ SĨ" },
    "CỔNG 02 · PHÒNG NGHE THỬ": { en: "PORTAL 02 · REVIEWER ROOM", vi: "CỔNG 02 · PHÒNG NGHE THỬ" },
    "CỔNG 03 · GIÁM SÁT MÁY CHỦ S3": { en: "PORTAL 03 · S3 OBLIVIOUS PROXY", vi: "CỔNG 03 · GIÁM SÁT MÁY CHỦ S3" },
    "TRẢI NGHIỆM KỊCH BẢN TẤN CÔNG THỰC TẾ": { en: "EXPERIENCE LIVE EXPLOIT SCENARIO", vi: "TRẢI NGHIỆM KỊCH BẢN TẤN CÔNG THỰC TẾ" },
    "Vào Két Sắt Nghệ Sĩ": { en: "Enter Artist Vault", vi: "Vào Két Sắt Nghệ Sĩ" },
    "Vào Phòng Nghe Thử": { en: "Enter Reviewer Room", vi: "Vào Phòng Nghe Thử" },
    "Xem Giám Sát S3": { en: "Inspect S3 Host", vi: "Xem Giám Sát S3" },

    // Footer
    "Cổng Trung Tâm": { en: "Central Portal", vi: "Cổng Trung Tâm" },
    "Cổng Nghệ Sĩ": { en: "Artist Portal", vi: "Cổng Nghệ Sĩ" },
    "Cổng Người Nghe (SONARA)": { en: "Reviewer Portal (SONARA)", vi: "Cổng Người Nghe (SONARA)" },
    "Giám Sát S3": { en: "S3 Security Monitor", vi: "Giám Sát S3" },
    "Mã Nguồn GitHub": { en: "GitHub Source Code", vi: "Mã Nguồn GitHub" },
    "Đội thi": { en: "Team", vi: "Đội thi" },
    "Trường Đại học Công nghệ Thông tin (UIT), ĐHQG-HCM": { en: "University of Information Technology (UIT), VNU-HCM", vi: "Trường Đại học Công nghệ Thông tin (UIT), ĐHQG-HCM" },
    "Tích hợp bảo mật TideCloak & Emergent Authority · RMIT Hackathon 2026": { en: "Powered by TideCloak & Emergent Authority · RMIT Hackathon 2026", vi: "Tích hợp bảo mật TideCloak & Emergent Authority · RMIT Hackathon 2026" }
  };

  // Mặc định là 'en' (Tiếng Anh), lưu trong localStorage
  let currentLang = localStorage.getItem('sonara_lang') || 'en';

  function applyLanguage(lang){
    currentLang = lang;
    localStorage.setItem('sonara_lang', lang);
    document.documentElement.lang = lang;

    // Cập nhật trạng thái nút bấm
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // Quét toàn bộ text nodes trong trang
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;
    while(node = walker.nextNode()){
      const raw = node.nodeValue.trim();
      if(!raw) continue;
      for(const key in DICT){
        if(raw === key || raw === DICT[key].vi || raw === DICT[key].en){
          node.nodeValue = node.nodeValue.replace(raw, DICT[key][lang] || raw);
          break;
        }
      }
    }

    // Quét các placeholder trong input
    document.querySelectorAll('input, textarea').forEach(el => {
      const ph = el.getAttribute('placeholder');
      if(!ph) return;
      for(const key in DICT){
        if(ph === key || ph === DICT[key].vi || ph === DICT[key].en){
          el.setAttribute('placeholder', DICT[key][lang]);
          break;
        }
      }
    });

    // Đồng bộ nút chọn trong UI
    const targetLabel = document.getElementById('comment-track-target');
    if(targetLabel && (targetLabel.textContent === 'Current Track' || targetLabel.textContent === 'Bài hát hiện tại')){
      targetLabel.textContent = lang === 'en' ? 'Current Track' : 'Bài hát hiện tại';
    }
  }

  window.setLanguage = function(lang){
    applyLanguage(lang);
    if(window.showToast){
      window.showToast(
        lang === 'en' ? 'Language Switched' : 'Đã đổi ngôn ngữ',
        lang === 'en' ? 'English is now active as default.' : 'Giao diện đã chuyển sang Tiếng Việt.',
        'ok'
      );
    }
  };

  window.getCurrentLang = function(){
    return currentLang;
  };

  // Khởi chạy khi DOM sẵn sàng
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', () => applyLanguage(currentLang));
  } else {
    applyLanguage(currentLang);
  }
})();
"""

def add_i18n_to_all_pages():
    for base in [FS_PROTO, BW_RMIT]:
        for page in ["index.html", "1/index.html", "2/index.html", "3/index.html"]:
            p = os.path.join(base, page)
            if not os.path.exists(p): continue
            with open(p, "r", encoding="utf-8") as f:
                code = f.read()

            # 1. Thêm I18N_CSS
            if 'I18N LANGUAGE SWITCHER' not in code:
                code = code.replace('</style>', I18N_CSS + '\n</style>', 1)

            # 2. Thêm Language Switcher vào thanh topbar-right
            switcher_html = """    <!-- I18N Language Switcher (EN / VI) -->
    <div class="lang-switcher" title="Switch Language / Đổi ngôn ngữ">
      <button class="lang-btn active" data-lang="en" onclick="setLanguage('en')">EN</button>
      <button class="lang-btn" data-lang="vi" onclick="setLanguage('vi')">VI</button>
    </div>
"""
            if 'class="lang-switcher"' not in code:
                code = code.replace('<div class="topbar-right">', '<div class="topbar-right">\n' + switcher_html, 1)

            # 3. Thêm I18N_JS vào ngay sau thẻ <body>
            if 'I18N CORE ENGINE' not in code:
                body_tag = '<body>'
                insert_pos = code.find(body_tag) + len(body_tag)
                code = code[:insert_pos] + '\n\n<script>\n' + I18N_JS + '\n</script>\n' + code[insert_pos:]

            with open(p, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"Added bilingual i18n support to: {p}")

add_i18n_to_all_pages()
print("✓ Hoàn tất tích hợp song ngữ Anh - Việt (Mặc định Tiếng Anh) cho toàn bộ trang web!")
