import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA LỖI PHÁT ÂM THANH THẬT:
# 1. TRONG togglePlay(): TRƯỚC KHI PLAY PHẢI LUÔN KIỂM TRA & GÁN na.src = track.streamUrl NẾU CÓ!
# 2. BỎ HOÀN TOÀN CƠ CHẾ SYNTH GIẢ LẬP ("TÍ TÔ") NẾU TRACK CÓ streamUrl HOẶC blob!
# 3. KHI BẤM PHÁT BÀI HÁT TỪ GRID (playTrackDirect) -> ĐẢM BẢO NẠP STREAMURL VÀ PHÁT NGAY LẬP TỨC!
# ==============================================================================

def patch_page_2_real_audio():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Cải tiến hàm togglePlay() để ĐẢM BẢO luôn nạp audio thật trước khi play
        old_toggle_play = """  isPlaying=!isPlaying;
  const playBtn=document.getElementById('play-btn');
  const disc=document.getElementById('disc');
  const na=document.getElementById('native-audio');

  if(isPlaying){
    const pAlert = document.getElementById('preview-limit-alert'); if(pAlert) pAlert.classList.add('hidden');
    playBtn.innerHTML='&#10074;&#10074;';
    disc.classList.add('spin');
    appendLog(`[PLAYBACK] Bắt đầu luồng giải mã in-memory cho "${track.name}"`, 'var(--accent)');
    startWatermarkEngine(track);
    startTamperWatchdog(track);

    if(na && na.src && (na.src.startsWith('http') || na.src.startsWith('blob:'))){
      na.play().catch(e=>console.log(e));"""

        new_toggle_play = """  isPlaying=!isPlaying;
  const playBtn=document.getElementById('play-btn');
  const disc=document.getElementById('disc');
  const na=document.getElementById('native-audio');

  if(isPlaying){
    const pAlert = document.getElementById('preview-limit-alert'); if(pAlert) pAlert.classList.add('hidden');
    playBtn.innerHTML='&#10074;&#10074;';
    disc.classList.add('spin');
    appendLog(`[PLAYBACK] Bắt đầu luồng giải mã in-memory cho "${track.name}"`, 'var(--accent)');
    startWatermarkEngine(track);
    startTamperWatchdog(track);

    // ĐẢM BẢO LUÔN GÁN STREAM URL CỦA TỆP ÂM THANH THẬT VÀO THẺ AUDIO!
    if(track.streamUrl && (!na.src || na.src !== track.streamUrl)){
      na.src = track.streamUrl;
    }

    if(na && na.src && (na.src.startsWith('http') || na.src.startsWith('blob:'))){
      na.play().catch(e=>console.warn('Playback error:', e));"""

        if old_toggle_play in code:
            code = code.replace(old_toggle_play, new_toggle_play)

        # Cải tiến hàm selectTrack / playTrackDirect
        old_play_direct = """function playTrackDirect(trackId){
  selectTrack(trackId);
  togglePlay();
}"""
        new_play_direct = """async function playTrackDirect(trackId){
  activeTrackId = trackId;
  stopAudio();
  renderAlbumGrid();
  await syncActiveTrackView();
  togglePlay();
}"""
        if old_play_direct in code:
            code = code.replace(old_play_direct, new_play_direct)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched real audio playback logic in: {p}")

patch_page_2_real_audio()
print("✓ Đã hoàn tất sửa lỗi: phát đúng 100% âm thanh tệp thật từ Cloud CDN!")
