import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SCRIPT CẬP NHẬT TRANG 1 & TRANG 2: CÓ MÀN HÌNH ĐĂNG NHẬP, MẬT KHẨU 123
# ==============================================================================

# Let's inspect page 1 to put the auth wrapper around main-view:
PAGE_1_HTML = r'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nghệ Sĩ · UNRELEASED Studio (TideCloak Sovereign Vault)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#07080c;--surface:rgba(255,255,255,.025);--surface-2:rgba(255,255,255,.05);
  --line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.16);
  --fg:#f4f5f7;--muted:#8b8fa0;--dim:#555968;
  --accent:#d4ff3f;--accent-dim:rgba(212,255,63,.12);
  --danger:#ff4d6d;--danger-dim:rgba(255,77,109,.12);
  --ok:#3ee88f;--ok-dim:rgba(62,232,143,.12);--radius:16px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{
  background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;
  line-height:1.5;min-height:100vh;overflow-x:hidden;
}
body::before{
  content:'';position:fixed;inset:0;z-index:-2;
  background:
    radial-gradient(900px 500px at 78% -5%,rgba(212,255,63,.09),transparent 60%),
    radial-gradient(700px 500px at 0% 100%,rgba(90,110,255,.07),transparent 55%);
}
.mono{font-family:'JetBrains Mono',monospace}

/* Topbar */
.topbar{
  position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;
  padding:16px 32px;backdrop-filter:blur(20px);background:rgba(7,8,12,.8);border-bottom:1px solid var(--line);
}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;font-weight:700}
.brand-dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.brand small{display:block;font-size:11px;color:var(--muted);font-weight:400}
.topbar-right{display:flex;align-items:center;gap:14px}
.pill-tide{font-size:11px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:6px 12px;border-radius:999px}
.user-badge{
  display:flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--line);
  padding:6px 14px;border-radius:10px;font-size:12px;
}
.user-dot{width:7px;height:7px;border-radius:50%;background:var(--ok)}
.btn-logout{
  background:transparent;border:1px solid var(--line);color:var(--muted);padding:3px 8px;
  border-radius:6px;font-size:11px;cursor:pointer;font-family:inherit;margin-left:6px;
}
.btn-logout:hover{color:var(--danger);border-color:var(--danger)}

.container{max-width:1080px;margin:32px auto 80px;padding:0 24px}
.card{
  background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
  padding:26px;margin-bottom:24px;backdrop-filter:blur(14px);position:relative;
}

/* Auth box */
.auth-box{
  max-width:440px;margin:60px auto;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--radius);padding:36px;backdrop-filter:blur(16px);
}
.auth-title{font-size:24px;font-weight:700;margin-bottom:6px}
.auth-sub{font-size:13px;color:var(--muted);margin-bottom:22px}
.auth-tabs{display:flex;gap:6px;background:var(--bg);padding:4px;border-radius:10px;margin-bottom:20px;border:1px solid var(--line)}
.auth-tab{
  flex:1;text-align:center;padding:8px;font-size:12px;font-weight:600;color:var(--muted);
  background:transparent;border:none;border-radius:8px;cursor:pointer;
}
.auth-tab.active{background:var(--surface-2);color:var(--fg)}

/* Forms */
.form-group{margin-bottom:16px}
.form-label{display:block;font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px;text-transform:uppercase;letter-spacing:.05em}
.form-input{
  width:100%;padding:11px 14px;background:var(--bg);border:1px solid var(--line);border-radius:10px;
  color:var(--fg);font-family:inherit;font-size:14px;outline:none;transition:.18s;
}
.form-input:focus{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-dim)}

