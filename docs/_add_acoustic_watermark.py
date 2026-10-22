import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# BỔ SUNG TÍNH NĂNG CHỐNG THU ÂM NGOÀI LOA (WATERMARK TIẾNG VỊT / GIỌNG NÓI AI)
# ==============================================================================

def patch_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Thêm hàm setWatermarkMode vào script Page 1
        wm_fn = """
function setWatermarkMode(trackId, mode){
  const tracks = getStoredTracks();
  const t = tracks.find(x => x.id === trackId);
  if(t){
    t.watermarkMode = mode || 'none';
    saveTracks(tracks);
    pushCloudUpdate('SET_WATERMARK_MODE', {trackId: trackId, mode: mode});
  }
}
"""
        if "function setWatermarkMode(" not in code:
            code = code.replace("function setTrackLimit(", f"{wm_fn}\nfunction setTrackLimit(")

        # Thêm bộ chọn watermark vào từng thẻ bài hát trong renderArtistTracks
        target_html = '<!-- Cài đặt giới hạn thời gian nghe thử của Nghệ sĩ -->'
        wm_html = """      <!-- Cài đặt chống thu âm ngoài loa (Audio Watermark) -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,255,255,0.03);padding:8px 14px;border-radius:10px;border:1px solid var(--line);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--accent);font-weight:700">Chống thu âm ngoài loa:</span>
        <select class="form-input" style="width:auto;padding:5px 10px;font-size:12px;margin:0" onchange="setWatermarkMode('${t.id}', this.value)">
          <option value="none" ${(!t.watermarkMode || t.watermarkMode==='none')?'selected':''}>Không chèn watermark</option>
          <option value="duck" ${t.watermarkMode==='duck'?'selected':''}>Chèn tiếng vịt kêu định kỳ</option>
          <option value="voice" ${t.watermarkMode==='voice'?'selected':''}>Giọng nói AI đọc cảnh báo bản quyền</option>
        </select>
        <span class="mono" style="font-size:11px;color:var(--dim)">
          ${t.watermarkMode==='duck' ? '· Chèn tiếng quack định kỳ để làm hỏng bản thu lậu' : (t.watermarkMode==='voice' ? '· Giọng AI đọc tên nghệ sĩ định kỳ' : '· Âm thanh nguyên bản')}
        </span>
      </div>

      <!-- Cài đặt giới hạn thời gian nghe thử của Nghệ sĩ -->"""

        if target_html in code and "<!-- Cài đặt chống thu âm ngoài loa" not in code:
            code = code.replace(target_html, wm_html)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched watermark settings on Page 1: {p}")

def patch_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Engine phát Watermark (tiếng vịt kêu / giọng AI)
        wm_engine_js = """
// ==================== ACOUSTIC WATERMARK ENGINE ====================
let watermarkTimer = null;
const duckAudio = new Audio('/rmit/tieng-vit.mp3');
duckAudio.volume = 0.85;

function startWatermarkEngine(track){
  stopWatermarkEngine();
  if(!track || !track.watermarkMode || track.watermarkMode === 'none') return;

  const mode = track.watermarkMode;
  const artistName = track.artistUsername || 'Nghệ Sĩ';
  const currentUser = localStorage.getItem('tide_logged_reviewer') || 'Reviewer';

  appendLog(`[WATERMARK ACTIVE] Đã kích hoạt cơ chế chống thu âm: ${mode === 'duck' ? 'Tiếng vịt kêu định kỳ' : 'Giọng nói AI bản quyền'}.`, 'var(--accent)');

  // Phát định kỳ mỗi 8-10 giây
  watermarkTimer = setInterval(() => {
    if(!isPlaying) {
      stopWatermarkEngine();
      return;
    }

    if(mode === 'duck'){
      duckAudio.currentTime = 0;
      duckAudio.play().catch(e => console.log('Duck audio play error:', e));
      appendLog(`[WATERMARK] Đã chèn tiếng vịt kêu để vô hiệu hóa thiết bị thu âm ngoài loa.`, 'var(--warn)');
    } else if(mode === 'voice'){
      if('speechSynthesis' in window){
        const utterance = new SpeechSynthesisUtterance(`Bản quyền thuộc về Nghệ Sĩ ${artistName}. Bản nghe thử bảo mật của ${currentUser}.`);
        utterance.lang = 'vi-VN';
        utterance.rate = 1.05;
        utterance.volume = 0.95;
        window.speechSynthesis.speak(utterance);
        appendLog(`[VOICE WATERMARK] Đã phát giọng đọc xác thực danh tính bản quyền.`, 'var(--warn)');
      }
    }
  }, 9000);
}

function stopWatermarkEngine(){
  if(watermarkTimer){
    clearInterval(watermarkTimer);
    watermarkTimer = null;
  }
  if(duckAudio) duckAudio.pause();
  if('speechSynthesis' in window) window.speechSynthesis.cancel();
}
"""
        if "function startWatermarkEngine(" not in code:
            code = code.replace("function tone(f){", f"{wm_engine_js}\nfunction tone(f){{")

        # Kích hoạt khi play và dừng khi stop
        if "startWatermarkEngine(track);" not in code:
            code = code.replace(
                "appendLog(`[PLAYBACK] Bắt đầu luồng giải mã in-memory cho \"${track.name}\"`, 'var(--accent)');",
                "appendLog(`[PLAYBACK] Bắt đầu luồng giải mã in-memory cho \"${track.name}\"`, 'var(--accent)');\n    startWatermarkEngine(track);"
            )

        if "stopWatermarkEngine();" not in code:
            code = code.replace("function stopAudio(){", "function stopAudio(){\n  stopWatermarkEngine();")

        # Hiển thị badge watermark trong player console nếu có
        old_badge_chunk = 'npBadge.innerHTML = `<span class="badge badge-ok">Đã được duyệt</span>${isSingle?\' <span class="badge badge-warn mono" style="margin-left:6px">Chỉ nghe 1 lần</span>\':\'\'}`;'
        new_badge_chunk = """let wmBadge = '';
    if(track.watermarkMode === 'duck') wmBadge = ' <span class="badge badge-warn mono" style="margin-left:6px">Watermark tiếng vịt</span>';
    else if(track.watermarkMode === 'voice') wmBadge = ' <span class="badge badge-warn mono" style="margin-left:6px">Watermark giọng AI</span>';
    npBadge.innerHTML = `<span class="badge badge-ok">Đã được duyệt</span>${isSingle?' <span class="badge badge-warn mono" style="margin-left:6px">Chỉ nghe 1 lần</span>':''}${wmBadge}`;"""

        if old_badge_chunk in code:
            code = code.replace(old_badge_chunk, new_badge_chunk)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched watermark engine on Page 2: {p}")

patch_page_1()
patch_page_2()
print("✓ Hoàn tất tích hợp Watermark tiếng vịt kêu và giọng nói AI bản quyền!")
