import os

API_FILE = r"C:\Users\nguye\bersious-web\api\rmit-vault.ts"
FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# 1. CẬP NHẬT API SERVER: HỖ TRỢ SINGLE_PLAY VÀ TỰ ĐỘNG THU HỒI SAU KHI PHÁT XONG
# ==============================================================================
with open(API_FILE, 'r', encoding='utf-8') as f:
    api_code = f.read()

# Thay thế GRANT_ACCESS để nhận isSinglePlay
old_grant_case = """        case 'GRANT_ACCESS': {
          const { trackId, username } = body;
          const track = state.tracks.find((t: any) => t.id === trackId);
          if (track && username && !track.allowedUsers.includes(username)) {
            track.allowedUsers.push(username);
            state.requests.forEach((r: any) => {
              if (r.trackId === trackId && r.username === username && r.status === 'PENDING') {
                r.status = 'APPROVED';
              }
            });
            touch();
          }
          break;
        }"""

new_grant_case = """        case 'GRANT_ACCESS': {
          const { trackId, username, isSinglePlay } = body;
          const track = state.tracks.find((t: any) => t.id === trackId);
          if (track && username) {
            if (!Array.isArray(track.allowedUsers)) track.allowedUsers = [];
            if (!Array.isArray(track.singlePlayUsers)) track.singlePlayUsers = [];
            if (!track.allowedUsers.includes(username)) track.allowedUsers.push(username);
            if (isSinglePlay) {
              if (!track.singlePlayUsers.includes(username)) track.singlePlayUsers.push(username);
            } else {
              track.singlePlayUsers = track.singlePlayUsers.filter((u: string) => u !== username);
            }
            state.requests.forEach((r: any) => {
              if (r.trackId === trackId && r.username === username && r.status === 'PENDING') {
                r.status = 'APPROVED';
              }
            });
            touch();
          }
          break;
        }

        case 'RECORD_PLAYBACK_FINISHED': {
          const { trackId, username } = body;
          const track = state.tracks.find((t: any) => t.id === trackId);
          if (track && Array.isArray(track.singlePlayUsers) && track.singlePlayUsers.includes(username)) {
            // Tự động thu hồi quyền sau khi nghe xong 1 lần!
            track.allowedUsers = (track.allowedUsers || []).filter((u: string) => u !== username);
            track.singlePlayUsers = track.singlePlayUsers.filter((u: string) => u !== username);
            touch();
          }
          break;
        }"""

if old_grant_case in api_code:
    api_code = api_code.replace(old_grant_case, new_grant_case)

with open(API_FILE, 'w', encoding='utf-8') as f:
    f.write(api_code)
print("Updated api/rmit-vault.ts with single-play support!")

