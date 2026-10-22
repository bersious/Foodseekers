import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA VÀ NÂNG CẤP ĐỒNG BỘ USER/ARTIST TOÀN DIỆN CHO CẢ TRANG 1 VÀ TRANG 2
# ==============================================================================

# Kiểm tra hàm updateUserSelect trong Page 2
def update_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Thêm hàm renderUserSelect() độc lập và gọi nó trong fetchCloudState()
        user_select_logic = """
function renderUserSelect(){
  const users = getStoredUsers();
  const select = document.getElementById('quick-user-select');
  const input = document.getElementById('reviewer-login-user');
  if(!select) return;

  if(!users || !users.length){
    select.innerHTML = '<option value="">(Đang tải danh sách từ Cloud...)</option>';
    return;
  }

  const currentVal = input ? input.value : '';
  select.innerHTML = users.map(u => `<option value="${u.username}" ${u.username===currentVal?'selected':''}>👤 ${u.name||u.username} (@${u.username})</option>`).join('');
  if(!currentVal && users.length && input){
    input.value = users[0].username;
  }
}
"""

        # Thay thế hoặc bổ sung
        if "function renderUserSelect()" not in code:
            code = code.replace("function switchAuthTab(tab){", f"{user_select_logic}\nfunction switchAuthTab(tab){{")

        # Trong fetchCloudState(), BẮT BUỘC gọi renderUserSelect()
        old_fetch_cb = """      renderArtistChips();
      renderAlbumGrid();
      syncActiveTrackView();"""

        new_fetch_cb = """      renderUserSelect();
      renderArtistChips();
      renderAlbumGrid();
      syncActiveTrackView();"""

        if old_fetch_cb in code:
            code = code.replace(old_fetch_cb, new_fetch_cb)

        # Trong pushCloudAction(), cũng gọi renderUserSelect()
        old_push_cb = """        renderAlbumGrid();
        syncActiveTrackView();"""
        new_push_cb = """        renderUserSelect();
        renderAlbumGrid();
        syncActiveTrackView();"""

        if old_push_cb in code:
            code = code.replace(old_push_cb, new_push_cb)

        # Cải thiện giao diện form đăng nhập Trang 2: có gợi ý mật khẩu tinh tế
        old_p_hint = '<input type="password" id="reviewer-login-pass" class="form-input" placeholder="••••••••">'
        new_p_hint = '<input type="password" id="reviewer-login-pass" class="form-input" placeholder="Nhập mật khẩu (123)">\n        <div style="font-size:11px;color:var(--dim);margin-top:4px" class="mono">Gợi ý: Mật khẩu xác thực cho tất cả tài khoản là <strong>123</strong></div>'
        if old_p_hint in code and 'Gợi ý: Mật khẩu xác thực' not in code:
            code = code.replace(old_p_hint, new_p_hint)

        old_reg_p_hint = '<input type="password" id="reg-pass" class="form-input" placeholder="••••••••">'
        new_reg_p_hint = '<input type="password" id="reg-pass" class="form-input" placeholder="Nhập mật khẩu khởi tạo (123)">\n        <div style="font-size:11px;color:var(--dim);margin-top:4px" class="mono">Gợi ý: Mật khẩu khởi tạo là <strong>123</strong></div>'
        if old_reg_p_hint in code and 'Gợi ý: Mật khẩu khởi tạo' not in code:
            code = code.replace(old_reg_p_hint, new_reg_p_hint)

        # Đảm bảo interval polling nhanh 1.5s
        code = code.replace("setInterval(fetchCloudState, 2000);", "setInterval(fetchCloudState, 1500);")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Đã nâng cấp đồng bộ danh sách user cho Trang 2: {p}")

def update_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Cải thiện form đăng nhập Trang 1: có gợi ý mật khẩu tinh tế
        old_p1_hint = '<input type="password" id="artist-login-pass" class="form-input" placeholder="••••••••">'
        new_p1_hint = '<input type="password" id="artist-login-pass" class="form-input" placeholder="Nhập mật khẩu (123)">\n        <div style="font-size:11px;color:var(--dim);margin-top:4px" class="mono">Gợi ý: Mật khẩu xác thực cho tất cả nghệ sĩ là <strong>123</strong></div>'
        if old_p1_hint in code and 'Gợi ý: Mật khẩu xác thực cho tất cả nghệ sĩ' not in code:
            code = code.replace(old_p1_hint, new_p1_hint)

        old_reg1_p_hint = '<input type="password" id="reg-artist-pass" class="form-input" placeholder="••••••••">'
        new_reg1_p_hint = '<input type="password" id="reg-artist-pass" class="form-input" placeholder="Nhập mật khẩu khởi tạo (123)">\n        <div style="font-size:11px;color:var(--dim);margin-top:4px" class="mono">Gợi ý: Mật khẩu khởi tạo là <strong>123</strong></div>'
        if old_reg1_p_hint in code and 'Gợi ý: Mật khẩu khởi tạo là' not in code:
            code = code.replace(old_reg1_p_hint, new_reg1_p_hint)

        # Trong fetchCloudState() của Trang 1, re-renderArtistTracks() để cập nhật dropdown người nghe
        old_p1_cb = """      updateArtistLoginSelect();
      renderArtistSwitcher();
      renderArtistTracks();
      renderRequests();"""

        new_p1_cb = """      updateArtistLoginSelect();
      renderArtistSwitcher();
      renderArtistTracks();
      renderRequests();"""
        # It's already there, ensure polling interval is 1.5s
        code = code.replace("setInterval(fetchCloudState, 2000);", "setInterval(fetchCloudState, 1500);")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Đã nâng cấp đồng bộ danh sách user cho Trang 1: {p}")

update_page_2()
update_page_1()
print("✓ Hoàn tất cập nhật đồng bộ User/Artist và cải thiện trình đăng nhập!")