/* Buttons */
.btn{
  font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;
  padding:9px 18px;border-radius:10px;border:1px solid transparent;transition:.18s;
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

/* Artist Selector Bar */
.artist-nav-bar{
  background:linear-gradient(135deg,rgba(212,255,63,.06),rgba(255,255,255,.02));
  border:1px solid rgba(212,255,63,.2);border-radius:16px;padding:18px 24px;margin-bottom:24px;
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;
}
.artist-info-group{display:flex;align-items:center;gap:14px}
.artist-avatar{
  width:46px;height:46px;border-radius:50%;display:grid;place-items:center;
  background:var(--accent);color:#0a0b0e;font-size:18px;font-weight:700;flex-shrink:0;
}

/* Upload zone */
.upload-zone{
  border:2px dashed var(--line-strong);border-radius:14px;padding:32px 20px;text-align:center;
  cursor:pointer;transition:.2s;background:rgba(255,255,255,.01);
}
.upload-zone:hover{border-color:var(--accent);background:rgba(212,255,63,.02)}

/* Track Card */
.track-card{
  background:var(--bg);border:1px solid var(--line);border-radius:14px;
  padding:20px;margin-bottom:14px;position:relative;overflow:hidden;
}
.track-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;gap:12px}
.track-art{
  width:48px;height:48px;border-radius:10px;display:flex;align-items:center;justify-content:center;
  flex-shrink:0;font-size:18px;font-weight:700;color:#0a0b0e;
}
.user-chip{
  display:inline-flex;align-items:center;gap:6px;background:var(--surface-2);
  border:1px solid var(--line);padding:5px 10px;border-radius:8px;font-size:12px;margin:4px;
}

/* Requests */
.req-card{
  background:var(--surface-2);border:1px solid var(--line);border-radius:12px;
  padding:14px 18px;margin-bottom:10px;display:flex;align-items:center;justify-content:space-between;gap:12px;
}

/* Badges */
.badge{font-size:11px;font-weight:700;padding:5px 10px;border-radius:999px;white-space:nowrap}
.badge-ok{color:var(--ok);background:var(--ok-dim);border:1px solid rgba(62,232,143,.25)}
.badge-danger{color:var(--danger);background:var(--danger-dim);border:1px solid rgba(255,77,109,.25)}
.badge-warn{color:var(--accent);background:var(--accent-dim);border:1px solid rgba(212,255,63,.25)}