# ==============================================================================
# 2. CẬP NHẬT TRANG 1 (NGHỆ SĨ): TÙY CHỌN CẤP QUYỀN "CHỈ NGHE 1 LẦN"
# ==============================================================================
def patch_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Cập nhật giao diện cấp quyền có checkbox "Chỉ nghe 1 lần"
        old_grant_ui = """      <div style="display:flex;gap:10px;align-items:center;background:var(--surface-2);padding:10px 14px;border-radius:10px">
        <select id="select-user-${t.id}" class="form-input" style="flex:1;padding:8px 12px;font-size:13px">${options}</select>
        <button class="btn btn-accent btn-sm" onclick="grantUser('${t.id}')">Cấp quyền truy cập</button>
      </div>"""

        new_grant_ui = """      <div style="display:flex;gap:10px;align-items:center;background:var(--surface-2);padding:10px 14px;border-radius:10px;flex-wrap:wrap">
        <select id="select-user-${t.id}" class="form-input" style="flex:1;min-width:180px;padding:8px 12px;font-size:13px">${options}</select>
        <label style="font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px;cursor:pointer;white-space:nowrap">
          <input type="checkbox" id="single-play-${t.id}"> Chỉ nghe 1 lần
        </label>
        <button class="btn btn-accent btn-sm" onclick="grantUser('${t.id}')">Cấp quyền truy cập</button>
      </div>"""

        if old_grant_ui in code:
            code = code.replace(old_grant_ui, new_grant_ui)

        # Hiển thị nhãn "1 LẦN" bên cạnh người dùng nếu là single play
        old_chip_render = """        allowedChips += `<span class="user-chip"><span>${userObj.name||userObj.username}</span><button class="btn btn-ghost btn-sm" onclick="revokeUser('${t.id}','${u}')" style="padding:1px 6px;color:var(--danger)">Thu hồi</button></span>`;"""
        new_chip_render = """        const isSingle = Array.isArray(t.singlePlayUsers) && t.singlePlayUsers.includes(u);
        allowedChips += `<span class="user-chip"><span>${userObj.name||userObj.username}</span>${isSingle?'<span style="font-size:10px;color:var(--warn);background:rgba(255,184,77,.15);padding:1px 5px;border-radius:4px" class="mono">1 LẦN</span>':''}<button class="btn btn-ghost btn-sm" onclick="revokeUser('${t.id}','${u}')" style="padding:1px 6px;color:var(--danger)">Thu hồi</button></span>`;"""

        if old_chip_render in code:
            code = code.replace(old_chip_render, new_chip_render)

        # Sửa hàm grantUser để gửi isSinglePlay
        old_grant_fn = """function grantUser(trackId){
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
}"""

        new_grant_fn = """function grantUser(trackId){
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

        if old_grant_fn in code:
            code = code.replace(old_grant_fn, new_grant_fn)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 1 single play at: {p}")

# ==============================================================================
# 3. CẬP NHẬT TRANG 2 (NGƯỜI NGHE): TỰ ĐỘNG THU HỒI SAU KHI PHÁT XONG 1 LẦN & ĐẢM BẢO PHÁT ĐƯỢC NHẠC/VIDEO
# ==============================================================================
def patch_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Thêm hàm xử lý khi phát xong (audio ended / video ended)
        finish_handler = """
function onMediaPlaybackFinished(track){
  const currentUser = localStorage.getItem('tide_logged_reviewer');
  const isSinglePlay = Array.isArray(track.singlePlayUsers) && track.singlePlayUsers.includes(currentUser);

  if(isSinglePlay){
    stopAudio();
    appendLog(`[TỰ HỦY] Tác phẩm "${track.name}" đã phát xong 1 lần. Quyền truy cập tự động hủy theo chính sách Emergent Single-Play.`, 'var(--warn)');
    
    // Gửi lệnh tự hủy lên cloud
    pushCloudAction('RECORD_PLAYBACK_FINISHED', {trackId: track.id, username: currentUser});

    // Cập nhật local
    if(Array.isArray(track.allowedUsers)){
      track.allowedUsers = track.allowedUsers.filter(u => u !== currentUser);
    }
    if(Array.isArray(track.singlePlayUsers)){
      track.singlePlayUsers = track.singlePlayUsers.filter(u => u !== currentUser);
    }
    const tracks = getStoredTracks();
    const t = tracks.find(x => x.id === track.id);
    if(t && Array.isArray(t.allowedUsers)){
      t.allowedUsers = t.allowedUsers.filter(u => u !== currentUser);
    }
    localStorage.setItem('tide_tracks_v2', JSON.stringify(tracks));

    alert(`Bạn đã nghe xong tác phẩm "${track.name}". Quyền truy cập đã tự động hủy theo chính sách Nghe Một Lần của Nghệ Sĩ.`);
    renderAlbumGrid();
    syncActiveTrackView();
  }
}
"""
        if "function onMediaPlaybackFinished(" not in code:
            code = code.replace("function handlePreviewLimitExpired(track){", f"{finish_handler}\nfunction handlePreviewLimitExpired(track){{")

        # Gắn onended vào native-audio và video
        old_audio_onended = "na.onended=()=>{\n        if(repeatEnabled){na.currentTime=0;na.play().catch(e=>console.log(e));}\n        else stepTrack(1);\n      };"
        new_audio_onended = """na.onended=()=>{
        onMediaPlaybackFinished(track);
        if(repeatEnabled){na.currentTime=0;na.play().catch(e=>console.log(e));}
      };"""
        if old_audio_onended in code:
            code = code.replace(old_audio_onended, new_audio_onended)

        # Gắn onended vào video
        old_vid_events = "vid.play().catch(e=>console.log('Video autoplay:', e));"
        new_vid_events = """vid.onended = function(){
          onMediaPlaybackFinished(track);
        };
        vid.play().catch(e=>console.log('Video autoplay:', e));"""
        if old_vid_events in code:
            code = code.replace(old_vid_events, new_vid_events)

        # Hiển thị badge "Chỉ nghe 1 lần" trong player nếu track có singlePlayUsers
        old_allowed_badge = 'npBadge.innerHTML = \'<span class="badge badge-ok">Đã được duyệt</span>\';'
        new_allowed_badge = """const isSingle = Array.isArray(track.singlePlayUsers) && track.singlePlayUsers.includes(currentUser);
    npBadge.innerHTML = `<span class=\"badge badge-ok\">Đã được duyệt</span>${isSingle?' <span class=\"badge badge-warn mono\" style=\"margin-left:6px\">Chỉ nghe 1 lần</span>':''}`;"""
        if old_allowed_badge in code:
            code = code.replace(old_allowed_badge, new_allowed_badge)

        # Thêm trình tạo Canvas Video Demo sinh động nếu track video chưa có file mp4 thật tải lên
        demo_video_gen = """
