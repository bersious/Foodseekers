import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA TRIỆT ĐỂ: LOẠI BỎ TOÀN BỘ NGUYÊN NHÂN GÂY "HOÀN TÁC / UNDO" Ở TRANG 1
# ==============================================================================

def fix_page_1_rock_solid():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Bổ sung lastUserActionTime để chặn fetchCloudState đè lên thao tác vừa click
        old_head_script = "const API_VAULT_URL = '/api/rmit-vault';\nlet isSyncingWithCloud = false;\nlet activeArtistUser = 'alice_artist';"
        new_head_script = """const API_VAULT_URL = '/api/rmit-vault';
let isSyncingWithCloud = false;
let activeArtistUser = localStorage.getItem('tide_logged_artist') || 'alice_artist';
let lastUserActionTime = 0;

function markUserAction(){
  lastUserActionTime = Date.now();
}"""
        if old_head_script in code:
            code = code.replace(old_head_script, new_head_script)

        # 2. Sửa fetchCloudState: nếu người dùng vừa thao tác trong vòng 4 giây -> BỎ QUA FETCH để không bị undo!
        old_fetch_fn = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloud = json.data;

      // 1. Chỉ cập nhật ngầm vào localStorage
      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloud.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloud.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloud.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));

      // 2. Chỉ cập nhật đơn xin quyền (nhẹ nhàng, không làm gián đoạn màn hình chính)
      renderRequests();

      // 3. TUYỆT ĐỐI KHÔNG GỌI renderArtistTracks() HOẶC renderArtistSwitcher() TRONG POLLING!
      // Việc này giúp DOM đứng yên 100%, người dùng tha hồ chọn dropdown, chỉnh âm lượng mà không bao giờ bị giật hay undo!
    }
  } catch (err) {}
}"""

        new_fetch_fn = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  // NẾU NGƯỜI DÙNG VỪA CLICK / THAO TÁC TRONG VÒNG 4 GIÂY: BỎ QUA ĐỂ TRÁNH BỊ UNDO!
  if (Date.now() - lastUserActionTime < 4000) return;

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

      // Chỉ cập nhật danh sách đơn xin quyền nền
      renderRequests();
    }
  } catch (err) {}
}"""
        if old_fetch_fn in code:
            code = code.replace(old_fetch_fn, new_fetch_fn)

        # 3. SỬA showCreateArtistModal: KHÔNG BAO GIỜ GỌI logoutArtist()!
        old_modal_call = """function showCreateArtistModal(){
  logoutArtist();
  switchArtistAuthTab('register');
}"""
        new_modal_call = """function showCreateArtistModal(){
  markUserAction();
  const el = document.getElementById('create-artist-card');
  if(el){
    el.classList.toggle('hidden');
    if(!el.classList.contains('hidden')){
      el.scrollIntoView({behavior:'smooth', block:'center'});
    }
  }
}"""
        if old_modal_call in code:
            code = code.replace(old_modal_call, new_modal_call)

        # 4. Sửa setTrackLimit: KHÔNG GỌI renderArtistTracks(), KHÔNG GỬI DOUBLE POST!
        old_limit_fn = """function setTrackLimit(trackId, limitSeconds){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.previewLimitSeconds = Number(limitSeconds) || 0;
    saveTracks(tracks);
    pushCloudUpdate('SET_PREVIEW_LIMIT', {trackId: trackId, limitSeconds: Number(limitSeconds) || 0});
  }
}"""
        new_limit_fn = """function setTrackLimit(trackId, limitSeconds){
  markUserAction();
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.previewLimitSeconds = Number(limitSeconds) || 0;
    localStorage.setItem('tide_tracks_v2', JSON.stringify(tracks));
    // Gửi 1 bản ghi duy nhất lên cloud, không gửi double post
    pushCloudUpdate('UPDATE_TRACKS', {tracks: tracks});

    // Cập nhật nhãn text trực tiếp tại chỗ, KHÔNG XÓA DOM BÀI HÁT
    const lbl = document.getElementById(`limit-label-${trackId}`);
    if(lbl){
      lbl.textContent = t.previewLimitSeconds > 0 ? `· Giới hạn ${t.previewLimitSeconds}s` : '· Toàn thời lượng';
      lbl.style.color = t.previewLimitSeconds > 0 ? 'var(--warn)' : 'var(--dim)';
    }
  }
}"""
        if old_limit_fn in code:
            code = code.replace(old_limit_fn, new_limit_fn)

        # 5. Sửa setWatermarkMode: KHÔNG GỌI renderArtistTracks(), KHÔNG GỬI DOUBLE POST!
        old_wm_fn = """function setWatermarkMode(trackId, mode){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.watermarkMode = mode || 'none';
    saveTracks(tracks);
    pushCloudUpdate('SET_WATERMARK_MODE', {trackId: trackId, mode: mode});
  }
}"""
        new_wm_fn = """function setWatermarkMode(trackId, mode){
  markUserAction();
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.watermarkMode = mode || 'none';
    localStorage.setItem('tide_tracks_v2', JSON.stringify(tracks));
    pushCloudUpdate('UPDATE_TRACKS', {tracks: tracks});

    const lbl = document.getElementById(`wm-label-${trackId}`);
    if(lbl){
      lbl.textContent = t.watermarkMode === 'duck' 
        ? '· Chèn tiếng quack định kỳ để làm hỏng bản thu lậu' 
        : (t.watermarkMode === 'voice' ? '· Giọng AI đọc tên nghệ sĩ định kỳ' : '· Âm thanh nguyên bản');
    }
  }
}"""
        if old_wm_fn in code:
            code = code.replace(old_wm_fn, new_wm_fn)

        # Gắn ID vào nhãn limit-label và wm-label trong card template để update trực tiếp
        code = code.replace(
            '<span class="mono" style="font-size:11px;color:${t.previewLimitSeconds>0?\'var(--warn)\':\'var(--dim)\'}">',
            '<span class="mono" id="limit-label-${t.id}" style="font-size:11px;color:${t.previewLimitSeconds>0?\'var(--warn)\':\'var(--dim)\'}">'
        )
        code = code.replace(
            '<span class="mono" style="font-size:11px;color:var(--dim)">\n          ${t.watermarkMode===\'duck\'',
            '<span class="mono" id="wm-label-${t.id}" style="font-size:11px;color:var(--dim)">\n          ${t.watermarkMode===\'duck\''
        )

        # 6. Sửa grantUser & revokeUser: KHÔNG GỬI DOUBLE POST
        old_grant_user = """function grantUser(trackId){
  const select = document.getElementById(`select-user-${trackId}`);
  const singleCheckbox = document.getElementById(`single-play-${trackId}`);
  const u = select ? select.value : '';
  const isSinglePlay = singleCheckbox ? singleCheckbox.checked : false;

  if(!u){alert('Vui lòng chọn người nghe!');return;}
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    if(!Array.isArray(t.allowedUsers)) t.allowedUsers = [];
    if(!Array.isArray(t.singlePlayUsers)) t.singlePlayUsers = [];
    if(!t.allowedUsers.includes(u)) t.allowedUsers.push(u);
    if(isSinglePlay && !t.singlePlayUsers.includes(u)) t.singlePlayUsers.push(u);
    saveTracks(tracks);
    pushCloudUpdate('GRANT_ACCESS', {trackId, username:u, isSinglePlay: isSinglePlay});
  }
}"""
        new_grant_user = """function grantUser(trackId){
  markUserAction();
  const select = document.getElementById(`select-user-${trackId}`);
  const singleCheckbox = document.getElementById(`single-play-${trackId}`);
  const u = select ? select.value : '';
  const isSinglePlay = singleCheckbox ? singleCheckbox.checked : false;

  if(!u){alert('Vui lòng chọn một danh tính người nghe từ danh sách!');return;}
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    if(!Array.isArray(t.allowedUsers)) t.allowedUsers = [];
    if(!Array.isArray(t.singlePlayUsers)) t.singlePlayUsers = [];
    if(!t.allowedUsers.includes(u)) t.allowedUsers.push(u);
    if(isSinglePlay && !t.singlePlayUsers.includes(u)) t.singlePlayUsers.push(u);
    saveTracks(tracks);
  }
}"""
        if old_grant_user in code:
            code = code.replace(old_grant_user, new_grant_user)

        old_revoke_user = """function revokeUser(trackId, username){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t && t.allowedUsers){
    t.allowedUsers = t.allowedUsers.filter(x => x !== username);
    saveTracks(tracks);
    pushCloudUpdate('REVOKE_ACCESS', {trackId, username});
  }
}"""
        new_revoke_user = """function revokeUser(trackId, username){
  markUserAction();
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t && t.allowedUsers){
    t.allowedUsers = t.allowedUsers.filter(x => x !== username);
    if(Array.isArray(t.singlePlayUsers)) t.singlePlayUsers = t.singlePlayUsers.filter(x => x !== username);
    saveTracks(tracks);
  }
}"""
        if old_revoke_user in code:
            code = code.replace(old_revoke_user, new_revoke_user)

        # 7. Sửa switchActiveArtist
        old_switch_artist = """function switchActiveArtist(username){
  activeArtistUser = username;
  localStorage.setItem('tide_logged_artist', username);
  renderArtistSwitcher();
  renderArtistTracks();
  renderRequests();
}"""
        new_switch_artist = """function switchActiveArtist(username){
  markUserAction();
  activeArtistUser = username;
  localStorage.setItem('tide_logged_artist', username);
  renderArtistSwitcher();
  renderArtistTracks();
  renderRequests();
}"""
        if old_switch_artist in code:
            code = code.replace(old_switch_artist, new_switch_artist)

        # 8. Sửa resolveRequest (Duyệt / Từ chối đơn)
        old_resolve = """function resolveRequest(requestId, decision){
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
}"""
        new_resolve = """function resolveRequest(requestId, decision){
  markUserAction();
  const requests = getStoredRequests();
  const req = requests.find(r => r.id === requestId);
  if(!req) return;
  const tracks = getStoredTracks();
  const track = tracks.find(t => t.id === req.trackId);
  if(decision === 'APPROVE'){
    if(track){
      if(!Array.isArray(track.allowedUsers)) track.allowedUsers = [];
      if(!track.allowedUsers.includes(req.username)) track.allowedUsers.push(req.username);
      saveTracks(tracks);
    }
    req.status = 'APPROVED';
  } else {
    if(track && Array.isArray(track.allowedUsers)) track.allowedUsers = track.allowedUsers.filter(u => u !== req.username);
    req.status = 'DENIED';
    saveTracks(tracks);
  }
  localStorage.setItem('tide_requests_v2', JSON.stringify(requests));
  pushCloudUpdate('RESOLVE_REQUEST', {requestId, decision});
  renderRequests();
}"""
        if old_resolve in code:
            code = code.replace(old_resolve, new_resolve)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Rock-solid Page 1 saved at: {p}")

fix_page_1_rock_solid()
print("✓ Đã loại bỏ hoàn toàn hiện tượng undo trên Trang 1!")
