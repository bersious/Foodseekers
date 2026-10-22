import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UNRELEASED — Zero-Trust Audio Preview Studio (Powered by TideCloak)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0b0f19;
      --panel-bg: rgba(18, 24, 38, 0.75);
      --border: rgba(255, 255, 255, 0.08);
      --primary: #f43f5e;
      --primary-glow: rgba(244, 63, 94, 0.4);
      --accent: #38bdf8;
      --purple: #a855f7;
      --emerald: #10b981;
      --amber: #f59e0b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      background-image: 
        radial-gradient(at 15% 15%, rgba(244, 63, 94, 0.12) 0px, transparent 45%),
        radial-gradient(at 85% 85%, rgba(56, 189, 248, 0.12) 0px, transparent 45%);
      color: var(--text);
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      line-height: 1.5;
    }
    header {
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(16px);
      position: sticky;
      top: 0;
      z-index: 50;
      padding: 1rem 2.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }
    .brand-logo {
      background: linear-gradient(135deg, #f43f5e, #a855f7);
      width: 42px;
      height: 42px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      font-weight: 800;
      box-shadow: 0 0 20px rgba(244, 63, 94, 0.35);
    }
    .brand-text h1 {
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: -0.02em;
    }
    .brand-text p {
      font-size: 0.75rem;
      color: var(--text-muted);
    }
    .tide-tag {
      background: rgba(244, 63, 94, 0.1);
      border: 1px solid rgba(244, 63, 94, 0.3);
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      color: #fda4af;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    .role-bar {
      display: flex;
      gap: 0.4rem;
      background: rgba(255, 255, 255, 0.04);
      padding: 0.3rem;
      border-radius: 12px;
      border: 1px solid var(--border);
    }
    .role-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-weight: 600;
      cursor: pointer;
      font-size: 0.85rem;
      font-family: inherit;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }
    .role-btn.active {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }
    .role-btn.artist.active { border-left: 3px solid var(--primary); }
    .role-btn.reviewer.active { border-left: 3px solid var(--accent); }
    .role-btn.admin.active { border-left: 3px solid var(--amber); }

    main {
      max-width: 1200px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }

    .quorum-banner {
      background: var(--panel-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.25rem 2rem;
      margin-bottom: 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      backdrop-filter: blur(12px);
    }
    .quorum-left {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }
    .pulse-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--emerald);
      box-shadow: 0 0 14px var(--emerald);
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(1.2); }
      100% { opacity: 1; transform: scale(1); }
    }

    .view-card {
      background: var(--panel-bg);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 2rem;
      backdrop-filter: blur(16px);
      box-shadow: 0 24px 48px rgba(0,0,0,0.4);
    }
    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.75rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border);
    }

    .track-list {
      display: grid;
      gap: 1rem;
    }
    .track-item {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1.25rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s ease;
    }
    .track-item:hover {
      border-color: rgba(255, 255, 255, 0.2);
    }
    .track-meta {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }
    .track-icon {
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.05);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
    }
    .track-title {
      font-size: 1.05rem;
      font-weight: 600;
      color: #fff;
    }
    .track-sub {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }
    .badge {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.3rem 0.7rem;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
    }
    .badge-allowed {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid rgba(16, 185, 129, 0.35);
    }
    .badge-locked {
      background: rgba(244, 63, 94, 0.15);
      color: var(--primary);
      border: 1px solid rgba(244, 63, 94, 0.35);
    }

    .player-box {
      background: rgba(0,0,0,0.5);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.5rem;
      margin-top: 1.5rem;
    }
    .waveform-visualizer {
      display: flex;
      align-items: center;
      gap: 3px;
      height: 48px;
      margin: 1.25rem 0;
      padding: 0 0.5rem;
      background: rgba(255,255,255,0.02);
      border-radius: 8px;
    }
    .bar {
      flex: 1;
      background: rgba(255,255,255,0.15);
      border-radius: 3px;
      height: 20%;
      transition: height 0.1s ease;
    }
    .bar.playing {
      background: linear-gradient(to top, var(--primary), var(--accent));
      animation: jump 0.8s ease-in-out infinite alternate;
    }
    @keyframes jump {
      0% { height: 15%; }
      50% { height: 85%; }
      100% { height: 35%; }
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.65rem 1.35rem;
      border-radius: 10px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      font-family: inherit;
      border: none;
      transition: all 0.2s ease;
    }
    .btn-primary {
      background: var(--primary);
      color: #fff;
    }
    .btn-primary:hover {
      background: #e11d48;
      box-shadow: 0 0 16px var(--primary-glow);
    }
    .btn-outline {
      background: transparent;
      border: 1px solid var(--border);
      color: #fff;
    }
    .btn-outline:hover {
      background: rgba(255,255,255,0.08);
    }

    .admin-storage-table {
      width: 100%;
      border-collapse: collapse;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      margin-top: 1rem;
    }
    .admin-storage-table th, .admin-storage-table td {
      border: 1px solid var(--border);
      padding: 0.75rem 1rem;
      text-align: left;
    }
    .admin-storage-table th {
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
    }

    .info-callout {
      border-left: 4px solid var(--primary);
      background: rgba(244, 63, 94, 0.06);
      padding: 1rem;
      border-radius: 0 10px 10px 0;
      margin: 1.25rem 0;
      font-size: 0.88rem;
    }

    .hidden { display: none !important; }
  </style>