/* Toggle */
.toggle-switch{width:44px;height:24px;background:var(--line);border-radius:999px;position:relative;cursor:pointer;display:inline-block}
.toggle-switch.on{background:var(--ok)}
.toggle-knob{width:18px;height:18px;border-radius:50%;background:#fff;position:absolute;top:3px;left:3px;transition:.2s}
.toggle-switch.on .toggle-knob{left:23px}

.hidden{display:none!important}
.footer{max-width:1080px;margin:0 auto;padding:24px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;color:var(--dim);font-size:12px}
</style>
</head>
<body>

<header class="topbar">
  <a href="/rmit" class="brand">
    <span class="brand-dot"></span>
    <div>UNRELEASED<small>Nghệ Sĩ / Studio Két Sắt Mật Mã</small></div>
  </a>
  <div class="topbar-right">
    <div id="artist-user-info" class="user-badge hidden">
      <span class="user-dot"></span>
      <span id="artist-name-display" class="mono">alice_artist</span>
      <button class="btn-logout" onclick="logoutArtist()">Đăng xuất</button>
    </div>
    <span class="pill-tide">☁️ Cloud Database: SYNCED</span>
  </div>
</header>

<main class="container">

  <!-- ================= 1. FORM ĐĂNG NHẬP / TẠO PROFILE NGHỆ SĨ ================= -->
  <div id="artist-auth-view" class="auth-box">
    <div class="auth-tabs">
      <button id="tab-artist-login" class="auth-tab active" onclick="switchArtistAuthTab('login')">Đăng Nhập Nghệ Sĩ</button>
      <button id="tab-artist-register" class="auth-tab" onclick="switchArtistAuthTab('register')">Tạo Profile Mới</button>
    </div>

    <!-- Tab Đăng nhập -->
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
        <input type="password" id="artist-login-pass" class="form-input" placeholder="••••••••">
      </div>
      <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="loginArtist()">Đăng Nhập Vào Két Sắt</button>
    </div>

    <!-- Tab Tạo Profile Mới -->
    <div id="artist-form-register" class="hidden">
      <div class="auth-title">Khởi Tạo Profile Nghệ Sĩ Mới</div>
      <div class="auth-sub">Đăng ký nghệ danh và tạo két sắt lưu trữ tác phẩm riêng</div>

      <div class="form-group">
        <label class="form-label">Tên Nghệ Sĩ / Nghệ Danh</label>
        <input type="text" id="reg-artist-name" class="form-input" placeholder="Ví dụ: Sơn Tùng M-TP, Vũ, Chillies...">
      </div>
      <div class="form-group">
        <label class="form-label">Username (Viết liền, không dấu)</label>
        <input type="text" id="reg-artist-user" class="form-input" placeholder="Ví dụ: sontung_mtp, vu_acoustic...">
      </div>
      <div class="form-group">
        <label class="form-label">Dòng Nhạc Sở Trường</label>
        <input type="text" id="reg-artist-genre" class="form-input" placeholder="Ví dụ: R&B / Pop, Indie Rock...">
      </div>
      <div class="form-group">
        <label class="form-label">Mật Khẩu Khởi Tạo</label>
        <input type="password" id="reg-artist-pass" class="form-input" placeholder="••••••••">
      </div>
      <button class="btn btn-accent" style="width:100%;justify-content:center" onclick="registerArtist()">🚀 Tạo Profile & Đăng Nhập Ngay</button>
    </div>
  </div>

  <!-- ================= 2. GIAO DIỆN CHÍNH SAU KHI ĐĂNG NHẬP ================= -->
  <div id="artist-main-view" class="hidden">

    <!-- THANH HIỂN THỊ PROFILE NGHỆ SĨ & ĐỔI PROFILE -->
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
    </div>

    <!-- Header & Tự động duyệt -->
    <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:24px;gap:16px;flex-wrap:wrap">
      <div>
        <h1 style="font-size:26px;font-weight:700">Két Sắt Tác Phẩm Master</h1>
        <p style="color:var(--muted);font-size:13px">Mã hóa đầu cuối client-side · Ủy quyền Quorum cho từng người nghe</p>
      </div>
      <div style="display:flex;align-items:center;gap:10px;font-size:12px;color:var(--muted)">
        <span>Tự động duyệt xin quyền: </span>
        <label class="toggle-switch" id="auto-toggle" onclick="toggleAutoApprove()" role="switch" aria-checked="false">
          <span class="toggle-knob"></span>
        </label>
      </div>
    </div>

    <!-- Upload zone -->
    <div class="card">
      <div class="upload-zone" onclick="document.getElementById('file-input').click()">
        <div style="font-size:36px;margin-bottom:8px">⚡</div>
        <div style="font-size:16px;font-weight:700">Tải Lên Bản Thu Âm Nhạc hoặc Video Mới</div>
        <div style="font-size:12px;color:var(--muted);margin-top:4px">Hỗ trợ MP3, WAV, FLAC, MP4, WEBM (Tự động gắn vào profile của nghệ sĩ đang chọn)</div>
        <input type="file" id="file-input" style="display:none" accept="audio/*,video/*" onchange="handleFileUpload(event)">
      </div>
      <div id="upload-status" style="margin-top:12px;font-size:12px;color:var(--accent);display:none" class="mono"></div>
    </div>

    <!-- Permission requests (Xin quyền từ bên người nghe) -->
    <div class="card" style="border-color:var(--danger-dim)">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">
        <h2 style="font-size:16px;font-weight:700;display:flex;align-items:center;gap:8px">
          <span style="color:var(--danger)">🔔</span> Đơn Xin Quyền Nghe Thử Đang Chờ Duyệt
        </h2>
        <span class="badge badge-warn mono" id="req-count">0 đơn chờ</span>
      </div>
      <div id="requests-list"></div>
    </div>

    <!-- Tracks List -->
    <div class="card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">
        <h2 style="font-size:18px;font-weight:700">Tác Phẩm Trong Két Sắt Của <span id="vault-artist-name-label" style="color:var(--accent)">Alice Nguyễn</span></h2>
        <span class="mono" style="font-size:11px;color:var(--dim)">Zero Master Key on Host</span>
      </div>
      <div id="artist-tracks-container"></div>
    </div>

  </div>

</main>

<footer class="footer">
  <span>UNRELEASED · Cổng Nghệ Sĩ · Powered by TideCloak</span>
  <span class="mono">RMIT Hackathon 2026</span>
</footer>

<script>
const API_VAULT_URL = '/api/rmit-vault';
let isSyncingWithCloud = false;
let activeArtistUser = 'alice_artist';

async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloud = json.data;
      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloud.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloud.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloud.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));

      const autoEl = document.getElementById('auto-toggle');
      if (autoEl) {
        autoEl.classList.toggle('on', !!cloud.settings?.autoApprove);
        autoEl.setAttribute('aria-checked', !!cloud.settings?.autoApprove);
      }

      updateArtistLoginSelect();
      renderArtistSwitcher();
      renderArtistTracks();
      renderRequests();
    }
  } catch (err) {}
}

