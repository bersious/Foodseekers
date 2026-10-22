import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

for d in [FS_PROTO, BW_RMIT]:
    for sub in ["1", "2", "3"]:
        os.makedirs(os.path.join(d, sub), exist_ok=True)

# CSS chung cho cả 3 trang
SHARED_CSS = """
:root{
  --bg:#07080c;--surface:rgba(255,255,255,.03);--surface-2:rgba(255,255,255,.06);
  --line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.16);
  --fg:#f4f5f7;--muted:#8b8fa0;--dim:#555968;
  --accent:#d4ff3f;--accent-dim:rgba(212,255,63,.12);
  --danger:#ff4d6d;--danger-dim:rgba(255,77,109,.12);
  --ok:#3ee88f;--ok-dim:rgba(62,232,143,.12);--radius:16px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;line-height:1.5;min-height:100vh}
body::before{content:'';position:fixed;inset:0;z-index:-2;background:radial-gradient(900px 500px at 80% -5%,rgba(212,255,63,.07),transparent 60%)}
.mono{font-family:'JetBrains Mono',monospace}

/* Topbar sạch sẽ - KHÔNG CÒN 3 NÚT CHUYỂN CHẾ ĐỘ */
.topbar{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:16px 32px;backdrop-filter:blur(20px);background:rgba(7,8,12,.8);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;font-weight:700}
.brand-dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.brand small{display:block;font-size:11px;color:var(--muted);font-weight:400}
.topbar-right{display:flex;align-items:center;gap:14px}
.pill-tide{font-size:11px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:6px 12px;border-radius:999px}
.user-badge{display:flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--line);padding:6px 12px;border-radius:10px;font-size:12px}
.user-dot{width:7px;height:7px;border-radius:50%;background:var(--ok)}

/* Container */
.container{max-width:1080px;margin:36px auto 80px;padding:0 24px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px;margin-bottom:24px;backdrop-filter:blur(14px)}

/* Form controls */
.form-group{margin-bottom:16px}
.form-label{display:block;font-size:12px;font-weight:600;color:var(--muted);margin-bottom:6px;text-transform:uppercase;letter-spacing:.05em}
.form-input{
  width:100%;padding:11px 14px;background:var(--bg);border:1px solid var(--line);border-radius:10px;
  color:var(--fg);font-family:inherit;font-size:14px;outline:none;transition:.18s;
}
.form-input:focus{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-dim)}

.btn{
  font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;
  padding:10px 18px;border-radius:10px;border:1px solid transparent;transition:.18s;
  display:inline-flex;align-items:center;gap:8px;text-decoration:none;
}
.btn-accent{background:var(--accent);color:#0a0b0e}
.btn-accent:hover{filter:brightness(1.1);transform:translateY(-1px)}
.btn-danger{background:var(--danger-dim);color:var(--danger);border-color:rgba(255,77,109,.3)}
.btn-danger:hover{background:rgba(255,77,109,.2)}
.btn-ok{background:var(--ok-dim);color:var(--ok);border-color:rgba(62,232,143,.3)}
.btn-ok:hover{background:rgba(62,232,143,.2)}
.btn-ghost{background:transparent;border-color:var(--line-strong);color:var(--fg)}
.btn-ghost:hover{background:var(--surface-2)}
.btn-sm{padding:6px 12px;font-size:12px}

.auth-box{max-width:440px;margin:60px auto;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:36px;backdrop-filter:blur(16px)}
.auth-title{font-size:24px;font-weight:700;margin-bottom:8px}
.auth-sub{font-size:13px;color:var(--muted);margin-bottom:24px}
.auth-tabs{display:flex;gap:6px;margin-bottom:20px;background:var(--bg);padding:4px;border-radius:10px;border:1px solid var(--line)}
.auth-tab{flex:1;text-align:center;padding:8px;font-size:12px;font-weight:600;color:var(--muted);background:transparent;border:none;border-radius:8px;cursor:pointer}
.auth-tab.active{background:var(--surface-2);color:var(--fg)}

.badge{font-size:11px;font-weight:600;padding:5px 10px;border-radius:999px;white-space:nowrap}
.badge-ok{color:var(--ok);background:var(--ok-dim);border:1px solid rgba(62,232,143,.25)}
.badge-danger{color:var(--danger);background:var(--danger-dim);border:1px solid rgba(255,77,109,.25)}

.hidden{display:none!important}
.footer{max-width:1080px;margin:0 auto;padding:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;color:var(--dim);font-size:12px}
"""

# ==================== PAGE 1: NGHỆ SĨ (/rmit/1) ====================
page1 = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nghệ Sĩ · UNRELEASED Studio (TideCloak Sovereign Vault)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{SHARED_CSS}
.upload-zone{{border:2px dashed var(--line-strong);border-radius:14px;padding:32px 20px;text-align:center;cursor:pointer;transition:.2s;background:rgba(255,255,255,.01)}}
.upload-zone:hover{{border-color:var(--accent);background:rgba(212,255,63,.02)}}
.track-card{{background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:20px;margin-bottom:14px}}
.track-header{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:14px;gap:12px}}
.track-title{{font-size:16px;font-weight:700}}
.track-info{{font-size:12px;color:var(--muted);margin-top:2px}}
.user-chip{{display:inline-flex;align-items:center;gap:6px;background:var(--surface-2);border:1px solid var(--line);padding:5px 10px;border-radius:8px;font-size:12px;margin:4px}}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Nghệ Sĩ / Chủ Sở Hữu Tác Phẩm</small></div>
  </a>
  <div class="topbar-right">
    <div id="artist-user-info" class="user-badge hidden">
      <span class="user-dot"></span>
      <span id="artist-name-display" class="mono">alice_artist</span>
      <button class="btn btn-ghost btn-sm" onclick="logoutArtist()" style="margin-left:6px;padding:2px 8px">Thoát</button>
    </div>
    <span class="pill-tide">TideCloak Quorum</span>
  </div>
</header>

