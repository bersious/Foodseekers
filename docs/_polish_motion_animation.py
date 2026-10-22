import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# MOTION DESIGN SYSTEM — tối ưu animation cho quay video sản phẩm
# - Mọi animation chạy trên GPU (transform/opacity), không layout thrash
# - requestAnimationFrame thay cho setInterval cho visualizer
# - Toast system thay cho alert() để UI sang trọng khi quay
# - Stagger entrance animation, ripple effect, count-up number
# ==============================================================================

MOTION_CSS = r"""
/* ==================== MOTION DESIGN SYSTEM ==================== */
:root{
  --ease-out:cubic-bezier(.22,1,.36,1);
  --ease-spring:cubic-bezier(.34,1.4,.64,1);
  --ease-smooth:cubic-bezier(.4,0,.2,1);
}
html{scroll-behavior:smooth}
body{
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
  text-rendering:optimizeLegibility;
}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{
    animation-duration:.01ms!important;animation-iteration-count:1!important;
    transition-duration:.01ms!important;scroll-behavior:auto!important;
  }
}

/* Nút: phản hồi nhấn + ripple */
.btn{position:relative;overflow:hidden;transition:transform .2s var(--ease-out),filter .2s,background .2s,box-shadow .2s,border-color .2s}
.btn:active{transform:translateY(0) scale(.965)}
.btn-accent:active{filter:brightness(.94)}
.ripple{
  position:absolute;border-radius:50%;pointer-events:none;transform:scale(0);
  background:rgba(255,255,255,.45);animation:rippleOut .62s var(--ease-out) forwards;
}
@keyframes rippleOut{to{transform:scale(2.8);opacity:0}}

/* Card hover nổi bật + viền phát sáng */
.card,.album-card,.track-card,.req-card{
  transition:transform .28s var(--ease-out),border-color .28s,box-shadow .28s,background .28s;
}
.card:hover{box-shadow:0 18px 50px rgba(0,0,0,.34)}

/* Entrance animation */
@keyframes riseIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.rise{animation:riseIn .58s var(--ease-out) both}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.fade-in{animation:fadeIn .5s ease both}
@keyframes slideInRight{from{opacity:0;transform:translateX(26px) scale(.97)}to{opacity:1;transform:none}}
@keyframes popIn{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}

/* Skeleton shimmer cho trạng thái loading */
@keyframes shimmer{0%{background-position:-220% 0}100%{background-position:220% 0}}
.skeleton{
  background:linear-gradient(90deg,rgba(255,255,255,.04) 25%,rgba(255,255,255,.1) 50%,rgba(255,255,255,.04) 75%);
  background-size:220% 100%;animation:shimmer 1.5s linear infinite;border-radius:8px;
}

/* Live pulse cho nhãn đồng bộ */
@keyframes liveGlow{
  0%,100%{box-shadow:0 0 0 0 rgba(184,243,107,.34)}
  50%{box-shadow:0 0 0 7px rgba(184,243,107,0)}
}
.pill-live{animation:liveGlow 2.4s var(--ease-smooth) infinite}

/* Toast system */
.toast-host{
  position:fixed;right:24px;bottom:24px;z-index:99999;
  display:flex;flex-direction:column;gap:10px;pointer-events:none;max-width:380px;
}
.toast{
  display:flex;align-items:flex-start;gap:11px;pointer-events:auto;
  background:rgba(16,20,17,.96);border:1px solid var(--line-strong);border-left-width:3px;
  border-radius:12px;padding:13px 17px;font-size:13px;color:var(--fg);line-height:1.5;
  box-shadow:0 14px 42px rgba(0,0,0,.5);backdrop-filter:blur(18px);
  animation:toastIn .42s var(--ease-spring) both;
}
.toast.out{animation:toastOut .32s var(--ease-smooth) forwards}
.toast-bar{width:3px;align-self:stretch;border-radius:2px;background:var(--accent);flex-shrink:0}
.toast-ok .toast-bar{background:var(--ok)}
.toast-warn .toast-bar{background:var(--warn)}
.toast-danger .toast-bar{background:var(--danger)}
.toast-title{font-weight:700;margin-bottom:2px}
.toast-body{color:var(--muted);font-size:12px}
@keyframes toastIn{from{opacity:0;transform:translateX(34px) scale(.95)}to{opacity:1;transform:none}}
@keyframes toastOut{to{opacity:0;transform:translateX(34px) scale(.95)}}

/* Số liệu đếm tăng */
.count-num{font-variant-numeric:tabular-nums;transition:opacity .2s}
.count-num.bump{animation:countBump .42s var(--ease-spring)}
@keyframes countBump{0%{transform:scale(1)}40%{transform:scale(1.14)}100%{transform:scale(1)}}

/* Scanline cho trang hạ tầng S3 */
@keyframes scanSweep{0%{transform:translateY(-100%)}100%{transform:translateY(1200%)}}
.scan-line{
  position:absolute;left:0;right:0;height:2px;pointer-events:none;
  background:linear-gradient(90deg,transparent,var(--accent),transparent);
  opacity:.55;animation:scanSweep 5.5s linear infinite;
}
.s3-table tbody tr{transition:background .2s}
.s3-table tbody tr.flash{animation:rowFlash 1.1s ease}
@keyframes rowFlash{
  0%{background:rgba(255,77,109,.22)}
  100%{background:transparent}
}

/* Visualizer: dùng transform thay height để không gây layout thrash */
.bar{
  flex:1;background:var(--line-strong);border-radius:2px;height:100%;
  transform:scaleY(.1);transform-origin:bottom;
  transition:transform .12s linear,background .12s linear;
  will-change:transform;
}
.bar.on{background:linear-gradient(180deg,var(--accent),rgba(184,243,107,.25))}

/* Dòng log terminal trôi mượt */
.terminal-output>div{animation:fadeIn .28s ease both}

/* Ẩn con trỏ khi người dùng không cần */
.rec-cursor-hide, .rec-cursor-hide *{cursor:none!important}
"""

