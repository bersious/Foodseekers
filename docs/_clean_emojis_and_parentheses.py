import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA SẠCH EMOJI VÀ MỞ NGOẶC TRÊN CẢ 2 TRANG - PHONG CÁCH TỐI GIẢN CHUYÊN NGHIỆP
# ==============================================================================

def clean_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()

        # Bỏ emojis ở topbar và thẻ
        c = c.replace('<span class="pill-tide">☁️ Cloud Database: SYNCED</span>', '<span class="pill-tide">Cloud Database Synced</span>')
        c = c.replace('🎨 Khởi Tạo Hồ Sơ Nghệ Sĩ Mới', 'Khởi tạo hồ sơ nghệ sĩ mới')
        c = c.replace('🚀 Tạo Profile & Đăng Nhập Ngay', 'Tạo hồ sơ và đăng nhập')
        c = c.replace('🚀 Tạo Profile & Chuyển Sang Nghệ Sĩ Này', 'Tạo hồ sơ và chuyển đổi')
        c = c.replace('<div style="font-size:36px;margin-bottom:8px">⚡</div>', '<div style="font-size:20px;font-weight:700;color:var(--accent);margin-bottom:6px" class="mono">UPLOAD</div>')
        c = c.replace('<span style="color:var(--danger)">🔔</span> Đơn Xin Quyền Nghe Thử Đang Chờ Duyệt', 'Yêu cầu xin quyền nghe thử đang chờ duyệt')
        c = c.replace('⚡ Cấp Quyền Truy Cập', 'Cấp quyền truy cập')
        c = c.replace('⚡', '')
        c = c.replace('🎨', '')
        c = c.replace('🔔', '')
        c = c.replace('🚀', '')
        c = c.replace('🎧', '')
        c = c.replace('🎵', '')
        c = c.replace('🎬', '')
        c = c.replace('⏱️', '')
        c = c.replace('🔒', '')
        c = c.replace('👤', '')
        c = c.replace('✓', '')
        c = c.replace('✕', '')

        # Bỏ mở ngoặc rườm rà
        c = c.replace(' (Viết liền, không dấu)', '')
        c = c.replace(' (Mật khẩu: 123)', '')
        c = c.replace(' (Tự động gắn vào profile của nghệ sĩ đang chọn)', '')
        c = c.replace(' (Full 100%)', '')
        c = c.replace(' (Teaser ngắn)', '')
        c = c.replace(' (Snippet)', '')
        c = c.replace(' (Sample 30s)', '')
        c = c.replace(' (1 phút Demo)', '')
        c = c.replace(' (Bảo mật tuyệt đối)', '')
        c = c.replace(' (Username)', '')
        c = c.replace(' (Chưa có tệp video thực tế tải lên)', ' · Tệp mẫu chưa có video tải lên')
        c = c.replace(' (Bản demo mẫu)', ' · Bản demo mẫu')

        # Dọn sạch các chuỗi hiển thị
        c = c.replace("`(${t.previewLimitSeconds}s)`", "`${t.previewLimitSeconds}s`")
        c = c.replace("` (Đang giới hạn người nghe chỉ được nghe ${t.previewLimitSeconds}s đầu)`", "` · Giới hạn ${t.previewLimitSeconds}s đầu`")
        c = c.replace("'(Người nghe được nghe toàn bộ bài)'", "'· Toàn thời lượng'")

        with open(p, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Cleaned Page 1 at: {p}")

def clean_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()

        # Bỏ emojis ở topbar, hero, player
        c = c.replace('<span class="pill-tide"><span class="sync-pulse"></span> Cloud Sync: ACTIVE</span>', '<span class="pill-tide"><span class="sync-pulse"></span> Cloud Sync Active</span>')
        c = c.replace('content:"♫";', 'content:"";')
        c = c.replace('🔒 Tide In-Memory Stream · CẤM TẢI VỀ', 'Tide In-Memory Stream · Chống tải về')
        c = c.replace('<div class="locked-icon">🔒</div>', '<div class="locked-icon mono" style="font-size:20px;color:var(--warn)">PROTECTED</div>')
        c = c.replace('⚡ Gửi Yêu Cầu Xin Quyền Nghe Thử Tới Nghệ Sĩ', 'Gửi yêu cầu xin quyền nghe thử')
        c = c.replace('⏱️ ĐÃ HẾT THỜI LƯỢNG NGHE THỬ', 'Hết thời lượng nghe thử')
        c = c.replace('🔑 Gửi Yêu Cầu Xin Cấp Quyền Nghe Full Toàn Bộ Bài', 'Yêu cầu mở khóa toàn bộ bài hát')
        c = c.replace('<span style="color:var(--accent)">⚡</span> Nhật Ký Thực Thi Quyền Hạn TideCloak Quorum (Execution Log)', 'Nhật ký thực thi quyền hạn TideCloak Quorum')
        c = c.replace('⚡ Xin Quyền Nghe', 'Xin quyền nghe')
        c = c.replace('▶ Phát Ngay', 'Phát ngay')
        c = c.replace('▶', '')
        c = c.replace('⏸', '')
        c = c.replace('⚡', '')
        c = c.replace('🎨', '')
        c = c.replace('🔔', '')
        c = c.replace('🚀', '')
        c = c.replace('🎧', '')
        c = c.replace('🎵', '')
        c = c.replace('🎬', '')
        c = c.replace('⏱️', '')
        c = c.replace('🔒', '')
        c = c.replace('👤', '')
        c = c.replace('✓', '')
        c = c.replace('⏳', '')
        c = c.replace('🌟', '')

        # Bỏ mở ngoặc rườm rà
        c = c.replace(' (TideCloak BYOiD)', ' · TideCloak BYOiD')
        c = c.replace(' (Viết liền, không dấu)', '')
        c = c.replace(' (Tên đăng nhập)', '')
        c = c.replace(' (Username)', '')
        c = c.replace(' (Username viết liền)', '')
        c = c.replace(' (Mật khẩu: 123)', '')
        c = c.replace(' (Emergent Authority)', ' · Emergent Authority')
        c = c.replace(' (CHỌN CHỨ KHÔNG GÕ)', '')
        c = c.replace(' (Execution Log)', '')
        c = c.replace(' (Chờ duyệt)', '')

        # Badges chuẩn, tinh tế
        c = c.replace('<span class="badge badge-ok"> ĐÃ CÓ QUYỀN</span>', '<span class="badge badge-ok">Đã cấp quyền</span>')
        c = c.replace('<span class="badge badge-warn"> ĐANG CHỜ DUYỆT</span>', '<span class="badge badge-warn">Đang chờ duyệt</span>')
        c = c.replace('<span class="badge badge-danger"> BỊ KHÓA</span>', '<span class="badge badge-danger">Chưa cấp quyền</span>')
        c = c.replace('<span class="badge badge-ok"> ĐÃ ĐƯỢC DUYỆT</span>', '<span class="badge badge-ok">Đã được duyệt</span>')
        c = c.replace('<span class="badge badge-warn"> CHỜ DUYỆT</span>', '<span class="badge badge-warn">Chờ duyệt</span>')

        with open(p, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Cleaned Page 2 at: {p}")

clean_page_1()
clean_page_2()
print("✓ Hoàn tất tinh chỉnh giao diện tối giản, chuyên nghiệp!")
