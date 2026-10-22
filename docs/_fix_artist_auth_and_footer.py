import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

FOOTER_CSS = r"""
/* ==================== PROFESSIONAL FOOTER ==================== */
.footer{
  max-width:1200px;margin:48px auto 20px;padding:32px 24px 24px;
  border-top:1px solid var(--line);display:flex;flex-direction:column;gap:18px;
  color:var(--dim);font-size:12px;
}
.footer-top{
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;
}
.footer-brand{
  display:flex;align-items:center;gap:10px;color:var(--fg);font-weight:700;font-size:13px;
}
.footer-brand img{width:22px;height:22px;object-fit:contain}
.footer-links{
  display:flex;align-items:center;gap:18px;flex-wrap:wrap;
}
.footer-links a{
  color:var(--muted);text-decoration:none;transition:color .2s;
}
.footer-links a:hover{color:var(--accent)}
.footer-bottom{
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;
  padding-top:16px;border-top:1px dashed rgba(255,255,255,.06);font-size:11px;color:var(--dim);
}
.footer-badge{
  display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.03);
  padding:4px 10px;border-radius:6px;border:1px solid var(--line);
}
"""

FOOTER_HTML = r"""<footer class="footer">
  <div class="footer-top">
    <div class="footer-brand">
      <img src="/rmit/logo.png" alt="UNRELEASED">
      <span>UNRELEASED · Studio Két Sắt Âm Nhạc Zero-Trust</span>
    </div>
    <div class="footer-links mono">
      <a href="/rmit">Cổng Trung Tâm</a>
      <span>·</span>
      <a href="/rmit/1">Cổng Nghệ Sĩ</a>
      <span>·</span>
      <a href="/rmit/2">Cổng Người Nghe (SONORA)</a>
      <span>·</span>
      <a href="/rmit/3">Giám Sát S3</a>
      <span>·</span>
      <a href="https://github.com/bersious/Foodseekers" target="_blank" rel="noopener">Mã Nguồn GitHub</a>
    </div>
  </div>
  <div class="footer-bottom mono">
    <div>Đội thi <strong>Foodseekers</strong> — Trường Đại học Công nghệ Thông tin (UIT), ĐHQG-HCM</div>
    <div class="footer-badge">
      <span style="color:var(--accent)">●</span> Tích hợp bảo mật TideCloak & Emergent Authority · RMIT Hackathon 2026
    </div>
  </div>
</footer>"""

