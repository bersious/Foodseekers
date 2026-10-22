import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

# Đọc file hiện tại và bổ sung khung Quy Tắc Phân Quyền (Tide Policy Engine)
def patch_page_1():
    p = os.path.join(FS_PROTO, "1", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    policy_ui = """
    <!-- KHUNG QUY TẮC PHÂN QUYỀN TIDECLOAK -->
    <div class="card" style="margin-top:24px;border-color:rgba(212,255,63,.25)">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
        <div>
          <h2 style="font-size:16px;font-weight:700;display:flex;align-items:center;gap:8px">
            <span style="color:var(--accent)">📜</span> Quy Tắc Phân Quyền Mật Mã TideCloak (Access Control Policy)
          </h2>
          <p style="font-size:12px;color:var(--muted);margin-top:2px">
            Quy định rõ: <strong>Ai được mở dữ liệu? Trong hoàn cảnh nào?</strong> (Tự động cập nhật vào mạng Quorum)
          </p>
        </div>
        <span class="mono" style="font-size:11px;color:var(--accent)">Engine: TideCloak v2.4</span>
      </div>

      <div style="background:#050608;border:1px solid var(--line);border-radius:12px;padding:16px;font-size:12px;color:#a5b4fc" class="mono" id="policy-json-viewer">
        // Đang đồng bộ chính sách bảo mật với mạng Tide Fabric Quorum...
      </div>
    </div>
    """

    # Chèn trước đóng main
    if "<!-- KHUNG QUY TẮC PHÂN QUYỀN TIDECLOAK -->" not in html:
        html = html.replace("</div>\n  </div>\n\n</main>", f"</div>\n  </div>\n{policy_ui}\n</main>")

    # Chèn hàm cập nhật JSON viewer trong script
    update_fn = """
function updatePolicyViewer(){
  const tracks = getStoredTracks();
  const users = getStoredUsers();
  const policyObj = {
    tideVersion: "2.4.0-emergent",
    timestamp: new Date().toISOString(),
    securityModel: "ZeroMasterKey_EmergentAuthority",
    vaultOwner: "tide:usr:alice_artist",
    quorumConsensusRequired: 3,
    accessRules: tracks.map(t => ({
      resourceId: t.id,
      resourceName: t.name,
      allowedIdentities: t.allowedUsers.map(u => {
        const uObj = users.find(x => x.username === u);
        return {
          username: u,
          did: uObj ? uObj.did : `tide:usr:${u}`,
          authorizedAction: "STREAM_DECRYPT_IN_MEMORY",
          circumstanceConditions: {
            inMemoryOnly: true,
            allowLocalDiskSave: false,
            sessionTtlSeconds: 86400,
            requireQuorumConsensus: true
          },
          status: "ACTIVE"
        };
      }),
      revocationPolicy: "InstantQuorumInvalidation_ZeroLatency"
    }))
  };
  const box = document.getElementById('policy-json-viewer');
  if(box) box.textContent = JSON.stringify(policyObj, null, 2);
}
"""
    if "function updatePolicyViewer" not in html:
        html = html.replace("checkAuth();", f"{update_fn}\ncheckAuth();\nupdatePolicyViewer();")
        html = html.replace("renderArtistTracks();", "renderArtistTracks();\nupdatePolicyViewer();")

    return html

def patch_page_2():
    p = os.path.join(FS_PROTO, "2", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    audit_ui = """
    <!-- BẢNG THEO DÕI GIẢI MÃ THỜI GIAN THỰC TIDECLOAK -->
    <div class="card" style="margin-top:24px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
        <h3 style="font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px">
          <span style="color:var(--ok)">⚡</span> Nhật Ký Đánh Giá Quy Tắc Mật Mã (Tide Execution Log)
        </h3>
        <span class="mono" style="font-size:11px;color:var(--dim)">Zero Master Key</span>
      </div>
      <div id="tide-execution-log" class="mono" style="background:#050608;border:1px solid var(--line);border-radius:10px;padding:14px;font-size:12px;color:var(--muted);line-height:1.7">
        > TideCloak SDK initialized. Sẵn sàng đánh giá chính sách phân quyền cho phiên người nghe.
      </div>
    </div>
    """
    if "<!-- BẢNG THEO DÕI GIẢI MÃ THỜI GIAN THỰC TIDECLOAK -->" not in html:
        html = html.replace("</div>\n  </div>\n\n</main>", f"</div>\n  </div>\n{audit_ui}\n</main>")

    log_fn = """
function appendExecutionLog(msg, isSuccess, isError){
  const logBox = document.getElementById('tide-execution-log');
  if(!logBox) return;
  const time = new Date().toLocaleTimeString();
  let color = 'var(--muted)';
  if(isSuccess) color = 'var(--ok)';
  if(isError) color = 'var(--danger)';
  logBox.innerHTML += `<div style="color:${color}">[${time}] ${msg}</div>`;
  logBox.scrollTop = logBox.scrollHeight;
}
"""
    if "function appendExecutionLog" not in html:
        html = html.replace("checkAuth();", f"{log_fn}\ncheckAuth();")
        html = html.replace("npTitle.textContent=track.name;", """
        npTitle.textContent=track.name;
        if(isAllowed){
          appendExecutionLog(`[QUORUM MATCH] Danh tính ${currentUser} khớp quy tắc: Cấp khóa phiên in-memory cho ${track.name}`, true);
        } else {
          appendExecutionLog(`[QUORUM DENIED] Danh tính ${currentUser} KHÔNG có trong quy tắc cho phép của ${track.name} (Chính sách bị từ chối 403)`, false, true);
        }
        """)

    return html

p1_content = patch_page_1()
p2_content = patch_page_2()

# Ghi ra cả 2 nơi
for base in [FS_PROTO, BW_RMIT]:
    with open(os.path.join(base, "1", "index.html"), "w", encoding="utf-8") as f:
        f.write(p1_content)
    with open(os.path.join(base, "2", "index.html"), "w", encoding="utf-8") as f:
        f.write(p2_content)

print("✓ Đã cập nhật khung Quy Tắc Phân Quyền TideCloak (Access Control Policy) vào cả 2 repo!")
