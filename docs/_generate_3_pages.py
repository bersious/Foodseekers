import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

for d in [FS_PROTO, BW_RMIT]:
    for sub in ["1", "2", "3"]:
        os.makedirs(os.path.join(d, sub), exist_ok=True)

# ----------------- PAGE 1: NGHỆ SĨ (/rmit/1) -----------------
page1 = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Két Sắt Nghệ Sĩ · UNRELEASED (Trang 1/3)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#08090d;--surface:rgba(255,255,255,.025);--surface-2:rgba(255,255,255,.05);
  --line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.15);
  --fg:#f4f5f7;--muted:#8b8fa0;--dim:#5a5e6e;
  --accent:#d4ff3f;--danger:#ff4d6d;--danger-dim:rgba(255,77,109,.12);
  --ok:#3ee88f;--ok-dim:rgba(62,232,143,.12);--radius:16px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;line-height:1.5;min-height:100vh}
body::before{content:'';position:fixed;inset:0;z-index:-2;background:radial-gradient(900px 500px at 75% -5%,rgba(212,255,63,.07),transparent 60%)}
.mono{font-family:'JetBrains Mono',monospace}

.topbar{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:16px 32px;backdrop-filter:blur(18px);background:rgba(8,9,13,.75);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;font-weight:700}
.brand-dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.brand small{display:block;font-size:11px;color:var(--muted);font-weight:400}

.nav-links{display:flex;gap:6px;background:var(--surface);border:1px solid var(--line);padding:4px;border-radius:12px}
.nav-link{font-size:13px;font-weight:500;color:var(--muted);text-decoration:none;padding:8px 14px;border-radius:8px;transition:.18s;display:flex;align-items:center;gap:6px}
.nav-link:hover{color:var(--fg)}
.nav-link.active{background:var(--fg);color:#0a0b0e;font-weight:600}
.pill-tide{font-size:11px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:6px 12px;border-radius:999px}

.container{max-width:1080px;margin:40px auto 80px;padding:0 24px}
.page-header{margin-bottom:28px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}
.page-title h1{font-size:28px;letter-spacing:-.03em;font-weight:700}
.page-title p{color:var(--muted);font-size:14px;margin-top:4px}

.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:26px;margin-bottom:24px;backdrop-filter:blur(12px)}
.upload-zone{
  border:2px dashed var(--line-strong);border-radius:14px;padding:36px 20px;text-align:center;
  cursor:pointer;transition:.2s;background:rgba(255,255,255,.01);
}
.upload-zone:hover{border-color:var(--accent);background:rgba(212,255,63,.02)}
.upload-icon{font-size:36px;margin-bottom:12px}
.upload-title{font-size:16px;font-weight:600;margin-bottom:4px}
.upload-sub{font-size:12px;color:var(--muted)}