TOAST_JS = r"""
/* ==================== TOAST SYSTEM (thay alert() để UI sang trọng) ==================== */
(function(){
  if(window.__toastReady) return;
  window.__toastReady = true;

  function host(){
    let h = document.querySelector('.toast-host');
    if(!h){
      h = document.createElement('div');
      h.className = 'toast-host';
      document.body.appendChild(h);
    }
    return h;
  }

  window.showToast = function(title, body, kind){
    kind = kind || 'ok';
    const el = document.createElement('div');
    el.className = 'toast toast-' + kind;
    el.innerHTML = '<div class="toast-bar"></div><div><div class="toast-title"></div>' +
                   (body ? '<div class="toast-body"></div>' : '') + '</div>';
    el.querySelector('.toast-title').textContent = title;
    if(body) el.querySelector('.toast-body').textContent = body;
    host().appendChild(el);
    setTimeout(function(){
      el.classList.add('out');
      setTimeout(function(){ el.remove(); }, 340);
    }, 4200);
  };

  // Ripple effect cho mọi nút
  document.addEventListener('pointerdown', function(e){
    const btn = e.target.closest ? e.target.closest('.btn, .auth-tab, .artist-chip, .album-card') : null;
    if(!btn) return;
    const r = btn.getBoundingClientRect();
    const size = Math.max(r.width, r.height);
    const span = document.createElement('span');
    span.className = 'ripple';
    span.style.width = span.style.height = size + 'px';
    span.style.left = (e.clientX - r.left - size/2) + 'px';
    span.style.top = (e.clientY - r.top - size/2) + 'px';
    if(getComputedStyle(btn).position === 'static') btn.style.position = 'relative';
    btn.appendChild(span);
    setTimeout(function(){ span.remove(); }, 640);
  }, {passive:true});

  // Bộ đếm số tăng dần
  window.animateCount = function(el, to, suffix){
    if(!el) return;
    const from = parseInt(String(el.textContent).replace(/[^\d]/g,''), 10) || 0;
    const target = Number(to) || 0;
    const start = performance.now();
    const dur = 620;
    el.classList.remove('bump');
    void el.offsetWidth;
    el.classList.add('bump');
    function step(now){
      const p = Math.min((now - start)/dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(from + (target - from) * eased) + (suffix || '');
      if(p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  };

  // Stagger entrance cho danh sách card
  window.staggerIn = function(container, selector){
    if(!container) return;
    const items = container.querySelectorAll(selector);
    items.forEach(function(el, i){
      el.classList.remove('rise');
      void el.offsetWidth;
      el.style.animationDelay = Math.min(i * 55, 420) + 'ms';
      el.classList.add('rise');
    });
  };
})();
"""


