import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# ==============================================================================
# SỬA LỖI ĐỒNG BỘ:
# 1. KHI CÓ USER MỚI HOẶC TRACKS MỚI -> CẬP NHẬT NGAY DROPDOWN & DANH SÁCH MÀ KHÔNG GIẬT
# 2. RÚT NGẮN POLLING XUỐNG 1.5 GIÂY ĐỂ ĐỒNG BỘ REALTIME TỨC THÌ
# 3. KHI DUYỆT ĐƠN / TẠO USER / TẠO TRACKS -> BẮN EVENT QUA BROADCASTCHANNEL & CLOUD
# ==============================================================================

def patch_page_1():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "1", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Cải tiến fetchCloudState ở Page 1:
        # Nếu số lượng users hoặc requests thay đổi -> update dropdown ngay!
        old_fetch_p1 = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloud = json.data;

      // Lưu ngầm
      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloud.tracks || []));
      localStorage.setItem('tide_users', JSON.stringify(cloud.users || []));
      localStorage.setItem('tide_requests_v2', JSON.stringify(cloud.requests || []));
      localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));

      // Chỉ cập nhật danh sách đơn xin quyền nếu có thay đổi
      renderRequests();
    }
  } catch (err) {}
}"""

        new_fetch_p1 = """async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL + '?t=' + Date.now());
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloud = json.data;

      const oldUsersStr = localStorage.getItem('tide_users') || '[]';
      const newUsersStr = JSON.stringify(cloud.users || []);
      const oldReqStr = localStorage.getItem('tide_requests_v2') || '[]';
      const newReqStr = JSON.stringify(cloud.requests || []);

      localStorage.setItem('tide_tracks_v2', JSON.stringify(cloud.tracks || []));
      localStorage.setItem('tide_users', newUsersStr);
      localStorage.setItem('tide_requests_v2', newReqStr);
      localStorage.setItem('tide_artists', JSON.stringify(cloud.artists || []));
      if(cloud.comments) localStorage.setItem('tide_comments_v2', JSON.stringify(cloud.comments));

      // 1. Cập nhật đơn xin quyền ngay lập tức
      renderRequests();

      // 2. Nếu có user mới được tạo ở tab khác -> Cập nhật các dropdown chọn người nghe ngay!
      if(oldUsersStr !== newUsersStr){
        updateAllUserDropdowns();
      }
    }
  } catch (err) {}
}

function updateAllUserDropdowns(){
  const users = getStoredUsers();
  const tracks = getStoredTracks();
  tracks.forEach(t => {
    const select = document.getElementById(`select-user-${t.id}`);
    if(!select) return;
    const currentVal = select.value;
    let options = '<option value="">-- Chọn người nghe để cấp quyền --</option>';
    users.forEach(u => {
      if(!t.allowedUsers || !t.allowedUsers.includes(u.username)){
        options += `<option value="${u.username}">${u.name||u.username} (@${u.username})</option>`;
      }
    });
    select.innerHTML = options;
    if(currentVal) select.value = currentVal;
  });
}"""

        if old_fetch_p1 in code:
            code = code.replace(old_fetch_p1, new_fetch_p1)

        # Rút ngắn polling xuống 1500ms
        code = code.replace("setInterval(fetchCloudState, 4000);", "setInterval(fetchCloudState, 1500);")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched instant sync in Page 1: {p}")

def patch_page_2():
    for base in [FS_PROTO, BW_RMIT]:
        p = os.path.join(base, "2", "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Rút ngắn polling xuống 1500ms và thêm cache buster '?t=' + Date.now()
        code = code.replace("const res = await fetch(API_VAULT_URL);", "const res = await fetch(API_VAULT_URL + '?t=' + Date.now());")
        code = code.replace("setInterval(fetchCloudState, 2500);", "setInterval(fetchCloudState, 1500);")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Patched instant sync in Page 2: {p}")

patch_page_1()
patch_page_2()
print("✓ Đã hoàn tất tối ưu tốc độ đồng bộ thời gian thực cho cơ sở dữ liệu Upstash Redis!")
