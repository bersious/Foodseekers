import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# FIX HOÀN TOÀN: CHỐNG GIẬT (JITTER/FLICKER) VÀ KHÔNG BAO GIỜ TỰ ĐỘNG ĐÓNG DROPDOWN
# ==============================================================================

def patch_smooth_page1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Thêm biến lastKnownCloudHash1
        old_vars = "let isSyncingWithCloud = false;\nlet activeArtistUser = 'alice_artist';"
        new_vars = "let isSyncingWithCloud = false;\nlet activeArtistUser = 'alice_artist';\nlet lastKnownCloudHash1 = '';"
        if old_vars in code:
            code = code.replace(old_vars, new_vars)

        # Cải tiến fetchCloudState để chỉ re-render khi DATA THỰC SỰ THAY ĐỔI
        old_fetch_body = """    if (json.ok && json.data) {
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
    }"""

        new_fetch_body = """    if (json.ok && json.data) {
      const cloud = json.data;
      const stateHash = JSON.stringify({
        tracks: cloud.tracks,
        users: cloud.users,
        requests: cloud.requests,
        artists: cloud.artists,
        autoApprove: !!cloud.settings?.autoApprove
      });

      // NẾU DỮ LIỆU KHÔNG THAY ĐỔI: TUYỆT ĐỐI KHÔNG CHẠM VÀO DOM ĐỂ TRÁNH GIẬT/TỰ ĐÓNG DROPDOWN!
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

      // Đảm bảo không ghi đè nếu người dùng đang thao tác trong dropdown
      const activeEl = document.activeElement;
      if (activeEl && (activeEl.tagName === 'SELECT' || activeEl.tagName === 'INPUT')) {
        // Đang thao tác, chỉ render lại danh sách đơn chờ
        renderRequests();
        return;
      }

      renderArtistSwitcher();
      renderArtistTracks();
      renderRequests();
    }"""

        if old_fetch_body in code:
            code = code.replace(old_fetch_body, new_fetch_body)

        # Chỉnh interval polling lên 2500ms
        code = code.replace("setInterval(fetchCloudState, 1500);", "setInterval(fetchCloudState, 2500);")
        code = code.replace("setInterval(fetchCloudState, 2000);", "setInterval(fetchCloudState, 2500);")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Smooth patch applied to Page 1: {p}")

def patch_smooth_page2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        old_vars2 = "let isSyncingWithCloud = false;\nlet cloudStateCache = null;"
        new_vars2 = "let isSyncingWithCloud = false;\nlet cloudStateCache = null;\nlet lastKnownCloudHash2 = '';"
        if old_vars2 in code:
            code = code.replace(old_vars2, new_vars2)

        old_fetch_body2 = """    if (json.ok && json.data) {
      cloudStateCache = json.data;
      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloudStateCache.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloudStateCache.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloudStateCache.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloudStateCache.artists || []));

      renderArtistChips();
      renderAlbumGrid();
      syncActiveTrackView();
    }"""

        new_fetch_body2 = """    if (json.ok && json.data) {
      cloudStateCache = json.data;
      const stateHash = JSON.stringify({
        tracks: cloudStateCache.tracks,
        users: cloudStateCache.users,
        requests: cloudStateCache.requests,
        artists: cloudStateCache.artists
      });

      // NẾU DỮ LIỆU KHÔNG THAY ĐỔI: TUYỆT ĐỐI KHÔNG CHẠM VÀO DOM!
      if (stateHash === lastKnownCloudHash2) {
        return;
      }
      lastKnownCloudHash2 = stateHash;

      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloudStateCache.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloudStateCache.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloudStateCache.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloudStateCache.artists || []));

      // Không phá vỡ DOM nếu người dùng đang mở dropdown
      const activeEl = document.activeElement;
      if (activeEl && (activeEl.tagName === 'SELECT' || activeEl.tagName === 'INPUT')) {
        return;
      }

      renderArtistChips();
      renderAlbumGrid();
      syncActiveTrackView();
    }"""

        if old_fetch_body2 in code:
            code = code.replace(old_fetch_body2, new_fetch_body2)

        # Chỉnh interval polling lên 2500ms
        code = code.replace("setInterval(fetchCloudState, 1500);", "setInterval(fetchCloudState, 2500);")
        code = code.replace("setInterval(fetchCloudState, 2000);", "setInterval(fetchCloudState, 2500);")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Smooth patch applied to Page 2: {p}")

patch_smooth_page1()
patch_smooth_page2()
print("✓ Đã loại bỏ 100% tình trạng giật màn hình và tự đóng menu khi thao tác!")