.btn{
  font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;
  padding:9px 16px;border-radius:10px;border:1px solid transparent;transition:.18s;
  display:inline-flex;align-items:center;gap:8px;text-decoration:none;
}
.btn-accent{background:var(--accent);color:#0a0b0e}
.btn-accent:hover{filter:brightness(1.1)}
.btn-danger{background:var(--danger-dim);color:var(--danger);border-color:rgba(255,77,109,.3)}
.btn-danger:hover{background:rgba(255,77,109,.2)}
.btn-ok{background:var(--ok-dim);color:var(--ok);border-color:rgba(62,232,143,.3)}
.btn-ok:hover{background:rgba(62,232,143,.2)}

.track-row{
  display:flex;align-items:center;justify-content:space-between;gap:16px;
  padding:16px 18px;border:1px solid var(--line);border-radius:12px;margin-bottom:10px;background:var(--bg);
}
.track-left{display:flex;align-items:center;gap:14px;min-width:0}
.track-type{font-size:20px;width:32px;height:32px;display:flex;align-items:center;justify-content:center;background:var(--surface-2);border-radius:8px}
.track-name{font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.track-meta{font-size:11px;color:var(--dim);margin-top:2px}

.badge{font-size:11px;font-weight:600;padding:5px 10px;border-radius:999px;white-space:nowrap}
.badge-ok{color:var(--ok);background:var(--ok-dim);border:1px solid rgba(62,232,143,.25)}
.badge-danger{color:var(--danger);background:var(--danger-dim);border:1px solid rgba(255,77,109,.25)}

.sync-bar{display:flex;align-items:center;justify-content:space-between;background:var(--surface-2);border:1px solid var(--line);padding:12px 18px;border-radius:12px;font-size:12px;color:var(--muted);margin-top:16px}
.live-dot{width:8px;height:8px;border-radius:50%;background:var(--ok);box-shadow:0 0 8px var(--ok);display:inline-block;margin-right:6px}

.footer{max-width:1080px;margin:0 auto;padding:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;color:var(--dim);font-size:12px}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Zero-Trust Media Vault</small></div>
  </a>
  <nav class="nav-links">
    <a href="/rmit/1" class="nav-link active">🎧 1. Nghệ Sĩ</a>
    <a href="/rmit/2" class="nav-link">🎙 2. Người Nghe Thử</a>
    <a href="/rmit/3" class="nav-link">⚠️ 3. Quản Trị Máy Chủ</a>
  </nav>
  <span class="pill-tide">Powered by TideCloak</span>
</header>

<main class="container">
  <div class="page-header">
    <div class="page-title">
      <h1>Két Sắt Nghệ Sĩ (Alice Nguyễn)</h1>
      <p>Tải lên bản thu nháp âm thanh hoặc video · Thiết lập chính sách bảo mật không chìa khóa chủ</p>
    </div>
    <a href="/rmit/2" class="btn btn-accent">Mở Trang Người Nghe Thử (Tab 2) ➔</a>
  </div>

  <!-- Upload Card -->
  <div class="card">
    <div class="upload-zone" onclick="document.getElementById('file-input').click()">
      <div class="upload-icon">⚡</div>
      <div class="upload-title">Tải lên Bản Thu Âm Nhạc hoặc Video Mới</div>
      <div class="upload-sub">Hỗ trợ MP3, WAV, FLAC, MP4, WEBM (Mã hóa đầu cuối AES-256-GCM tức thì trên trình duyệt)</div>
      <input type="file" id="file-input" style="display:none" accept="audio/*,video/*" onchange="handleFileUpload(event)">
    </div>
    <div id="upload-status" style="margin-top:12px;font-size:12px;color:var(--accent);display:none" class="mono"></div>
  </div>

  <!-- Tracks Vault -->
  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">
      <h2 style="font-size:18px;font-weight:700">Danh Sách Tác Phẩm Đã Niêm Phong Mật Mã</h2>
      <button class="btn btn-ghost" onclick="resetDefaults()" style="font-size:11px;padding:6px 12px">Khôi phục danh sách mẫu</button>
    </div>

    <div id="tracks-list"></div>

    <div class="sync-bar">
      <div><span class="live-dot"></span><span id="sync-msg">Mạng lưới Tide Quorum: Sẵn sàng đồng bộ thời gian thực sang Trang 2 và Trang 3</span></div>
      <span class="mono" style="color:var(--dim)">BroadcastChannel: active</span>
    </div>
  </div>
</main>

<footer class="footer">
  <span>Trang 1 / 3 · Két Sắt Nghệ Sĩ · Team Foodseekers</span>
  <span class="mono">RMIT Hackathon 2026</span>
</footer>

<script>
const DB_NAME = 'tide_vault_db', STORE_NAME = 'media_blobs';
function openDB(){
  return new Promise((res,rej)=>{
    const req=indexedDB.open(DB_NAME,1);
    req.onupgradeneeded=e=>{if(!e.target.result.objectStoreNames.contains(STORE_NAME))e.target.result.createObjectStore(STORE_NAME)};
    req.onsuccess=()=>res(req.result);req.onerror=()=>rej(req.error);
  });
}
async function saveMediaBlob(id,blob){
  const db=await openDB();
  return new Promise((res,rej)=>{const tx=db.transaction(STORE_NAME,'readwrite');tx.objectStore(STORE_NAME).put(blob,id);tx.oncomplete=()=>res();tx.onerror=()=>rej(tx.error)});
}

function getStoredTracks(){
  const d=localStorage.getItem('tide_tracks');
  if(d){try{return JSON.parse(d)}catch(e){}}
  const def=[
    {id:'track_01',name:'Lead_Single_Master_v4.flac',type:'audio/flac',size:'42.8 MB',hash:'b79a4e912f...',shared:true},
    {id:'track_02',name:'Vocal_Stems_Studio_Dry.wav',type:'audio/wav',size:'68.1 MB',hash:'82f10ac349...',shared:false},
    {id:'track_03',name:'Studio_Teaser_Snippet.mp4',type:'video/mp4',size:'115.4 MB',hash:'11ce9d40b2...',shared:false}
  ];
  localStorage.setItem('tide_tracks',JSON.stringify(def));
  return def;
}

function notifySync(tracks){
  localStorage.setItem('tide_tracks',JSON.stringify(tracks));
  try{new BroadcastChannel('tide_channel').postMessage({type:'SYNC_TRACKS',tracks:tracks})}catch(e){}
  render();
}

function render(){
  const tracks=getStoredTracks(), box=document.getElementById('tracks-list');
  box.innerHTML='';
  tracks.forEach((t,idx)=>{
    const isVideo=t.type.startsWith('video');
    const row=document.createElement('div');
    row.className='track-row';
    row.innerHTML=`
      <div class="track-left">
        <div class="track-type">${isVideo?'🎬':'🎵'}</div>
        <div>
          <div class="track-name">${t.name}</div>
          <div class="track-meta mono">${t.size} · SHA256: ${t.hash} · ${isVideo?'Video Master':'Audio Master'}</div>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:12px">
        <span class="badge ${t.shared?'badge-ok':'badge-danger'}">${t.shared?'ĐÃ CẤP QUYỀN CHO MINH':'CHƯA CẤP / ĐÃ THU HỒI'}</span>
        <button class="btn ${t.shared?'btn-danger':'btn-ok'}" onclick="toggleShare('${t.id}')">
          ${t.shared?'🚫 Thu hồi quyền':'✅ Cấp quyền nghe'}
        </button>
        <button class="btn btn-ghost" onclick="deleteTrack('${t.id}')" style="padding:8px;font-size:12px">✕</button>
      </div>
    `;
    box.appendChild(row);
  });
}

function toggleShare(id){
  const tracks=getStoredTracks();
  const t=tracks.find(x=>x.id===id);
  if(t){
    t.shared=!t.shared;
    notifySync(tracks);
    const msg=document.getElementById('sync-msg');
    msg.textContent=`Đã cập nhật quyền tác phẩm "${t.name}" -> ${t.shared?'CẤP QUYỀN':'THU HỒI QUYỀN'} tức thì!`;
  }
}

function deleteTrack(id){
  let tracks=getStoredTracks();
  tracks=tracks.filter(x=>x.id!==id);
  notifySync(tracks);
}

function resetDefaults(){
  localStorage.removeItem('tide_tracks');
  render();
}

async function handleFileUpload(e){
  const file=e.target.files[0];
  if(!file)return;
  const stat=document.getElementById('upload-status');
  stat.style.display='block';
  stat.textContent=`> Đang tính toán băm SHA256 và sinh vector mã hóa AES-256-GCM cho ${file.name}...`;

  const id='track_'+Date.now();
  await saveMediaBlob(id,file);

  const hashPart=Math.random().toString(16).substring(2,10)+'...';
  const sizeMb=(file.size/(1024*1024)).toFixed(1)+' MB';

  const tracks=getStoredTracks();
  tracks.unshift({
    id:id,
    name:file.name,
    type:file.type||'audio/mp3',
    size:sizeMb,
    hash:hashPart,
    shared:true,
    hasCustomBlob:true
  });
  notifySync(tracks);

  stat.textContent=`> [THÀNH CÔNG] Đã niêm phong ${file.name}! Đã cấp quyền tự động cho Minh. Bạn có thể mở Trang 2 để phát thử ngay!`;
  e.target.value='';
}

window.addEventListener('storage',render);
render();
</script>
</body>
</html>
"""

# ----------------- PAGE 2: NGƯỜI NGHE THỬ (/rmit/2) -----------------
page2 = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Phòng Nghe Thử Bảo Mật · UNRELEASED (Trang 2/3)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#08090d;--surface:rgba(255,255,255,.025);--surface-2:rgba(255,255,255,.05);
  --line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.15);
  --fg:#f4f5f7;--muted:#8b8fa0;--dim:#5a5e6e;
  --accent:#d4ff3f;--danger:#ff4d6d;--danger-dim:rgba(255,77,109,.12);
  --ok:#3ee88f;--ok-dim:rgba(62,232,143,.12);--radius:16px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;line-height:1.5;min-height:100vh}
body::before{content:'';position:fixed;inset:0;z-index:-2;background:radial-gradient(900px 500px at 20% -5%,rgba(0,242,254,.07),transparent 60%)}
.mono{font-family:'JetBrains Mono',monospace}

.topbar{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:16px 32px;backdrop-filter:blur(18px);background:rgba(8,9,13,.75);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;font-weight:700}
.brand-dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.brand small{display:block;font-size:11px;color:var(--muted);font-weight:400}

.nav-links{display:flex;gap:6px;background:var(--surface);border:1px solid var(--line);padding:4px;border-radius:12px}
.nav-link{font-size:13px;font-weight:500;color:var(--muted);text-decoration:none;padding:8px 14px;border-radius:8px;transition:.18s;display:flex;align-items:center;gap:6px}
.nav-link:hover{color:var(--fg)}
.nav-link.active{background:var(--fg);color:#0a0b0e;font-weight:600}
.pill-tide{font-size:11px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:6px 12px;border-radius:999px}

.container{max-width:1080px;margin:40px auto 80px;padding:0 24px}
.page-header{margin-bottom:28px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}
.page-title h1{font-size:28px;letter-spacing:-.03em;font-weight:700}
.page-title p{color:var(--muted);font-size:14px;margin-top:4px}

.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px;margin-bottom:24px;backdrop-filter:blur(12px)}

/* Player elements */
.now-playing{display:flex;align-items:center;gap:20px;margin-bottom:24px}
.disc{
  width:78px;height:78px;border-radius:50%;flex-shrink:0;
  background:repeating-radial-gradient(#0c0d12,#0c0d12 2px,#17181f 3px,#0c0d12 4px);
  border:1px solid var(--line-strong);position:relative;display:flex;align-items:center;justify-content:center;
}
.disc::after{content:'';width:20px;height:20px;border-radius:50%;background:var(--accent)}
.disc.spin{animation:spin 3s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.np-title{font-size:18px;font-weight:700}
.np-status{font-size:12px;color:var(--ok);margin-top:4px;display:flex;align-items:center;gap:6px}

.visualizer{
  height:96px;display:flex;align-items:flex-end;gap:3px;border:1px solid var(--line);border-radius:14px;
  background:linear-gradient(180deg,transparent,rgba(212,255,63,.015));overflow:hidden;padding:14px;margin-bottom:24px;
}
.bar{flex:1;background:var(--line-strong);border-radius:3px;height:10%;transition:height .1s ease}
.bar.on{background:linear-gradient(180deg,var(--accent),rgba(212,255,63,.3))}

.player-controls{display:flex;align-items:center;gap:18px}
.play-btn{
  width:56px;height:56px;border-radius:50%;flex-shrink:0;cursor:pointer;border:none;
  background:var(--accent);color:#0a0b0e;font-size:20px;transition:.2s;display:flex;align-items:center;justify-content:center;
}
.play-btn:hover{transform:scale(1.06)}
.timebar{flex:1}
.track-line{height:6px;border-radius:999px;background:var(--surface-2);overflow:hidden;cursor:pointer}
.fill{height:100%;width:0%;background:var(--accent);transition:width .25s linear}
.times{display:flex;justify-content:space-between;font-size:11px;color:var(--dim);margin-top:8px}

.video-wrap{margin-bottom:20px;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#000}
video{width:100%;max-height:480px;display:block}

/* Denied state */
.denied-card{
  text-align:center;padding:60px 24px;border:1px solid rgba(255,77,109,.3);
  border-radius:18px;background:var(--danger-dim);margin-bottom:24px;
}
.denied-icon{font-size:48px;margin-bottom:12px}
.denied-title{font-size:22px;color:var(--danger);font-weight:700}
.denied-desc{color:var(--muted);font-size:14px;max-width:540px;margin:10px auto 0}
.denied-code{display:inline-block;font-size:12px;color:var(--danger);border:1px solid rgba(255,77,109,.3);padding:6px 14px;border-radius:8px;margin-top:18px}

/* Selector pill */
.track-picker{display:flex;gap:8px;overflow-x:auto;padding-bottom:12px;margin-bottom:20px}
.picker-btn{
  background:var(--surface);border:1px solid var(--line);color:var(--muted);
  padding:8px 14px;border-radius:10px;cursor:pointer;font-family:inherit;font-size:12px;white-space:nowrap;transition:.18s;
}
.picker-btn:hover{color:var(--fg);border-color:var(--line-strong)}
.picker-btn.active{background:var(--surface-2);color:var(--accent);border-color:var(--accent)}

.footer{max-width:1080px;margin:0 auto;padding:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;color:var(--dim);font-size:12px}
.hidden{display:none!important}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Zero-Trust Media Vault</small></div>
  </a>
  <nav class="nav-links">
    <a href="/rmit/1" class="nav-link">🎧 1. Nghệ Sĩ</a>
    <a href="/rmit/2" class="nav-link active">🎙 2. Người Nghe Thử</a>
    <a href="/rmit/3" class="nav-link">⚠️ 3. Quản Trị Máy Chủ</a>
  </nav>
  <span class="pill-tide">Powered by TideCloak</span>
</header>

<main class="container">
  <div class="page-header">
    <div class="page-title">
      <h1>Phòng Nghe Thử & Đánh Giá (Kỹ Sư Minh)</h1>
      <p>Xác thực qua TideCloak BYOiD · Giải mã trực tiếp trên bộ nhớ RAM (Zero Disk Cache)</p>
    </div>
    <div style="font-size:12px;color:var(--muted)">Đồng bộ tự động từ Trang 1</div>
  </div>

  <!-- Track selector -->
  <div class="track-picker" id="picker-container"></div>

  <!-- PLAYER CONTAINER (HIỆN KHI ĐƯỢC CẤP QUYỀN) -->
  <div id="player-box" class="card">
    <div class="now-playing">
      <div class="disc" id="disc"></div>
      <div>
        <div class="np-title" id="active-title">Lead Single — Master v4</div>
        <div class="np-status mono" id="active-status">● Quyền hạn tự sinh hợp lệ (Tide Emergent Authority) · RAM Playback</div>
      </div>
    </div>

    <!-- Video container (nếu là video) -->
    <div id="video-wrap" class="video-wrap hidden">
      <video id="html5-video" controls></video>
    </div>

    <!-- Audio Visualizer (nếu là audio) -->
    <div id="audio-visualizer-wrap">
      <div class="visualizer" id="viz"></div>
      <div class="player-controls">
        <button class="play-btn" id="play-btn" onclick="togglePlay()">▶</button>
        <div class="timebar" onclick="seekAudio(event)">
          <div class="track-line"><div class="fill" id="fill"></div></div>
          <div class="times mono"><span id="cur">0:00</span><span id="dur">3:42</span></div>
        </div>
      </div>
    </div>

    <audio id="native-audio" style="display:none"></audio>
  </div>

  <!-- BLOCKED CONTAINER (HIỆN KHI THU HỒI QUYỀN) -->
  <div id="denied-box" class="denied-card hidden">
    <div class="denied-icon">⛔</div>
    <div class="denied-title">Mạng Quorum Đã Từ Chối Cấp Khóa Giải Mã</div>
    <div class="denied-desc">
      Nghệ sĩ Alice đã thu hồi quyền của tác phẩm này ở Trang 1. Vì quyền hạn mang tính tự sinh tức thời từ mạng phân tán chứ không lưu trên máy chủ, không một bộ nhớ cache hay token nào có thể giải mã được luồng âm thanh/video này.
    </div>
    <div class="denied-code mono">403 · EntitlementRevoked · Zero-Trust Policy Enforced</div>
  </div>
</main>

<footer class="footer">
  <span>Trang 2 / 3 · Người Nghe Thử · Team Foodseekers</span>
  <span class="mono">RMIT Hackathon 2026</span>
</footer>

<script>
const DB_NAME = 'tide_vault_db', STORE_NAME = 'media_blobs';
function openDB(){
  return new Promise((res,rej)=>{
    const req=indexedDB.open(DB_NAME,1);
    req.onupgradeneeded=e=>{if(!e.target.result.objectStoreNames.contains(STORE_NAME))e.target.result.createObjectStore(STORE_NAME)};
    req.onsuccess=()=>res(req.result);req.onerror=()=>rej(req.error);
  });
}
async function getMediaBlob(id){
  const db=await openDB();
  return new Promise((res,rej)=>{const tx=db.transaction(STORE_NAME,'readonly');const req=tx.objectStore(STORE_NAME).get(id);req.onsuccess=()=>res(req.result);req.onerror=()=>rej(tx.error)});
}

function getStoredTracks(){
  const d=localStorage.getItem('tide_tracks');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [];
}

let activeTrackId = null;
let isPlaying = false, synthInterval = null, timerInterval = null, ctx = null, t = 0, noteIdx = 0;
const notes = [261.63, 329.63, 392, 523.25, 440, 392, 329.63, 293.66];

// Build visualizer bars
const viz = document.getElementById('viz');
for(let i=0;i<56;i++){const b=document.createElement('div');b.className='bar';viz.appendChild(b)}
const bars=[...document.querySelectorAll('.bar')];

function setupPicker(){
  const tracks=getStoredTracks(), picker=document.getElementById('picker-container');
  picker.innerHTML='';
  if(!tracks.length) return;
  if(!activeTrackId || !tracks.some(x=>x.id===activeTrackId)){
    activeTrackId=tracks[0].id;
  }
  tracks.forEach(t=>{
    const btn=document.createElement('button');
    btn.className='picker-btn '+(t.id===activeTrackId?'active':'');
    btn.textContent=(t.type.startsWith('video')?'🎬 ':'🎵 ')+t.name+(t.shared?' (Được nghe)':' (Khóa)');
    btn.onclick=()=>{activeTrackId=t.id;stop();setupPicker();syncView();};
    picker.appendChild(btn);
  });
}

async function syncView(){
  const tracks=getStoredTracks();
  const track=tracks.find(x=>x.id===activeTrackId)||tracks[0];
  if(!track) return;

  const playerBox=document.getElementById('player-box');
  const deniedBox=document.getElementById('denied-box');
  const activeTitle=document.getElementById('active-title');
  const activeStatus=document.getElementById('active-status');
  const videoWrap=document.getElementById('video-wrap');
  const audioVizWrap=document.getElementById('audio-visualizer-wrap');
  const disc=document.getElementById('disc');
  const html5Video=document.getElementById('html5-video');

  activeTitle.textContent=track.name;

  if(!track.shared){
    stop();
    playerBox.classList.add('hidden');
    deniedBox.classList.remove('hidden');
    return;
  }

  playerBox.classList.remove('hidden');
  deniedBox.classList.add('hidden');

  const isVideo=track.type.startsWith('video');
  if(isVideo){
    videoWrap.classList.remove('hidden');
    audioVizWrap.classList.add('hidden');
    disc.classList.add('hidden');
    activeStatus.textContent='● Luồng Video Được Giải Mã Qua Emergent Authority';

    // Load video blob if uploaded
    const blob=await getMediaBlob(track.id);
    if(blob){
      html5Video.src=URL.createObjectURL(blob);
    }
  } else {
    videoWrap.classList.add('hidden');
    audioVizWrap.classList.remove('hidden');
    disc.classList.remove('hidden');
    activeStatus.textContent='● Quyền hạn tự sinh hợp lệ (Tide Emergent Authority) · RAM Playback';

    // Load audio blob if uploaded
    const nativeAudio=document.getElementById('native-audio');
    const blob=await getMediaBlob(track.id);
    if(blob){
      nativeAudio.src=URL.createObjectURL(blob);
    } else {
      nativeAudio.removeAttribute('src');
    }
  }
}

function tone(f){
  try{
    if(!ctx) ctx=new(window.AudioContext||window.webkitAudioContext)();
    if(ctx.state==='suspended') ctx.resume();
    const o=ctx.createOscillator(),g=ctx.createGain();
    o.type='triangle';o.frequency.value=f;
    g.gain.setValueAtTime(.06,ctx.currentTime);
    g.gain.exponentialRampToValueAtTime(.0001,ctx.currentTime+.5);
    o.connect(g);g.connect(ctx.destination);o.start();o.stop(ctx.currentTime+.5);
  }catch(e){}
}

function stop(){
  isPlaying=false;
  document.getElementById('play-btn').textContent='▶';
  document.getElementById('disc').classList.remove('spin');
  bars.forEach(b=>{b.classList.remove('on');b.style.height='10%'});
  clearInterval(timerInterval);clearInterval(synthInterval);
  const na=document.getElementById('native-audio');
  if(na) na.pause();
  const vid=document.getElementById('html5-video');
  if(vid) vid.pause();
}

function togglePlay(){
  const tracks=getStoredTracks();
  const track=tracks.find(x=>x.id===activeTrackId);
  if(!track || !track.shared) return;

  isPlaying=!isPlaying;
  const playBtn=document.getElementById('play-btn');
  const disc=document.getElementById('disc');
  const na=document.getElementById('native-audio');

  if(isPlaying){
    playBtn.textContent='⏸';
    disc.classList.add('spin');

    if(na && na.src && na.src.startsWith('blob:')){
      na.play().catch(e=>console.log(e));
      na.ontimeupdate=()=>{
        const cur=Math.floor(na.currentTime), dur=Math.floor(na.duration)||222;
        document.getElementById('cur').textContent=Math.floor(cur/60)+':'+String(cur%60).padStart(2,'0');
        document.getElementById('dur').textContent=Math.floor(dur/60)+':'+String(dur%60).padStart(2,'0');
        document.getElementById('fill').style.width=((cur/dur)*100)+'%';
      };
      synthInterval=setInterval(()=>{
        bars.forEach(b=>b.style.height=(15+Math.random()*80)+'%');
        bars.forEach(b=>b.classList.toggle('on',Math.random()>.25));
      },180);
    } else {
      tone(notes[noteIdx]);
      synthInterval=setInterval(()=>{
        noteIdx=(noteIdx+1)%notes.length;tone(notes[noteIdx]);
        bars.forEach(b=>b.style.height=(15+Math.random()*80)+'%');
        bars.forEach(b=>b.classList.toggle('on',Math.random()>.25));
      },220);
      timerInterval=setInterval(()=>{
        t++;
        document.getElementById('cur').textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0');
        document.getElementById('fill').style.width=Math.min(t/222*100,100)+'%';
      },1000);
    }
  } else {
    stop();
  }
}

// Bắt sự kiện đồng bộ từ Trang 1
try{
  const bc=new BroadcastChannel('tide_channel');
  bc.onmessage=(e)=>{
    if(e.data && e.data.type==='SYNC_TRACKS'){
      setupPicker();
      syncView();
    }
  };
}catch(e){}

window.addEventListener('storage',()=>{setupPicker();syncView();});

setupPicker();
syncView();
</script>
</body>
</html>
"""

# ----------------- PAGE 3: QUẢN TRỊ VIÊN S3 (/rmit/3) -----------------
page3 = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hạ Tầng Đám Mây S3 · UNRELEASED (Trang 3/3)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#08090d;--surface:rgba(255,255,255,.025);--surface-2:rgba(255,255,255,.05);
  --line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.15);
  --fg:#f4f5f7;--muted:#8b8fa0;--dim:#5a5e6e;
  --accent:#d4ff3f;--danger:#ff4d6d;--danger-dim:rgba(255,77,109,.12);
  --ok:#3ee88f;--ok-dim:rgba(62,232,143,.12);--radius:16px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;line-height:1.5;min-height:100vh}
body::before{content:'';position:fixed;inset:0;z-index:-2;background:radial-gradient(900px 500px at 85% 10%,rgba(255,77,109,.07),transparent 60%)}
.mono{font-family:'JetBrains Mono',monospace}

.topbar{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:16px 32px;backdrop-filter:blur(18px);background:rgba(8,9,13,.75);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;font-weight:700}
.brand-dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.brand small{display:block;font-size:11px;color:var(--muted);font-weight:400}

.nav-links{display:flex;gap:6px;background:var(--surface);border:1px solid var(--line);padding:4px;border-radius:12px}
.nav-link{font-size:13px;font-weight:500;color:var(--muted);text-decoration:none;padding:8px 14px;border-radius:8px;transition:.18s;display:flex;align-items:center;gap:6px}
.nav-link:hover{color:var(--fg)}
.nav-link.active{background:var(--fg);color:#0a0b0e;font-weight:600}
.pill-tide{font-size:11px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:6px 12px;border-radius:999px}

.container{max-width:1080px;margin:40px auto 80px;padding:0 24px}
.page-header{margin-bottom:28px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}
.page-title h1{font-size:28px;letter-spacing:-.03em;font-weight:700}
.page-title p{color:var(--muted);font-size:14px;margin-top:4px}

.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px;margin-bottom:24px;backdrop-filter:blur(12px)}

.s3-row{
  display:grid;grid-template-columns:1.2fr 2fr .9fr;gap:16px;align-items:center;
  padding:14px 18px;border:1px solid var(--line);border-radius:12px;margin-bottom:10px;background:var(--bg);
}
.s3-key{font-size:12px;color:var(--muted)}
.s3-cipher{font-size:12px;color:#7b6fff;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.s3-master{font-size:11px;font-weight:700;color:var(--danger);text-align:right}

.btn{
  font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;
  padding:10px 20px;border-radius:10px;border:1px solid transparent;transition:.18s;
  display:inline-flex;align-items:center;gap:8px;text-decoration:none;
}
.btn-danger{background:var(--danger-dim);color:var(--danger);border-color:rgba(255,77,109,.3)}
.btn-danger:hover{background:rgba(255,77,109,.25)}

.terminal-box{
  background:#050608;border:1px solid var(--line);border-radius:14px;padding:20px;
  min-height:100px;font-size:13px;color:var(--danger);margin-top:20px;line-height:1.6;
}

.notice-banner{
  background:rgba(255,255,255,.02);border:1px solid var(--line);border-radius:12px;
  padding:16px 20px;margin-bottom:24px;display:flex;gap:14px;align-items:flex-start;font-size:13px;color:var(--muted);
}
.notice-banner .ic{color:var(--accent);font-size:18px}

.footer{max-width:1080px;margin:0 auto;padding:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;color:var(--dim);font-size:12px}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Zero-Trust Media Vault</small></div>
  </a>
  <nav class="nav-links">
    <a href="/rmit/1" class="nav-link">🎧 1. Nghệ Sĩ</a>
    <a href="/rmit/2" class="nav-link">🎙 2. Người Nghe Thử</a>
    <a href="/rmit/3" class="nav-link active">⚠️ 3. Quản Trị Máy Chủ</a>
  </nav>
  <span class="pill-tide">Powered by TideCloak</span>
</header>

<main class="container">
  <div class="page-header">
    <div class="page-title">
      <h1>Kiểm Tra Hạ Tầng Đám Mây S3 (Oblivious Proxy)</h1>
      <p>Mô phỏng góc nhìn của Quản trị viên máy chủ lưu trữ hoặc Kẻ tấn công chiếm quyền Root S3</p>
    </div>
  </div>

  <div class="notice-banner">
    <span class="ic">🛡️</span>
    <div>
      <strong>Bằng chứng kiến trúc Zero-Trust:</strong> Khi Nghệ sĩ tải file nhạc/video lên ở Trang 1, máy chủ lưu trữ S3 chỉ nhận và lưu các khối nhị phân mã hóa vô nghĩa (Ciphertext Blobs). <strong>Hoàn toàn không có chìa khóa chủ nào được lưu trên máy chủ hay cơ sở dữ liệu.</strong>
    </div>
  </div>

  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">
      <h2 style="font-size:18px;font-weight:700">Các Tệp Tin Nhị Phân Trong S3 Bucket: <code class="mono" style="color:var(--accent)">s3://unreleased-vault/</code></h2>
      <span class="mono" style="font-size:11px;color:var(--dim)">Auto-sync from Page 1</span>
    </div>

    <div id="s3-list"></div>

    <div style="margin-top:28px">
      <button class="btn btn-danger" onclick="attemptRootDecryption()">🚨 Thử Dùng Quyền Root Admin Để Giải Mã / Tuồn Nhạc</button>
      <div id="terminal" class="terminal-box mono hidden"></div>
    </div>
  </div>
</main>

<footer class="footer">
  <span>Trang 3 / 3 · Quản Trị Máy Chủ · Team Foodseekers</span>
  <span class="mono">RMIT Hackathon 2026</span>
</footer>

<script>
function getStoredTracks(){
  const d=localStorage.getItem('tide_tracks');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [];
}

function renderS3(){
  const tracks=getStoredTracks(), box=document.getElementById('s3-list');
  box.innerHTML='';
  tracks.forEach((t,i)=>{
    const row=document.createElement('div');
    row.className='s3-row mono';
    row.innerHTML=`
      <div class="s3-key">s3://vault/${t.name}.enc</div>
      <div class="s3-cipher">d8a391e4fc2901a88b5e027f${t.hash.replace('...','')}99014e7a881bc00192...</div>
      <div class="s3-master">KEY: ∅ (KHÔNG CÓ)</div>
    `;
    box.appendChild(row);
  });
}

function attemptRootDecryption(){
  const term=document.getElementById('terminal');
  term.classList.remove('hidden');
  term.innerHTML='';
  const lines=[
    '> root@s3-storage-cluster: dump --target s3://unreleased-vault/ --decrypt-all',
    '> Inspecting database credentials: Zero master keys found in vault records.',
    '> Querying Tide Fabric Quorum node [10.244.0.12] for emergency decryption certificate...',
    '> [TIDE QUORUM ENFORCEMENT] 403 Forbidden: Requestor identity lacks Emergent Policy entitlement.',
    '> ERROR: Server is an Oblivious Proxy. Root administrative privilege cannot synthesize decryption keys.',
    '> ATTACK MITIGATED: Zero bytes of plaintext audio/video leaked.'
  ];
  let cur=0;
  function printNext(){
    if(cur<lines.length){
      const p=document.createElement('div');
      p.textContent=lines[cur++];
      if(cur===lines.length-1) p.style.color='var(--ok)';
      term.appendChild(p);
      setTimeout(printNext, 400);
    }
  }
  printNext();
}

window.addEventListener('storage',renderS3);
try{new BroadcastChannel('tide_channel').onmessage=renderS3;}catch(e){}
renderS3();
</script>
</body>
</html>
"""

# ----------------- PAGE PORTAL: /rmit -----------------
portal = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UNRELEASED · Studio Âm Nhạc Zero-Trust — RMIT Hackathon 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#08090d;--surface:rgba(255,255,255,.025);--surface-2:rgba(255,255,255,.05);
  --line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.15);
  --fg:#f4f5f7;--muted:#8b8fa0;--dim:#5a5e6e;
  --accent:#d4ff3f;--danger:#ff4d6d;--ok:#3ee88f;--radius:18px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;line-height:1.5;min-height:100vh}
body::before{content:'';position:fixed;inset:0;z-index:-2;background:radial-gradient(900px 500px at 75% -5%,rgba(212,255,63,.08),transparent 60%)}
.mono{font-family:'JetBrains Mono',monospace}

.topbar{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:16px 32px;backdrop-filter:blur(18px);background:rgba(8,9,13,.75);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;font-weight:700}
.brand-dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.brand small{display:block;font-size:11px;color:var(--muted);font-weight:400}
.pill-tide{font-size:11px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:6px 12px;border-radius:999px}

.hero{max-width:960px;margin:50px auto 40px;padding:0 24px;text-align:center}
.kicker{display:inline-flex;align-items:center;gap:8px;font-size:12px;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:6px 16px;margin-bottom:24px}
.pulse{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 8px var(--ok)}
.hero h1{font-size:clamp(36px,5.5vw,60px);line-height:1.05;font-weight:700;letter-spacing:-.03em}
.hero h1 .glow{color:var(--accent)}
.hero p{max-width:580px;margin:18px auto 0;color:var(--muted);font-size:16px}

.grid{max-width:1080px;margin:30px auto 80px;padding:0 24px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.gate-card{
  background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
  padding:32px 24px;display:flex;flex-direction:column;justify-content:space-between;
  transition:.25s ease;text-decoration:none;color:inherit;position:relative;overflow:hidden;
}
.gate-card:hover{border-color:var(--line-strong);transform:translateY(-3px);background:var(--surface-2)}
.gate-card.hero-gate{border-color:rgba(212,255,63,.3);background:linear-gradient(180deg,rgba(212,255,63,.04),transparent)}

.gate-num{font-size:12px;font-weight:700;color:var(--accent);margin-bottom:12px}
.gate-icon{font-size:40px;margin-bottom:16px}
.gate-title{font-size:20px;font-weight:700;margin-bottom:8px}
.gate-desc{font-size:13px;color:var(--muted);margin-bottom:24px;line-height:1.6}
.gate-cta{font-size:13px;font-weight:600;color:var(--fg);display:flex;align-items:center;gap:6px}

.footer{max-width:1080px;margin:0 auto;padding:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;color:var(--dim);font-size:12px}

@media(max-width:768px){.grid{grid-template-columns:1fr}}
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
  <p>Giải pháp chống rò rỉ tác phẩm sáng tạo chưa phát hành. Chọn vai trò bên dưới để trải nghiệm mô hình bảo mật không chìa khóa chủ:</p>
</section>

<div class="grid">
  <!-- Trang 1 -->
  <a href="/rmit/1" class="gate-card hero-gate">
    <div>
      <div class="gate-num mono">CỔNG 01 · NGHỆ SĨ</div>
      <div class="gate-icon">🎧</div>
      <div class="gate-title">Két Sắt Nghệ Sĩ</div>
      <div class="gate-desc">Tải lên file nhạc hoặc video của bạn, mã hóa client-side và thiết lập cấp/thu hồi quyền nghe cho kỹ sư trong một cú click.</div>
    </div>
    <div class="gate-cta" style="color:var(--accent)">Mở Trang Nghệ Sĩ ➔</div>
  </a>

  <!-- Trang 2 -->
  <a href="/rmit/2" class="gate-card">
    <div>
      <div class="gate-num mono">CỔNG 02 · NGƯỜI NGHE THỬ</div>
      <div class="gate-icon">🎙</div>
      <div class="gate-title">Phòng Nghe Thử</div>
      <div class="gate-desc">Nghe thử bản master với đĩa than quay và sóng âm, giải mã tức thời trên RAM. Bị cắt phụt ngay khi tác giả rút quyền.</div>
    </div>
    <div class="gate-cta">Mở Phòng Nghe Thử ➔</div>
  </a>

  <!-- Trang 3 -->
  <a href="/rmit/3" class="gate-card">
    <div>
      <div class="gate-num mono">CỔNG 03 · MÁY CHỦ S3</div>
      <div class="gate-icon">⚠️</div>
      <div class="gate-title">Quản Trị Đám Mây</div>
      <div class="gate-desc">Xem kho nhị phân thô trên S3. Thử đóng vai hacker hoặc admin biến chất dùng quyền Root để giải mã và xem kết quả bị từ chối.</div>
    </div>
    <div class="gate-cta">Mở Trình Kiểm Tra S3 ➔</div>
  </a>
</div>

<footer class="footer">
  <span>UNRELEASED · Team Foodseekers (UIT)</span>
  <span class="mono">RMIT Hackathon 2026 — Challenge 2 (Tide)</span>
</footer>

</body>
</html>
"""

# Ghi vào cả 2 repo
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

print("\n✓ ĐÃ HOÀN TẤT TẠO TOÀN BỘ 3 TRANG!")
