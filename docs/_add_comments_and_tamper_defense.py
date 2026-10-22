import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# BỔ SUNG:
# 1. HỆ THỐNG BÌNH LUẬN & GÓP Ý THẨM ĐỊNH CHO NGHỆ SĨ
# 2. CƠ CHẾ PHÁT HIỆN CAN THIỆP PHẦN MỀM THỨ 3 & TỰ ĐỘNG THU HỒI QUYỀN TỨC THÌ
# ==============================================================================

def patch_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Thêm hàm toggleTrackTamperProtection
        tamper_fn = """
function toggleTrackTamperProtection(trackId){
  markUserAction();
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.tamperProtection = !t.tamperProtection;
    saveTracks(tracks);
    renderArtistTracks();
  }
}
"""
        if "function toggleTrackTamperProtection(" not in code:
            code = code.replace("function setWatermarkMode(", f"{tamper_fn}\nfunction setWatermarkMode(")

        # Thêm mục cài đặt Tamper Protection và Hộp bình luận vào từng track card trên Page 1
        old_card_settings = "<!-- Cài đặt chống thu âm ngoài loa (Audio Watermark) -->"
        new_card_settings = """<!-- Cài đặt chống can thiệp phần mềm thứ 3 -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,82,108,0.06);padding:8px 14px;border-radius:10px;border:1px solid rgba(255,82,108,0.25);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--danger);font-weight:700">Tự động thu hồi khi phát hiện can thiệp:</span>
        <label class="toggle-switch ${t.tamperProtection?'on':''}" onclick="toggleTrackTamperProtection('${t.id}')">
          <span class="toggle-knob"></span>
        </label>
        <span class="mono" style="font-size:11px;color:var(--dim)">
          ${t.tamperProtection ? 'Đang bật bảo vệ chống can thiệp và ghi âm lậu' : 'Đang tắt'}
        </span>
      </div>

      <!-- Cài đặt chống thu âm ngoài loa (Audio Watermark) -->"""

        if old_card_settings in code and "<!-- Cài đặt chống can thiệp" not in code:
            code = code.replace(old_card_settings, new_card_settings)

        # Thêm hiển thị bình luận vào cuối track card
        old_card_end = """      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${allowedChips}</div>
      </div>"""

        new_card_end = """      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${allowedChips}</div>
      </div>

      <!-- Khung hiển thị bình luận từ Người Nghe -->
      <div style="margin-bottom:14px;background:#050705;border:1px solid var(--line);border-radius:10px;padding:12px">
        <div style="font-size:11px;font-weight:700;color:var(--accent);margin-bottom:6px">
          GÓP Ý & BÌNH LUẬN TỪ NGƯỜI NGHE:
        </div>
        <div id="comments-box-${t.id}">
          ${renderCommentsForTrack(t.id)}
        </div>
      </div>"""

        if old_card_end in code and "<!-- Khung hiển thị bình luận" not in code:
            code = code.replace(old_card_end, new_card_end)

        # Thêm hàm helper renderCommentsForTrack
        comments_helper = """
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
      <strong>${c.username}</strong>: <span style="color:var(--fg)">${c.text}</span>
      <span style="font-size:10px;color:var(--dim);margin-left:6px" class="mono">${new Date(c.createdAt||Date.now()).toLocaleTimeString()}</span>
    </div>
  `).join('');
}
"""
        if "function renderCommentsForTrack(" not in code:
            code = code.replace("function renderArtistTracks(){", f"{comments_helper}\nfunction renderArtistTracks(){{")

        # Lưu comments trong fetchCloudState của Page 1
        old_cloud_store = "localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));"
        new_cloud_store = "localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));\n      localStorage.setItem('tide_comments_v2', JSON.stringify(cloud.comments || []));"
        if old_cloud_store in code and "tide_comments_v2" not in code:
            code = code.replace(old_cloud_store, new_cloud_store)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 1 with comments & tamper toggle at: {p}")