def fix_page1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Thêm FOOTER_CSS
        if '.footer-top{' not in code:
            code = code.replace('</style>', FOOTER_CSS + '\n</style>', 1)

        # 2. XÓA BỎ NÚT CHỌN SANG TÀI KHOẢN NGƯỜI KHÁC
        # Thay thế khối artist-nav-bar cũ
        old_nav_bar = """    <!-- THANH HIỂN THỊ PROFILE NGHỆ SĨ & ĐỔI PROFILE -->
    <div class="artist-nav-bar">
      <div class="artist-info-group">
        <div class="artist-avatar" id="current-artist-avatar">A</div>
        <div>
          <div style="font-size:16px;font-weight:700" id="current-artist-name">Alice Nguyễn</div>
          <div style="font-size:12px;color:var(--muted)" class="mono">
            @<span id="current-artist-user">alice_artist</span> · <span id="current-artist-genre">Indie Pop / Electronic</span>
          </div>
        </div>
      </div>

      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
        <label style="font-size:12px;color:var(--muted)">Đổi Nghệ Sĩ:</label>
        <select id="artist-switcher-select" class="form-input" style="width:200px;padding:7px 10px;font-size:13px" onchange="switchActiveArtist(this.value)">
        </select>
        <button class="btn btn-accent btn-sm" onclick="showCreateArtistModal()">+ Tạo Profile Mới</button>
      </div>
    </div>"""

        new_nav_bar = """    <!-- THANH PROFILE NGHỆ SĨ CHÍNH CHỦ (CHUẨN BẢO MẬT SOVEREIGN IDENTITY) -->
    <div class="artist-nav-bar">
      <div class="artist-info-group">
        <div class="artist-avatar" id="current-artist-avatar">A</div>
        <div>
          <div style="font-size:16px;font-weight:700" id="current-artist-name">Alice Nguyễn</div>
          <div style="font-size:12px;color:var(--muted)" class="mono">
            Tài khoản: @<strong id="current-artist-user" style="color:var(--accent)">alice_artist</strong> · <span id="current-artist-genre">Indie Pop / Electronic</span>
          </div>
        </div>
      </div>

      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
        <span class="badge badge-ok mono" style="font-size:11px">KÉT SẮT RIÊNG TƯ ĐANG KHÓA CHẶT</span>
        <button class="btn btn-ghost btn-sm" onclick="logoutArtist()" style="color:var(--danger)">Chuyển sang tài khoản khác</button>
      </div>
    </div>"""

        if old_nav_bar in code:
            code = code.replace(old_nav_bar, new_nav_bar)

        # 3. Sửa hàm renderArtistSwitcher: không còn dropdown đổi nghệ sĩ
        old_switcher_js = """function renderArtistSwitcher(){
  const artists = getStoredArtists();
  const current = artists.find(a => a.username === activeArtistUser) || artists[0] || {username:'alice_artist', name:'Alice Nguyễn', genre:'Indie Pop', artSeed:0};
  activeArtistUser = current.username;

  document.getElementById('current-artist-name').textContent = current.name;
  document.getElementById('current-artist-user').textContent = current.username;
  document.getElementById('current-artist-genre').textContent = current.genre || 'Âm nhạc';
  document.getElementById('current-artist-avatar').textContent = (current.name||'A').charAt(0).toUpperCase();
  document.getElementById('vault-artist-name-label').textContent = current.name;
  document.getElementById('artist-name-display').textContent = current.username;

  const select = document.getElementById('artist-switcher-select');
  if(select){
    select.innerHTML = artists.map(a => `<option value="${a.username}" ${a.username===activeArtistUser?'selected':''}>${a.name} (@${a.username})</option>`).join('');
  }
}"""

        new_switcher_js = """function renderArtistSwitcher(){
  const artists = getStoredArtists();
  // Khóa chặt theo đúng tài khoản đã đăng nhập trong localStorage
  const logged = localStorage.getItem('tide_logged_artist') || 'alice_artist';
  activeArtistUser = logged;
  const current = artists.find(a => a.username.toLowerCase() === logged.toLowerCase()) || {username:logged, name:logged, genre:'Âm nhạc đương đại', artSeed:0};

  document.getElementById('current-artist-name').textContent = current.name;
  document.getElementById('current-artist-user').textContent = current.username;
  document.getElementById('current-artist-genre').textContent = current.genre || 'Âm nhạc đương đại';
  document.getElementById('current-artist-avatar').textContent = (current.name||'A').charAt(0).toUpperCase();
  const vaultLabel = document.getElementById('vault-artist-name-label');
  if(vaultLabel) vaultLabel.textContent = current.name;
  const nameDisp = document.getElementById('artist-name-display');
  if(nameDisp) nameDisp.textContent = current.username;
}"""

        if old_switcher_js in code:
            code = code.replace(old_switcher_js, new_switcher_js)

        # 4. Thay thế Footer cũ bằng Footer chuyên nghiệp
        old_footer = re.search(r'<footer class="footer">.*?</footer>', code, re.S)
        if old_footer:
            code = code[:old_footer.start()] + FOOTER_HTML + code[old_footer.end():]

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Fixed Page 1 (No switcher, professional footer): {p}")

def fix_pages_2_and_3():
    for base in [FS_PROTO, BW_RMIT]:
        for page in ["index.html", "2/index.html", "3/index.html"]:
            p = os.path.join(base, page)
            if not os.path.exists(p): continue
            with open(p, "r", encoding="utf-8") as f:
                code = f.read()

            if '.footer-top{' not in code:
                code = code.replace('</style>', FOOTER_CSS + '\n</style>', 1)

            old_footer = re.search(r'<footer class="footer">.*?</footer>', code, re.S)
            if old_footer:
                code = code[:old_footer.start()] + FOOTER_HTML + code[old_footer.end():]

            with open(p, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"Added professional footer to: {p}")

fix_page1()
fix_pages_2_and_3()
print("✓ Hoàn tất tinh chỉnh chân trang và logic đăng nhập chính chủ cho Nghệ Sĩ!")
