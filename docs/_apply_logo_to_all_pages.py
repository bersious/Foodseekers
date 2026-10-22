import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# GẮN LOGO MỚI (Ổ KHÓA + KHÓA SOL + SÓNG NHẠC) VÀO TẤT CẢ CÁC TRANG VÀ FAVICON
# ==============================================================================

def patch_logo_in_page(path, page_num):
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Thêm Favicon
    fav_tag = '<link rel="icon" type="image/png" href="/rmit/logo.png">\n'
    if '/rmit/logo.png' not in code:
        code = code.replace('<meta name="viewport"', fav_tag + '  <meta name="viewport"')

    # 2. Thay thế thẻ brand dot bằng ảnh Logo
    old_brand_dot = '<span class="brand-dot"></span>'
    new_logo_img = '<img src="/rmit/logo.png" alt="UNRELEASED Logo" style="width:34px;height:34px;object-fit:contain;filter:drop-shadow(0 0 8px rgba(184,243,107,0.45));flex-shrink:0;">'

    if old_brand_dot in code:
        code = code.replace(old_brand_dot, new_logo_img)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Updated Logo in: {path}")

# Cập nhật cho cả 3 trang + trang index chính
for base in [FS_PROTO, BW_RMIT]:
    for p in ["index.html", "1/index.html", "2/index.html", "3/index.html"]:
        full_p = os.path.join(base, p)
        if os.path.exists(full_p):
            patch_logo_in_page(full_p, p)

print("✓ Đã gắn Logo tách nền hoàn hảo vào tất cả các trang web!")