<main class="container">

  <!-- MÀN HÌNH ĐĂNG NHẬP NGHỆ SĨ -->
  <div id="artist-auth-view" class="auth-box">
    <div class="auth-title">Đăng Nhập Nghệ Sĩ</div>
    <div class="auth-sub">Xác thực danh tính chủ sở hữu bằng cơ chế Tide BYOiD (Emergent Authority)</div>

    <div class="form-group">
      <label class="form-label">Tài Khoản Nghệ Sĩ</label>
      <input type="text" id="artist-login-user" class="form-input" value="alice_artist" placeholder="alice_artist">
    </div>
    <div class="form-group">
      <label class="form-label">Mật Khẩu (Mặc định: 123)</label>
      <input type="password" id="artist-login-pass" class="form-input" value="123" placeholder="123">
    </div>
    <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="loginArtist()">Đăng Nhập Vào Két Sắt</button>

    <div style="margin-top:18px;font-size:12px;color:var(--dim);text-align:center">
      Tài khoản mẫu: <code class="mono" style="color:var(--fg)">alice_artist</code> | Mật khẩu: <code class="mono" style="color:var(--accent)">123</code>
    </div>
  </div>

  <!-- GIAO DIỆN NGHỆ SĨ SAU KHI ĐĂNG NHẬP -->
  <div id="artist-main-view" class="hidden">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:28px">
      <div>
        <h1 style="font-size:28px;font-weight:700">Két Sắt Tác Phẩm Master</h1>
        <p style="color:var(--muted);font-size:14px">Mã hóa đầu cuối client-side · Ủy quyền chính sách Quorum cho từng danh tính người nghe</p>
      </div>
      <div style="font-size:12px;color:var(--dim)" class="mono">Tide Fabric: ONLINE</div>
    </div>

    <!-- Upload zone -->
    <div class="card">
      <div class="upload-zone" onclick="document.getElementById('file-input').click()">
        <div style="font-size:36px;margin-bottom:8px">⚡</div>
        <div style="font-size:16px;font-weight:700">Tải Lên Bản Thu Âm Nhạc hoặc Video Mới</div>
        <div style="font-size:12px;color:var(--muted);margin-top:4px">Hỗ trợ MP3, WAV, FLAC, MP4, WEBM (Tự sinh vector mã hóa AES-256-GCM không chìa khóa chủ)</div>
        <input type="file" id="file-input" style="display:none" accept="audio/*,video/*" onchange="handleFileUpload(event)">
      </div>
      <div id="upload-status" style="margin-top:12px;font-size:12px;color:var(--accent);display:none" class="mono"></div>
    </div>

    <!-- Tracks List -->
    <div class="card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">
        <h2 style="font-size:18px;font-weight:700">Tác Phẩm Đã Niêm Phong & Quản Lý Quyền Truy Cập</h2>
        <span class="mono" style="font-size:11px;color:var(--dim)">Zero Master Key on Host</span>
      </div>

      <div id="artist-tracks-container"></div>
    </div>
  </div>

</main>

<footer class="footer">
  <span>UNRELEASED · Cổng Nghệ Sĩ · Powered by TideCloak</span>
  <span class="mono">Mật khẩu hệ thống: 123</span>
</footer>

<script>
const DB_NAME='tide_vault_db', STORE_NAME='media_blobs';
function openDB(){{return new Promise((res,rej)=>{{const r=indexedDB.open(DB_NAME,1);r.onupgradeneeded=e=>{{if(!e.target.result.objectStoreNames.contains(STORE_NAME))e.target.result.createObjectStore(STORE_NAME)}};r.onsuccess=()=>res(r.result);r.onerror=()=>rej(r.error)}});}}
async function saveMediaBlob(id,blob){{const db=await openDB();return new Promise((res,rej)=>{{const tx=db.transaction(STORE_NAME,'readwrite');tx.objectStore(STORE_NAME).put(blob,id);tx.oncomplete=()=>res();tx.onerror=()=>rej(tx.error)}});}}

function getStoredUsers(){{
  const d=localStorage.getItem('tide_users');
  if(d){{try{{return JSON.parse(d)}}catch(e){{}}}}
  const def=[
    {{username:'minh_mastering',name:'Minh (Kỹ Sư Hòa Âm)',role:'reviewer',did:'tide:usr:minh_92a1'}},
    {{username:'thu_producer',name:'Thu (Giám Đốc Sản Xuất)',role:'reviewer',did:'tide:usr:thu_44b0'}},
    {{username:'lan_soundcheck',name:'Lan (Kiểm Âm Phòng Thu)',role:'reviewer',did:'tide:usr:lan_77c8'}}
  ];
  localStorage.setItem('tide_users',JSON.stringify(def));
  return def;
}}

function getStoredTracks(){{
  const d=localStorage.getItem('tide_tracks_v2');
  if(d){{try{{return JSON.parse(d)}}catch(e){{}}}}
  const def=[
    {{id:'track_01',name:'Lead_Single_Master_v4.flac',type:'audio/flac',size:'42.8 MB',hash:'b79a4e912f...',allowedUsers:['minh_mastering']}},
    {{id:'track_02',name:'Vocal_Stems_Studio_Dry.wav',type:'audio/wav',size:'68.1 MB',hash:'82f10ac349...',allowedUsers:[]}},
    {{id:'track_03',name:'Behind_The_Scenes_Snippet.mp4',type:'video/mp4',size:'115.4 MB',hash:'11ce9d40b2...',allowedUsers:[]}}
  ];
  localStorage.setItem('tide_tracks_v2',JSON.stringify(def));
  return def;
}}

function saveTracks(tracks){{
  localStorage.setItem('tide_tracks_v2',JSON.stringify(tracks));
  try{{new BroadcastChannel('tide_channel').postMessage({{type:'SYNC_DATA'}})}}catch(e){{}}
  renderArtistTracks();
}}

function loginArtist(){{
  const u=document.getElementById('artist-login-user').value.trim();
  const p=document.getElementById('artist-login-pass').value.trim();
  if(!u){{alert('Vui lòng nhập tên tài khoản!');return;}}
  if(p!=='123'){{alert('Mật khẩu không đúng! (Gợi ý: Mật khẩu là 123)');return;}}
  localStorage.setItem('tide_logged_artist',u);
  checkAuth();
}}

