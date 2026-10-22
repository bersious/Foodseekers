import os

# Đường dẫn thư mục
FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

SHARED_HEAD = """
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#08090d;
  --surface:rgba(255,255,255,.025);
  --surface-2:rgba(255,255,255,.05);
  --line:rgba(255,255,255,.08);
  --line-strong:rgba(255,255,255,.15);
  --fg:#f4f5f7;
  --muted:#8b8fa0;
  --dim:#5a5e6e;
  --accent:#d4ff3f;
  --accent-dim:rgba(212,255,63,.12);
  --danger:#ff4d6d;
  --danger-dim:rgba(255,77,109,.12);
  --ok:#3ee88f;
  --ok-dim:rgba(62,232,143,.12);
  --radius:16px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{
  background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;line-height:1.5;
  -webkit-font-smoothing:antialiased;min-height:100vh;overflow-x:hidden;
}
body::before{
  content:'';position:fixed;inset:0;z-index:-2;
  background:
    radial-gradient(900px 500px at 75% -5%,rgba(212,255,63,.07),transparent 60%),
    radial-gradient(700px 500px at 0% 100%,rgba(90,110,255,.06),transparent 55%);
}
body::after{
  content:'';position:fixed;inset:0;z-index:-1;opacity:.35;
  background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);
  background-size:64px 64px;
}
.mono{font-family:'JetBrains Mono',monospace}

/* Nav */
.topbar{
  position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;
  padding:16px 32px;backdrop-filter:blur(18px);background:rgba(8,9,13,.75);border-bottom:1px solid var(--line);
}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;font-weight:700}
.brand-dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.brand small{display:block;font-size:11px;color:var(--muted);font-weight:400}

.nav-links{display:flex;gap:6px;background:var(--surface);border:1px solid var(--line);padding:4px;border-radius:12px}
.nav-link{
  font-size:13px;font-weight:500;color:var(--muted);text-decoration:none;
  padding:8px 14px;border-radius:8px;transition:.18s;display:flex;align-items:center;gap:6px;
}
.nav-link:hover{color:var(--fg)}
.nav-link.active{background:var(--fg);color:#0a0b0e;font-weight:600}

.pill-tide{font-size:11px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:6px 12px;border-radius:999px}

/* Container */
.container{max-width:1080px;margin:40px auto 80px;padding:0 24px}
.page-header{margin-bottom:32px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}
.page-title h1{font-size:28px;letter-spacing:-.03em;font-weight:700}
.page-title p{color:var(--muted);font-size:14px;margin-top:4px}

.card{
  background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
  padding:28px;position:relative;overflow:hidden;backdrop-filter:blur(12px);
}

.btn{
  font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;
  padding:10px 18px;border-radius:10px;border:1px solid transparent;transition:.18s;
  display:inline-flex;align-items:center;gap:8px;text-decoration:none;
}
.btn-accent{background:var(--accent);color:#0a0b0e}
.btn-accent:hover{filter:brightness(1.1);transform:translateY(-1px)}
.btn-danger{background:var(--danger-dim);color:var(--danger);border-color:rgba(255,77,109,.3)}
.btn-danger:hover{background:rgba(255,77,109,.2)}
.btn-ok{background:var(--ok-dim);color:var(--ok);border-color:rgba(62,232,143,.3)}
.btn-ok:hover{background:rgba(62,232,143,.2)}
.btn-ghost{background:transparent;border-color:var(--line-strong);color:var(--fg)}
.btn-ghost:hover{background:var(--surface-2)}

.badge{font-size:11px;font-weight:600;padding:5px 10px;border-radius:999px;white-space:nowrap}
.badge-ok{color:var(--ok);background:var(--ok-dim);border:1px solid rgba(62,232,143,.25)}
.badge-danger{color:var(--danger);background:var(--danger-dim);border:1px solid rgba(255,77,109,.25)}
.badge-dim{color:var(--muted);background:var(--surface-2);border:1px solid var(--line)}

.footer{
  max-width:1080px;margin:0 auto;padding:24px;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;align-items:center;color:var(--dim);font-size:12px;
}
</style>
"""

SHARED_JS = """
// Quản lý cơ sở dữ liệu IndexedDB lưu trữ media
const DB_NAME = 'tide_vault_db';
const STORE_NAME = 'media_blobs';

function openDB() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, 1);
    req.onupgradeneeded = (e) => {
      const db = e.target.result;
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME);
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

async function saveMediaBlob(id, blob) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readwrite');
    tx.objectStore(STORE_NAME).put(blob, id);
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

async function getMediaBlob(id) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readonly');
    const req = tx.objectStore(STORE_NAME).get(id);
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

// Khởi tạo danh sách bài hát mặc định nếu chưa có
function getStoredTracks() {
  const data = localStorage.getItem('tide_tracks');
  if (data) {
    try { return JSON.parse(data); } catch(e){}
  }
  const defaultTracks = [
    { id: 'track_01', name: 'Lead_Single_Master_v4.flac', type: 'audio/flac', size: '42.8 MB', hash: 'b79a4e912f...', shared: true, isDefault: true },
    { id: 'track_02', name: 'Vocal_Stems_Studio_Dry.wav', type: 'audio/wav', size: '68.1 MB', hash: '82f10ac349...', shared: false, isDefault: true },
    { id: 'track_03', name: 'Studio_Behind_The_Scenes.mp4', type: 'video/mp4', size: '124.5 MB', hash: '11ce9d40b2...', shared: false, isDefault: true }
  ];
  localStorage.setItem('tide_tracks', JSON.stringify(defaultTracks));
  return defaultTracks;
}

function saveTracks(tracks) {
  localStorage.setItem('tide_tracks', JSON.stringify(tracks));
  // Phát tín hiệu đồng bộ sang các tab khác
  try {
    const bc = new BroadcastChannel('tide_channel');
    bc.postMessage({ type: 'SYNC_TRACKS', tracks: tracks });
  } catch(e){}
}
"""

print("Đang khởi tạo các trang...")