def inject_css_and_js(code, extra_css=""):
    if 'MOTION DESIGN SYSTEM' not in code:
        code = code.replace('</style>', MOTION_CSS + extra_css + '\n</style>', 1)
    if '__toastReady' not in code:
        code = code.replace('</body>', TOAST_JS + '\n</body>', 1)
    return code


# ==============================================================================
# TRANG 1 — Nghệ sĩ
# ==============================================================================
def patch_page1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        code = inject_css_and_js(code, """
/* Nghệ sĩ: switcher + upload zone */
.artist-chip,.auth-tab{transition:background .22s var(--ease-out),color .22s,border-color .22s,transform .22s var(--ease-out)}
.artist-chip:active,.auth-tab:active{transform:scale(.97)}
.upload-zone{transition:border-color .25s,background .25s,transform .25s var(--ease-out)}
.upload-zone:active{transform:scale(.995)}
.toggle-knob{transition:left .28s var(--ease-spring),transform .2s}
.toggle-switch{transition:background .28s var(--ease-out)}
.toggle-switch:active .toggle-knob{transform:scale(.85)}
.user-chip{animation:popIn .32s var(--ease-spring) both;transition:background .2s,border-color .2s}
.user-chip:hover{background:var(--surface-2);border-color:var(--line-strong)}
.track-art{transition:transform .3s var(--ease-out)}
.track-card:hover .track-art{transform:scale(1.06) rotate(-2deg)}
""")

        # Upload zone -> highlight khi kéo file vào
        code = code.replace(
            "async function handleFileUpload(e){",
            """function setupUploadZone(){
  const zone = document.getElementById('upload-zone');
  if(!zone) return;
  const input = document.getElementById('file-input');
  if(!input) return;
  // Lưu ý: zone đã có onclick="...file-input.click()" sẵn trong HTML, không gắn thêm để tránh mở 2 hộp thoại
  ['dragenter','dragover'].forEach(function(ev){
    zone.addEventListener(ev, function(e){
      e.preventDefault(); e.stopPropagation();
      zone.style.borderColor = 'var(--accent)';
      zone.style.background = 'rgba(212,255,63,.07)';
      zone.style.transform = 'scale(1.01)';
    });
  });
  ['dragleave','drop'].forEach(function(ev){
    zone.addEventListener(ev, function(e){
      e.preventDefault(); e.stopPropagation();
      zone.style.borderColor = '';
      zone.style.background = '';
      zone.style.transform = '';
    });
  });
  zone.addEventListener('drop', function(e){
    const f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
    if(f && input){
      try{
        const dt = new DataTransfer();
        dt.items.add(f);
        input.files = dt.files;
        input.dispatchEvent(new Event('change'));
      }catch(err){}
    }
  });
}

async function handleFileUpload(e){"""
        )

        # Thay alert() bằng toast trong các thao tác chính
        code = code.replace(
            "if(!u){ alert('Vui lòng nhập username của nghệ sĩ!'); return; }",
            "if(!u){ showToast('Thiếu tên đăng nhập','Vui lòng nhập username của nghệ sĩ.','warn'); return; }")
        code = code.replace(
            "if(p !== '123'){ alert('Mật khẩu xác thực không chính xác.'); return; }",
            "if(p !== '123'){ showToast('Mật khẩu không đúng','Mật khẩu xác thực của hệ thống là 123.','danger'); return; }")
        code = code.replace(
            "if(!name || !user){ alert('Vui lòng điền tên nghệ sĩ và username!'); return; }",
            "if(!name || !user){ showToast('Thiếu thông tin','Vui lòng điền tên nghệ sĩ và username.','warn'); return; }")
        code = code.replace(
            "if(p !== '123'){ alert('Mật khẩu không hợp lệ.'); return; }",
            "if(p !== '123'){ showToast('Mật khẩu không hợp lệ','Mật khẩu khởi tạo là 123.','danger'); return; }")
        code = code.replace(
            "    alert('Username nghệ sĩ này đã tồn tại!');\n    return;",
            "    showToast('Username đã tồn tại','Hãy chọn một tên đăng nhập khác.','warn');\n    return;")
        code = code.replace(
            "alert(`Đã tạo thành công Profile Nghệ Sĩ: ${name}!`);",
            "showToast('Tạo hồ sơ thành công', `Két sắt của ${name} đã sẵn sàng.`, 'ok');")
        code = code.replace(
            "if(!u){ alert('Vui lòng chọn một người nghe từ danh sách!'); return; }",
            "if(!u){ showToast('Chưa chọn người nghe','Vui lòng chọn một danh tính từ danh sách.','warn'); return; }")

        # Toast khi cấp quyền / thu hồi / upload / xóa
        code = code.replace(
            "    // Xóa user khỏi dropdown\n    if(select){",
            "    showToast('Đã cấp quyền', `Danh tính @${u} đã có thể giải mã tác phẩm.`, 'ok');\n\n    // Xóa user khỏi dropdown\n    if(select){")
        code = code.replace(
            "    // Thêm lại vào dropdown\n    const select = document.getElementById(`select-user-${trackId}`);",
            "    showToast('Đã thu hồi quyền', `@${username} không còn có thể giải mã tác phẩm.`, 'warn');\n\n    // Thêm lại vào dropdown\n    const select = document.getElementById(`select-user-${trackId}`);")
        code = code.replace(
            "  stat.textContent = `> [THÀNH CÔNG] Đã tải lên và niêm phong tác phẩm \"${file.name}\" vào két sắt của @${activeArtistUser}!`;",
            "  stat.textContent = `> [THÀNH CÔNG] Đã tải lên và niêm phong tác phẩm \"${file.name}\" vào két sắt của @${activeArtistUser}!`;\n  showToast('Tải lên thành công', `\"${file.name}\" đã được niêm phong vào két sắt.`, 'ok');")
        code = code.replace(
            "  const card = document.getElementById(`card-${trackId}`);\n  if(card) card.remove();",
            "  const card = document.getElementById(`card-${trackId}`);\n  if(card){ card.style.transition='opacity .25s,transform .25s'; card.style.opacity='0'; card.style.transform='scale(.97)'; setTimeout(()=>card.remove(),260); }\n  showToast('Đã xóa tác phẩm', 'Tệp tin đã bị loại bỏ khỏi két sắt.', 'warn');")

        # Stagger animation khi render danh sách bài hát
        code = code.replace(
            "    box.appendChild(card);\n\n    // Nạp source phát nhạc/video vào player ngay lập tức",
            "    box.appendChild(card);\n    card.classList.add('rise');\n    card.style.animationDelay = Math.min(myTracks.indexOf(t) * 70, 400) + 'ms';\n\n    // Nạp source phát nhạc/video vào player ngay lập tức")

        # Đếm số đơn chờ bằng animation
        code = code.replace(
            "  count.textContent = `${pending.length} đơn chờ`;",
            "  animateCount(count, pending.length, ' đơn chờ');")

        # Khởi chạy setupUploadZone
        code = code.replace(
            "// Khởi chạy\ncheckArtistAuth();",
            "// Khởi chạy\nsetupUploadZone();\ncheckArtistAuth();")

        # Nhãn pill đồng bộ -> live glow
        code = code.replace(
            '<span class="pill-tide">Cloud Database Synced</span>',
            '<span class="pill-tide pill-live">Cloud Database Synced</span>')

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"[P1] Motion polish applied: {p}")


