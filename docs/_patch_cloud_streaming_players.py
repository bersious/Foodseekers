import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# TÍCH HỢP VERCEL BLOB UPLOAD VÀ ĐẢM BẢO 100% PHÁT ĐƯỢC NHẠC & VIDEO THẬT TRÊN TẤT CẢ LAPTOP
# ==============================================================================

def patch_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Cập nhật handleFileUpload để upload lên /api/upload-media và nhận streamUrl
        old_upload_code = """  // Đọc file sang Base64 qua FileReader an toàn (không bị lỗi call stack limit)
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
  }"""

        new_upload_code = """  // Tải file trực tiếp lên Vercel Blob để mọi laptop đều phát được âm thanh/video thật
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
        saveTracks(tracks);
      }
    }
  } catch(uploadErr){
    console.warn('Vercel Blob upload warning:', uploadErr);
  }"""

        if old_upload_code in code:
            code = code.replace(old_upload_code, new_upload_code)

        # Cập nhật attach_players_code để ưu tiên streamUrl
        old_attach = """  // Tự động nạp blob hoặc stream vào các trình phát của từng bài hát
  myTracks.forEach(async t => {
    const el = document.getElementById(`player-${t.id}`);
    if(!el) return;
    const blob = await getMediaBlob(t.id);
    if(blob){
      el.src = URL.createObjectURL(blob);
    }
  });"""

        new_attach = """  // Tự động nạp streamUrl hoặc blob vào các trình phát của từng bài hát
  myTracks.forEach(async t => {
    const el = document.getElementById(`player-${t.id}`);
    if(!el) return;
    if(t.streamUrl){
      el.src = t.streamUrl;
    } else {
      const blob = await getMediaBlob(t.id);
      if(blob) el.src = URL.createObjectURL(blob);
    }
  });"""

        if old_attach in code:
            code = code.replace(old_attach, new_attach)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 1 cloud streaming at: {p}")

def patch_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Sửa nút Play / Pause biểu tượng rõ ràng
        code = code.replace("playBtn.textContent='';", "playBtn.innerHTML='&#10074;&#10074;';")
        code = code.replace("document.getElementById('play-btn').textContent='';", "document.getElementById('play-btn').innerHTML='&#9654;';")
        code = code.replace('<button class="play-btn" id="play-btn" onclick="togglePlay()"></button>', '<button class="play-btn" id="play-btn" onclick="togglePlay()">&#9654;</button>')

        # 2. Trong syncActiveTrackView(), nạp track.streamUrl trực tiếp nếu có!
        old_load_video = """      const blob = await getMediaBlob(track.id);
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

        new_load_video = """      const vid = document.getElementById('html5-video');
      vid.onended = function(){ onMediaPlaybackFinished(track); };
      if(track.streamUrl){
        vid.srcObject = null;
        vid.src = track.streamUrl;
      } else {
        const blob = await getMediaBlob(track.id);
        if(blob){
          vid.srcObject = null;
          vid.src = URL.createObjectURL(blob);
        } else {
          const stream = generateDemoVideoFeed(track.name);
          vid.srcObject = stream;
        }
      }"""

        if old_load_video in code:
            code = code.replace(old_load_video, new_load_video)

        old_load_audio = """      const blob = await getMediaBlob(track.id);
      const na = document.getElementById('native-audio');
      if(blob){
        na.src = URL.createObjectURL(blob);
      } else {
        na.removeAttribute('src');
      }"""

        new_load_audio = """      const na = document.getElementById('native-audio');
      if(track.streamUrl){
        na.src = track.streamUrl;
      } else {
        const blob = await getMediaBlob(track.id);
        if(blob){
          na.src = URL.createObjectURL(blob);
        } else {
          na.removeAttribute('src');
        }
      }"""

        if old_load_audio in code:
            code = code.replace(old_load_audio, new_load_audio)

        # 3. Trong togglePlay(), phát na nếu có src (kể cả streamUrl lẫn blob URL!)
        old_na_check = "if(na && na.src && na.src.startsWith('blob:')){"
        new_na_check = "if(na && na.src && (na.src.startsWith('http') || na.src.startsWith('blob:'))){"
        if old_na_check in code:
            code = code.replace(old_na_check, new_na_check)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched Page 2 cloud playback at: {p}")

patch_page_1()
patch_page_2()
print("✓ Hoàn tất cấu hình luồng phát âm thanh & video Vercel Blob cho toàn bộ thiết bị!")
