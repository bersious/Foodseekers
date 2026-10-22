import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

REC_JS = r"""
/* ==================== DEMO RECORDING MODE ==================== */
(function(){
  if(window.__recModeReady) return;
  window.__recModeReady = true;

  var HINT_ID = 'rec-mode-hint';

  function ensureHint(){
    if(document.getElementById(HINT_ID)) return;
    var el = document.createElement('div');
    el.id = HINT_ID;
    el.style.cssText = 'position:fixed;left:50%;bottom:28px;transform:translateX(-50%) translateY(20px);' +
      'background:rgba(16,20,17,.96);border:1px solid rgba(212,255,63,.4);color:#f4f5f7;' +
      'font:600 12px/1.5 "Space Grotesk",system-ui,sans-serif;padding:9px 18px;border-radius:999px;' +
      'z-index:99999;opacity:0;transition:opacity .28s,transform .28s;pointer-events:none;' +
      'box-shadow:0 10px 34px rgba(0,0,0,.5)';
    el.textContent = 'Chế độ quay video đã bật · Ẩn con trỏ · Nhấn ESC để thoát';
    document.body.appendChild(el);
  }

  window.toggleRecMode = function(on){
    ensureHint();
    var hint = document.getElementById(HINT_ID);
    if(on === undefined) on = !document.body.classList.contains('rec-cursor-hide');
    document.body.classList.toggle('rec-cursor-hide', on);
    if(hint){
      if(on){
        hint.style.opacity = '1';
        hint.style.transform = 'translateX(-50%) translateY(0)';
        setTimeout(function(){ hint.style.opacity = '0'; }, 2600);
      }else{
        hint.style.opacity = '0';
        hint.style.transform = 'translateX(-50%) translateY(20px)';
      }
    }
  };

  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){
      if(document.body.classList.contains('rec-cursor-hide')){
        window.toggleRecMode(false);
      }
    }
    // Phím R (không phải khi đang gõ vào input) -> bật/tắt chế độ quay
    if((e.key === 'r' || e.key === 'R') && !e.ctrlKey && !e.metaKey && !e.altKey){
      var tag = (e.target && e.target.tagName) || '';
      if(tag === 'INPUT' || tag === 'TEXTAREA' || e.target.isContentEditable) return;
      window.toggleRecMode();
    }
  });
})();
"""

for base in [FS_PROTO, BW_RMIT]:
    for page in ["1", "2", "3"]:
        p = os.path.join(base, page, "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        if "__recModeReady" in code:
            print(f"  skip (already): {p}")
            continue

        marker = "/* ==================== DEMO RECORDING MODE ==================== */"
        anchor = "/* ==================== TOAST SYSTEM (thay alert() để UI sang trọng) ==================== */"
        if anchor in code:
            code = code.replace(anchor, REC_JS + "\n" + anchor, 1)
        else:
            body_i = code.find("<body>")
            code = code[:body_i+len("<body>")] + "\n\n<script>\n" + REC_JS + "\n</script>\n" + code[body_i+len("<body>"):]

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  rec mode added: {p}")

print("✓ Đã thêm chế độ quay video (nhấn R để ẩn con trỏ, ESC để thoát) cho cả 3 trang.")