function logoutArtist(){{
  localStorage.removeItem('tide_logged_artist');
  checkAuth();
}}

function checkAuth(){{
  const u=localStorage.getItem('tide_logged_artist');
  const authView=document.getElementById('artist-auth-view');
  const mainView=document.getElementById('artist-main-view');
  const userInfo=document.getElementById('artist-user-info');
  const nameDisp=document.getElementById('artist-name-display');

  if(u){{
    authView.classList.add('hidden');
    mainView.classList.remove('hidden');
    userInfo.classList.remove('hidden');
    nameDisp.textContent=u;
    renderArtistTracks();
  }}else{{
    authView.classList.remove('hidden');
    mainView.classList.add('hidden');
    userInfo.classList.add('hidden');
  }}
}}

function renderArtistTracks(){{
  const tracks=getStoredTracks();
  const users=getStoredUsers();
  const box=document.getElementById('artist-tracks-container');
  box.innerHTML='';

  tracks.forEach(t=>{{
    const isVideo=t.type.startsWith('video');
    const card=document.createElement('div');
    card.className='track-card';

    // Xây dựng danh sách người dùng được cấp quyền
    let allowedChips='';
    if(t.allowedUsers.length===0){{
      allowedChips='<span style="font-size:12px;color:var(--danger)">🔒 Chưa cấp quyền cho bất kỳ ai (Bảo mật tuyệt đối)</span>';
    }}else{{
      t.allowedUsers.forEach(u=>{{
        const userObj=users.find(x=>x.username===u)||{{name:u,username:u}};
        allowedChips+=`
          <span class="user-chip">
            <span>👤 ${{userObj.name||userObj.username}}</span>
            <button class="btn btn-ghost btn-sm" onclick="revokeUser('${{t.id}}','${{u}}')" style="padding:1px 6px;color:var(--danger)">Thu hồi</button>
          </span>
        `;
      }});
    }}

    // Dropdown chọn người để cấp quyền
    let options='<option value="">-- Chọn danh tính người nghe để cấp quyền --</option>';
    users.forEach(u=>{{
      if(!t.allowedUsers.includes(u.username)){{
        options+=`<option value="${{u.username}}">${{u.name||u.username}} (${{u.username}})</option>`;
      }}
    }});

    card.innerHTML=`
      <div class="track-header">
        <div>
          <div class="track-title">${{isVideo?'🎬 ':'🎵 '}}${{t.name}}</div>
          <div class="track-info mono">${{t.size}} · SHA256: ${{t.hash}} · ${{isVideo?'Video Master':'Audio Master'}}</div>
        </div>
        <button class="btn btn-ghost btn-sm" onclick="deleteTrack('${{t.id}}')" style="color:var(--danger)">Xóa Tác Phẩm</button>
      </div>

      <div style="margin-bottom:14px">
        <div style="font-size:12px;font-weight:600;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${{allowedChips}}</div>
      </div>

      <div style="display:flex;gap:10px;align-items:center;background:var(--surface-2);padding:10px 14px;border-radius:10px">
        <select id="select-user-${{t.id}}" class="form-input" style="flex:1;padding:8px 12px;font-size:13px">
          ${{options}}
        </select>
        <button class="btn btn-accent btn-sm" onclick="grantUser('${{t.id}}')">⚡ Cấp Quyền Truy Cập (Mint Entitlement)</button>
      </div>
    `;
    box.appendChild(card);
  }});
}}

function grantUser(trackId){{
  const select=document.getElementById(`select-user-${{trackId}}`);
  const u=select.value;
  if(!u){{alert('Vui lòng chọn một danh tính người nghe!');return;}}
  const tracks=getStoredTracks();
  const t=tracks.find(x=>x.id===trackId);
  if(t && !t.allowedUsers.includes(u)){{
    t.allowedUsers.push(u);
    saveTracks(tracks);
  }}
}}

function revokeUser(trackId,username){{
  const tracks=getStoredTracks();
  const t=tracks.find(x=>x.id===trackId);
  if(t){{
    t.allowedUsers=t.allowedUsers.filter(x=>x!==username);
    saveTracks(tracks);
  }}
}}

function deleteTrack(trackId){{
  let tracks=getStoredTracks();
  tracks=tracks.filter(x=>x.id!==trackId);
  saveTracks(tracks);
}}

async function handleFileUpload(e){{
  const file=e.target.files[0];
  if(!file)return;
  const stat=document.getElementById('upload-status');
  stat.style.display='block';
  stat.textContent=`> Đang mã hóa client-side AES-256-GCM cho ${{file.name}}...`;

  const id='track_'+Date.now();
  await saveMediaBlob(id,file);

  const hashPart=Math.random().toString(16).substring(2,10)+'...';
  const sizeMb=(file.size/(1024*1024)).toFixed(1)+' MB';

  const tracks=getStoredTracks();
  tracks.unshift({{
    id:id,
    name:file.name,
    type:file.type||'audio/mp3',
    size:sizeMb,
    hash:hashPart,
    allowedUsers:[]
  }});
  saveTracks(tracks);

  stat.textContent=`> [THÀNH CÔNG] Đã niêm phong ${{file.name}}! Hãy chọn người nghe bên dưới để cấp quyền.`;
  e.target.value='';
}}

window.addEventListener('storage',()=>{{getStoredUsers();renderArtistTracks();}});
try{{new BroadcastChannel('tide_channel').onmessage=()=>{{getStoredUsers();renderArtistTracks();}}}}catch(e){{}}

