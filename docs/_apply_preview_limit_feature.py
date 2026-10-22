import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# BỔ SUNG TÍNH NĂNG GIỚI HẠN THỜI GIAN NGHE / XEM THỬ CHO NGHỆ SĨ & NGƯỜI NGHE
# ==============================================================================

def patch_p1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Thêm hàm setTrackLimit vào script Page 1
        limit_fn = """
function setTrackLimit(trackId, limitSeconds){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.previewLimitSeconds = Number(limitSeconds) || 0;
    saveTracks(tracks);
    pushCloudUpdate('SET_PREVIEW_LIMIT', {trackId: trackId, limitSeconds: Number(limitSeconds) || 0});
  }
}
"""
        if "function setTrackLimit(" not in code:
            code = code.replace("function deleteTrack(trackId){", f"{limit_fn}\nfunction deleteTrack(trackId){{")

        # Thêm thanh chọn giới hạn thời gian nghe thử vào từng track card trên Page 1
        old_track_card_inner = """      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${allowedChips}</div>
      </div>"""

        new_track_card_inner = """      <!-- Cài đặt giới hạn thời gian nghe thử của Nghệ sĩ -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,255,255,0.03);padding:8px 14px;border-radius:10px;border:1px solid var(--line);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--accent);font-weight:700">⏱️ Giới Hạn Thời Gian Xem / Nghe Thử:</span>
        <select class="form-input" style="width:auto;padding:5px 10px;font-size:12px;margin:0" onchange="setTrackLimit('${t.id}', this.value)">
          <option value="0" ${(!t.previewLimitSeconds || t.previewLimitSeconds==0)?'selected':''}>🎵 Toàn bộ bài hát (Full 100%)</option>
          <option value="10" ${t.previewLimitSeconds==10?'selected':''}>⏱️ 10 giây đầu (Teaser ngắn)</option>
          <option value="15" ${t.previewLimitSeconds==15?'selected':''}>⏱️ 15 giây đầu (Snippet)</option>
          <option value="30" ${t.previewLimitSeconds==30?'selected':''}>⏱️ 30 giây đầu (Sample 30s)</option>
          <option value="60" ${t.previewLimitSeconds==60?'selected':''}>⏱️ 60 giây đầu (1 phút Demo)</option>
        </select>
        <span class="mono" style="font-size:11px;color:${t.previewLimitSeconds>0?'var(--warn)':'var(--dim)'}">
          ${t.previewLimitSeconds>0 ? `(Đang giới hạn người nghe chỉ được nghe ${t.previewLimitSeconds}s đầu)` : '(Người nghe được nghe toàn bộ bài)'}
        </span>
      </div>

      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${allowedChips}</div>
      </div>"""

        if old_track_card_inner in code:
            code = code.replace(old_track_card_inner, new_track_card_inner)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 1 preview limit at: {p}")