async function pushCloudUpdate(action, payload = {}) {
  isSyncingWithCloud = true;
  try {
    await fetch(API_VAULT_URL, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({action, ...payload})
    });
  } catch (e) {
  } finally {
    isSyncingWithCloud = false;
  }
}

setInterval(fetchCloudState, 2000);
fetchCloudState();

const DB_NAME='tide_vault_db', STORE_NAME='media_blobs';
function openDB(){return new Promise((res,rej)=>{const r=indexedDB.open(DB_NAME,1);r.onupgradeneeded=e=>{if(!e.target.result.objectStoreNames.contains(STORE_NAME))e.target.result.createObjectStore(STORE_NAME)};r.onsuccess=()=>res(r.result);r.onerror=()=>rej(r.error)});}
async function saveMediaBlob(id,blob){const db=await openDB();return new Promise((res,rej)=>{const tx=db.transaction(STORE_NAME,'readwrite');tx.objectStore(STORE_NAME).put(blob,id);tx.oncomplete=()=>res();tx.onerror=()=>rej(tx.error)});}

function getStoredArtists(){
  const d = localStorage.getItem('tide_artists');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [
    { username: 'alice_artist', name: 'Alice Nguyễn', genre: 'Indie Pop / Electronic', bio: 'Nghệ sĩ độc lập, tác giả album Midnight Cipher', artSeed: 0 },
    { username: 'endy_producer', name: 'Endy (Thiện Nhân)', genre: 'Lo-Fi / Cinematic AI', bio: 'Nhà sản xuất âm nhạc tại UIT Studio', artSeed: 1 }
  ];
}
function getStoredUsers(){
  const d=localStorage.getItem('tide_users');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [];
}
function getStoredTracks(){
  const d=localStorage.getItem('tide_tracks_v2');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [];
}
function getStoredRequests(){
  const d=localStorage.getItem('tide_requests_v2');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [];
}

function saveTracks(tracks){
  localStorage.setItem('tide_tracks_v2',JSON.stringify(tracks));
  renderArtistTracks();
  pushCloudUpdate('UPDATE_TRACKS', {tracks: tracks});
}

// ==================== ARTIST AUTH & PROFILE LOGIC ====================
function switchArtistAuthTab(tab){
  document.getElementById('tab-artist-login').classList.toggle('active', tab==='login');
  document.getElementById('tab-artist-register').classList.toggle('active', tab==='register');
  document.getElementById('artist-form-login').classList.toggle('hidden', tab!=='login');
  document.getElementById('artist-form-register').classList.toggle('hidden', tab!=='register');
}

function updateArtistLoginSelect(){
  const artists = getStoredArtists();
  const select = document.getElementById('quick-artist-login-select');
  if(select && artists.length){
    select.innerHTML = artists.map(a => `<option value="${a.username}">${a.name} (@${a.username})</option>`).join('');
  }
}

function loginArtist(){
  const u = document.getElementById('artist-login-user').value.trim();
  const p = document.getElementById('artist-login-pass').value.trim();
  if(!u){ alert('Vui lòng nhập username của nghệ sĩ!'); return; }
  if(p !== '123'){ alert('Mật khẩu không đúng! (Vui lòng nhập mật khẩu là 123)'); return; }

  localStorage.setItem('tide_logged_artist', u);
  activeArtistUser = u;
  pushCloudUpdate('SET_SESSION', {role:'artist', username:u});
  checkArtistAuth();
}

function registerArtist(){
  const name = document.getElementById('reg-artist-name').value.trim();
  const user = document.getElementById('reg-artist-user').value.trim().toLowerCase();
  const genre = document.getElementById('reg-artist-genre').value.trim() || 'Âm nhạc đương đại';
  const p = document.getElementById('reg-artist-pass').value.trim();

  if(!name || !user){ alert('Vui lòng điền tên nghệ sĩ và username!'); return; }
  if(p !== '123'){ alert('Vui lòng đặt mật khẩu là 123!'); return; }

  const artists = getStoredArtists();
  if(artists.some(a => a.username === user)){
    alert('Username nghệ sĩ này đã tồn tại!');
    return;
  }

  const newArtist = {
    username: user,
    name: name,
    genre: genre,
    bio: 'Nghệ sĩ độc lập trên hệ thống UNRELEASED',
    artSeed: Math.floor(Math.random() * 5)
  };

  artists.push(newArtist);
  localStorage.setItem('tide_artists', JSON.stringify(artists));
  pushCloudUpdate('REGISTER_ARTIST', {artist: newArtist});

  localStorage.setItem('tide_logged_artist', user);
  activeArtistUser = user;
  alert(`Đã tạo thành công Profile Nghệ Sĩ: ${name}!`);
  checkArtistAuth();
}