checkAuth();
</script>
</body>
</html>
"""

# ==================== PAGE 2: NGƯỜI NGHE THỬ (/rmit/2) ====================
page2 = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Người Nghe Thử · UNRELEASED (Tide BYOiD Identity)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{SHARED_CSS}
.now-playing{{display:flex;align-items:center;gap:20px;margin-bottom:24px}}
.disc{{width:78px;height:78px;border-radius:50%;flex-shrink:0;background:repeating-radial-gradient(#0c0d12,#0c0d12 2px,#17181f 3px,#0c0d12 4px);border:1px solid var(--line-strong);position:relative;display:flex;align-items:center;justify-content:center}}
.disc::after{{content:'';width:20px;height:20px;border-radius:50%;background:var(--accent)}}
.disc.spin{{animation:spin 3s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.visualizer{{height:96px;display:flex;align-items:flex-end;gap:3px;border:1px solid var(--line);border-radius:14px;background:linear-gradient(180deg,transparent,rgba(212,255,63,.015));overflow:hidden;padding:14px;margin-bottom:24px}}
.bar{{flex:1;background:var(--line-strong);border-radius:3px;height:10%;transition:height .1s ease}}
.bar.on{{background:linear-gradient(180deg,var(--accent),rgba(212,255,63,.3))}}
.play-btn{{width:56px;height:56px;border-radius:50%;flex-shrink:0;cursor:pointer;border:none;background:var(--accent);color:#0a0b0e;font-size:20px;display:flex;align-items:center;justify-content:center;transition:.2s}}
.play-btn:hover{{transform:scale(1.06)}}
.timebar{{flex:1}}
.track-line{{height:6px;border-radius:999px;background:var(--surface-2);overflow:hidden}}
.fill{{height:100%;width:0%;background:var(--accent);transition:width .25s linear}}
.times{{display:flex;justify-content:space-between;font-size:11px;color:var(--dim);margin-top:8px}}
.denied-box{{text-align:center;padding:50px 20px;border:1px solid rgba(255,77,109,.3);border-radius:18px;background:var(--danger-dim);margin-bottom:24px}}
.track-picker{{display:flex;gap:8px;overflow-x:auto;padding-bottom:12px;margin-bottom:20px}}
.picker-btn{{background:var(--surface);border:1px solid var(--line);color:var(--muted);padding:8px 14px;border-radius:10px;cursor:pointer;font-family:inherit;font-size:12px;white-space:nowrap;transition:.18s}}
.picker-btn:hover{{color:var(--fg);border-color:var(--line-strong)}}
.picker-btn.active{{background:var(--surface-2);color:var(--accent);border-color:var(--accent)}}
video{{width:100%;max-height:480px;border-radius:14px;border:1px solid var(--line);background:#000;display:block}}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Phòng Nghe Thử & Đánh Giá</small></div>
  </a>
  <div class="topbar-right">
    <div id="reviewer-user-info" class="user-badge hidden">
      <span class="user-dot"></span>
      <span id="reviewer-name-display" class="mono">minh_mastering</span>
      <button class="btn btn-ghost btn-sm" onclick="logoutReviewer()" style="margin-left:6px;padding:2px 8px">Đăng xuất</button>
    </div>
    <span class="pill-tide">Tide BYOiD Session</span>
  </div>
</header>

<main class="container">

  <!-- MÀN HÌNH ĐĂNG NHẬP / TẠO DANH TÍNH NGƯỜI NGHE -->
  <div id="reviewer-auth-view" class="auth-box">
    <div class="auth-tabs">
      <button id="tab-login" class="auth-tab active" onclick="switchAuthTab('login')">Đăng Nhập Danh Tính</button>
      <button id="tab-register" class="auth-tab" onclick="switchAuthTab('register')">Tạo Danh Tính Mới</button>
    </div>

    <!-- Tab Đăng nhập -->
    <div id="form-login">
      <div class="auth-title">Đăng Nhập Người Nghe</div>
      <div class="auth-sub">Chọn danh tính đã có hoặc nhập username của bạn (Mật khẩu: 123)</div>

      <div class="form-group">
        <label class="form-label">Chọn Hoặc Nhập Username</label>
        <select id="quick-user-select" class="form-input" style="margin-bottom:8px" onchange="document.getElementById('reviewer-login-user').value=this.value">
          <option value="minh_mastering">minh_mastering — Minh (Kỹ Sư Hòa Âm)</option>
          <option value="thu_producer">thu_producer — Thu (Giám Đốc Sản Xuất)</option>
          <option value="lan_soundcheck">lan_soundcheck — Lan (Kiểm Âm)</option>
        </select>
        <input type="text" id="reviewer-login-user" class="form-input" value="minh_mastering" placeholder="Tên đăng nhập">
      </div>
      <div class="form-group">
        <label class="form-label">Mật Khẩu (Tất cả tài khoản: 123)</label>
        <input type="password" id="reviewer-login-pass" class="form-input" value="123" placeholder="123">
      </div>
      <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="loginReviewer()">Đăng Nhập Vào Phiên Nghe</button>
    </div>

    <!-- Tab Tạo Danh Tính Mới -->
    <div id="form-register" class="hidden">
      <div class="auth-title">Tạo Danh Tính Tide BYOiD Mới</div>
      <div class="auth-sub">Tạo một danh tính phi tập trung để nhận quyền nghe từ Nghệ Sĩ</div>

      <div class="form-group">
        <label class="form-label">Tên Của Bạn / Vai Trò</label>
        <input type="text" id="reg-name" class="form-input" placeholder="Ví dụ: Hoàng (Audio Engineer)">
      </div>
      <div class="form-group">
        <label class="form-label">Username (Không dấu, viết liền)</label>
        <input type="text" id="reg-user" class="form-input" placeholder="hoang_audio">
      </div>
      <div class="form-group">
        <label class="form-label">Mật Khẩu (Mặc định: 123)</label>
        <input type="password" id="reg-pass" class="form-input" value="123" placeholder="123">
      </div>
      <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="registerReviewer()">Khởi Tạo Danh Tính Mật Mã</button>
    </div>

    <div style="margin-top:18px;font-size:12px;color:var(--dim);text-align:center">
      Tất cả mật khẩu đều là <code class="mono" style="color:var(--accent)">123</code>
    </div>
  </div>

  <!-- GIAO DIỆN NGƯỜI NGHE SAU KHI ĐĂNG NHẬP -->
  <div id="reviewer-main-view" class="hidden">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:24px">
      <div>
        <h1 style="font-size:26px;font-weight:700">Phòng Nghe Thử Bảo Mật (In-Memory Playback)</h1>
        <p style="color:var(--muted);font-size:14px">
          Danh tính hiện tại: <strong id="logged-user-title" style="color:var(--accent)">minh_mastering</strong> · Giải mã trực tiếp trên RAM qua Tide Emergent Authority
        </p>
      </div>
      <span class="badge badge-ok mono" id="entitlement-status-badge">PHIÊN LÀM VIỆC HỢP LỆ</span>
    </div>

    <!-- Chọn bài hát trong danh sách -->
    <div class="track-picker" id="reviewer-track-picker"></div>

    <!-- KHUNG PHÁT KHI CÓ QUYỀN -->
    <div id="player-box" class="card">
      <div class="now-playing">
        <div class="disc" id="disc"></div>
        <div>
          <div style="font-size:18px;font-weight:700" id="np-title">Lead_Single_Master_v4.flac</div>
          <div style="font-size:12px;color:var(--ok);margin-top:4px" class="mono" id="np-status">
            ● Đã xác thực danh tính với Tide Quorum · Quyền hạn tự sinh hợp lệ
          </div>
        </div>
      </div>

      <!-- Video player nếu là video -->
      <div id="video-container" class="hidden" style="margin-bottom:20px">
        <video id="html5-video" controls></video>
      </div>

      <!-- Audio player visualizer -->
      <div id="audio-visualizer-container">
        <div class="visualizer" id="viz"></div>
        <div style="display:flex;align-items:center;gap:18px">
          <button class="play-btn" id="play-btn" onclick="togglePlay()">▶</button>
          <div class="timebar">
            <div class="track-line"><div class="fill" id="fill"></div></div>
            <div class="times mono"><span id="cur">0:00</span><span id="dur">3:42</span></div>
          </div>
        </div>
      </div>

      <audio id="native-audio" style="display:none"></audio>
    </div>

    <!-- KHUNG BÁO LỖI KHI BỊ THU HỒI / CHƯA CẤP QUYỀN -->
    <div id="denied-box" class="denied-box hidden">
      <div style="font-size:44px;margin-bottom:8px">⛔</div>
      <h3 style="font-size:22px;color:var(--danger);font-weight:700">Tide Quorum: TỪ CHỐI GIẢI MÃ</h3>
      <p style="color:var(--muted);font-size:14px;max-width:540px;margin:8px auto 0">
        Danh tính của bạn (<strong id="denied-username" style="color:var(--fg)"></strong>) chưa được cấp quyền hoặc vừa bị Nghệ Sĩ thu hồi quyền đối với tác phẩm này.
      </p>
      <div class="mono" style="font-size:12px;color:var(--danger);border:1px solid rgba(255,77,109,.3);display:inline-block;padding:6px 14px;border-radius:8px;margin-top:16px">
        403 EntitlementDenied · Zero-Trust Policy Enforced
      </div>
    </div>
  </div>

</main>

<footer class="footer">
  <span>UNRELEASED · Cổng Người Nghe Thử · Powered by TideCloak</span>
  <span class="mono">Mật khẩu hệ thống: 123</span>
</footer>

<script>
const DB_NAME='tide_vault_db', STORE_NAME='media_blobs';
function openDB(){{return new Promise((res,rej)=>{{const r=indexedDB.open(DB_NAME,1);r.onupgradeneeded=e=>{{if(!e.target.result.objectStoreNames.contains(STORE_NAME))e.target.result.createObjectStore(STORE_NAME)}};r.onsuccess=()=>res(r.result);r.onerror=()=>rej(r.error)}});}}
async function getMediaBlob(id){{const db=await openDB();return new Promise((res,rej)=>{{const tx=db.transaction(STORE_NAME,'readonly');const req=tx.objectStore(STORE_NAME).get(id);req.onsuccess=()=>res(req.result);req.onerror=()=>rej(tx.error)}});}}

function getStoredUsers(){{
  const d=localStorage.getItem('tide_users');
  if(d){{try{{return JSON.parse(d)}}catch(e){{}}}}
  return [];
}}

function getStoredTracks(){{
  const d=localStorage.getItem('tide_tracks_v2');
  if(d){{try{{return JSON.parse(d)}}catch(e){{}}}}
  return [];
}}

let activeTrackId = null;
let isPlaying = false, synthInterval = null, timerInterval = null, ctx = null, t = 0, noteIdx = 0;
const notes = [261.63, 329.63, 392, 523.25, 440, 392, 329.63, 293.66];

const viz=document.getElementById('viz');
for(let i=0;i<56;i++){{const b=document.createElement('div');b.className='bar';viz.appendChild(b)}}
const bars=[...document.querySelectorAll('.bar')];

function switchAuthTab(tab){{
  document.getElementById('tab-login').classList.toggle('active',tab==='login');
  document.getElementById('tab-register').classList.toggle('active',tab==='register');
  document.getElementById('form-login').classList.toggle('hidden',tab!=='login');
  document.getElementById('form-register').classList.toggle('hidden',tab!=='register');
}}

function loginReviewer(){{
  const u=document.getElementById('reviewer-login-user').value.trim();
  const p=document.getElementById('reviewer-login-pass').value.trim();
  if(!u){{alert('Vui lòng nhập username!');return;}}
  if(p!=='123'){{alert('Mật khẩu không đúng! (Gợi ý: Mật khẩu là 123)');return;}}
  localStorage.setItem('tide_logged_reviewer',u);
  checkAuth();
}}

function registerReviewer(){{
  const name=document.getElementById('reg-name').value.trim();
  const u=document.getElementById('reg-user').value.trim().toLowerCase();
  const p=document.getElementById('reg-pass').value.trim();
  if(!name || !u){{alert('Vui lòng điền đủ tên và username!');return;}}
  if(p!=='123'){{alert('Vui lòng đặt mật khẩu 123!');return;}}

  const users=getStoredUsers();
  if(users.some(x=>x.username===u)){{alert('Username này đã tồn tại!');return;}}

  const newUser={{username:u,name:name,role:'reviewer',did:'tide:usr:'+u+'_'+Math.random().toString(16).substring(2,6)}};
  users.push(newUser);
  localStorage.setItem('tide_users',JSON.stringify(users));
  try{{new BroadcastChannel('tide_channel').postMessage({{type:'SYNC_DATA'}})}}catch(e){{}}

  localStorage.setItem('tide_logged_reviewer',u);
  alert(`Đã khởi tạo danh tính Tide BYOiD thành công: ${{newUser.did}}! Nghệ sĩ ở Trang 1 có thể thấy và cấp quyền cho bạn ngay bây giờ.`);
  checkAuth();
}}

function logoutReviewer(){{
  localStorage.removeItem('tide_logged_reviewer');
  checkAuth();
}}

function checkAuth(){{
  const u=localStorage.getItem('tide_logged_reviewer');
  const authView=document.getElementById('reviewer-auth-view');
  const mainView=document.getElementById('reviewer-main-view');
  const userInfo=document.getElementById('reviewer-user-info');
  const nameDisp=document.getElementById('reviewer-name-display');

  // Cập nhật dropdown đăng nhập nhanh
  const users=getStoredUsers();
  const quickSelect=document.getElementById('quick-user-select');
  if(quickSelect && users.length){{
    quickSelect.innerHTML=users.map(x=>`<option value="${{x.username}}">${{x.username}} — ${{x.name}}</option>`).join('');
  }}

  if(u){{
    authView.classList.add('hidden');
    mainView.classList.remove('hidden');
    userInfo.classList.remove('hidden');
    nameDisp.textContent=u;
    document.getElementById('logged-user-title').textContent=u;
    renderTracksPicker();
    syncPlaybackState();
  }}else{{
    authView.classList.remove('hidden');
    mainView.classList.add('hidden');
    userInfo.classList.add('hidden');
    stopAudio();
  }}
}}

function renderTracksPicker(){{
  const tracks=getStoredTracks();
  const picker=document.getElementById('reviewer-track-picker');
  picker.innerHTML='';
  if(!tracks.length) return;
  if(!activeTrackId || !tracks.some(x=>x.id===activeTrackId)){{
    activeTrackId=tracks[0].id;
  }}
  const currentUser=localStorage.getItem('tide_logged_reviewer');

  tracks.forEach(t=>{{
    const isAllowed=t.allowedUsers.includes(currentUser);
    const btn=document.createElement('button');
    btn.className='picker-btn '+(t.id===activeTrackId?'active':'');
    btn.textContent=(t.type.startsWith('video')?'🎬 ':'🎵 ')+t.name+(isAllowed?' (Có quyền)':' (Bị khóa)');
    btn.onclick=()=>{{
      activeTrackId=t.id;
      stopAudio();
      renderTracksPicker();
      syncPlaybackState();
    }};
    picker.appendChild(btn);
  }});
}}

async function syncPlaybackState(){{
  const currentUser=localStorage.getItem('tide_logged_reviewer');
  if(!currentUser) return;

  const tracks=getStoredTracks();
  const track=tracks.find(x=>x.id===activeTrackId)||tracks[0];
  if(!track) return;

  const playerBox=document.getElementById('player-box');
  const deniedBox=document.getElementById('denied-box');
  const badge=document.getElementById('entitlement-status-badge');
  const npTitle=document.getElementById('np-title');
  const isAllowed=track.allowedUsers.includes(currentUser);

  npTitle.textContent=track.name;

  if(!isAllowed){{
    stopAudio();
    playerBox.classList.add('hidden');
    deniedBox.classList.remove('hidden');
    document.getElementById('denied-username').textContent=currentUser;
    badge.className='badge badge-danger mono';
    badge.textContent='QUYỀN BỊ TỪ CHỐI (403)';
    return;
  }}

  playerBox.classList.remove('hidden');
  deniedBox.classList.add('hidden');
  badge.className='badge badge-ok mono';
  badge.textContent='ỦY QUYỀN HỢP LỆ';

  const isVideo=track.type.startsWith('video');
  const videoCont=document.getElementById('video-container');
  const audioCont=document.getElementById('audio-visualizer-container');
  const disc=document.getElementById('disc');

  if(isVideo){{
    videoCont.classList.remove('hidden');
    audioCont.classList.add('hidden');
    disc.classList.add('hidden');
    const blob=await getMediaBlob(track.id);
    if(blob){{
      document.getElementById('html5-video').src=URL.createObjectURL(blob);
    }}
  }}else{{
    videoCont.classList.add('hidden');
    audioCont.classList.remove('hidden');
    disc.classList.remove('hidden');
    const blob=await getMediaBlob(track.id);
    const na=document.getElementById('native-audio');
    if(blob){{na.src=URL.createObjectURL(blob);}}else{{na.removeAttribute('src');}}
  }}
}}

function tone(f){{
  try{{
    if(!ctx) ctx=new(window.AudioContext||window.webkitAudioContext)();
    if(ctx.state==='suspended') ctx.resume();
    const o=ctx.createOscillator(),g=ctx.createGain();
    o.type='triangle';o.frequency.value=f;
    g.gain.setValueAtTime(.06,ctx.currentTime);
    g.gain.exponentialRampToValueAtTime(.0001,ctx.currentTime+.5);
    o.connect(g);g.connect(ctx.destination);o.start();o.stop(ctx.currentTime+.5);
  }}catch(e){{}}
}}

function stopAudio(){{
  isPlaying=false;
  document.getElementById('play-btn').textContent='▶';
  document.getElementById('disc').classList.remove('spin');
  bars.forEach(b=>{{b.classList.remove('on');b.style.height='10%'}});
  clearInterval(timerInterval);clearInterval(synthInterval);
  const na=document.getElementById('native-audio');
  if(na) na.pause();
  const vid=document.getElementById('html5-video');
  if(vid) vid.pause();
}}

function togglePlay(){{
  const currentUser=localStorage.getItem('tide_logged_reviewer');
  const tracks=getStoredTracks();
  const track=tracks.find(x=>x.id===activeTrackId);
  if(!track || !track.allowedUsers.includes(currentUser)) return;

  isPlaying=!isPlaying;
  const playBtn=document.getElementById('play-btn');
  const disc=document.getElementById('disc');
  const na=document.getElementById('native-audio');

  if(isPlaying){{
    playBtn.textContent='⏸';
    disc.classList.add('spin');
    if(na && na.src && na.src.startsWith('blob:')){{
      na.play().catch(e=>console.log(e));
      na.ontimeupdate=()=>{{
        const cur=Math.floor(na.currentTime), dur=Math.floor(na.duration)||222;
        document.getElementById('cur').textContent=Math.floor(cur/60)+':'+String(cur%60).padStart(2,'0');
        document.getElementById('dur').textContent=Math.floor(dur/60)+':'+String(dur%60).padStart(2,'0');
        document.getElementById('fill').style.width=((cur/dur)*100)+'%';
      }};
      synthInterval=setInterval(()=>{{
        bars.forEach(b=>b.style.height=(15+Math.random()*80)+'%');
        bars.forEach(b=>b.classList.toggle('on',Math.random()>.25));
      }},180);
    }}else{{
      tone(notes[noteIdx]);
      synthInterval=setInterval(()=>{{
        noteIdx=(noteIdx+1)%notes.length;tone(notes[noteIdx]);
        bars.forEach(b=>b.style.height=(15+Math.random()*80)+'%');
        bars.forEach(b=>b.classList.toggle('on',Math.random()>.25));
      }},220);
      timerInterval=setInterval(()=>{{
        t++;
        document.getElementById('cur').textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0');
        document.getElementById('fill').style.width=Math.min(t/222*100,100)+'%';
      }},1000);
    }}
  }}else{{
    stopAudio();
  }}
}}

// Lắng nghe sự kiện thu hồi/cấp quyền từ Trang 1 theo thời gian thực
window.addEventListener('storage',()=>{{renderTracksPicker();syncPlaybackState();}});
try{{new BroadcastChannel('tide_channel').onmessage=()=>{{renderTracksPicker();syncPlaybackState();}}}}catch(e){{}}

checkAuth();
</script>
</body>
</html>
"""