</head>
<body>

  <header>
    <div class="brand-wrap">
      <div class="brand-logo">⚡</div>
      <div class="brand-text">
        <h1>UNRELEASED</h1>
        <p>Zero-Trust Audio Preview Studio · Challenge 2 (Tide × RMIT 2026)</p>
      </div>
    </div>

    <div class="role-bar">
      <button class="role-btn artist active" onclick="switchRole('artist')">🎧 Artist / Producer</button>
      <button class="role-btn reviewer" onclick="switchRole('reviewer')">🎙️ Guest Reviewer</button>
      <button class="role-btn admin" onclick="switchRole('admin')">⚠️ Cloud Host Admin</button>
    </div>

    <div class="tide-tag">
      <span>●</span> TideCloak Emergent Authority
    </div>
  </header>

  <main>

    <div class="quorum-banner">
      <div class="quorum-left">
        <div class="pulse-dot" id="quorum-pulse"></div>
        <div>
          <strong id="quorum-title">Tide Fabric Quorum: LIVE & ENFORCING</strong>
          <p style="font-size: 0.8rem; color: var(--text-muted);">Decentralized authorization nodes verify scoped playback tokens. Oblivious proxy server.</p>
        </div>
      </div>
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;">
        Track Entitlement: <span id="entitlement-status" style="color: var(--emerald); font-weight: 600;">ACTIVE (1 TRACK)</span>
      </div>
    </div>

    <div class="views-wrapper">

      <!-- 1. ARTIST DASHBOARD -->
      <section id="artist-view" class="view-card">
        <div class="card-top">
          <div>
            <h2 style="font-size: 1.5rem; font-weight: 700;">Album Vault: "MIDNIGHT CIPHER" (Upcoming Release)</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Lead Artist: Alice Nguyen · 3 confidential master assets uploaded.</p>
          </div>
          <div>
            <span class="badge badge-allowed" id="artist-policy-badge">SHARING POLICY: ACTIVE</span>
          </div>
        </div>

        <div class="track-list">
          <div class="track-item">
            <div class="track-meta">
              <div class="track-icon">🎵</div>
              <div>
                <div class="track-title">01_Lead_Single_Master_v4.flac</div>
                <div class="track-sub">SHA256: 0xb79a4... · AES-256-GCM Session Sealed</div>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem;">
              <span class="badge badge-allowed" id="track1-share-badge">SHARED WITH REVIEWER MINH</span>
              <button class="btn btn-outline" style="font-size: 0.8rem;" onclick="toggleReviewerAccess()" id="btn-toggle-access">
                🚫 Revoke Minh's Access
              </button>
            </div>
          </div>

          <div class="track-item">
            <div class="track-meta">
              <div class="track-icon">🎚️</div>
              <div>
                <div class="track-title">02_Vocal_Stems_Dry_Studio.wav</div>
                <div class="track-sub">SHA256: 0x82f10... · Private Studio Stem</div>
              </div>
            </div>
            <div>
              <span class="badge badge-locked">STRICTLY PRIVATE (LOCKED)</span>
            </div>
          </div>

          <div class="track-item">
            <div class="track-meta">
              <div class="track-icon">🎹</div>
              <div>
                <div class="track-title">03_Unannounced_Feature_Draft.flac</div>
                <div class="track-sub">SHA256: 0x11ce9... · Unreleased Collaboration</div>
              </div>
            </div>
            <div>
              <span class="badge badge-locked">STRICTLY PRIVATE (LOCKED)</span>
            </div>
          </div>
        </div>

        <div class="info-callout">
          💡 <strong>Why TideCloak is Essential:</strong> On conventional platforms (Dropbox, Google Drive, SoundCloud Private), platform admins and storage servers hold the master decryption key. If a rogue employee leaks the file or AWS credentials are compromised, the unreleased album leaks worldwide. With TideCloak, <strong>no master key exists anywhere</strong>—Alice's tracks remain unbreakable ciphertext.
        </div>
      </section>

      <!-- 2. REVIEWER PLAYER -->
      <section id="reviewer-view" class="view-card hidden">
        <div class="card-top">
          <div>
            <h2 style="font-size: 1.5rem; font-weight: 700;">Collaborator Listening Room</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Authenticated as: Minh (Mixing & Mastering Engineer) via TideCloak BYOiD</p>
          </div>
          <div>
            <span class="badge badge-allowed" id="reviewer-status-badge">SESSION ENTITLED</span>
          </div>
        </div>

        <div id="reviewer-player-container">
          <div class="player-box" id="player-active">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div>
                <h3 style="font-size: 1.15rem; color: #fff;">01_Lead_Single_Master_v4.flac</h3>
                <p style="font-size: 0.8rem; color: var(--accent); font-family: 'JetBrains Mono', monospace;">
                  ✓ Decrypted Just-In-Time via Tide Emergent Authority
                </p>
              </div>
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: var(--text-muted);" id="time-display">
                0:00 / 3:42
              </div>
            </div>

            <div class="waveform-visualizer" id="waveform"></div>

            <div style="display: flex; gap: 1rem; align-items: center;">
              <button class="btn btn-primary" onclick="togglePlay()" id="btn-play">
                ▶ Play Decrypted Stream
              </button>
              <span style="font-size: 0.8rem; color: var(--text-muted);">
                Audio is decrypted directly inside Minh's secure browser sandbox. No file is cached to disk.
              </span>
            </div>
          </div>

          <div class="player-box hidden" id="player-revoked" style="border-color: rgba(244, 63, 94, 0.4); background: rgba(244, 63, 94, 0.05);">
            <h3 style="color: var(--primary); margin-bottom: 0.5rem;">✕ Stream Decryption Denied by Tide Quorum</h3>
            <p style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 0.5rem;">
              <strong>Error 403: EntitlementRevoked.</strong>
            </p>
            <p style="font-size: 0.85rem; color: var(--text-muted);"><br>
              Alice Nguyen has revoked reviewer entitlement for this session. Because authority is emergent, no cached token or backend manipulation can reconstruct the decryption key.
            </p>
          </div>
        </div>

        <div style="margin-top: 1.5rem;">
          <h4 style="font-size: 0.95rem; margin-bottom: 0.5rem;">Other Tracks in Album:</h4>
          <p style="font-size: 0.85rem; color: var(--text-muted);">
            • <code>02_Vocal_Stems_Dry_Studio.wav</code> — <span style="color: var(--primary);">Access Denied (Out of Scope)</span><br>
            • <code>03_Unannounced_Feature_Draft.flac</code> — <span style="color: var(--primary);">Access Denied (Out of Scope)</span>
          </p>
        </div>
      </section>

      <!-- 3. CLOUD ADMIN VIEW -->
      <section id="admin-view" class="view-card hidden">
        <div class="card-top">
          <div>
            <h2 style="font-size: 1.5rem; font-weight: 700;">Cloud Storage & Database Inspector</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Simulating a Rogue Platform Operator or Leaked AWS S3 Bucket</p>
          </div>
          <div>
            <span class="badge badge-locked">OBLIVIOUS SERVER — ZERO MASTER KEYS</span>
          </div>
        </div>

        <div class="info-callout">
          ⚠️ <strong>RMIT Hackathon Live Proof:</strong> In legacy apps (SoundCloud, Google Drive), an AWS S3 administrator or database operator can download and leak the `.flac` files directly. Below is the actual raw data stored on UNRELEASED servers:
        </div>

        <table class="admin-storage-table">
          <thead>
            <tr>
              <th>s3_object_key</th>
              <th>creator_uid</th>
              <th>raw_binary_payload (Storage Layer)</th>
              <th>master_key_presence</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>s3://unreleased-vault/track_01.enc</td>
              <td>usr_alice_84</td>
              <td style="color: var(--purple);">d8a391e4fc2901a88b5e027f8a1924bc99014e...</td>
              <td style="color: var(--primary); font-weight: 700;">NONE (Keys Never Exist)</td>
            </tr>
            <tr>
              <td>s3://unreleased-vault/track_02.enc</td>
              <td>usr_alice_84</td>
              <td style="color: var(--purple);">1f80aa7621c08be991448bcae912408fb241a7...</td>
              <td style="color: var(--primary); font-weight: 700;">NONE (Keys Never Exist)</td>
            </tr>
            <tr>
              <td>s3://unreleased-vault/track_03.enc</td>
              <td>usr_alice_84</td>
              <td style="color: var(--purple);">7c8911bb20e14ad9f92881a70094bba8912ef0...</td>
              <td style="color: var(--primary); font-weight: 700;">NONE (Keys Never Exist)</td>
            </tr>
          </tbody>
        </table>

        <div style="margin-top: 1.5rem; display: flex; gap: 1rem; align-items: center;">
          <button class="btn btn-outline" style="border-color: var(--primary); color: var(--primary);" onclick="attemptAdminLeak()">
            🚨 Attempt Root Master Decryption / Leak
          </button>
          <span id="admin-leak-status" style="font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;"></span>
        </div>
      </section>

    </div>
  </main>

  <script>
    let isEntitlementActive = true;
    let isPlaying = false;
    let playInterval = null;
    let currentSeconds = 0;

    const wf = document.getElementById('waveform');
    for (let i = 0; i < 70; i++) {
      const b = document.createElement('div');
      b.className = 'bar';
      const h = Math.floor(Math.sin(i * 0.15) * 40 + Math.random() * 30 + 20);
      b.style.height = `${h}%`;
      wf.appendChild(b);
    }

    function switchRole(role) {
      document.querySelectorAll('.role-btn').forEach(b => b.classList.remove('active'));
      document.querySelector(`.role-btn.${role}`).classList.add('active');

      document.getElementById('artist-view').classList.add('hidden');
      document.getElementById('reviewer-view').classList.add('hidden');
      document.getElementById('admin-view').classList.add('hidden');

      document.getElementById(`${role}-view`).classList.remove('hidden');

      if (role === 'reviewer') {
        renderReviewerPlayer();
      }
    }

    function toggleReviewerAccess() {
      isEntitlementActive = !isEntitlementActive;
      updateState();
    }

    function updateState() {
      const shareBadge = document.getElementById('track1-share-badge');
      const toggleBtn = document.getElementById('btn-toggle-access');
      const entitlementStatus = document.getElementById('entitlement-status');
      const quorumTitle = document.getElementById('quorum-title');
      const quorumPulse = document.getElementById('quorum-pulse');

      if (isEntitlementActive) {
        shareBadge.className = 'badge badge-allowed';
        shareBadge.innerText = 'SHARED WITH REVIEWER MINH';
        toggleBtn.innerText = "🚫 Revoke Minh's Access";
        entitlementStatus.innerText = 'ACTIVE (1 TRACK)';
        entitlementStatus.style.color = 'var(--emerald)';
        quorumPulse.style.background = 'var(--emerald)';
        quorumPulse.style.boxShadow = '0 0 14px var(--emerald)';
        quorumTitle.innerText = 'Tide Fabric Quorum: LIVE & ENFORCING';
      } else {
        shareBadge.className = 'badge badge-locked';
        shareBadge.innerText = 'ACCESS REVOKED (LOCKED)';
        toggleBtn.innerText = "✅ Re-Grant Minh's Access";
        entitlementStatus.innerText = 'REVOKED (0 TRACKS)';
        entitlementStatus.style.color = 'var(--primary)';
        quorumPulse.style.background = 'var(--primary)';
        quorumPulse.style.boxShadow = '0 0 14px var(--primary)';
        quorumTitle.innerText = 'Tide Fabric Quorum: POLICY ENFORCED (DENIED)';
        if (isPlaying) togglePlay();
      }
      renderReviewerPlayer();
    }

    function renderReviewerPlayer() {
      const activeP = document.getElementById('player-active');
      const revokedP = document.getElementById('player-revoked');
      const statusB = document.getElementById('reviewer-status-badge');

      if (isEntitlementActive) {
        activeP.classList.remove('hidden');
        revokedP.classList.add('hidden');
        statusB.className = 'badge badge-allowed';
        statusB.innerText = 'SESSION ENTITLED';
      } else {
        activeP.classList.add('hidden');
        revokedP.classList.remove('hidden');
        statusB.className = 'badge badge-locked';
        statusB.innerText = 'ENTITLEMENT REVOKED';
      }
    }

    function togglePlay() {
      const btn = document.getElementById('btn-play');
      const bars = document.querySelectorAll('.bar');
      const timeDisplay = document.getElementById('time-display');

      isPlaying = !isPlaying;
      if (isPlaying) {
        btn.innerText = '⏸ Pause Stream';
        btn.style.background = 'var(--accent)';
        bars.forEach(b => b.classList.add('playing'));
        playInterval = setInterval(() => {
          currentSeconds++;
          const m = Math.floor(currentSeconds / 60);
          const s = currentSeconds % 60;
          timeDisplay.innerText = `${m}:${s < 10 ? '0' : ''}${s} / 3:42`;
        }, 1000);
      } else {
        btn.innerText = '▶ Play Decrypted Stream';
        btn.style.background = 'var(--primary)';
        bars.forEach(b => b.classList.remove('playing'));
        clearInterval(playInterval);
      }
    }

    function attemptAdminLeak() {
      const stat = document.getElementById('admin-leak-status');
      stat.innerText = 'Querying Tide Fabric Quorum... ERROR: Unilateral master key does not exist. Oblivious proxy cannot leak audio.';
      stat.style.color = 'var(--primary)';
    }
  </script>
</body>
</html>
"""

with open(r"C:\Users\nguye\Foodseekers\prototype\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("Updated prototype/index.html to UNRELEASED successfully!")
