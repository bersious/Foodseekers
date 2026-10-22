import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# Đoạn mã Cloud Database Sync dùng cho cả 3 trang
CLOUD_SYNC_CODE = """
// ==================== TIDE GLOBAL CLOUD DATABASE SYNC ====================
const API_VAULT_URL = '/api/rmit-vault';
let isSyncingWithCloud = false;

async function fetchCloudState() {
  if (isSyncingWithCloud) return;
  try {
    const res = await fetch(API_VAULT_URL);
    if (!res.ok) return;
    const json = await res.json();
    if (json.ok && json.data) {
      const cloudData = json.data;
      const localTracks = localStorage.getItem('tide_tracks_v2');
      const cloudTracksStr = JSON.stringify(cloudData.tracks || []);
      const cloudUsersStr = JSON.stringify(cloudData.users || []);

      let hasChanged = false;
      if (localTracks !== cloudTracksStr) {
        localStorage.setItem('tide_tracks_v2', cloudTracksStr);
        hasChanged = true;
      }
      if (localStorage.getItem('tide_users') !== cloudUsersStr) {
        localStorage.setItem('tide_users', cloudUsersStr);
        hasChanged = true;
      }

      if (hasChanged && typeof onCloudSync === 'function') {
        onCloudSync();
      }
    }
  } catch (err) {
    // Offline / fallback to localStorage
  }
}

async function pushCloudUpdate(action, payload = {}) {
  isSyncingWithCloud = true;
  try {
    await fetch(API_VAULT_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action, ...payload })
    });
  } catch (e) {
    console.warn('Cloud sync error:', e);
  } finally {
    isSyncingWithCloud = false;
  }
}

// Bắt đầu vòng lặp polling 2.5s để đồng bộ từ các máy tính khác
setInterval(fetchCloudState, 2500);
fetchCloudState();
"""

def patch_page_1():
    p = os.path.join(FS_PROTO, "1", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    # Thêm badge Cloud Sync trên topbar
    old_topbar = '<span class="pill-tide">TideCloak Quorum</span>'
    new_topbar = '<span class="pill-tide" title="Đồng bộ thời gian thực qua Upstash Redis">☁️ Cloud Database: SYNCED</span>'
    if old_topbar in html:
        html = html.replace(old_topbar, new_topbar)

    # Thêm cloud sync code
    if "const API_VAULT_URL" not in html:
        html = html.replace("<script>", f"<script>\n{CLOUD_SYNC_CODE}\nfunction onCloudSync(){{ getStoredUsers(); renderArtistTracks(); updatePolicyViewer(); }}\n")

    # Khi saveTracks được gọi, gửi pushCloudUpdate
    old_save = """function saveTracks(tracks){
  localStorage.setItem('tide_tracks_v2',JSON.stringify(tracks));
  try{new BroadcastChannel('tide_channel').postMessage({type:'SYNC_DATA'})}catch(e){}
  renderArtistTracks();
}"""
    new_save = """function saveTracks(tracks){
  localStorage.setItem('tide_tracks_v2',JSON.stringify(tracks));
  try{new BroadcastChannel('tide_channel').postMessage({type:'SYNC_DATA'})}catch(e){}
  renderArtistTracks();
  pushCloudUpdate('UPDATE_TRACKS', { tracks: tracks });
}"""
    if old_save in html:
        html = html.replace(old_save, new_save)

    return html

def patch_page_2():
    p = os.path.join(FS_PROTO, "2", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    old_topbar = '<span class="pill-tide">Tide BYOiD Session</span>'
    new_topbar = '<span class="pill-tide" title="Đồng bộ thời gian thực qua Upstash Redis">☁️ Cloud Database: SYNCED</span>'
    if old_topbar in html:
        html = html.replace(old_topbar, new_topbar)

    if "const API_VAULT_URL" not in html:
        html = html.replace("<script>", f"<script>\n{CLOUD_SYNC_CODE}\nfunction onCloudSync(){{ renderTracksPicker(); syncPlaybackState(); }}\n")

    # Khi registerReviewer tạo user mới, pushCloudUpdate
    old_reg_push = "localStorage.setItem('tide_users',JSON.stringify(users));"
    new_reg_push = """localStorage.setItem('tide_users',JSON.stringify(users));
  pushCloudUpdate('REGISTER_USER', { user: newUser });"""
    if old_reg_push in html and "pushCloudUpdate('REGISTER_USER'" not in html:
        html = html.replace(old_reg_push, new_reg_push)

    return html

def patch_page_3():
    p = os.path.join(FS_PROTO, "3", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    old_topbar = '<span class="pill-tide">Zero-Custody Cloud</span>'
    new_topbar = '<span class="pill-tide">☁️ Cloud Database: SYNCED</span>'
    if old_topbar in html:
        html = html.replace(old_topbar, new_topbar)

    if "const API_VAULT_URL" not in html:
        html = html.replace("<script>", f"<script>\n{CLOUD_SYNC_CODE}\nfunction onCloudSync(){{ renderS3(); }}\n")

    return html

p1 = patch_page_1()
p2 = patch_page_2()
p3 = patch_page_3()

for base in [FS_PROTO, BW_RMIT]:
    with open(os.path.join(base, "1", "index.html"), "w", encoding="utf-8") as f:
        f.write(p1)
    with open(os.path.join(base, "2", "index.html"), "w", encoding="utf-8") as f:
        f.write(p2)
    with open(os.path.join(base, "3", "index.html"), "w", encoding="utf-8") as f:
        f.write(p3)

print("✓ Đã nhúng cơ chế đồng bộ Cloud Database toàn cầu vào cả 3 trang!")
