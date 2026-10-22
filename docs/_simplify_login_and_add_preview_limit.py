import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# 1. ĐƠN GIẢN HÓA CỬA SỔ ĐĂNG NHẬP: CHỈ ĐÚNG 2 Ô USERNAME + MẬT KHẨU (BỎ HẾT DROPDOWN)
# 2. BỔ SUNG TÍNH NĂNG GIỚI HẠN THỜI LƯỢNG NGHE/XEM THỬ X GIÂY ĐẦU CHO NGHỆ SĨ
# ==============================================================================

# Run the preview limit patch first
exec(open(r"C:\Users\nguye\Foodseekers\docs\_apply_preview_limit_feature.py", encoding='utf-8').read())

# Now simplify login windows on Page 1 & Page 2
def simplify_login():
    for base in [FS_PROTO, BW_RMIT]:
        # --- PAGE 1 ---
        p1 = os.path.join(base, "1", "index.html")
        with open(p1, "r", encoding="utf-8") as f:
            code1 = f.read()

        # Thay thế khối form đăng nhập của Nghệ Sĩ thành chỉ đúng 2 ô
        old_form_login_1 = """    <!-- Tab Đăng nhập -->
    <div id="artist-form-login">
      <div class="auth-title">Đăng Nhập Nghệ Sĩ</div>
      <div class="auth-sub">Chọn hồ sơ nghệ sĩ hoặc nhập username của bạn (Mật khẩu: 123)</div>

      <div class="form-group">
        <label class="form-label">Chọn Nghệ Sĩ Hoặc Nhập Username</label>
        <select id="quick-artist-login-select" class="form-input" style="margin-bottom:8px" onchange="document.getElementById('artist-login-user').value=this.value">
        </select>
        <input type="text" id="artist-login-user" class="form-input" value="alice_artist" placeholder="alice_artist">
      </div>
      <div class="form-group">
        <label class="form-label">Mật Khẩu Xác Thực</label>
        <input type="password" id="artist-login-pass" class="form-input" placeholder="Nhập mật khẩu (123)">
        <div style="font-size:11px;color:var(--dim);margin-top:4px" class="mono">Gợi ý: Mật khẩu xác thực cho tất cả nghệ sĩ là <strong>123</strong></div>
      </div>
      <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="loginArtist()">Đăng Nhập Vào Két Sắt</button>
    </div>"""

        new_form_login_1 = """    <!-- Form Đăng nhập Nghệ Sĩ -->
    <div id="artist-form-login">
      <div class="auth-title">Đăng Nhập Nghệ Sĩ</div>
      <div class="auth-sub">Nhập tên đăng nhập và mật khẩu để mở két sắt tác phẩm</div>

      <div class="form-group">
        <label class="form-label">Tên Đăng Nhập (Username)</label>
        <input type="text" id="artist-login-user" class="form-input" placeholder="Ví dụ: alice_artist, endy_producer...">
      </div>
      <div class="form-group">
        <label class="form-label">Mật Khẩu</label>
        <input type="password" id="artist-login-pass" class="form-input" placeholder="••••••••">
      </div>
      <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="loginArtist()">Đăng Nhập</button>
    </div>"""

        if old_form_login_1 in code1:
            code1 = code1.replace(old_form_login_1, new_form_login_1)
        else:
            # Flexible replacement of any previous dropdown select inside artist-form-login
            import re
            code1 = re.sub(
                r'<div id="artist-form-login">.*?<button class="btn btn-accent".*?onclick="loginArtist\(\)".*?</button>\s*</div>',
                new_form_login_1,
                code1,
                flags=re.DOTALL
            )

        with open(p1, "w", encoding="utf-8") as f:
            f.write(code1)
        print(f"Simplified login on Page 1: {p1}")

        # --- PAGE 2 ---
        p2 = os.path.join(base, "2", "index.html")
        with open(p2, "r", encoding="utf-8") as f:
            code2 = f.read()

        new_form_login_2 = """    <!-- Form Đăng nhập Người Nghe -->
    <div id="form-login">
      <div class="auth-title">Đăng Nhập Người Nghe</div>
      <div class="auth-sub">Nhập tên đăng nhập và mật khẩu để vào phòng nghe thử</div>

      <div class="form-group">
        <label class="form-label">Tên Đăng Nhập (Username)</label>
        <input type="text" id="reviewer-login-user" class="form-input" placeholder="Ví dụ: minh_mastering, thu_producer, nhânn...">
      </div>
      <div class="form-group">
        <label class="form-label">Mật Khẩu</label>
        <input type="password" id="reviewer-login-pass" class="form-input" placeholder="••••••••">
      </div>
      <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="loginReviewer()">Đăng Nhập</button>
    </div>"""

        import re
        code2 = re.sub(
            r'<div id="form-login">.*?<button class="btn btn-accent".*?onclick="loginReviewer\(\)".*?</button>\s*</div>',
            new_form_login_2,
            code2,
            flags=re.DOTALL
        )

        with open(p2, "w", encoding="utf-8") as f:
            f.write(code2)
        print(f"Simplified login on Page 2: {p2}")

simplify_login()
print("✓ Đã gỡ bỏ toàn bộ cửa sổ chọn trong khung đăng nhập, chỉ giữ đúng 2 ô username & mật khẩu!")
