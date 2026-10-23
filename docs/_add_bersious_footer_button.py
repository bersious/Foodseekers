import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# CSS VÀ HTML CHO NÚT "bersious." GRADIENT XANH DƯƠNG HỒNG Ở FOOTER
# Gradient chuẩn từ bersious.io.vn/tmn: linear-gradient(135deg, #60a5fa, #ec4899)
# ==============================================================================

BERSIOUS_BTN_CSS = r"""
/* Nút về trang chính bersious. nhỏ gọn tinh tế */
.bersious-home-btn{
  display:inline-flex;align-items:center;gap:6px;padding:4px 10px;
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.14);
  border-radius:999px;text-decoration:none;transition:all .22s var(--ease-out);
  backdrop-filter:blur(8px);
}
.bersious-home-btn:hover{
  background:rgba(255,255,255,.08);border-color:rgba(236,72,153,.45);
  transform:translateY(-1px);box-shadow:0 4px 14px rgba(96,165,250,.22);
}
.bersious-home-btn .bersious-logo-text{
  font-weight:700;font-size:12px;letter-spacing:-0.02em;
  background:linear-gradient(135deg, #60a5fa, #ec4899);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}
.bersious-home-btn .bersious-arrow{
  font-size:10px;color:rgba(255,255,255,.4);transition:transform .2s;
}
.bersious-home-btn:hover .bersious-arrow{
  color:#ec4899;transform:translateX(2px);
}
"""

def update_footer_with_bersious_btn(path):
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Thêm CSS nếu chưa có
    if '.bersious-home-btn{' not in code:
        code = code.replace('</style>', BERSIOUS_BTN_CSS + '\n</style>', 1)

    # 2. Thêm nút vào footer-links
    old_target = '<a href="https://github.com/bersious/Foodseekers" target="_blank" rel="noopener">GitHub Source Code</a>'
    old_target_vi = '<a href="https://github.com/bersious/Foodseekers" target="_blank" rel="noopener">Mã Nguồn GitHub</a>'

    btn_html = """<span>·</span>
      <a href="/" class="bersious-home-btn" title="Trở về trang chủ bersious.">
        <span class="bersious-logo-text">bersious.</span>
        <span class="bersious-arrow">↗</span>
      </a>"""

    if 'class="bersious-home-btn"' not in code:
        if old_target in code:
            code = code.replace(old_target, old_target + '\n      ' + btn_html)
        elif old_target_vi in code:
            code = code.replace(old_target_vi, old_target_vi + '\n      ' + btn_html)
        else:
            # Fallback nếu cấu trúc khác: chèn vào trước </div> của footer-links
            code = re.sub(r'(<div class="footer-links[^>]*>.*?)(</div>)', r'\1      ' + btn_html + r'\n    \2', code, flags=re.S)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print("Updated footer in:", path)

for base in [FS_PROTO, BW_RMIT]:
    for p in ["index.html", "1/index.html", "2/index.html", "3/index.html"]:
        full_p = os.path.join(base, p)
        if os.path.exists(full_p):
            update_footer_with_bersious_btn(full_p)

print("✓ Hoàn tất gắn nút 'bersious.' gradient xanh dương - hồng vào toàn bộ chân trang!")