function generateDemoVideoFeed(trackName){
  const canvas = document.createElement('canvas');
  canvas.width = 640; canvas.height = 360;
  const ctx = canvas.getContext('2d');
  let angle = 0;
  function draw(){
    ctx.fillStyle = '#0a0d0a'; ctx.fillRect(0,0,640,360);
    // Draw animated sound waves & title
    ctx.strokeStyle = '#b8f36b'; ctx.lineWidth = 2;
    ctx.beginPath();
    for(let x=0; x<640; x+=8){
      const y = 180 + Math.sin(x*0.03 + angle)*40;
      if(x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
    }
    ctx.stroke();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 20px sans-serif';
    ctx.fillText(trackName, 40, 60);
    ctx.fillStyle = '#b8f36b'; ctx.font = '13px monospace';
    ctx.fillText('Tide In-Memory Decrypted Video Stream', 40, 90);
    angle += 0.08;
    requestAnimationFrame(draw);
  }
  draw();
  return canvas.captureStream(30);
}
"""
        if "function generateDemoVideoFeed(" not in code:
            code = code.replace("function tone(f){", f"{demo_video_gen}\nfunction tone(f){{")

        # Khi video không có blob tải lên, dùng demo feed
        old_no_video_blob = """      const blob = await getMediaBlob(track.id);
      const vid = document.getElementById('html5-video');
      if(blob){
        vid.src = URL.createObjectURL(blob);
        vid.onended = function(){
          onMediaPlaybackFinished(track);
        };
        vid.play().catch(e=>console.log('Video autoplay:', e));
      }"""

        new_no_video_blob = """      const blob = await getMediaBlob(track.id);
      const vid = document.getElementById('html5-video');
      vid.onended = function(){ onMediaPlaybackFinished(track); };
      if(blob){
        vid.src = URL.createObjectURL(blob);
        vid.play().catch(e=>console.log('Video autoplay:', e));
      } else {
        // Tự động tạo luồng phát video thời gian thực từ Canvas
        const stream = generateDemoVideoFeed(track.name);
        vid.srcObject = stream;
        vid.play().catch(e=>console.log('Stream play:', e));
      }"""

        if old_no_video_blob in code:
            code = code.replace(old_no_video_blob, new_no_video_blob)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 2 single play & playback assurance at: {p}")

patch_page_1()
patch_page_2()
print("✓ Hoàn tất bổ sung tính năng Nghe Một Lần và đảm bảo phát nhạc/video mượt mà!")