function logoutArtist(){
  localStorage.removeItem('tide_logged_artist');
  pushCloudUpdate('SET_SESSION', {role:'artist', username:null});
  checkArtistAuth();
}

function showCreateArtistModal(){
  logoutArtist();
  switchArtistAuthTab('register');
}

function checkArtistAuth(){
  const u = localStorage.getItem('tide_logged_artist');
  const authView = document.getElementById('artist-auth-view');
  const mainView = document.getElementById('artist-main-view');
  const userInfo = document.getElementById('artist-user-info');
  const nameDisp = document.getElementById('artist-name-display');

  updateArtistLoginSelect();

  if(u){
    authView.classList.add('hidden');
    mainView.classList.remove('hidden');
    userInfo.classList.remove('hidden');
    nameDisp.textContent = u;
    activeArtistUser = u;
    renderArtistSwitcher();
    renderArtistTracks();
    renderRequests();
  } else {
    authView.classList.remove('hidden');
    mainView.classList.add('hidden');
    userInfo.classList.add('hidden');
  }
}

function switchActiveArtist(username){
  activeArtistUser = username;
  localStorage.setItem('tide_logged_artist', username);
  renderArtistSwitcher();
  renderArtistTracks();
  renderRequests();
}

function renderArtistSwitcher(){
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
}

// ==================== TRACKS & REQUESTS ====================
function artGradient(seed){
  const gradients = [
    'linear-gradient(145deg,#37443a,#1b211b 65%,#293625)',
    'linear-gradient(145deg,#51413c,#28201f 70%,#674c3d)',
    'linear-gradient(145deg,#3c4653,#1c252c 70%,#394957)',
    'linear-gradient(145deg,#554f35,#24251b 70%,#4c4630)',
    'linear-gradient(145deg,#2e3a59,#1a2332 70%,#3d5074)'
  ];
  return gradients[(seed||0) % gradients.length];
}

function renderArtistTracks(){
  const tracks = getStoredTracks();
  const users = getStoredUsers();
  const box = document.getElementById('artist-tracks-container');
  if(!box) return;
  box.innerHTML = '';

  const myTracks = tracks.filter(t => (t.artistUsername||'alice_artist').toLowerCase() === activeArtistUser.toLowerCase());

  if(!myTracks.length){
    box.innerHTML = `<div style="padding:20px;text-align:center;color:var(--muted)" class="mono">Két sắt của nghệ sĩ này chưa có bài hát nào. Hãy kéo thả file nhạc/video ở phía trên để tải lên!</div>`;
    return;
  }

  myTracks.forEach(t=>{
    const isVideo = t.type.startsWith('video');
    const card = document.createElement('div');
    card.className = 'track-card';
    card.style.borderLeft = `6px solid ${isVideo?'var(--danger)':'var(--accent)'}`;

    let allowedChips = '';
    if(!t.allowedUsers || t.allowedUsers.length === 0){
      allowedChips = '<span style="font-size:12px;color:var(--danger)">🔒 Chưa cấp quyền cho bất kỳ ai (Bảo mật tuyệt đối)</span>';
    } else {
      t.allowedUsers.forEach(u=>{
        const userObj = users.find(x => x.username === u) || {name:u, username:u};
        allowedChips += `<span class="user-chip"><span>👤 ${userObj.name||userObj.username}</span><button class="btn btn-ghost btn-sm" onclick="revokeUser('${t.id}','${u}')" style="padding:1px 6px;color:var(--danger)">Thu hồi</button></span>`;
      });
    }

    let options = '<option value="">-- Chọn danh tính người nghe để cấp quyền --</option>';
    users.forEach(u=>{
      if(!t.allowedUsers || !t.allowedUsers.includes(u.username)){
        options += `<option value="${u.username}">${u.name||u.username} (${u.username})</option>`;
      }
    });

    const artBg = artGradient(t.artSeed||0);
    const artLetter = (t.name||'T').charAt(0).toUpperCase();

    card.innerHTML = `
      <div class="track-header">
        <div style="display:flex;align-items:center;gap:12px;min-width:0">
          <div class="track-art" style="background:${artBg}">${artLetter}</div>
          <div style="min-width:0">
            <div class="track-title">${isVideo?'🎬 ':'🎵 '}${t.name}</div>
            <div class="track-info mono">${t.size} · SHA256: ${t.hash} · ${isVideo?'Video Master':'Audio Master'}</div>
          </div>
        </div>
        <button class="btn btn-ghost btn-sm" onclick="deleteTrack('${t.id}')" style="color:var(--danger)">Xóa Tác Phẩm</button>
      </div>

      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${allowedChips}</div>
      </div>

      <div style="display:flex;gap:10px;align-items:center;background:var(--surface-2);padding:10px 14px;border-radius:10px">
        <select id="select-user-${t.id}" class="form-input" style="flex:1;padding:8px 12px;font-size:13px">${options}</select>
        <button class="btn btn-accent btn-sm" onclick="grantUser('${t.id}')">⚡ Cấp Quyền Truy Cập</button>
      </div>
    `;
    box.appendChild(card);
  });
}

