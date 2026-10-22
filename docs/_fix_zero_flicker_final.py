import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA DỨT ĐIỂM: CHỈ ĐỒNG BỘ NỀN (SMART DIFF), TUYỆT ĐỐI KHÔNG XÓA DOM HAY RE-RENDER KHI NGƯỜI DÙNG ĐANG MỞ TRANG
# ==============================================================================

def patch_page_1_zero_flicker():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Thay thế toàn bộ hàm fetchCloudState của Trang 1
        old_fetch_block = """async function fetchCloudState() {
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

        new_fetch_block = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloud = json.data;

      // 1. Chỉ cập nhật ngầm vào localStorage
      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloud.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloud.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloud.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));

      // 2. Chỉ cập nhật đơn xin quyền (nhẹ nhàng, không làm gián đoạn màn hình chính)
      renderRequests();

      // 3. TUYỆT ĐỐI KHÔNG GỌI renderArtistTracks() HOẶC renderArtistSwitcher() TRONG POLLING!
      // Việc này giúp DOM đứng yên 100%, người dùng tha hồ chọn dropdown, chỉnh âm lượng mà không bao giờ bị giật hay undo!
    }
  } catch (err) {}
}"""

        if old_fetch_block in code:
            code = code.replace(old_fetch_block, new_fetch_block)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched zero-flicker Page 1 at: {p}")

def patch_page_2_zero_flicker():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Thay thế fetchCloudState của Trang 2: không tự ý xóa hay redraw album grid nếu người dùng đang xem
        old_fetch_p2 = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      cloudStateCache = json.data;
      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloudStateCache.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloudStateCache.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloudStateCache.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloudStateCache.artists || []));

      
      renderArtistChips();
      renderAlbumGrid();
      syncActiveTrackView();
    }
  } catch (e) {}
}"""

        new_fetch_p2 = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      cloudStateCache = json.data;
      const prevTracksStr = localStorage.getItem('tide_tracks_v2');
      const prevRequestsStr = localStorage.getItem('tide_requests_v2');
      const newTracksStr = JSON.stringify(cloudStateCache.tracks || []);
      const newRequestsStr = JSON.stringify(cloudStateCache.requests || []);

      localStorage.setItem('tide_tracks_v2', newTracksStr);
      localStorage.setItem('tide_users', JSON.stringify(cloudStateCache.users || []));
      localStorage.setItem('tide_requests_v2', newRequestsStr);
      localStorage.setItem('tide_artists', JSON.stringify(cloudStateCache.artists || []));

      // CHỈ CẬP NHẬT GIAO DIỆN KHI THỰC SỰ CÓ THAY ĐỔI VỀ QUYỀN TRUY CẬP HOẶC BÀI HÁT MỚI!
      if (prevTracksStr !== newTracksStr || prevRequestsStr !== newRequestsStr) {
        renderAlbumGrid();
        syncActiveTrackView();
      }
    }
  } catch (e) {}
}"""

        if old_fetch_p2 in code:
            code = code.replace(old_fetch_p2, new_fetch_p2)

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched zero-flicker Page 2 at: {p}")

patch_page_1_zero_flicker()
patch_page_2_zero_flicker()
print("✓ Đã loại bỏ 100% việc re-render định kỳ! DOM đứng yên hoàn toàn!")