def patch_p2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Thêm khung thông báo hết thời gian nghe thử vào player box
        limit_alert_html = """
      <!-- THÔNG BÁO HẾT THỜI GIAN NGHE THỬ GIỚI HẠN -->
      <div id="preview-limit-alert" class="hidden" style="background:var(--warn-dim);border:1px solid rgba(255,184,77,.35);border-radius:12px;padding:16px;margin-top:16px;text-align:center">
        <div style="font-size:14px;font-weight:700;color:var(--warn);margin-bottom:4px" id="limit-alert-title">
          ⏱️ ĐÃ HẾT THỜI LƯỢNG NGHE THỬ
        </div>
        <div style="font-size:12px;color:var(--muted);margin-bottom:12px" id="limit-alert-desc">
          Nghệ sĩ giới hạn bản xem thử này. Khóa giải mã phiên đã tạm ngắt theo chính sách TideCloak.
        </div>
        <button class="btn btn-accent btn-sm" onclick="requestAccessCurrentTrack()">
          🔑 Gửi Yêu Cầu Xin Cấp Quyền Nghe Full Toàn Bộ Bài
        </button>
      </div>
"""
        if "<!-- THÔNG BÁO HẾT THỜI GIAN NGHE THỬ GIỚI HẠN -->" not in code:
            code = code.replace('<audio id="native-audio" style="display:none"></audio>', f'{limit_alert_html}\n      <audio id="native-audio" style="display:none"></audio>')

        # 2. Xử lý ontimeupdate cho video và audio để ngắt khi chạm ngưỡng previewLimitSeconds
        old_audio_ontimeupdate = """        const cur=Math.floor(na.currentTime), dur=Math.floor(na.duration)||222;
        document.getElementById('cur').textContent=Math.floor(cur/60)+':'+String(cur%60).padStart(2,'0');
        document.getElementById('dur').textContent=Math.floor(dur/60)+':'+String(dur%60).padStart(2,'0');
        document.getElementById('fill').style.width=((cur/dur)*100)+'%';"""

        new_audio_ontimeupdate = """        const cur=Math.floor(na.currentTime), dur=Math.floor(na.duration)||222;
        document.getElementById('cur').textContent=Math.floor(cur/60)+':'+String(cur%60).padStart(2,'0');
        document.getElementById('dur').textContent=Math.floor(dur/60)+':'+String(dur%60).padStart(2,'0');
        document.getElementById('fill').style.width=((cur/dur)*100)+'%';

        // Kiểm tra giới hạn thời lượng nghe thử
        if(track.previewLimitSeconds > 0 && na.currentTime >= track.previewLimitSeconds){
          na.pause();
          handlePreviewLimitExpired(track);
        }"""

        if old_audio_ontimeupdate in code:
            code = code.replace(old_audio_ontimeupdate, new_audio_ontimeupdate)

        # Xử lý video ontimeupdate
        old_vid_mount = "vid.play().catch(e=>console.log('Video autoplay:', e));"
        new_vid_mount = """vid.ontimeupdate = function(){
          if(track.previewLimitSeconds > 0 && vid.currentTime >= track.previewLimitSeconds){
            vid.pause();
            handlePreviewLimitExpired(track);
          }
        };
        vid.play().catch(e=>console.log('Video autoplay:', e));"""

        if old_vid_mount in code:
            code = code.replace(old_vid_mount, new_vid_mount)

        # Xử lý timerInterval (synth audio)
        old_synth_timer = """      timerInterval=setInterval(()=>{
        t++;
        document.getElementById('cur').textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0');
        document.getElementById('fill').style.width=Math.min(t/222*100,100)+'%';
      },1000);"""

        new_synth_timer = """      timerInterval=setInterval(()=>{
        t++;
        document.getElementById('cur').textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0');
        document.getElementById('fill').style.width=Math.min(t/222*100,100)+'%';
        if(track.previewLimitSeconds > 0 && t >= track.previewLimitSeconds){
          handlePreviewLimitExpired(track);
        }
      },1000);"""

        if old_synth_timer in code:
            code = code.replace(old_synth_timer, new_synth_timer)

        # Thêm hàm handlePreviewLimitExpired
        limit_handler_js = """
function handlePreviewLimitExpired(track){
  stopAudio();
  const alertBox = document.getElementById('preview-limit-alert');
  const title = document.getElementById('limit-alert-title');
  const desc = document.getElementById('limit-alert-desc');
  if(alertBox){
    alertBox.classList.remove('hidden');
    title.textContent = `⏱️ ĐÃ HẾT ${track.previewLimitSeconds} GIÂY NGHE THỬ GIỚI HẠN`;
    desc.textContent = `Nghệ sĩ ${track.artistUsername} thiết lập chính sách chỉ cho phép nghe thử ${track.previewLimitSeconds} giây đầu. Chìa khóa phiên TideCloak JIT đã tự động hủy.`;
  }
  appendLog(`[HẾT HẠN PREVIEW] Chạm mốc giới hạn ${track.previewLimitSeconds}s. Luồng giải mã đã tự động ngắt theo chính sách Quorum.`, 'var(--warn)');
}
"""
        if "function handlePreviewLimitExpired(" not in code:
            code = code.replace("function stopAudio(){", f"{limit_handler_js}\nfunction stopAudio(){{")

        # Khi bấm Play mới, ẩn thông báo alert đi
        if "document.getElementById('preview-limit-alert').classList.add('hidden');" not in code:
            code = code.replace("if(isPlaying){", "if(isPlaying){\n    const pAlert = document.getElementById('preview-limit-alert'); if(pAlert) pAlert.classList.add('hidden');")

        # Hiển thị badge trên thẻ album card nếu bài hát có previewLimitSeconds
        old_card_meta = '<div class="card-sub mono">${t.size} · ${isVideo?\'Video Master\':\'Audio Master\'}</div>'
        new_card_meta = '<div class="card-sub mono">${t.size} · ${isVideo?\'Video Master\':\'Audio Master\'}${t.previewLimitSeconds>0?` · <span style=\"color:var(--warn)\">⏱️ ${t.previewLimitSeconds}s đầu</span>`:""}</div>'
        if old_card_meta in code:
            code = code.replace(old_card_meta, new_card_meta)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 2 preview limit at: {p}")

patch_p1()
patch_p2()
print("✓ Hoàn tất bổ sung tính năng giới hạn thời gian nghe thử X giây đầu!")
