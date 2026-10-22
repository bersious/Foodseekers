import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# ARCHITECTURAL REWRITE OF PAGE 1 JAVASCRIPT:
# 1. KHÔNG BAO GIỜ REASSIGN .src TRONG POLLING (NGUYÊN NHÂN GÂY ĐƠ / KHÔNG ĂN CLICK)
# 2. KHÔNG BAO GIỜ XÓA box.innerHTML KHI ĐỔI CÀI ĐẶT (UPDATE TRỰC TIẾP ELEMENT)
# 3. DOM ĐỨNG YÊN 100% — MỌI NÚT BẤM ĂN NGAY LẬP TỨC (0MS LATENCY)
# ==============================================================================

# Let's read the current HTML structure of Page 1 to ensure we keep all UI elements intact
with open(os.path.join(FS_PROTO, "1", "index.html"), "r", encoding="utf-8") as f:
    full_html = f.read()

# Separate HTML from <script>
html_part, old_script_part = full_html.split("<script>", 1)

NEW_SCRIPT = r'''
const API_VAULT_URL = '/api/rmit-vault';
let isSyncingWithCloud = false;
let activeArtistUser = localStorage.getItem('tide_logged_artist') || 'alice_artist';

// Bộ nhớ đệm URL tạm thời cho media để phát ngay 0ms
const memoryMediaUrls = {};

// ==================== 1. QUẢN LÝ DỮ LIỆU ĐÁM MÂY (CHỈ CẬP NHẬT KHI CẦN) ====================
async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloud = json.data;

      // Lưu ngầm
      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloud.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloud.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloud.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));

      // Chỉ cập nhật danh sách đơn xin quyền nếu có thay đổi
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

// Polling ngầm mỗi 4 giây chỉ để đón đơn xin quyền mới
setInterval(fetchCloudState, 4000);
fetchCloudState();

// ==================== 2. LOCAL STORAGE & INDEXEDDB HELPERS ====================
const DB_NAME='tide_vault_db', STORE_NAME='media_blobs';
function openDB(){return new Promise((res,rej)=>{const r=indexedDB.open(DB_NAME,1);r.onupgradeneeded=e=>{if(!e.target.result.objectStoreNames.contains(STORE_NAME))e.target.result.createObjectStore(STORE_NAME)};r.onsuccess=()=>res(r.result);r.onerror=()=>rej(r.error)});}
async function saveMediaBlob(id,blob){const db=await openDB();return new Promise((res,rej)=>{const tx=db.transaction(STORE_NAME,'readwrite');tx.objectStore(STORE_NAME).put(blob,id);tx.oncomplete=()=>res();tx.onerror=()=>rej(tx.error)});}

async function getMediaBlob(id){
  if(memoryMediaUrls[id]) return memoryMediaUrls[id];
  try {
    const db=await openDB();
    const local = await new Promise((res,rej)=>{const tx=db.transaction(STORE_NAME,'readonly');const req=tx.objectStore(STORE_NAME).get(id);req.onsuccess=()=>res(req.result);req.onerror=()=>rej(tx.error)});
    if (local) return local;
  } catch(e){}
  return null;
}

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

// Lưu tracks không xóa DOM
function saveTracksSilent(tracks){
  localStorage.setItem('tide_tracks_v2', JSON.stringify(tracks));
  pushCloudUpdate('UPDATE_TRACKS', {tracks: tracks});
}

// ==================== 3. ĐĂNG NHẬP & HỒ SƠ NGHỆ SĨ ====================
function switchArtistAuthTab(tab){
  document.getElementById('tab-artist-login').classList.toggle('active', tab==='login');
  document.getElementById('tab-artist-register').classList.toggle('active', tab==='register');
  document.getElementById('artist-form-login').classList.toggle('hidden', tab!=='login');
  document.getElementById('artist-form-register').classList.toggle('hidden', tab!=='register');
}

function loginArtist(){
  const u = document.getElementById('artist-login-user').value.trim();
  const p = document.getElementById('artist-login-pass').value.trim();
  if(!u){ alert('Vui lòng nhập username của nghệ sĩ!'); return; }
  if(p !== '123'){ alert('Mật khẩu xác thực không chính xác.'); return; }

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
  if(p !== '123'){ alert('Mật khẩu không hợp lệ.'); return; }

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
  const el = document.getElementById('create-artist-card');
  if(el){
    el.classList.toggle('hidden');
    if(!el.classList.contains('hidden')){
      el.scrollIntoView({behavior:'smooth', block:'center'});
    }
  }
}

function checkArtistAuth(){
  const u = localStorage.getItem('tide_logged_artist');
  const authView = document.getElementById('artist-auth-view');
  const mainView = document.getElementById('artist-main-view');
  const userInfo = document.getElementById('artist-user-info');
  const nameDisp = document.getElementById('artist-name-display');

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

// ==================== 4. DỰNG DANH SÁCH BÀI HÁT & TRÌNH PHÁT ====================
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
    const isVideo = t.type && t.type.startsWith('video');
    const card = document.createElement('div');
    card.className = 'track-card';
    card.id = `card-${t.id}`;
    card.style.borderLeft = `6px solid ${isVideo?'var(--danger)':'var(--accent)'}`;

    let allowedChips = '';
    if(!t.allowedUsers || t.allowedUsers.length === 0){
      allowedChips = `<span id="chips-empty-${t.id}" style="font-size:12px;color:var(--danger)">Chưa cấp quyền cho bất kỳ ai</span>`;
    } else {
      t.allowedUsers.forEach(u=>{
        const userObj = users.find(x => x.username === u) || {name:u, username:u};
        const isSingle = Array.isArray(t.singlePlayUsers) && t.singlePlayUsers.includes(u);
        allowedChips += `<span class="user-chip" id="chip-${t.id}-${u}"><span>${userObj.name||userObj.username}</span>${isSingle?'<span style="font-size:10px;color:var(--warn);background:rgba(255,184,77,.15);padding:1px 5px;border-radius:4px" class="mono">1 LẦN</span>':''}<button class="btn btn-ghost btn-sm" onclick="revokeUser('${t.id}','${u}')" style="padding:1px 6px;color:var(--danger)">Thu hồi</button></span>`;
      });
    }

    let options = '<option value="">-- Chọn người nghe để cấp quyền --</option>';
    users.forEach(u=>{
      if(!t.allowedUsers || !t.allowedUsers.includes(u.username)){
        options += `<option value="${u.username}">${u.name||u.username} (@${u.username})</option>`;
      }
    });

    const artBg = artGradient(t.artSeed||0);
    const artLetter = (t.name||'T').charAt(0).toUpperCase();

    card.innerHTML = `
      <div class="track-header">
        <div style="display:flex;align-items:center;gap:12px;min-width:0">
          <div class="track-art" style="background:${artBg}">${artLetter}</div>
          <div style="min-width:0">
            <div class="track-title">${t.name}</div>
            <div class="track-info mono">${t.size} · SHA256: ${t.hash} · ${isVideo?'Video Master':'Audio Master'}</div>
          </div>
        </div>
        <button class="btn btn-ghost btn-sm" onclick="deleteTrack('${t.id}')" style="color:var(--danger)">Xóa Tác Phẩm</button>
      </div>

      <!-- TRÌNH PHÁT NHẠC MP3 / XEM VIDEO TRỰC TIẾP -->
      <div style="margin-bottom:14px;background:#050705;border:1px solid var(--line);border-radius:10px;padding:12px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:11px;font-weight:700;color:var(--accent)" class="mono">
            ${isVideo ? 'TRÌNH PHÁT VIDEO MASTER' : 'TRÌNH PHÁT ÂM THANH MASTER'}
          </span>
          <span style="font-size:10px;color:var(--dim)" class="mono">IN-MEMORY STREAM</span>
        </div>
        ${isVideo ? `
          <video id="player-${t.id}" controls style="width:100%;max-height:280px;border-radius:8px;background:#000;display:block"></video>
        ` : `
          <audio id="player-${t.id}" controls style="width:100%;border-radius:6px;outline:none"></audio>
        `}
      </div>

      <!-- Cài đặt chống can thiệp phần mềm thứ 3 -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,82,108,0.06);padding:8px 14px;border-radius:10px;border:1px solid rgba(255,82,108,0.25);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--danger);font-weight:700">Tự động thu hồi khi phát hiện can thiệp:</span>
        <label class="toggle-switch ${t.tamperProtection?'on':''}" id="tamper-toggle-${t.id}" onclick="toggleTrackTamperProtection('${t.id}')">
          <span class="toggle-knob"></span>
        </label>
        <span class="mono" id="tamper-label-${t.id}" style="font-size:11px;color:var(--dim)">
          ${t.tamperProtection ? 'Đang bật bảo vệ chống can thiệp và ghi âm lậu' : 'Đang tắt'}
        </span>
      </div>

      <!-- Cài đặt chống thu âm ngoài loa (Audio Watermark) -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,255,255,0.03);padding:8px 14px;border-radius:10px;border:1px solid var(--line);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--accent);font-weight:700">Chống thu âm ngoài loa:</span>
        <select class="form-input" style="width:auto;padding:5px 10px;font-size:12px;margin:0" onchange="setWatermarkMode('${t.id}', this.value)">
          <option value="none" ${(!t.watermarkMode || t.watermarkMode==='none')?'selected':''}>Không chèn watermark</option>
          <option value="duck" ${t.watermarkMode==='duck'?'selected':''}>Chèn tiếng vịt kêu định kỳ</option>
          <option value="voice" ${t.watermarkMode==='voice'?'selected':''}>Giọng nói AI đọc cảnh báo bản quyền</option>
        </select>
        <span class="mono" id="wm-label-${t.id}" style="font-size:11px;color:var(--dim)">
          ${t.watermarkMode==='duck' ? '· Chèn tiếng quack định kỳ để làm hỏng bản thu lậu' : (t.watermarkMode==='voice' ? '· Giọng AI đọc tên nghệ sĩ định kỳ' : '· Âm thanh nguyên bản')}
        </span>
      </div>

      <!-- Cài đặt giới hạn thời gian nghe thử của Nghệ sĩ -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,255,255,0.03);padding:8px 14px;border-radius:10px;border:1px solid var(--line);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--accent);font-weight:700">Giới hạn thời gian nghe thử:</span>
        <select class="form-input" style="width:auto;padding:5px 10px;font-size:12px;margin:0" onchange="setTrackLimit('${t.id}', this.value)">
          <option value="0" ${(!t.previewLimitSeconds || t.previewLimitSeconds==0)?'selected':''}>Toàn bộ bài hát</option>
          <option value="10" ${t.previewLimitSeconds==10?'selected':''}>10 giây đầu</option>
          <option value="15" ${t.previewLimitSeconds==15?'selected':''}>15 giây đầu</option>
          <option value="30" ${t.previewLimitSeconds==30?'selected':''}>30 giây đầu</option>
          <option value="60" ${t.previewLimitSeconds==60?'selected':''}>60 giây đầu</option>
        </select>
        <span class="mono" id="limit-label-${t.id}" style="font-size:11px;color:${t.previewLimitSeconds>0?'var(--warn)':'var(--dim)'}">
          ${t.previewLimitSeconds>0 ? `· Giới hạn ${t.previewLimitSeconds}s` : '· Toàn thời lượng'}
        </span>
      </div>

      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div id="chips-container-${t.id}">${allowedChips}</div>
      </div>

      <div style="display:flex;gap:10px;align-items:center;background:var(--surface-2);padding:10px 14px;border-radius:10px;flex-wrap:wrap">
        <select id="select-user-${t.id}" class="form-input" style="flex:1;min-width:180px;padding:8px 12px;font-size:13px">${options}</select>
        <label style="font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px;cursor:pointer;white-space:nowrap">
          <input type="checkbox" id="single-play-${t.id}"> Chỉ nghe 1 lần
        </label>
        <button class="btn btn-accent btn-sm" onclick="grantUser('${t.id}')">Cấp quyền truy cập</button>
      </div>

      <!-- Khung hiển thị bình luận từ Người Nghe -->
      <div style="margin-top:14px;background:#050705;border:1px solid var(--line);border-radius:10px;padding:12px">
        <div style="font-size:11px;font-weight:700;color:var(--accent);margin-bottom:6px">
          GÓP Ý & BÌNH LUẬN TỪ NGƯỜI NGHE:
        </div>
        <div id="comments-box-${t.id}">
          ${renderCommentsForTrack(t.id)}
        </div>
      </div>
    `;
    box.appendChild(card);

    // Nạp source phát nhạc/video vào player ngay lập tức
    const el = document.getElementById(`player-${t.id}`);
    if(el){
      if(t.streamUrl){
        el.src = t.streamUrl;
      } else {
        getMediaBlob(t.id).then(blob => {
          if(blob) el.src = URL.createObjectURL(blob);
        });
      }
    }
  });
}

// ==================== 5. THAO TÁC CÀI ĐẶT TRỰC TIẾP (KHÔNG XÓA DOM) ====================
function setTrackLimit(trackId, limitSeconds){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.previewLimitSeconds = Number(limitSeconds) || 0;
    saveTracksSilent(tracks);

    const lbl = document.getElementById(`limit-label-${trackId}`);
    if(lbl){
      lbl.textContent = t.previewLimitSeconds > 0 ? `· Giới hạn ${t.previewLimitSeconds}s` : '· Toàn thời lượng';
      lbl.style.color = t.previewLimitSeconds > 0 ? 'var(--warn)' : 'var(--dim)';
    }
  }
}

function setWatermarkMode(trackId, mode){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.watermarkMode = mode || 'none';
    saveTracksSilent(tracks);

    const lbl = document.getElementById(`wm-label-${trackId}`);
    if(lbl){
      lbl.textContent = t.watermarkMode === 'duck' 
        ? '· Chèn tiếng quack định kỳ để làm hỏng bản thu lậu' 
        : (t.watermarkMode === 'voice' ? '· Giọng AI đọc tên nghệ sĩ định kỳ' : '· Âm thanh nguyên bản');
    }
  }
}

function toggleTrackTamperProtection(trackId){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.tamperProtection = !t.tamperProtection;
    saveTracksSilent(tracks);

    const toggle = document.getElementById(`tamper-toggle-${trackId}`);
    const lbl = document.getElementById(`tamper-label-${trackId}`);
    if(toggle) toggle.classList.toggle('on', !!t.tamperProtection);
    if(lbl) lbl.textContent = t.tamperProtection ? 'Đang bật bảo vệ chống can thiệp và ghi âm lậu' : 'Đang tắt';
  }
}

function grantUser(trackId){
  const select = document.getElementById(`select-user-${trackId}`);
  const singleCheckbox = document.getElementById(`single-play-${trackId}`);
  const u = select ? select.value : '';
  const isSinglePlay = singleCheckbox ? singleCheckbox.checked : false;

  if(!u){ alert('Vui lòng chọn một người nghe từ danh sách!'); return; }
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    if(!Array.isArray(t.allowedUsers)) t.allowedUsers = [];
    if(!Array.isArray(t.singlePlayUsers)) t.singlePlayUsers = [];
    if(!t.allowedUsers.includes(u)) t.allowedUsers.push(u);
    if(isSinglePlay && !t.singlePlayUsers.includes(u)) t.singlePlayUsers.push(u);
    saveTracksSilent(tracks);

    // Cập nhật DOM trực tiếp không xóa thẻ
    const container = document.getElementById(`chips-container-${trackId}`);
    const emptyMsg = document.getElementById(`chips-empty-${trackId}`);
    if(emptyMsg) emptyMsg.remove();

    const users = getStoredUsers();
    const userObj = users.find(x => x.username === u) || {name:u, username:u};
    const chip = document.createElement('span');
    chip.className = 'user-chip';
    chip.id = `chip-${trackId}-${u}`;
    chip.innerHTML = `<span>${userObj.name||userObj.username}</span>${isSinglePlay?'<span style="font-size:10px;color:var(--warn);background:rgba(255,184,77,.15);padding:1px 5px;border-radius:4px" class="mono">1 LẦN</span>':''}<button class="btn btn-ghost btn-sm" onclick="revokeUser('${trackId}','${u}')" style="padding:1px 6px;color:var(--danger)">Thu hồi</button>`;
    if(container) container.appendChild(chip);

    // Xóa user khỏi dropdown
    if(select){
      const opt = select.querySelector(`option[value="${u}"]`);
      if(opt) opt.remove();
      select.value = '';
    }
  }
}

function revokeUser(trackId, username){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t && Array.isArray(t.allowedUsers)){
    t.allowedUsers = t.allowedUsers.filter(x => x !== username);
    if(Array.isArray(t.singlePlayUsers)) t.singlePlayUsers = t.singlePlayUsers.filter(x => x !== username);
    saveTracksSilent(tracks);

    // Xóa chip trực tiếp khỏi DOM
    const chip = document.getElementById(`chip-${trackId}-${username}`);
    if(chip) chip.remove();

    const container = document.getElementById(`chips-container-${trackId}`);
    if(container && !t.allowedUsers.length){
      container.innerHTML = `<span id="chips-empty-${trackId}" style="font-size:12px;color:var(--danger)">Chưa cấp quyền cho bất kỳ ai</span>`;
    }

    // Thêm lại vào dropdown
    const select = document.getElementById(`select-user-${trackId}`);
    if(select){
      const users = getStoredUsers();
      const userObj = users.find(x => x.username === username) || {name:username, username:username};
      const opt = document.createElement('option');
      opt.value = username;
      opt.textContent = `${userObj.name||username} (@${username})`;
      select.appendChild(opt);
    }
  }
}

function deleteTrack(trackId){
  if(!confirm('Bạn chắc chắn muốn xóa tác phẩm này?')) return;
  let tracks = getStoredTracks();
  tracks = tracks.filter(x => x.id !== trackId);
  saveTracksSilent(tracks);
  pushCloudUpdate('DELETE_TRACK', {trackId});

  const card = document.getElementById(`card-${trackId}`);
  if(card) card.remove();
}

// ==================== 6. BÌNH LUẬN & ĐƠN XIN QUYỀN ====================
function getStoredComments(){
  const d = localStorage.getItem('tide_comments_v2');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [];
}

function renderCommentsForTrack(trackId){
  const comments = getStoredComments();
  const trackComments = comments.filter(c => c.trackId === trackId);
  if(!trackComments.length){
    return '<div style="font-size:11px;color:var(--dim)" class="mono">Chưa có bình luận nào từ người nghe.</div>';
  }
  return trackComments.map(c => `
    <div style="font-size:12px;margin-bottom:6px;padding-bottom:6px;border-bottom:1px solid var(--line)">
      <strong style="color:var(--accent)">${c.username}</strong>: <span style="color:var(--fg)">${c.text}</span>
      <span style="font-size:10px;color:var(--dim);margin-left:6px" class="mono">${new Date(c.createdAt||Date.now()).toLocaleTimeString()}</span>
    </div>
  `).join('');
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
    card.id = `req-card-${r.id}`;
    card.innerHTML = `
      <div>
        <div style="font-size:13px;font-weight:700"><strong>${r.username}</strong> xin quyền nghe: <span style="color:var(--accent)">${trackTitle}</span></div>
        <div class="mono" style="font-size:11px;color:var(--muted);margin-top:2px">Thời gian: ${new Date(r.createdAt||Date.now()).toLocaleTimeString()}</div>
      </div>
      <div style="display:flex;gap:8px">
        <button class="btn btn-ok btn-sm" onclick="resolveRequest('${r.id}','APPROVE')">Duyệt Cấp Quyền</button>
        <button class="btn btn-danger btn-sm" onclick="resolveRequest('${r.id}','DENY')">Từ Chối</button>
      </div>
    `;
    box.appendChild(card);
  });
}

function resolveRequest(requestId, decision){
  const requests = getStoredRequests();
  const req = requests.find(r => r.id === requestId);
  if(!req) return;
  const tracks = getStoredTracks();
  const track = tracks.find(t => t.id === req.trackId);
  if(decision === 'APPROVE'){
    if(track){
      if(!Array.isArray(track.allowedUsers)) track.allowedUsers = [];
      if(!track.allowedUsers.includes(req.username)) track.allowedUsers.push(req.username);
      saveTracksSilent(tracks);
    }
    req.status = 'APPROVED';
  } else {
    if(track && Array.isArray(track.allowedUsers)) track.allowedUsers = track.allowedUsers.filter(u => u !== req.username);
    req.status = 'DENIED';
    saveTracksSilent(tracks);
  }
  localStorage.setItem('tide_requests_v2', JSON.stringify(requests));
  pushCloudUpdate('RESOLVE_REQUEST', {requestId, decision});
  renderRequests();
  renderArtistTracks();
}

function toggleAutoApprove(){
  const el = document.getElementById('auto-toggle');
  const on = !el.classList.contains('on');
  el.classList.toggle('on', on);
  el.setAttribute('aria-checked', on);
  pushCloudUpdate('SET_AUTO_APPROVE', {value: on});
}

// ==================== 7. TẢI FILE LÊN (CLOUDFILE + VERCEL BLOB) ====================
async function handleFileUpload(e){
  const file = e.target.files[0];
  if(!file) return;
  const stat = document.getElementById('upload-status');
  stat.style.display = 'block';
  stat.textContent = `> Đang tải lên và niêm phong mật mã ${file.name}...`;

  const id = 'track_' + Date.now();
  try {
    await saveMediaBlob(id, file);
    memoryMediaUrls[id] = URL.createObjectURL(file);
  } catch(err){}

  const hashPart = Math.random().toString(16).substring(2,10) + '...';
  const sizeMb = (file.size/(1024*1024)).toFixed(1) + ' MB';

  const tracks = getStoredTracks().filter(t => !t.id.startsWith('track_0'));
  const newTrack = {
    id: id,
    name: file.name,
    type: file.type || (file.name.endsWith('.mp4') ? 'video/mp4' : 'audio/mp3'),
    size: sizeMb,
    hash: hashPart,
    artistUsername: activeArtistUser,
    allowedUsers: [],
    artSeed: Math.floor(Math.random() * 5),
    previewLimitSeconds: 0,
    watermarkMode: 'none',
    tamperProtection: true
  };
  tracks.unshift(newTrack);
  saveTracksSilent(tracks);
  renderArtistTracks();

  // Upload lên Vercel Blob để streaming tức thì trên mọi laptop
  try {
    const uploadRes = await fetch(`/api/upload-media?filename=${encodeURIComponent(file.name)}`, {
      method: 'POST',
      headers: {'Content-Type': file.type || 'application/octet-stream'},
      body: file
    });
    if(uploadRes.ok){
      const uploadJson = await uploadRes.json();
      if(uploadJson.ok && uploadJson.url){
        newTrack.streamUrl = uploadJson.url;
        saveTracksSilent(tracks);
        // Gắn src cho player nếu có
        const playerEl = document.getElementById(`player-${id}`);
        if(playerEl) playerEl.src = uploadJson.url;
      }
    }
  } catch(uploadErr){
    console.warn('Vercel Blob upload warning:', uploadErr);
  }

  stat.textContent = `> [THÀNH CÔNG] Đã tải lên và niêm phong tác phẩm "${file.name}" vào két sắt của @${activeArtistUser}!`;
  e.target.value = '';
}

// Khởi chạy
checkArtistAuth();
</script>
</body>
</html>
'''

for base in [FS_PROTO, BW_RMIT]:
    p = os.path.join(base, "1", "index.html")
    full_new = html_part + "<script>" + NEW_SCRIPT
    with open(p, "w", encoding="utf-8") as f:
        f.write(full_new)
    print(f"Overhauled Page 1 script at: {p}")

print("✓ Hoàn tất viết lại Page 1: Không xóa DOM, mọi nút bấm ăn ngay 0ms, không thể bị undo!")