def patch_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Lưu comments trong fetchCloudState của Page 2
        old_p2_store = "localStorage.setItem('tide_artists', JSON.stringify(cloudStateCache.artists || []));"
        new_p2_store = "localStorage.setItem('tide_artists', JSON.stringify(cloudStateCache.artists || []));\n      localStorage.setItem('tide_comments_v2', JSON.stringify(cloudStateCache.comments || []));"
        if old_p2_store in code and "tide_comments_v2" not in code:
            code = code.replace(old_p2_store, new_p2_store)

        # Thêm khung bình luận dưới player card
        comments_ui_html = """
    <!-- KHUNG GÓP Ý & BÌNH LUẬN CHO NGHỆ SĨ -->
    <div class="card" style="margin-top:20px;background:linear-gradient(145deg,#141914,#0e130f)">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
        <h3 style="font-size:14px;font-weight:700">Góp ý & Đánh giá gửi tới Nghệ Sĩ</h3>
        <span class="mono" style="font-size:11px;color:var(--muted)" id="comment-track-target">Bài hát hiện tại</span>
      </div>
      <div style="display:flex;gap:10px;margin-bottom:14px">
        <input type="text" id="comment-input" class="form-input" style="flex:1" placeholder="Nhập nhận xét về bản mix, vocal, độ dày của bass..." onkeydown="if(event.key==='Enter')submitReviewerComment()">
        <button class="btn btn-accent btn-sm" onclick="submitReviewerComment()">Gửi góp ý</button>
      </div>
      <div id="reviewer-comments-list" style="max-height:160px;overflow-y:auto;display:flex;flex-direction:column;gap:8px">
      </div>
    </div>
"""
        if "<!-- KHUNG GÓP Ý & BÌNH LUẬN CHO NGHỆ SĨ -->" not in code:
            code = code.replace('<!-- BẢNG NHẬT KÝ ĐÁNH GIÁ QUYỀN HẠN TIDECLOAK', f'{comments_ui_html}\n    <!-- BẢNG NHẬT KÝ ĐÁNH GIÁ QUYỀN HẠN TIDECLOAK')

        # Thêm logic gửi bình luận và nhận diện can thiệp (Tamper Detection Engine)
        tamper_and_comments_js = """
// ==================== BÌNH LUẬN & GÓP Ý CHO NGHỆ SĨ ====================
function getStoredComments(){
  const d = localStorage.getItem('tide_comments_v2');
  if(d){try{return JSON.parse(d)}catch(e){}}
  return [];
}

function renderReviewerComments(){
  const list = document.getElementById('reviewer-comments-list');
  const targetLabel = document.getElementById('comment-track-target');
  if(!list) return;

  const tracks = getStoredTracks();
  const track = tracks.find(x => x.id === activeTrackId);
  if(!track){
    list.innerHTML = '<div style="font-size:12px;color:var(--muted)">Chọn một bài hát để xem và gửi nhận xét.</div>';
    return;
  }

  if(targetLabel) targetLabel.textContent = track.name;
  const comments = getStoredComments();
  const trackComments = comments.filter(c => c.trackId === track.id);

  if(!trackComments.length){
    list.innerHTML = '<div style="font-size:12px;color:var(--dim)" class="mono">Chưa có bình luận nào cho bài hát này. Hãy để lại nhận xét đầu tiên!</div>';
    return;
  }

  list.innerHTML = trackComments.map(c => `
    <div style="background:var(--surface-2);border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:12px">
      <div style="display:flex;justify-content:space-between;margin-bottom:2px">
        <strong style="color:var(--accent)">${c.username}</strong>
        <span style="font-size:10px;color:var(--dim)" class="mono">${new Date(c.createdAt||Date.now()).toLocaleTimeString()}</span>
      </div>
      <div style="color:var(--fg)">${c.text}</div>
    </div>
  `).join('');
}

function submitReviewerComment(){
  const input = document.getElementById('comment-input');
  const text = input ? input.value.trim() : '';
  const currentUser = localStorage.getItem('tide_logged_reviewer') || 'Reviewer';
  if(!text){ alert('Vui lòng nhập nội dung nhận xét!'); return; }
  if(!activeTrackId){ alert('Vui lòng chọn bài hát trước khi bình luận!'); return; }

  const newComment = {
    id: 'cmt_' + Date.now(),
    trackId: activeTrackId,
    username: currentUser,
    text: text,
    createdAt: new Date().toISOString()
  };

  const comments = getStoredComments();
  comments.unshift(newComment);
  localStorage.setItem('tide_comments_v2', JSON.stringify(comments));

  pushCloudAction('ADD_COMMENT', {
    trackId: activeTrackId,
    username: currentUser,
    text: text
  });

  input.value = '';
  renderReviewerComments();
  appendLog(`[GÓP Ý] Đã gửi nhận xét tới Nghệ Sĩ cho bài hát.`, 'var(--ok)');
}

// ==================== CƠ CHẾ PHÁT HIỆN CAN THIỆP & TỰ ĐỘNG THU HỒI ====================
let tamperWatchdogTimer = null;

function startTamperWatchdog(track){
  stopTamperWatchdog();
  if(!track || !track.tamperProtection) return;

  tamperWatchdogTimer = setInterval(() => {
    if(!isPlaying) return;

    // 1. Phát hiện mở DevTools bằng chênh lệch kích thước cửa sổ
    const widthDiff = window.outerWidth - window.innerWidth;
    const heightDiff = window.outerHeight - window.innerHeight;
    const isDevToolsOpen = widthDiff > 160 || heightDiff > 160;

    // 2. Phát hiện khi trình duyệt bị mất focus (chuyển sang phần mềm ghi màn hình OBS/Screen Recorder)
    const isWindowBlurred = document.hidden || document.visibilityState === 'hidden';

    if(isDevToolsOpen || isWindowBlurred){
      triggerInstantTamperRevocation(track, isDevToolsOpen ? 'Phát hiện mở công cụ DevTools / Trích xuất luồng' : 'Phát hiện chuyển sang ứng dụng quay quét màn hình');
    }
  }, 1000);
}

function stopTamperWatchdog(){
  if(tamperWatchdogTimer){
    clearInterval(tamperWatchdogTimer);
    tamperWatchdogTimer = null;
  }
}

function triggerInstantTamperRevocation(track, reason){
  stopAudio();
  stopTamperWatchdog();
  const currentUser = localStorage.getItem('tide_logged_reviewer');

  appendLog(`[CẢNH BÁO CAN THIỆP] ${reason}! Kích hoạt thu hồi quyền khẩn cấp.`, 'var(--danger)');

  // Thu hồi quyền hạn ngay lập tức trên cloud
  pushCloudAction('REVOKE_ACCESS', { trackId: track.id, username: currentUser });

  // Thu hồi quyền cục bộ
  if(Array.isArray(track.allowedUsers)){
    track.allowedUsers = track.allowedUsers.filter(u => u !== currentUser);
  }
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === track.id);
  if(t && Array.isArray(t.allowedUsers)){
    t.allowedUsers = t.allowedUsers.filter(u => u !== currentUser);
  }
  localStorage.setItem('tide_tracks_v2', JSON.stringify(tracks));

  alert(`CẢNH BÁO AN NINH TIDECLOAK:\n${reason}!\nTheo chính sách bảo vệ tác phẩm của Nghệ Sĩ, quyền nghe của bạn đã bị thu hồi ngay lập tức.`);

  renderAlbumGrid();
  syncActiveTrackView();
}
"""
        if "function submitReviewerComment(" not in code:
            code = code.replace("function appendLog(", f"{tamper_and_comments_js}\nfunction appendLog(")

        # Gọi renderReviewerComments() trong syncActiveTrackView()
        if "renderReviewerComments();" not in code:
            code = code.replace("npTitle.textContent = track.name;", "npTitle.textContent = track.name;\n  renderReviewerComments();")

        # Bật startTamperWatchdog khi phát nhạc, tắt khi dừng nhạc
        if "startTamperWatchdog(track);" not in code:
            code = code.replace("startWatermarkEngine(track);", "startWatermarkEngine(track);\n    startTamperWatchdog(track);")

        if "stopTamperWatchdog();" not in code:
            code = code.replace("stopWatermarkEngine();", "stopWatermarkEngine();\n  stopTamperWatchdog();")

        # Hiển thị badge chống can thiệp nếu bật
        old_badges_render = "if(track.watermarkMode === 'duck') wmBadge = ' <span class=\"badge badge-warn mono\" style=\"margin-left:6px\">Watermark tiếng vịt</span>';"
        new_badges_render = """let tamperBadge = '';
    if(track.tamperProtection) tamperBadge = ' <span class=\"badge badge-danger mono\" style=\"margin-left:6px\">Chống can thiệp: Bật</span>';
    if(track.watermarkMode === 'duck') wmBadge = ' <span class=\"badge badge-warn mono\" style=\"margin-left:6px\">Watermark tiếng vịt</span>';"""
        if old_badges_render in code:
            code = code.replace(old_badges_render, new_badges_render)
            code = code.replace("${wmBadge}", "${tamperBadge}${wmBadge}")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 2 with comments & tamper detection at: {p}")

patch_page_1()
patch_page_2()
print("✓ Hoàn tất tích hợp Hệ thống Bình luận & Cơ chế chống can thiệp tự động thu hồi!")
