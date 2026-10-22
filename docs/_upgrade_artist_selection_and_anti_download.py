import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==================== CẬP NHẬT TRANG 1: LƯU TÁC PHẨM KÈM ARTIST USERNAME ====================
def update_page_1():
    p = os.path.join(FS_PROTO, "1", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        code = f.read()

    # Đảm bảo bài hát mặc định và bài hát tải lên có trường artistUsername
    old_default = """  const def=[
    {id:'track_01',name:'Lead_Single_Master_v4.flac',type:'audio/flac',size:'42.8 MB',hash:'b79a4e912f...',allowedUsers:['minh_mastering']},
    {id:'track_02',name:'Vocal_Stems_Studio_Dry.wav',type:'audio/wav',size:'68.1 MB',hash:'82f10ac349...',allowedUsers:[]},
    {id:'track_03',name:'Behind_The_Scenes_Snippet.mp4',type:'video/mp4',size:'115.4 MB',hash:'11ce9d40b2...',allowedUsers:[]}
  ];"""

    new_default = """  const def=[
    {id:'track_01',name:'Lead_Single_Master_v4.flac',type:'audio/flac',size:'42.8 MB',hash:'b79a4e912f...',artistUsername:'alice_artist',allowedUsers:['minh_mastering']},
    {id:'track_02',name:'Vocal_Stems_Studio_Dry.wav',type:'audio/wav',size:'68.1 MB',hash:'82f10ac349...',artistUsername:'alice_artist',allowedUsers:[]},
    {id:'track_03',name:'Behind_The_Scenes_Snippet.mp4',type:'video/mp4',size:'115.4 MB',hash:'11ce9d40b2...',artistUsername:'alice_artist',allowedUsers:[]}
  ];"""

    if old_default in code:
        code = code.replace(old_default, new_default)

    # Khi tải file mới lên, gắn artistUsername = người đang đăng nhập
    old_upload = """  tracks.unshift({
    id:id,
    name:file.name,
    type:file.type||'audio/mp3',
    size:sizeMb,
    hash:hashPart,
    allowedUsers:[]
  });"""

    new_upload = """  const currentArtist = localStorage.getItem('tide_logged_artist') || 'alice_artist';
  tracks.unshift({
    id:id,
    name:file.name,
    type:file.type||'audio/mp3',
    size:sizeMb,
    hash:hashPart,
    artistUsername: currentArtist,
    allowedUsers:[]
  });"""

    if old_upload in code:
        code = code.replace(old_upload, new_upload)

    return code

# ==================== CẬP NHẬT TRANG 2: CHỌN NGHỆ SĨ & CHỐNG TẢI VIDEO/AUDIO ====================
def update_page_2():
    p = os.path.join(FS_PROTO, "2", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Chống tải về trên toàn bộ player: cấm chuột phải, cấm kéo thả, nodownload
    old_video_tag = '<video id="html5-video" controls></video>'
    new_video_tag = """<div style="position:relative;user-select:none;-webkit-user-select:none;" oncontextmenu="return false;">
          <video id="html5-video" controls controlsList="nodownload nofullscreen noplaybackrate" disablePictureInPicture oncontextmenu="return false;" style="pointer-events:auto;"></video>
          <div style="position:absolute;top:10px;right:10px;background:rgba(0,0,0,0.65);border:1px solid rgba(255,255,255,0.15);padding:4px 10px;border-radius:6px;font-size:11px;color:var(--accent);pointer-events:none;" class="mono">
            🔒 Tide In-Memory Stream · CẤM TẢI VỀ
          </div>
        </div>"""

    if old_video_tag in code:
        code = code.replace(old_video_tag, new_video_tag)

    # 2. Thêm thanh chọn / tìm kiếm tài khoản Nghệ Sĩ
    artist_selector_html = """
    <!-- CHỌN HOẶC NHẬP TÀI KHOẢN NGHỆ SĨ -->
    <div class="card" style="margin-bottom:20px;padding:20px;border-color:rgba(212,255,63,.2)">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:10px">
        <div>
          <span style="font-size:13px;font-weight:700;color:var(--fg);display:flex;align-items:center;gap:6px">
            <span>🎨</span> Kết Nối Tới Két Sắt Của Nghệ Sĩ:
          </span>
          <p style="font-size:12px;color:var(--muted);margin-top:2px">
            Chọn hoặc nhập username của Nghệ Sĩ để yêu cầu Quorum cấp khóa giải mã tài liệu của người đó
          </p>
        </div>
        <span class="badge badge-ok mono" id="connected-artist-badge">Đang kết nối: alice_artist</span>
      </div>

      <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
        <select id="quick-artist-select" class="form-input" style="flex:1;min-width:200px;font-size:13px;padding:8px 12px" onchange="switchArtist(this.value)">
          <option value="alice_artist">alice_artist (Nghệ sĩ Alice Nguyễn)</option>
          <option value="endy_producer">endy_producer (Nhà sản xuất Endy)</option>
        </select>
        <div style="display:flex;gap:6px;align-items:center;flex:1;min-width:220px">
          <input type="text" id="custom-artist-input" class="form-input" style="font-size:13px;padding:8px 12px" placeholder="Nhập username nghệ sĩ khác...">
          <button class="btn btn-accent btn-sm" onclick="applyCustomArtist()">Kết Nối</button>
        </div>
      </div>
    </div>
    """

    if "<!-- CHỌN HOẶC NHẬP TÀI KHOẢN NGHỆ SĨ -->" not in code:
        code = code.replace('<div class="track-picker" id="reviewer-track-picker"></div>', f"{artist_selector_html}\n    <div class=\"track-picker\" id=\"reviewer-track-picker\"></div>")

    # 3. Logic chọn nghệ sĩ và lọc bài hát theo nghệ sĩ
    artist_logic_js = """
let selectedArtist = 'alice_artist';

function switchArtist(artistName){
  selectedArtist = artistName.trim().toLowerCase();
  document.getElementById('connected-artist-badge').textContent = `Đang kết nối: ${selectedArtist}`;
  const customInput = document.getElementById('custom-artist-input');
  if(customInput) customInput.value = selectedArtist;
  appendExecutionLog(`[TIDE QUORUM] Chuyển kết nối tới Két Sắt của Nghệ Sĩ: ${selectedArtist}`, true);
  activeTrackId = null;
  stopAudio();
  renderTracksPicker();
  syncPlaybackState();
}

function applyCustomArtist(){
  const val = document.getElementById('custom-artist-input').value.trim();
  if(!val){ alert('Vui lòng nhập username của nghệ sĩ!'); return; }
  switchArtist(val);
}
"""

    if "let selectedArtist = 'alice_artist';" not in code:
        code = code.replace("let activeTrackId = null;", f"{artist_logic_js}\nlet activeTrackId = null;")

    # 4. Lọc bài hát theo selectedArtist
    old_picker_loop = "tracks.forEach(t=>{"
    new_picker_loop = """
  // Cập nhật danh sách nghệ sĩ trong dropdown nếu có thêm nghệ sĩ mới
  const artistSelect = document.getElementById('quick-artist-select');
  if(artistSelect){
    const uniqueArtists = Array.from(new Set(tracks.map(x => x.artistUsername || 'alice_artist')));
    if(!uniqueArtists.includes('alice_artist')) uniqueArtists.unshift('alice_artist');
    artistSelect.innerHTML = uniqueArtists.map(a => `<option value="${a}" ${a===selectedArtist?'selected':''}>${a} (${a==='alice_artist'?'Nghệ sĩ Alice':'Nghệ sĩ '+a})</option>`).join('');
  }

  // Lọc chỉ các track thuộc về nghệ sĩ đang được chọn
  const filteredTracks = tracks.filter(x => (x.artistUsername || 'alice_artist').toLowerCase() === selectedArtist.toLowerCase());

  if(filteredTracks.length === 0){
    picker.innerHTML = `<div style="font-size:13px;color:var(--muted);padding:8px" class="mono">Chưa có tác phẩm nào từ nghệ sĩ "${selectedArtist}".</div>`;
    syncPlaybackState();
    return;
  }

  if(!activeTrackId || !filteredTracks.some(x=>x.id===activeTrackId)){
    activeTrackId = filteredTracks[0].id;
  }

  filteredTracks.forEach(t=>{"""

    if "const filteredTracks = tracks.filter" not in code:
        code = code.replace("tracks.forEach(t=>{", new_picker_loop)

    return code

p1 = update_page_1()
p2 = update_page_2()

# Ghi vào cả 2 repo
for base_dir in [FS_PROTO, BW_RMIT]:
    with open(os.path.join(base_dir, "1", "index.html"), "w", encoding="utf-8") as f:
        f.write(p1)
    with open(os.path.join(base_dir, "2", "index.html"), "w", encoding="utf-8") as f:
        f.write(p2)

print("✓ Đã cập nhật tính năng Chọn Tài Khoản Nghệ Sĩ và Chống Tải Video/Audio!")