# ==============================================================================
# TRANG 2 — Người nghe (SONORA)
# ==============================================================================
def patch_page2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        code = inject_css_and_js(code, """
/* SONORA: disc xoay mượt, chips, album card */
.disc{transition:transform .3s var(--ease-out),box-shadow .3s}
.disc.spin{animation:spin 6s linear infinite;box-shadow:0 0 30px rgba(184,243,107,.22)}
.artist-chip{transition:background .24s var(--ease-out),border-color .24s,box-shadow .24s,transform .24s var(--ease-out)}
.artist-chip:active{transform:scale(.97)}
.album-card{transition:transform .3s var(--ease-out),border-color .3s,box-shadow .3s,background .3s}
.album-card:hover{transform:translateY(-4px);box-shadow:0 16px 42px rgba(0,0,0,.34)}
.album-card.active-card{transform:translateY(-2px)}
.play-btn{transition:transform .2s var(--ease-spring),box-shadow .25s,background .25s}
.play-btn:hover{transform:scale(1.08)}
.now-playing{animation:fadeIn .4s ease both}
.music-hero{animation:riseIn .7s var(--ease-out) both}
.visualizer{position:relative}
.locked-panel{animation:riseIn .45s var(--ease-out) both}
.req-row{animation:popIn .3s var(--ease-spring) both}
""")

        # Thay alert() bằng toast
        code = code.replace(
            "if(!text){ alert('Vui lòng nhập nội dung nhận xét!'); return; }",
            "if(!text){ showToast('Chưa có nội dung','Vui lòng nhập nhận xét của bạn.','warn'); return; }")
        code = code.replace(
            "if(!activeTrackId){ alert('Vui lòng chọn bài hát trước khi bình luận!'); return; }",
            "if(!activeTrackId){ showToast('Chưa chọn tác phẩm','Hãy chọn một bài hát trước khi gửi góp ý.','warn'); return; }")
        code = code.replace(
            "    alert('Vui lòng chọn một bài hát từ danh sách phía trên!');",
            "    showToast('Chưa chọn tác phẩm','Hãy chọn một bài hát từ danh sách phía trên.','warn');")
        code = code.replace(
            "    alert(`Tác phẩm \"${track.name}\" đang bị khóa đối với tài khoản của bạn! Nhấn nút \"Xin quyền nghe\" để yêu cầu Nghệ Sĩ mở khóa.`);",
            "    showToast('Tác phẩm đang bị khóa', `Nhấn \"Xin quyền nghe\" để yêu cầu Nghệ Sĩ mở khóa tác phẩm \"${track.name}\".`, 'warn');")

        # Visualizer dùng requestAnimationFrame + transform (GPU) thay setInterval height
        old_viz_native = """      synthInterval=setInterval(()=>{
        bars.forEach(b=>b.style.height=(15+Math.random()*80)+'%');
        bars.forEach(b=>b.classList.toggle('on',Math.random()>.25));
      },180);"""
        new_viz_native = """      synthInterval = startVisualizerRAF();"""
        code = code.replace(old_viz_native, new_viz_native)

        old_viz_synth = """      synthInterval=setInterval(()=>{
        noteIdx=(noteIdx+1)%notes.length;tone(notes[noteIdx]);
        bars.forEach(b=>b.style.height=(15+Math.random()*80)+'%');
        bars.forEach(b=>b.classList.toggle('on',Math.random()>.25));
      },220);"""
        new_viz_synth = """      synthInterval = startVisualizerRAF();
      noteTimer=setInterval(()=>{
        noteIdx=(noteIdx+1)%notes.length;tone(notes[noteIdx]);
      },220);"""
        code = code.replace(old_viz_synth, new_viz_synth)

        # Hàm visualizer dựa trên requestAnimationFrame
        viz_fn = """
/* Visualizer chạy bằng requestAnimationFrame + transform scaleY (GPU) -> mượt 60fps, không layout thrash */
let vizRaf = null;
function startVisualizerRAF(){
  if(vizRaf) cancelAnimationFrame(vizRaf);
  function frame(){
    for(let i=0;i<bars.length;i++){
      const b = bars[i];
      const h = 0.14 + Math.random()*0.82;
      b.style.transform = 'scaleY(' + h + ')';
      b.classList.toggle('on', Math.random() > 0.22);
    }
    vizRaf = requestAnimationFrame(frame);
  }
  vizRaf = requestAnimationFrame(frame);
  return vizRaf;
}
function stopVisualizerRAF(){
  if(vizRaf){ cancelAnimationFrame(vizRaf); vizRaf = null; }
  bars.forEach(function(b){ b.style.transform='scaleY(.1)'; b.classList.remove('on'); });
}
"""
        if 'function startVisualizerRAF(' not in code:
            code = code.replace("function togglePlay(){", viz_fn + "\nfunction togglePlay(){")

        # Dọn visualizer khi dừng
        code = code.replace(
            "function stopAudio(){",
            "function stopAudio(){\n  stopVisualizerRAF();")

        # Khai báo noteTimer
        code = code.replace(
            "let isPlaying = false, synthInterval = null, timerInterval = null, ctx = null, t = 0, noteIdx = 0;",
            "let isPlaying = false, synthInterval = null, timerInterval = null, noteTimer = null, ctx = null, t = 0, noteIdx = 0;")

        # Stagger album card
        code = code.replace(
            "    container.appendChild(card);\n  });\n}",
            "    container.appendChild(card);\n    card.classList.add('rise');\n    card.style.animationDelay = Math.min(artistTracks.indexOf(t) * 60, 360) + 'ms';\n  });\n}")

        # Toast khi gửi góp ý
        code = code.replace(
            "  input.value = '';\n  renderReviewerComments();",
            "  input.value = '';\n  renderReviewerComments();\n  showToast('Đã gửi góp ý', 'Nghệ sĩ đã nhận được nhận xét của bạn.', 'ok');")

        # Toast khi xin quyền
        code = code.replace(
            "  appendLog(`[REQUEST] Đã gửi đơn xin quyền nghe tới Nghệ Sĩ cho tác phẩm này.`, 'var(--warn)');",
            "  appendLog(`[REQUEST] Đã gửi đơn xin quyền nghe tới Nghệ Sĩ cho tác phẩm này.`, 'var(--warn)');\n  showToast('Đã gửi đơn xin quyền', 'Nghệ sĩ sẽ duyệt trong vài giây tới.', 'ok');")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"[P2] Motion polish applied: {p}")