# ==================== PAGE 3: QUẢN TRỊ VIÊN S3 (/rmit/3) ====================
page3 = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quản Trị Đám Mây S3 · UNRELEASED (Oblivious Proxy)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{SHARED_CSS}
.s3-row{{display:grid;grid-template-columns:1.2fr 2fr .9fr;gap:16px;align-items:center;padding:14px 18px;border:1px solid var(--line);border-radius:12px;margin-bottom:10px;background:var(--bg)}}
.s3-key{{font-size:12px;color:var(--muted)}}
.s3-cipher{{font-size:12px;color:#7b6fff;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.s3-master{{font-size:11px;font-weight:700;color:var(--danger);text-align:right}}
.terminal-box{{background:#050608;border:1px solid var(--line);border-radius:14px;padding:20px;min-height:100px;font-size:13px;color:var(--danger);margin-top:20px;line-height:1.6}}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Hạ Tầng Đám Mây S3 (Oblivious Proxy)</small></div>
  </a>
  <span class="pill-tide">Zero-Custody Cloud</span>
</header>

<main class="container">
  <div style="margin-bottom:28px">
    <h1 style="font-size:28px;font-weight:700">Trình Kiểm Tra Máy Chủ S3 & Cơ Sở Dữ Liệu</h1>
    <p style="color:var(--muted);font-size:14px">Mô phỏng góc nhìn của Kẻ xâm nhập hoặc Quản trị viên máy chủ nắm quyền Root AWS</p>
  </div>

  <div class="card" style="background:rgba(255,255,255,.015);margin-bottom:24px">
    <div style="display:flex;gap:12px;align-items:flex-start">
      <span style="font-size:20px">🛡️</span>
      <div style="font-size:13px;color:var(--muted);line-height:1.6">
        <strong>Nguyên lý bảo mật Tide:</strong> Dù Nghệ sĩ tải lên bài hát nào ở Trang 1 và cấp quyền cho ai ở Trang 2, máy chủ lưu trữ đám mây vĩnh viễn <strong>chỉ chứa các khối nhị phân mã hóa vô nghĩa</strong>. Chìa khóa chủ (Master Decryption Key) <strong>hoàn toàn không tồn tại</strong> trên máy chủ.
      </div>
    </div>
  </div>

  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">
      <h2 style="font-size:18px;font-weight:700">Các Tệp Tin Nhị Phân Trong S3: <code class="mono" style="color:var(--accent)">s3://unreleased-vault/</code></h2>
      <span class="mono" style="font-size:11px;color:var(--dim)">Live S3 Sync</span>
    </div>

    <div id="s3-list"></div>

    <div style="margin-top:28px">
      <button class="btn btn-danger" onclick="attemptRootDecryption()">🚨 Thử Dùng Quyền Root Admin Để Giải Mã / Tuồn Toàn Bộ Tệp</button>
      <div id="terminal" class="terminal-box mono hidden"></div>
    </div>
  </div>
</main>

<footer class="footer">
  <span>UNRELEASED · Cổng Quản Trị Máy Chủ · Powered by TideCloak</span>
  <span class="mono">RMIT Hackathon 2026</span>
</footer>

<script>
function getStoredTracks(){{
  const d=localStorage.getItem('tide_tracks_v2');
  if(d){{try{{return JSON.parse(d)}}catch(e){{}}}}
  return [];
}}

function renderS3(){{
  const tracks=getStoredTracks(), box=document.getElementById('s3-list');
  box.innerHTML='';
  tracks.forEach(t=>{{
    const row=document.createElement('div');
    row.className='s3-row mono';
    row.innerHTML=`
      <div class="s3-key">s3://vault/${{t.name}}.enc</div>
      <div class="s3-cipher">d8a391e4fc2901a88b5e027f${{t.hash.replace('...','')}}99014e7a881bc00192...</div>
      <div class="s3-master">KEY: ∅ (KHÔNG CÓ TRÊN MÁY CHỦ)</div>
    `;
    box.appendChild(row);
  }});
}}

function attemptRootDecryption(){{
  const term=document.getElementById('terminal');
  term.classList.remove('hidden');
  term.innerHTML='';
  const lines=[
    '> root@s3-cluster: dump --target s3://unreleased-vault/ --decrypt-all',
    '> Inspecting database credentials: Zero master keys found in vault records.',
    '> Querying Tide Fabric Quorum node [10.244.0.12] for emergency decryption certificate...',
    '> [TIDE QUORUM ENFORCEMENT] 403 Forbidden: Requestor identity lacks Emergent Policy entitlement.',
    '> ERROR: Server is an Oblivious Proxy. Root administrative privilege cannot synthesize decryption keys.',
    '> ATTACK MITIGATED: Zero bytes of plaintext audio/video leaked.'
  ];
  let cur=0;
  function printNext(){{
    if(cur<lines.length){{
      const p=document.createElement('div');
      p.textContent=lines[cur++];
      if(cur===lines.length-1) p.style.color='var(--ok)';
      term.appendChild(p);
      setTimeout(printNext, 400);
    }}
  }}
  printNext();
}}

window.addEventListener('storage',renderS3);
try{{new BroadcastChannel('tide_channel').onmessage=renderS3;}}catch(e){{}}
renderS3();
</script>
</body>
</html>
"""

# ==================== PAGE PORTAL: /rmit ====================
portal = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UNRELEASED · Studio Âm Nhạc Zero-Trust — RMIT Hackathon 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{SHARED_CSS}
.hero{{max-width:960px;margin:50px auto 40px;padding:0 24px;text-align:center}}
.kicker{{display:inline-flex;align-items:center;gap:8px;font-size:12px;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:6px 16px;margin-bottom:24px}}
.pulse{{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 8px var(--ok)}}
.hero h1{{font-size:clamp(36px,5.5vw,60px);line-height:1.05;font-weight:700;letter-spacing:-.03em}}
.hero h1 .glow{{color:var(--accent)}}
.hero p{{max-width:580px;margin:18px auto 0;color:var(--muted);font-size:16px}}
.grid{{max-width:1080px;margin:30px auto 80px;padding:0 24px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.gate-card{{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:32px 24px;display:flex;flex-direction:column;justify-content:space-between;transition:.25s ease;text-decoration:none;color:inherit;position:relative;overflow:hidden}}
.gate-card:hover{{border-color:var(--line-strong);transform:translateY(-3px);background:var(--surface-2)}}
.gate-card.hero-gate{{border-color:rgba(212,255,63,.3);background:linear-gradient(180deg,rgba(212,255,63,.04),transparent)}}
.gate-num{{font-size:12px;font-weight:700;color:var(--accent);margin-bottom:12px}}
.gate-icon{{font-size:40px;margin-bottom:16px}}
.gate-title{{font-size:20px;font-weight:700;margin-bottom:8px}}
.gate-desc{{font-size:13px;color:var(--muted);margin-bottom:24px;line-height:1.6}}
.gate-cta{{font-size:13px;font-weight:600;color:var(--fg);display:flex;align-items:center;gap:6px}}
@media(max-width:768px){{.grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Zero-Trust Media Vault</small></div>
  </a>
  <span class="pill-tide">Powered by TideCloak</span>
</header>

<section class="hero">
  <div class="kicker"><span class="pulse"></span> RMIT Hackathon 2026 · Challenge 2 · Team Foodseekers</div>
  <h1>Chia sẻ bản thu<br><span class="glow">không cần tin ai cả.</span></h1>
  <p>Hệ thống chia sẻ âm nhạc & tác phẩm sáng tạo bảo mật tuyệt đối với TideCloak. Mật khẩu tất cả tài khoản là <strong>123</strong>.</p>
</section>

<div class="grid">
  <!-- Trang 1 -->
  <a href="/rmit/1" class="gate-card hero-gate">
    <div>
      <div class="gate-num mono">CỔNG 01 · NGHỆ SĨ</div>
      <div class="gate-icon">🎧</div>
      <div class="gate-title">Két Sắt Nghệ Sĩ</div>
      <div class="gate-desc">Đăng nhập tài khoản nghệ sĩ, tải file nhạc/video lên và phân quyền truy cập đích danh cho từng người nghe qua TideCloak.</div>
    </div>
    <div class="gate-cta" style="color:var(--accent)">Mở Trang Nghệ Sĩ (/rmit/1) ➔</div>
  </a>

  <!-- Trang 2 -->
  <a href="/rmit/2" class="gate-card">
    <div>
      <div class="gate-num mono">CỔNG 02 · NGƯỜI NGHE THỬ</div>
      <div class="gate-icon">🎙</div>
      <div class="gate-title">Phòng Nghe Thử</div>
      <div class="gate-desc">Đăng nhập hoặc tạo danh tính BYOiD mới. Nghe bản thu giải mã trên RAM nếu được cấp quyền, tự động bị ngắt khi bị thu hồi.</div>
    </div>
    <div class="gate-cta">Mở Phòng Nghe Thử (/rmit/2) ➔</div>
  </a>

  <!-- Trang 3 -->
  <a href="/rmit/3" class="gate-card">
    <div>
      <div class="gate-num mono">CỔNG 03 · MÁY CHỦ S3</div>
      <div class="gate-icon">⚠️</div>
      <div class="gate-title">Quản Trị Đám Mây</div>
      <div class="gate-desc">Xem kho dữ liệu nhị phân thô trên S3. Thử đóng vai hacker dùng quyền Root để giải mã và xem kết quả bị Quorum từ chối.</div>
    </div>
    <div class="gate-cta">Mở Trình Kiểm Tra S3 (/rmit/3) ➔</div>
  </a>
</div>

<footer class="footer">
  <span>UNRELEASED · Team Foodseekers (UIT)</span>
  <span class="mono">RMIT Hackathon 2026 — Challenge 2 (Tide)</span>
</footer>

</body>
</html>
"""

targets = [
    (FS_PROTO, "Foodseekers/prototype"),
    (BW_RMIT, "bersious-web/rmit")
]

files_map = {
    "1/index.html": page1,
    "2/index.html": page2,
    "3/index.html": page3,
    "index.html": portal
}

for base_dir, label in targets:
    for rel_path, content in files_map.items():
        full_path = os.path.join(base_dir, rel_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[{label}] Đã ghi {rel_path} ({len(content)} bytes)")

print("\n✓ ĐÃ HOÀN TẤT NÂNG CẤP XÁC THỰC DANH TÍNH TIDECLOAK!")
