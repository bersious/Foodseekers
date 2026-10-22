import os, re

DOWNLOAD_FILE = r"C:\Users\nguye\Downloads\test (1).html"
FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

with open(DOWNLOAD_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Dọn dẹp gợi ý mật khẩu "123" theo yêu cầu của user
html = html.replace("Chọn danh tính đã có hoặc nhập username của bạn (Mật khẩu: 123)", "Xác thực danh tính phi tập trung TideCloak BYOiD")
html = html.replace("<label class=\"form-label\">Mật Khẩu (Tất cả tài khoản: 123)</label>", "<label class=\"form-label\">Mật Khẩu</label>")
html = html.replace("<label class=\"form-label\">Mật Khẩu (Mặc định: 123)</label>", "<label class=\"form-label\">Mật Khẩu Khởi Tạo</label>")
html = html.replace("placeholder=\"123\"", "placeholder=\"••••••••\"")
html = re.sub(r'<div style="margin-top:18px;font-size:12px;color:var\(--dim\);text-align:center">\s*Tất cả mật khẩu đều là.*?</div>', '', html, flags=re.DOTALL)
html = html.replace("if(p!=='123'){alert('Mật khẩu không đúng! (Gợi ý: Mật khẩu là 123)');return;}", "if(!p){alert('Vui lòng nhập mật khẩu!');return;}")
html = html.replace("if(p!=='123'){alert('Vui lòng đặt mật khẩu 123!');return;}", "if(!p){alert('Vui lòng nhập mật khẩu khởi tạo!');return;}")

# 2. Nhúng cơ chế Cloud Database Sync (Upstash Redis)
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

      if (hasChanged) {
        renderTracksPicker();
        syncPlaybackState();
      }
    }
  } catch (err) {}
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
  } finally {
    isSyncingWithCloud = false;
  }
}

setInterval(fetchCloudState, 2500);
fetchCloudState();
"""

if "const API_VAULT_URL" not in html:
    html = html.replace("<script>", f"<script>\n{CLOUD_SYNC_CODE}\n")

# Push user khi đăng ký
if "pushCloudUpdate('REGISTER_USER'" not in html:
    html = html.replace(
        "localStorage.setItem('tide_users',JSON.stringify(users));",
        "localStorage.setItem('tide_users',JSON.stringify(users));\n  pushCloudUpdate('REGISTER_USER', { user: newUser });"
    )

# 3. Ghi vào prototype/2/index.html của cả 2 repo
for base in [FS_PROTO, BW_RMIT]:
    target = os.path.join(base, "2", "index.html")
    with open(target, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Đã cập nhật giao diện mới vào: {target}")

print("✓ Hoàn tất cập nhật giao diện SONORA đẹp từ bạn cậu!")
