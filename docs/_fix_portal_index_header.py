import os

FS_P = r"C:\Users\nguye\Foodseekers\prototype\index.html"
BW_P = r"C:\Users\nguye\bersious-web\rmit\index.html"

for p in [FS_P, BW_P]:
    with open(p, "r", encoding="utf-8") as f:
        code = f.read()

    old_header = """<header class="topbar">
  <a href="/rmit" class="brand">
    <img src="/rmit/logo.png" alt="SONARA Logo" style="width:34px;height:34px;object-fit:contain;filter:drop-shadow(0 0 8px rgba(184,243,107,0.45));flex-shrink:0;">
    <div>SONARA<small>Zero-Trust Media Vault</small></div>
  </a>
  <span class="pill-tide">Powered by TideCloak</span>
</header>"""

    new_header = """<header class="topbar">
  <a href="/rmit" class="brand">
    <img src="/rmit/logo.png" alt="SONARA Logo" style="width:34px;height:34px;object-fit:contain;filter:drop-shadow(0 0 8px rgba(184,243,107,0.45));flex-shrink:0;">
    <div>SONARA<small>Zero-Trust Media Vault</small></div>
  </a>
  <div style="display:flex;align-items:center;gap:12px">
    <div class="lang-switcher" title="Switch Language / Đổi ngôn ngữ">
      <button class="lang-btn active" data-lang="en" onclick="setLanguage('en')">EN</button>
      <button class="lang-btn" data-lang="vi" onclick="setLanguage('vi')">VI</button>
    </div>
    <span class="pill-tide">Powered by TideCloak</span>
  </div>
</header>"""

    if old_header in code:
        code = code.replace(old_header, new_header)

    with open(p, "w", encoding="utf-8") as f:
        f.write(code)
    print("Fixed portal index header:", p)
