import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA TRIỆT ĐỂ LỖI GIẬT/UNDO Ở TRANG 1 & THÊM TRÌNH PHÁT MP3 + VIDEO TRỰC TIẾP
# ==============================================================================

def patch_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Chống giật & chống undo: Hash comparison trong fetchCloudState()
        old_fetch = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
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

      const autoEl = document.getElementById('auto-toggle');
      if (autoEl) {
        autoEl.classList.toggle('on', !!cloud.settings?.autoApprove);
        autoEl.setAttribute('aria-checked', !!cloud.settings?.autoApprove);
      }

      renderArtistSwitcher();
      renderArtistTracks();
      renderRequests();
    }
  } catch (err) {}
}"""

        new_fetch = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloud = json.data;
      const stateHash = JSON.stringify({
        tracks: cloud.tracks,
        users: cloud.users,
        requests: cloud.requests,
        artists: cloud.artists,
        autoApprove: !!cloud.settings?.autoApprove
      });

      // NẾU DỮ LIỆU KHÔNG THAY ĐỔI: TUYỆT ĐỐI KHÔNG CHẠM VÀO DOM ĐỂ TRÁNH GIẬT/UNDO!
      if (stateHash === lastKnownCloudHash1) {
        return;
      }
      lastKnownCloudHash1 = stateHash;

      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloud.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloud.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloud.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));

      const autoEl = document.getElementById('auto-toggle');
      if (autoEl) {
        autoEl.classList.toggle('on', !!cloud.settings?.autoApprove);
        autoEl.setAttribute('aria-checked', !!cloud.settings?.autoApprove);
      }

      // Đang focus trong form hoặc dropdown thì hoãn re-render
      const activeEl = document.activeElement;
      if (activeEl && (activeEl.tagName === 'SELECT' || activeEl.tagName === 'INPUT')) {
        renderRequests();
        return;
      }

      renderArtistSwitcher();
      renderArtistTracks();
      renderRequests();
    }
  } catch (err) {}
}"""

        if old_fetch in code:
            code = code.replace(old_fetch, new_fetch)

        # 2. Thêm trình phát trực tiếp vào từng thẻ bài hát trong renderArtistTracks()
        old_track_render_template = """      <!-- Cài đặt giới hạn thời gian nghe thử của Nghệ sĩ -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,255,255,0.03);padding:8px 14px;border-radius:10px;border:1px solid var(--line);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--accent);font-weight:700"> Giới Hạn Thời Gian Xem / Nghe Thử:</span>
        <select class="form-input" style="width:auto;padding:5px 10px;font-size:12px;margin:0" onchange="setTrackLimit('${t.id}', this.value)">
          <option value="0" ${(!t.previewLimitSeconds || t.previewLimitSeconds==0)?'selected':''}> Toàn bộ bài hát</option>
          <option value="10" ${t.previewLimitSeconds==10?'selected':''}> 10 giây đầu</option>
          <option value="15" ${t.previewLimitSeconds==15?'selected':''}> 15 giây đầu</option>
          <option value="30" ${t.previewLimitSeconds==30?'selected':''}> 30 giây đầu</option>
          <option value="60" ${t.previewLimitSeconds==60?'selected':''}> 60 giây đầu</option>
        </select>
        <span class="mono" style="font-size:11px;color:${t.previewLimitSeconds>0?'var(--warn)':'var(--dim)'}">
          ${t.previewLimitSeconds>0 ? `(Đang giới hạn người nghe chỉ được nghe ${t.previewLimitSeconds}s đầu)` : '· Toàn thời lượng'}
        </span>
      </div>

      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${allowedChips}</div>
      </div>"""

        new_track_render_template = """      <!-- TRÌNH PHÁT NHẠC MP3 / XEM VIDEO TRỰC TIẾP -->
      <div style="margin-bottom:14px;background:#050705;border:1px solid var(--line);border-radius:10px;padding:12px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:11px;font-weight:700;color:var(--accent)" class="mono">
            ${isVideo ? 'TRÌNH PHÁT VIDEO MASTER' : 'TRÌNH PHÁT ÂM THANH MASTER'}
          </span>
          <span style="font-size:10px;color:var(--dim)" class="mono">RAM STREAM</span>
        </div>
        ${isVideo ? `
          <video id="player-${t.id}" controls style="width:100%;max-height:280px;border-radius:8px;background:#000;display:block"></video>
        ` : `
          <audio id="player-${t.id}" controls style="width:100%;border-radius:6px;outline:none"></audio>
        `}
      </div>

      <!-- Cài đặt giới hạn thời gian nghe thử của Nghệ sĩ -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;background:rgba(255,255,255,0.03);padding:8px 14px;border-radius:10px;border:1px solid var(--line);flex-wrap:wrap">
        <span style="font-size:12px;color:var(--accent);font-weight:700">Giới hạn thời gian nghe thử:</span>
        <select class="form-input" style="width:auto;padding:5px 10px;font-size:12px;margin:0" onchange="setTrackLimit('${t.id}', this.value)">
          <option value="0" ${(!t.previewLimitSeconds || t.previewLimitSeconds==0)?'selected':''}>Toàn bộ bài hát</option>
          <option value="10" ${t.previewLimitSeconds==10?'selected':''}>10 giây đầu</option>
          <option value="15" ${t.previewLimitSeconds==15?'selected':''}>15 giây đầu</option>
          <option value="30" ${t.previewLimitSeconds==30?'selected':''}>30 giây đầu</option>
          <option value="60" ${t.previewLimitSeconds==60?'selected':''}>60 giây đầu</option>
        </select>
        <span class="mono" style="font-size:11px;color:${t.previewLimitSeconds>0?'var(--warn)':'var(--dim)'}">
          ${t.previewLimitSeconds>0 ? `· Giới hạn ${t.previewLimitSeconds}s` : '· Toàn thời lượng'}
        </span>
      </div>

      <div style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px">DANH TÍNH ĐANG ĐƯỢC PHÉP GIẢI MÃ:</div>
        <div>${allowedChips}</div>
      </div>"""

        if old_track_render_template in code:
            code = code.replace(old_track_render_template, new_track_render_template)

        # 3. Kích hoạt nạp blob tự động vào từng player sau khi render
        attach_players_code = """
  // Tự động nạp blob hoặc stream vào các trình phát của từng bài hát
  myTracks.forEach(async t => {
    const el = document.getElementById(`player-${t.id}`);
    if(!el) return;
    const blob = await getMediaBlob(t.id);
    if(blob){
      el.src = URL.createObjectURL(blob);
    }
  });
"""
        old_render_end = "box.appendChild(card);\n  });\n}"
        new_render_end = f"box.appendChild(card);\n  }});\n{attach_players_code}\n}}"
        if old_render_end in code and attach_players_code not in code:
            code = code.replace(old_render_end, new_render_end)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched smooth Page 1 with direct players at: {p}")

patch_page_1()
print("✓ Hoàn tất nâng cấp chống giật và thêm trình phát MP3/Video cho Trang 1!")