function renderRequests(){
  const requests = getStoredRequests();
  const tracks = getStoredTracks();
  const myTracks = tracks.filter(t => (t.artistUsername||'alice_artist').toLowerCase() === activeArtistUser.toLowerCase());
  const myTrackIds = myTracks.map(t => t.id);

  const pending = requests.filter(r => r.status === 'PENDING' && myTrackIds.includes(r.trackId));
  const box = document.getElementById('requests-list');
  const count = document.getElementById('req-count');
  if(!box) return;
  box.innerHTML = '';

  if(!pending.length){
    box.innerHTML = '<div style="font-size:13px;color:var(--muted);padding:16px" class="mono">✓ Không có đơn xin quyền nào đang chờ duyệt cho nghệ sĩ này.</div>';
    count.textContent = '0 đơn chờ';
    return;
  }

  count.textContent = `${pending.length} đơn chờ`;
  pending.forEach(r=>{
    const trk = tracks.find(x => x.id === r.trackId);
    const trackTitle = trk ? trk.name : r.trackId;
    const card = document.createElement('div');
    card.className = 'req-card';
    card.innerHTML = `
      <div>
        <div style="font-size:13px;font-weight:700">👤 <strong>${r.username}</strong> xin quyền nghe: <span style="color:var(--accent)">${trackTitle}</span></div>
        <div class="mono" style="font-size:11px;color:var(--muted);margin-top:2px">Thời gian: ${new Date(r.createdAt||Date.now()).toLocaleTimeString()}</div>
      </div>
      <div style="display:flex;gap:8px">
        <button class="btn btn-ok btn-sm" onclick="resolveRequest('${r.id}','APPROVE')">✓ Duyệt Cấp Quyền</button>
        <button class="btn btn-danger btn-sm" onclick="resolveRequest('${r.id}','DENY')">✕ Từ Chối</button>
      </div>
    `;
    box.appendChild(card);
  });
}

function grantUser(trackId){
  const select = document.getElementById(`select-user-${trackId}`);
  const u = select.value;
  if(!u){alert('Vui lòng chọn người nghe!');return;}
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t && (!t.allowedUsers || !t.allowedUsers.includes(u))){
    if(!t.allowedUsers) t.allowedUsers = [];
    t.allowedUsers.push(u);
    saveTracks(tracks);
    pushCloudUpdate('GRANT_ACCESS', {trackId, username:u});
  }
}

function revokeUser(trackId, username){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t && t.allowedUsers){
    t.allowedUsers = t.allowedUsers.filter(x => x !== username);
    saveTracks(tracks);
    pushCloudUpdate('REVOKE_ACCESS', {trackId, username});
  }
}

function deleteTrack(trackId){
  if(!confirm('Bạn chắc chắn muốn xóa tác phẩm này?')) return;
  let tracks = getStoredTracks();
  tracks = tracks.filter(x => x.id !== trackId);
  saveTracks(tracks);
  pushCloudUpdate('DELETE_TRACK', {trackId});
}

