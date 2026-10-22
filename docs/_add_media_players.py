import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# BỔ SUNG TRÌNH PHÁT NHẠC VÀ XEM VIDEO CHO TRANG 1 (NGHỆ SĨ) VÀ TRANG 2 (NGƯỜI NGHE)
# ==============================================================================

def patch_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Thêm khung Player kiểm âm của Nghệ Sĩ ngay trên danh sách tác phẩm
        preview_box_html = """
    <!-- TRÌNH PHÁT KIỂM ÂM & XEM VIDEO CỦA NGHỆ SĨ -->
    <div id="artist-preview-box" class="card hidden" style="border-color:var(--accent);background:linear-gradient(145deg,#151c16,#0e130f);margin-bottom:20px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
        <div style="display:flex;align-items:center;gap:10px">
          <span style="font-size:18px">🎧</span>
          <div>
            <div style="font-size:14px;font-weight:700" id="artist-preview-name">Tên tác phẩm</div>
            <div style="font-size:11px;color:var(--muted)" class="mono" id="artist-preview-sub">Đang phát kiểm âm trực tiếp từ bộ nhớ RAM</div>
          </div>
        </div>
        <button class="btn btn-ghost btn-sm" onclick="closeArtistPreview()" style="color:var(--muted)">✕ Tắt Trình Phát</button>
      </div>

      <!-- Khung video nếu là video -->
      <div id="artist-video-wrap" class="hidden" style="margin-bottom:10px">
        <video id="artist-preview-video" controls style="width:100%;max-height:420px;border-radius:12px;background:#000;display:block"></video>
      </div>

      <!-- Khung audio nếu là audio -->
      <div id="artist-audio-wrap" class="hidden">
        <audio id="artist-preview-audio" controls style="width:100%;border-radius:8px;outline:none"></audio>
      </div>
    </div>
"""
        if "<!-- TRÌNH PHÁT KIỂM ÂM & XEM VIDEO CỦA NGHỆ SĨ -->" not in code:
            code = code.replace(
                '<!-- Tracks List -->\n    <div class="card">',
                f'{preview_box_html}\n    <!-- Tracks List -->\n    <div class="card">'
            )

        # 2. Thêm nút "▶ Phát / Xem Thử" trên từng thẻ bài hát của Nghệ Sĩ
        old_track_header = """        <div>
          <div class="track-title">${isVideo?'🎬 ':'🎵 '}${t.name}</div>
          <div class="track-info mono">${t.size} · SHA256: ${t.hash} · ${isVideo?'Video Master':'Audio Master'}</div>
        </div>
      </div>
      <button class="btn btn-ghost btn-sm" onclick="deleteTrack('${t.id}')" style="color:var(--danger)">Xóa Tác Phẩm</button>"""

        new_track_header = """        <div>
          <div class="track-title">${isVideo?'🎬 ':'🎵 '}${t.name}</div>
          <div class="track-info mono">${t.size} · SHA256: ${t.hash} · ${isVideo?'Video Master':'Audio Master'}</div>
        </div>
      </div>
      <div style="display:flex;gap:8px;align-items:center">
        <button class="btn btn-accent btn-sm" onclick="playArtistMedia('${t.id}')">${isVideo?'🎬 Xem Video':'▶ Nghe Bản Thu'}</button>
        <button class="btn btn-ghost btn-sm" onclick="deleteTrack('${t.id}')" style="color:var(--danger)">Xóa</button>
      </div>"""

        if old_track_header in code:
            code = code.replace(old_track_header, new_track_header)

        # 3. Thêm hàm getMediaBlob và playArtistMedia trong script của Trang 1
        artist_playback_js = """
async function getMediaBlob(id){
  try {
    const db=await openDB();
    const local = await new Promise((res,rej)=>{const tx=db.transaction(STORE_NAME,'readonly');const req=tx.objectStore(STORE_NAME).get(id);req.onsuccess=()=>res(req.result);req.onerror=()=>rej(tx.error)});
    if (local) return local;
  } catch(e){}

  try {
    const res = await fetch(`${API_VAULT_URL}?blob=${id}`);
    if (res.ok) {
      const j = await res.json();
      if (j.ok && j.data) {
        const byteCharacters = atob(j.data);
        const byteNumbers = new Array(byteCharacters.length);
        for (let i = 0; i < byteCharacters.length; i++) {
          byteNumbers[i] = byteCharacters.charCodeAt(i);
        }
        const byteArray = new Uint8Array(byteNumbers);
        const blob = new Blob([byteArray], {type: 'audio/mp3'});
        return blob;
      }
    }
  } catch(e){}
  return null;
}

let artistSynthCtx = null, artistSynthTimer = null, artistNoteIdx = 0;
const synthNotes = [261.63, 329.63, 392, 523.25, 440, 392, 329.63, 293.66];

function playSynthTone(f){
  try{
    if(!artistSynthCtx) artistSynthCtx = new (window.AudioContext || window.webkitAudioContext)();
    if(artistSynthCtx.state==='suspended') artistSynthCtx.resume();
    const osc = artistSynthCtx.createOscillator(), gain = artistSynthCtx.createGain();
    osc.type = 'triangle'; osc.frequency.value = f;
    gain.gain.setValueAtTime(0.06, artistSynthCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, artistSynthCtx.currentTime + 0.5);
    osc.connect(gain); gain.connect(artistSynthCtx.destination);
    osc.start(); osc.stop(artistSynthCtx.currentTime + 0.5);
  }catch(e){}
}

async function playArtistMedia(trackId){
  const tracks = getStoredTracks();
  const track = tracks.find(t => t.id === trackId);
  if(!track) return;

  const box = document.getElementById('artist-preview-box');
  const title = document.getElementById('artist-preview-name');
  const sub = document.getElementById('artist-preview-sub');
  const videoWrap = document.getElementById('artist-video-wrap');
  const audioWrap = document.getElementById('artist-audio-wrap');
  const videoEl = document.getElementById('artist-preview-video');
  const audioEl = document.getElementById('artist-preview-audio');

  box.classList.remove('hidden');
  title.textContent = track.name;
  const isVideo = track.type.startsWith('video');

  // Stop previous
  videoEl.pause();
  audioEl.pause();
  clearInterval(artistSynthTimer);

  const blob = await getMediaBlob(track.id);

  if(isVideo){
    videoWrap.classList.remove('hidden');
    audioWrap.classList.add('hidden');
    sub.textContent = 'Đang phát video master client-side';
    if(blob){
      videoEl.src = URL.createObjectURL(blob);
      videoEl.play().catch(e=>console.log(e));
    } else {
      sub.textContent = 'Tác phẩm mẫu (Chưa có tệp video thực tế tải lên)';
    }
  } else {
    videoWrap.classList.add('hidden');
    audioWrap.classList.remove('hidden');
    if(blob){
      sub.textContent = 'Đang phát âm thanh gốc đã tải lên';
      audioEl.src = URL.createObjectURL(blob);
      audioEl.play().catch(e=>console.log(e));
    } else {
      sub.textContent = 'Đang phát giai điệu tổng hợp Web Audio API (Bản demo mẫu)';
      playSynthTone(synthNotes[artistNoteIdx]);
      artistSynthTimer = setInterval(()=>{
        artistNoteIdx = (artistNoteIdx + 1) % synthNotes.length;
        playSynthTone(synthNotes[artistNoteIdx]);
      }, 300);
    }
  }
}

function closeArtistPreview(){
  const box = document.getElementById('artist-preview-box');
  const videoEl = document.getElementById('artist-preview-video');
  const audioEl = document.getElementById('artist-preview-audio');
  videoEl.pause();
  audioEl.pause();
  clearInterval(artistSynthTimer);
  box.classList.add('hidden');
}
"""
        if "async function playArtistMedia" not in code:
            code = code.replace("function artGradient(", f"{artist_playback_js}\nfunction artGradient(")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Đã cập nhật tính năng xem video & phát nhạc cho Trang 1: {p}")

def patch_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Trong syncActiveTrackView khi là video và có blob: gọi .play()
        old_video_play = """      const blob = await getMediaBlob(track.id);
      if(blob){
        document.getElementById('html5-video').src = URL.createObjectURL(blob);
      }"""
        new_video_play = """      const blob = await getMediaBlob(track.id);
      const vid = document.getElementById('html5-video');
      if(blob){
        vid.src = URL.createObjectURL(blob);
        vid.play().catch(e=>console.log('Video autoplay:', e));
      }"""
        if old_video_play in code:
            code = code.replace(old_video_play, new_video_play)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Đã cập nhật tính năng tự động phát video cho Trang 2: {p}")

patch_page_1()
patch_page_2()
print("✓ Hoàn tất cập nhật trình phát nhạc & video tải lên trên cả 2 trang!")
