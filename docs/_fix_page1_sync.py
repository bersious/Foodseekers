import os

def fix_page1():
    for base in [r"C:\Users\nguye\Foodseekers\prototype", r"C:\Users\nguye\bersious-web\rmit"]:
        path = os.path.join(base, "1", "index.html")
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Sync requests in fetchCloudState
        old_sync_chunk = """      if (localStorage.getItem('tide_users') !== cloudUsersStr) {
        localStorage.setItem('tide_users', cloudUsersStr);
        hasChanged = true;
      }"""
        new_sync_chunk = """      if (localStorage.getItem('tide_users') !== cloudUsersStr) {
        localStorage.setItem('tide_users', cloudUsersStr);
        hasChanged = true;
      }
      const cloudReqStr = JSON.stringify(cloud.requests || []);
      if (localStorage.getItem('tide_requests_v2') !== cloudReqStr) {
        localStorage.setItem('tide_requests_v2', cloudReqStr);
        hasChanged = true;
      }"""
        if old_sync_chunk in code:
            code = code.replace(old_sync_chunk, new_sync_chunk)

        # 2. Add onCloudSync function
        if "function onCloudSync()" not in code:
            code = code.replace(
                "setInterval(fetchCloudState, 2500);\nfetchCloudState();",
                "function onCloudSync(){\n  getStoredUsers();\n  renderArtistTracks();\n  renderRequests();\n  updatePolicyViewer();\n}\nsetInterval(fetchCloudState, 2000);\nfetchCloudState();"
            )

        # 3. Enhance renderRequests to show only PENDING and lookup track name
        old_render_req = """function renderRequests(){
  const stateRaw = localStorage.getItem('tide_requests_v2');
  const requests = stateRaw ? JSON.parse(stateRaw) : [];
  const box=document.getElementById('requests-list');
  const count=document.getElementById('req-count');
  box.innerHTML='';
  if(!requests.length){
    box.innerHTML='<div style="font-size:13px;color:var(--muted);padding:16px">Không có đơn xin quyền nào đang chờ duyệt.</div>';
    count.textContent='0 đơn chờ';
    return;
  }
  count.textContent=requests.length+' đơn chờ';
  requests.forEach(r=>{
    const card=document.createElement('div');
    card.className='req-card';
    card.innerHTML=`
      <div class="req-info">
        <div class="req-title">${r.username} muốn nghe <strong>${r.trackName||r.trackId}</strong></div>
        <div class="req-sub">Yêu cầu vào ${new Date(r.createdAt||Date.now()).toLocaleString()}</div>
      </div>
      <div class="req-actions">
        <button class="btn btn-ok btn-sm" onclick="resolveRequest('${r.id}','APPROVE')">Duyệt</button>
        <button class="btn btn-danger btn-sm" onclick="resolveRequest('${r.id}','DENY')">Từ chối</button>
      </div>
    `;
    box.appendChild(card);
  });
}"""

        new_render_req = """function renderRequests(){
  const stateRaw = localStorage.getItem('tide_requests_v2');
  const requests = stateRaw ? JSON.parse(stateRaw) : [];
  const pendingRequests = requests.filter(r => r.status === 'PENDING');
  const box=document.getElementById('requests-list');
  const count=document.getElementById('req-count');
  box.innerHTML='';
  if(!pendingRequests.length){
    box.innerHTML='<div style="font-size:13px;color:var(--muted);padding:16px" class="mono">✓ Không có đơn xin quyền nào đang chờ duyệt.</div>';
    count.textContent='0 đơn chờ';
    return;
  }
  count.textContent=pendingRequests.length+' đơn chờ';
  const tracks = getStoredTracks();
  pendingRequests.forEach(r=>{
    const trk = tracks.find(x => x.id === r.trackId);
    const trackTitle = trk ? trk.name : r.trackId;
    const card=document.createElement('div');
    card.className='req-card';
    card.innerHTML=`
      <div class="req-info">
        <div class="req-title">👤 <strong>${r.username}</strong> xin quyền nghe: <span style="color:var(--accent)">${trackTitle}</span></div>
        <div class="req-sub mono" style="font-size:11px;color:var(--muted);margin-top:2px">Thời gian: ${new Date(r.createdAt||Date.now()).toLocaleTimeString()}</div>
      </div>
      <div class="req-actions">
        <button class="btn btn-ok btn-sm" onclick="resolveRequest('${r.id}','APPROVE')">✓ Duyệt Cấp Quyền</button>
        <button class="btn btn-danger btn-sm" onclick="resolveRequest('${r.id}','DENY')">✕ Từ Chối</button>
      </div>
    `;
    box.appendChild(card);
  });
}"""

        if old_render_req in code:
            code = code.replace(old_render_req, new_render_req)

        with open(path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Fixed page 1 at: {path}")

fix_page1()