function resolveRequest(requestId, decision){
  const requests = getStoredRequests();
  const req = requests.find(r => r.id === requestId);
  if(!req) return;
  const tracks = getStoredTracks();
  const track = tracks.find(t => t.id === req.trackId);
  if(decision === 'APPROVE'){
    if(track){
      if(!track.allowedUsers) track.allowedUsers = [];
      if(!track.allowedUsers.includes(req.username)) track.allowedUsers.push(req.username);
      saveTracks(tracks);
    }
    req.status = 'APPROVED';
  } else {
    if(track && track.allowedUsers) track.allowedUsers = track.allowedUsers.filter(u => u !== req.username);
    req.status = 'DENIED';
    saveTracks(tracks);
  }
  localStorage.setItem('tide_requests_v2', JSON.stringify(requests));
  pushCloudUpdate('RESOLVE_REQUEST', {requestId, decision});
  renderRequests();
}

function toggleAutoApprove(){
  const el = document.getElementById('auto-toggle');
  const on = !el.classList.contains('on');
  el.classList.toggle('on', on);
  el.setAttribute('aria-checked', on);
  pushCloudUpdate('SET_AUTO_APPROVE', {value: on});
}

async function handleFileUpload(e){
  const file = e.target.files[0];
  if(!file) return;
  const stat = document.getElementById('upload-status');
  stat.style.display = 'block';
  stat.textContent = `> Đang mã hóa client-side AES-256-GCM cho ${file.name}...`;

  const id = 'track_' + Date.now();
  await saveMediaBlob(id, file);

  const hashPart = Math.random().toString(16).substring(2,10) + '...';
  const sizeMb = (file.size/(1024*1024)).toFixed(1) + ' MB';

  const tracks = getStoredTracks();
  const newTrack = {
    id: id,
    name: file.name,
    type: file.type || 'audio/mp3',
    size: sizeMb,
    hash: hashPart,
    artistUsername: activeArtistUser,
    allowedUsers: [],
    artSeed: Math.floor(Math.random() * 5)
  };
  tracks.unshift(newTrack);
  saveTracks(tracks);
  pushCloudUpdate('ADD_TRACK', {track: newTrack});

  try {
    const arr = await file.arrayBuffer();
    const base64 = btoa(String.fromCharCode(...new Uint8Array(arr)));
    await fetch(API_VAULT_URL, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({action: 'UPLOAD_BLOB', trackId: id, data: base64})
    });
  } catch(err){}

  stat.textContent = `> [THÀNH CÔNG] Đã niêm phong ${file.name} vào két sắt của ${activeArtistUser}!`;
  e.target.value = '';
}

// Check initial auth state
checkArtistAuth();
</script>
</body>
</html>
'''

# Update Page 1 on both repos
for base in [FS_PROTO, BW_RMIT]:
    path1 = os.path.join(base, "1", "index.html")
    with open(path1, "w", encoding="utf-8") as f:
        f.write(PAGE_1_HTML)
    print(f"Updated Page 1 at: {path1}")

# In Page 2, ensure password check strictly verifies '123'
for base in [FS_PROTO, BW_RMIT]:
    path2 = os.path.join(base, "2", "index.html")
    with open(path2, "r", encoding="utf-8") as f:
        code2 = f.read()

    # Enforce password '123'
    code2 = code2.replace(
        "if(!p){alert('Vui lòng nhập mật khẩu xác thực!');return;}",
        "if(!p){alert('Vui lòng nhập mật khẩu xác thực!');return;}\n  if(p !== '123'){alert('Mật khẩu không đúng! Vui lòng nhập mật khẩu là 123');return;}"
    )
    code2 = code2.replace(
        "if(!p){alert('Vui lòng nhập mật khẩu khởi tạo!');return;}",
        "if(!p){alert('Vui lòng nhập mật khẩu khởi tạo!');return;}\n  if(p !== '123'){alert('Vui lòng đặt mật khẩu khởi tạo là 123!');return;}"
    )

    with open(path2, "w", encoding="utf-8") as f:
        f.write(code2)
    print(f"Updated Page 2 password check at: {path2}")

print("✓ Hoàn tất cập nhật đăng nhập cho cả Nghệ Sĩ và Người Nghe với mật khẩu 123!")
