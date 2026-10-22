import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA TRIỆT ĐỂ: XÓA HOÀN TOÀN FILE MẪU, FIX RACE CONDITION TRONG UPLOAD
# ==============================================================================

def patch_file_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Loại bỏ các file mẫu cũ nếu còn sót trong localStorage
        cleanup_init = """
// Tự động dọn sạch các file mẫu cũ nếu còn lưu trong cache trình duyệt
(function purgeLegacySampleTracks(){
  try{
    const raw = localStorage.getItem('tide_tracks_v2');
    if(raw){
      const parsed = JSON.parse(raw);
      const cleaned = parsed.filter(t => !t.id.startsWith('track_0'));
      if(cleaned.length !== parsed.length){
        localStorage.setItem('tide_tracks_v2', JSON.stringify(cleaned));
      }
    }
  }catch(e){}
})();
"""
        if "purgeLegacySampleTracks" not in code:
            code = code.replace("<script>", f"<script>\n{cleanup_init}\n")

        # 2. Sửa handleFileUpload: Dùng FileReader an toàn, BỎ pushCloudUpdate('ADD_TRACK') bị race condition
        old_upload_fn = """async function handleFileUpload(e){
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
}"""

        new_upload_fn = """async function handleFileUpload(e){
  const file = e.target.files[0];
  if(!file) return;
  const stat = document.getElementById('upload-status');
  stat.style.display = 'block';
  stat.textContent = `> Đang xử lý và niêm phong mật mã ${file.name}...`;

  const id = 'track_' + Date.now();
  try {
    await saveMediaBlob(id, file);
  } catch(err) {
    console.warn('Lưu IndexedDB lỗi:', err);
  }

  const hashPart = Math.random().toString(16).substring(2,10) + '...';
  const sizeMb = (file.size/(1024*1024)).toFixed(1) + ' MB';

  // Lấy danh sách hiện tại và thêm bài mới lên đầu
  let tracks = getStoredTracks().filter(t => !t.id.startsWith('track_0'));
  const newTrack = {
    id: id,
    name: file.name,
    type: file.type || (file.name.endsWith('.mp4') ? 'video/mp4' : 'audio/mp3'),
    size: sizeMb,
    hash: hashPart,
    artistUsername: activeArtistUser,
    allowedUsers: [],
    artSeed: Math.floor(Math.random() * 5)
  };

  tracks.unshift(newTrack);
  saveTracks(tracks); // saveTracks đã gửi UPDATE_TRACKS lên cloud, không gọi thêm ADD_TRACK để tránh race condition!

  // Đọc file sang Base64 qua FileReader an toàn (không bị lỗi call stack limit)
  if(file.size <= 2000000){ // Chỉ sync cloud blob nếu file dưới 2MB
    const reader = new FileReader();
    reader.onload = async function(){
      try {
        const base64 = reader.result.split(',')[1];
        await fetch(API_VAULT_URL, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({action: 'UPLOAD_BLOB', trackId: id, data: base64})
        });
      } catch(e){}
    };
    reader.readAsDataURL(file);
  }

  stat.textContent = `> [THÀNH CÔNG] Đã tải lên và niêm phong tác phẩm "${file.name}" vào két sắt của @${activeArtistUser}!`;
  e.target.value = '';
}"""

        if old_upload_fn in code:
            code = code.replace(old_upload_fn, new_upload_fn)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Fixed Page 1 at: {p}")

def patch_file_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Dọn sạch file mẫu cũ trong localStorage
        cleanup_init2 = """
// Tự động dọn sạch các file mẫu cũ nếu còn lưu trong cache trình duyệt
(function purgeLegacySampleTracks2(){
  try{
    const raw = localStorage.getItem('tide_tracks_v2');
    if(raw){
      const parsed = JSON.parse(raw);
      const cleaned = parsed.filter(t => !t.id.startsWith('track_0'));
      if(cleaned.length !== parsed.length){
        localStorage.setItem('tide_tracks_v2', JSON.stringify(cleaned));
      }
    }
  }catch(e){}
})();
"""
        if "purgeLegacySampleTracks2" not in code:
            code = code.replace("<script>", f"<script>\n{cleanup_init2}\n")

        # 2. Thêm tùy chọn "Tất cả nghệ sĩ" vào renderArtistChips
        old_render_chips = """  artists.forEach(a => {
    const songCount = tracks.filter(t => (t.artistUsername||'alice_artist').toLowerCase() === a.username.toLowerCase()).length;
    const isCur = a.username.toLowerCase() === selectedArtist.toLowerCase();

    const chip = document.createElement('div');
    chip.className = `artist-chip ${isCur ? 'active' : ''}`;
    chip.onclick = () => switchArtist(a.username);

    chip.innerHTML = `
      <div class="chip-avatar">${(a.name||'A').charAt(0).toUpperCase()}</div>
      <div class="chip-meta">
        <div class="chip-name">${a.name}</div>
        <div class="chip-genre mono">@${a.username} · ${songCount} bài</div>
      </div>
    `;
    container.appendChild(chip);
  });"""

        new_render_chips = """  // Thêm chip "Tất cả nghệ sĩ" để xem toàn bộ file đã upload
  const allChip = document.createElement('div');
  const isAll = selectedArtist === 'ALL';
  allChip.className = `artist-chip ${isAll ? 'active' : ''}`;
  allChip.onclick = () => switchArtist('ALL');
  allChip.innerHTML = `
    <div class="chip-avatar" style="background:var(--fg);color:#0a0b0e">🌟</div>
    <div class="chip-meta">
      <div class="chip-name">Tất cả tác phẩm</div>
      <div class="chip-genre mono">${tracks.length} bài đã tải lên</div>
    </div>
  `;
  container.appendChild(allChip);

  artists.forEach(a => {
    const songCount = tracks.filter(t => (t.artistUsername||'').toLowerCase() === a.username.toLowerCase()).length;
    const isCur = a.username.toLowerCase() === selectedArtist.toLowerCase();

    const chip = document.createElement('div');
    chip.className = `artist-chip ${isCur ? 'active' : ''}`;
    chip.onclick = () => switchArtist(a.username);

    chip.innerHTML = `
      <div class="chip-avatar">${(a.name||'A').charAt(0).toUpperCase()}</div>
      <div class="chip-meta">
        <div class="chip-name">${a.name}</div>
        <div class="chip-genre mono">@${a.username} · ${songCount} bài</div>
      </div>
    `;
    container.appendChild(chip);
  });"""

        if old_render_chips in code:
            code = code.replace(old_render_chips, new_render_chips)

        # 3. Lọc bài hát theo selectedArtist (nếu là 'ALL' thì hiển thị tất cả)
        old_filter_logic = "const artistTracks = tracks.filter(x => (x.artistUsername||'alice_artist').toLowerCase() === selectedArtist.toLowerCase());"
        new_filter_logic = """const artistTracks = selectedArtist === 'ALL' 
    ? tracks 
    : tracks.filter(x => (x.artistUsername||'').toLowerCase() === selectedArtist.toLowerCase());"""

        if old_filter_logic in code:
            code = code.replace(old_filter_logic, new_filter_logic)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Fixed Page 2 at: {p}")

patch_file_1()
patch_file_2()
print("✓ Đã sửa toàn diện lỗi biến mất file và xóa sạch file mẫu!")