# ==============================================================================
# TRANG 3 — Hạ tầng S3
# ==============================================================================
def patch_page3():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "3", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        code = inject_css_and_js(code, """
/* S3: scanline, số liệu, terminal */
.metric-box{transition:background .25s,transform .3s var(--ease-out)}
.metric-box:hover{background:#0b0f0c;transform:translateY(-2px)}
.s3-card-wrap{position:relative;overflow:hidden}
.btn-danger{transition:transform .2s var(--ease-out),background .22s,box-shadow .22s}
.btn-danger:hover{box-shadow:0 6px 20px rgba(255,77,109,.22)}
.terminal-card{animation:riseIn .45s var(--ease-out) both}
""")

        # Số liệu blobs đếm tăng
        code = code.replace(
            "  countEl.textContent = `${tracks.length} Blobs`;",
            "  animateCount(countEl, tracks.length, ' Blobs');")

        # Flash dòng khi có bản ghi mới
        code = code.replace(
            "    tbody.appendChild(row);\n  });",
            "    row.classList.add('rise');\n    tbody.appendChild(row);\n  });")

        # Terminal gõ từng ký tự cho mượt + highlight
        code = code.replace(
            "  let idx = 0;\n  function printLine(){\n    if(idx < logs.length){\n      const p = document.createElement('div');\n      p.textContent = logs[idx++];\n      if(idx === logs.length) p.style.color = 'var(--ok)';\n      else if(logs[idx-1].includes('Forbidden') || logs[idx-1].includes('ERROR')) p.style.color = 'var(--danger)';\n      content.appendChild(p);\n      content.scrollTop = content.scrollHeight;\n      setTimeout(printLine, 350);\n    }\n  }\n  printLine();",
            """  let idx = 0;
  function printLine(){
    if(idx < logs.length){
      const line = logs[idx++];
      const p = document.createElement('div');
      p.textContent = '';
      if(idx === logs.length) p.style.color = 'var(--ok)';
      else if(line.includes('Forbidden') || line.includes('ERROR')) p.style.color = 'var(--danger)';
      else if(line.includes('MITIGATED')) p.style.color = 'var(--ok)';
      content.appendChild(p);
      content.scrollTop = content.scrollHeight;

      // Gõ từng ký tự: chậm vừa đủ để khán giả đọc kịp khi quay video
      let ci = 0;
      const speed = line.startsWith('> ') ? 12 : 6;
      (function typeChar(){
        if(ci < line.length){
          p.textContent += line.charAt(ci++);
          content.scrollTop = content.scrollHeight;
          setTimeout(typeChar, speed);
        }else{
          setTimeout(printLine, 240);
        }
      })();
    }
  }
  printLine();""")

        # Scanline animation trên card bảng S3
        code = code.replace(
            '  <!-- Bảng kiểm tra tệp tin nhị phân S3 thời gian thực -->\n  <div class="card">',
            '  <!-- Bảng kiểm tra tệp tin nhị phân S3 thời gian thực -->\n  <div class="card s3-card-wrap">\n    <div class="scan-line"></div>')

        # Toast khi chạy kịch bản tấn công
        code = code.replace(
            "  term.classList.remove('hidden');\n  content.innerHTML = '';",
            "  term.classList.remove('hidden');\n  content.innerHTML = '';\n  showToast('Đang chạy kịch bản tấn công', 'Kẻ tấn công đang dò quét máy chủ S3...', 'danger');")
        code = code.replace(
            "  printLine();\n}",
            "  printLine();\n  setTimeout(function(){\n    showToast('Tấn công bị chặn hoàn toàn', 'Quorum TideCloak từ chối giải mã. 0 byte rò rỉ.', 'ok');\n  }, 4200);\n}", 1)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"[P3] Motion polish applied: {p}")


patch_page1()
patch_page2()
patch_page3()
print("✓ Hoàn tất tối ưu Motion & Animation cho cả 3 trang!")
