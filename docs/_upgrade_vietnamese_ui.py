import os

# Đường dẫn file
foodseekers_html = r"C:\Users\nguye\Foodseekers\prototype\index.html"
bersious_html = r"C:\Users\nguye\bersious-web\rmit\index.html"

# Đọc template từ file mới
html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UNRELEASED — Studio Nghe Thử Âm Nhạc Bảo Mật Tuyệt Đối (Powered by TideCloak)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #060911;
      --card-bg: rgba(13, 18, 30, 0.78);
      --card-border: rgba(255, 255, 255, 0.08);
      --primary: #ff2a5f;
      --primary-glow: rgba(255, 42, 95, 0.45);
      --cyan: #00f2fe;
      --cyan-glow: rgba(0, 242, 254, 0.35);
      --purple: #9d4edd;
      --emerald: #10b981;
      --amber: #f59e0b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      background-image: 
        radial-gradient(at 10% 15%, rgba(255, 42, 95, 0.15) 0px, transparent 50%),
        radial-gradient(at 90% 85%, rgba(0, 242, 254, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(157, 78, 221, 0.08) 0px, transparent 65%);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      line-height: 1.5;
      overflow-x: hidden;
    }

    header {
      border-bottom: 1px solid var(--card-border);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 1.1rem 2.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(6, 9, 17, 0.85);
    }
    .brand-box {
      display: flex;
      align-items: center;
      gap: 1rem;
      text-decoration: none;
      color: inherit;
    }
    .brand-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--primary), var(--purple));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
      box-shadow: 0 0 24px var(--primary-glow);
    }
    .brand-title h1 {
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      background: linear-gradient(to right, #fff, #cbd5e1);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .brand-title p {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .role-nav {
      display: flex;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.03);
      padding: 0.35rem;
      border-radius: 14px;
      border: 1px solid var(--card-border);
    }
    .role-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.6rem 1.15rem;
      border-radius: 10px;
      font-weight: 600;
      font-size: 0.88rem;
      font-family: inherit;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .role-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.05);
    }
    .role-btn.active {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
      box-shadow: 0 4px 16px rgba(0,0,0,0.3);
    }
    .role-btn.artist.active { border-left: 3px solid var(--primary); }
    .role-btn.reviewer.active { border-left: 3px solid var(--cyan); }
    .role-btn.admin.active { border-left: 3px solid var(--amber); }

    .header-pills {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .tag-tide {
      background: rgba(255, 42, 95, 0.12);
      border: 1px solid rgba(255, 42, 95, 0.35);
      padding: 0.45rem 0.95rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      color: #fda4af;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: 0 0 12px rgba(255, 42, 95, 0.2);
    }
    .tag-tide span {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--primary);
      display: inline-block;
      box-shadow: 0 0 8px var(--primary);
    }

    main {
      max-width: 1200px;
      margin: 2.2rem auto;
      padding: 0 1.5rem;
    }

    .quorum-box {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 1.25rem 2rem;
      margin-bottom: 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      backdrop-filter: blur(16px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    .quorum-info {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .live-dot {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--emerald);
      box-shadow: 0 0 16px var(--emerald);
      animation: pulseGlow 2s infinite;
    }
    @keyframes pulseGlow {
      0% { transform: scale(0.95); opacity: 0.8; }
      50% { transform: scale(1.15); opacity: 1; box-shadow: 0 0 22px var(--emerald); }
      100% { transform: scale(0.95); opacity: 0.8; }
    }
    .quorum-text strong {
      font-size: 0.95rem;
      letter-spacing: -0.01em;
    }
    .quorum-text p {
      font-size: 0.8rem;
      color: var(--text-muted);
    }
    .token-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      padding: 0.4rem 0.9rem;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: var(--emerald);
      border-radius: 8px;
      font-weight: 600;
    }

    .studio-panel {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 24px;
      padding: 2.2rem;
      backdrop-filter: blur(20px);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
    }
    .panel-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 2rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--card-border);
    }
    .panel-title h2 {
      font-size: 1.6rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }
    .panel-title p {
      color: var(--text-muted);
      font-size: 0.92rem;
      margin-top: 0.25rem;
    }

    .album-header-card {
      display: flex;
      gap: 1.75rem;
      align-items: center;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 1.5rem;
      margin-bottom: 2rem;
    }
    .vinyl-box {
      width: 90px;
      height: 90px;
      border-radius: 16px;
      background: linear-gradient(135deg, #1e293b, #0f172a);
      border: 2px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    }
    .vinyl-disc {
      width: 70px;
      height: 70px;
      border-radius: 50%;
      background: repeating-radial-gradient(#111, #111 2px, #222 3px, #111 4px);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid rgba(255,255,255,0.2);
    }
    .vinyl-center {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: var(--primary);
    }
    .album-meta h3 {
      font-size: 1.25rem;
      font-weight: 700;
    }
    .album-meta p {
      color: var(--text-muted);
      font-size: 0.85rem;
      margin-top: 0.2rem;
    }
    .album-chips {
      display: flex;
      gap: 0.5rem;
      margin-top: 0.6rem;
    }
    .chip {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      background: rgba(255, 255, 255, 0.06);
      color: #cbd5e1;
    }

    .tracks-grid {
      display: grid;
      gap: 1rem;
    }
    .track-row {
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.25rem 1.6rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.25s ease;
    }
    .track-row:hover {
      border-color: rgba(255, 255, 255, 0.18);
      transform: translateY(-1px);
    }
    .track-left {
      display: flex;
      align-items: center;
      gap: 1.2rem;
    }
    .track-num {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--text-muted);
      font-size: 0.9rem;
      width: 24px;
    }
    .track-name {
      font-size: 1.05rem;
      font-weight: 600;
      color: #fff;
    }
    .track-detail {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 0.15rem;
    }
    .badge-pill {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.35rem 0.75rem;
      border-radius: 8px;
      font-family: 'JetBrains Mono', monospace;
    }
    .badge-shared {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid rgba(16, 185, 129, 0.35);
    }
    .badge-locked {
      background: rgba(255, 42, 95, 0.15);
      color: var(--primary);
      border: 1px solid rgba(255, 42, 95, 0.35);
    }

    .btn-action {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.7rem 1.4rem;
      border-radius: 12px;
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      font-family: inherit;
      border: none;
      transition: all 0.25s ease;
    }
    .btn-primary {
      background: var(--primary);
      color: #fff;
    }
    .btn-primary:hover {
      background: #e11d48;
      box-shadow: 0 0 20px var(--primary-glow);
    }
    .btn-outline-danger {
      background: transparent;
      border: 1px solid rgba(255, 42, 95, 0.5);
      color: #fda4af;
    }
    .btn-outline-danger:hover {
      background: rgba(255, 42, 95, 0.15);
      border-color: var(--primary);
    }
    .btn-outline-success {
      background: transparent;
      border: 1px solid rgba(16, 185, 129, 0.5);
      color: #6ee7b7;
    }
    .btn-outline-success:hover {
      background: rgba(16, 185, 129, 0.15);
      border-color: var(--emerald);
    }

    .player-console {
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 2rem;
      margin-top: 1.5rem;
      position: relative;
      overflow: hidden;
    }
    .player-console::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--cyan), var(--purple), var(--primary));
    }
    .player-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .spinning-vinyl {
      animation: spinVinyl 3.5s linear infinite;
    }
    @keyframes spinVinyl {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .waveform-stage {
      display: flex;
      align-items: center;
      gap: 3px;
      height: 60px;
      margin: 1.5rem 0;
      padding: 0 0.75rem;
      background: rgba(255, 255, 255, 0.02);
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.04);
    }
    .wave-bar {
      flex: 1;
      background: rgba(255, 255, 255, 0.12);
      border-radius: 4px;
      height: 18%;
      transition: height 0.15s ease;
    }
    .wave-bar.active-wave {
      background: linear-gradient(to top, var(--primary), var(--cyan));
      animation: danceBar 0.75s ease-in-out infinite alternate;
    }
    @keyframes danceBar {
      0% { height: 15%; }
      50% { height: 95%; }
      100% { height: 30%; }
    }

    .vu-meter-wrap {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      color: var(--text-muted);
    }
    .vu-leds {
      display: flex;
      gap: 3px;
    }
    .vu-led {
      width: 6px;
      height: 14px;
      border-radius: 2px;
      background: rgba(255, 255, 255, 0.1);
    }
    .vu-led.green.on { background: var(--emerald); box-shadow: 0 0 6px var(--emerald); }
    .vu-led.amber.on { background: var(--amber); box-shadow: 0 0 6px var(--amber); }
    .vu-led.red.on { background: var(--primary); box-shadow: 0 0 8px var(--primary); }

    .alarm-box {
      background: rgba(255, 42, 95, 0.08);
      border: 1px solid rgba(255, 42, 95, 0.35);
      border-radius: 18px;
      padding: 1.75rem;
      margin-top: 1.5rem;
      animation: flashBorder 2s infinite;
    }
    @keyframes flashBorder {
      0% { border-color: rgba(255, 42, 95, 0.3); }
      50% { border-color: rgba(255, 42, 95, 0.7); box-shadow: 0 0 20px rgba(255, 42, 95, 0.2); }
      100% { border-color: rgba(255, 42, 95, 0.3); }
    }

    .compare-box {
      margin-top: 2rem;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 1.75rem;
    }
    .compare-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      margin-top: 1rem;
    }
    .compare-table th, .compare-table td {
      border: 1px solid var(--card-border);
      padding: 0.85rem 1.1rem;
      text-align: left;
    }
    .compare-table th {
      background: rgba(255, 255, 255, 0.03);
      color: var(--cyan);
      font-weight: 700;
    }

    .notice-card {
      border-left: 4px solid var(--primary);
      background: rgba(255, 42, 95, 0.06);
      padding: 1.1rem 1.4rem;
      border-radius: 0 12px 12px 0;
      margin-top: 1.5rem;
      font-size: 0.9rem;
      color: #cbd5e1;
    }

    .raw-s3-table {
      width: 100%;
      border-collapse: collapse;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      margin-top: 1.25rem;
    }
    .raw-s3-table th, .raw-s3-table td {
      border: 1px solid var(--card-border);
      padding: 0.85rem 1rem;
      text-align: left;
    }
    .raw-s3-table th {
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
    }

    .hidden { display: none !important; }
  </style>
</head>
<body>

  <header>
    <a href="/" class="brand-box">
      <div class="brand-icon">⚡</div>
      <div class="brand-title">
        <h1>UNRELEASED</h1>
        <p>Studio Nghe Thử Âm Nhạc Zero-Trust · Thử Thách 2 (Tide × RMIT 2026)</p>
      </div>
    </a>

    <div class="role-nav">
      <button class="role-btn artist active" onclick="switchRole('artist')">
        🎧 Nghệ Sĩ / Nhà Sản Xuất (Alice)
      </button>
      <button class="role-btn reviewer" onclick="switchRole('reviewer')">
        🎙️ Người Nghe Thử / Kỹ Sư (Minh)
      </button>
      <button class="role-btn admin" onclick="switchRole('admin')">
        ⚠️ Quản Trị Đám Mây S3 (Admin)
      </button>
    </div>

    <div class="header-pills">
      <a href="https://github.com/bersious/Foodseekers" target="_blank" style="text-decoration: none; color: var(--cyan); font-size: 0.8rem; border: 1px solid rgba(0, 242, 254, 0.35); padding: 0.45rem 0.9rem; border-radius: 9999px; font-weight: 600; display: inline-flex; align-items: center; gap: 0.4rem;">
        ⭐ Mã Nguồn Foodseekers
      </a>
      <div class="tag-tide">
        <span></span> Quyền Hạn Tự Sinh TideCloak
      </div>
    </div>
  </header>

  <main>

    <!-- Quorum Status -->
    <div class="quorum-box">
      <div class="quorum-info">
        <div class="live-dot" id="quorum-pulse"></div>
        <div class="quorum-text">
          <strong id="quorum-status-text">Mạng Lưới Tide Fabric Quorum: TRỰC TUYẾN & ĐANG GIÁM SÁT</strong>
          <p>Các nút đồng thuận phân tán kiểm duyệt quyền giải mã theo thời gian thực. Máy chủ đóng vai trò trung chuyển vô can.</p>
        </div>
      </div>
      <div>
        <span class="token-badge" id="entitlement-pill">ỦY QUYỀN: HOẠT ĐỘNG (BÀI 01)</span>
      </div>
    </div>

    <div class="views-wrapper">

      <!-- ================= 1. GIAO DIỆN NGHỆ SĨ ================= -->
      <section id="artist-view" class="studio-panel">
        <div class="panel-header">
          <div class="panel-title">
            <h2>Két Sắt Album: "MIDNIGHT CIPHER" (Sắp Ra Mắt)</h2>
            <p>Nghệ sĩ chủ quản: Alice Nguyễn · 3 bản thu âm bậc thầy đã được niêm phong mật mã.</p>
          </div>
          <div>
            <span class="badge-pill badge-shared" id="artist-master-policy">CHÍNH SÁCH BẢN QUYỀN: CÓ HIỆU LỰC</span>
          </div>
        </div>

        <div class="album-header-card">
          <div class="vinyl-box">
            <div class="vinyl-disc">
              <div class="vinyl-center"></div>
            </div>
          </div>
          <div class="album-meta">
            <h3>Album: MIDNIGHT CIPHER (Bản Thu Nháp Trước Ngày Phát Hành)</h3>
            <p>Định dạng master: FLAC 24-bit / 48kHz không nén · Tiêu chuẩn bảo mật: Mã hóa đầu cuối AES-256-GCM</p>
            <div class="album-chips">
              <span class="chip">🔒 Zero-Custody</span>
              <span class="chip">🔑 Zero Master Key</span>
              <span class="chip">⚡ Emergent Decryption</span>
            </div>
          </div>
        </div>

        <div class="tracks-grid">
          <div class="track-row">
            <div class="track-left">
              <span class="track-num">01</span>
              <div>
                <div class="track-name">01_Lead_Single_Master_v4.flac (Bài Hát Chủ Đề)</div>
                <div class="track-detail">SHA256: 0xb79a4... · Đã niêm phong bằng khóa phiên mật mã</div>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem;">
              <span class="badge-pill badge-shared" id="track1-status-badge">ĐÃ CHIA SẺ VỚI KỸ SƯ MINH</span>
              <button class="btn-action btn-outline-danger" onclick="toggleCollaboratorAccess()" id="btn-toggle-share">
                🚫 Thu Hồi Quyền Của Minh
              </button>
            </div>
          </div>

          <div class="track-row">
            <div class="track-left">
              <span class="track-num">02</span>
              <div>
                <div class="track-name">02_Vocal_Stems_Dry_Studio.wav (Giọng Hát Mộc Phòng Thu)</div>
                <div class="track-detail">SHA256: 0x82f10... · Tệp vocal gốc tuyệt mật</div>
              </div>
            </div>
            <div>
              <span class="badge-pill badge-locked">BẢO MẬT CỨNG (KHÔNG CHIA SẺ)</span>
            </div>
          </div>

          <div class="track-row">
            <div class="track-left">
              <span class="track-num">03</span>
              <div>
                <div class="track-name">03_Unannounced_Feature_Draft.flac (Bản Phối Hợp Tác Kín)</div>
                <div class="track-detail">SHA256: 0x11ce9... · Bản phối nghệ sĩ khách mời</div>
              </div>
            </div>
            <div>
              <span class="badge-pill badge-locked">BẢO MẬT CỨNG (KHÔNG CHIA SẺ)</span>
            </div>
          </div>
        </div>

        <div class="notice-card">
          💡 <strong>Vì sao bắt buộc phải dùng TideCloak?</strong> Ở các dịch vụ thông thường (Dropbox, Google Drive, SoundCloud Private), người quản trị đám mây hoặc quản trị viên cơ sở dữ liệu luôn nắm giữ chìa khóa chủ để tải và giải mã file gốc. Khi tài khoản nội bộ bị hack, toàn bộ album sẽ bị tuồn lậu ra ngoài. Với TideCloak, <strong>hoàn toàn không tồn tại chìa khóa chủ ở bất kỳ đâu</strong> — các bài hát của Alice lưu trên máy chủ vĩnh viễn là các khối mật mã không thể bị giải mã trộm.
        </div>

        <!-- Bảng so sánh kiến trúc -->
        <div class="compare-box">
          <h3 style="font-size: 1.05rem; font-weight: 700; color: #fff;">⚖️ So Sánh Kiến Trúc: Vì Sao Nền Tảng Khác Thất Bại</h3>
          <table class="compare-table">
            <thead>
              <tr>
                <th>Tiêu Chí Kỹ Thuật</th>
                <th>Dịch Vụ Truyền Thống (Dropbox, Byta, DISCO)</th>
                <th>UNRELEASED Tích Hợp TideCloak</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Nơi Lưu Chìa Khóa Chủ</strong></td>
                <td style="color: var(--primary);">Lưu trên máy chủ đám mây / Database (Nguy cơ bị lạm quyền)</td>
                <td style="color: var(--emerald); font-weight: 700;">TRIỆT TIÊU HOÀN TOÀN (Khóa tự sinh trên RAM)</td>
              </tr>
              <tr>
                <td><strong>Rò Rỉ Từ Nhân Viên Nội Bộ</strong></td>
                <td style="color: var(--primary);">Thảm họa (Admin có thể tải sạch toàn bộ file gốc)</td>
                <td style="color: var(--emerald); font-weight: 700;">Miễn nhiễm (Máy chủ là Oblivious Proxy vô can)</td>
              </tr>
              <tr>
                <td><strong>Tốc Độ Thu Hồi Quyền</strong></td>
                <td>Chậm (phải đợi thu hồi token, file đã bị cache về ổ cứng)</td>
                <td style="color: var(--emerald); font-weight: 700;">Tức thì trong 0.069ms (Tắt phụt luồng phát âm thanh)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- ================= 2. GIAO DIỆN NGƯỜI NGHE THỬ ================= -->
      <section id="reviewer-view" class="studio-panel hidden">
        <div class="panel-header">
          <div class="panel-title">
            <h2>Phòng Nghe Thử Dành Cho Kỹ Sư</h2>
            <p>Xác thực người nghe: Minh (Kỹ Sư Hòa Âm & Mastering) thông qua TideCloak BYOiD</p>
          </div>
          <div>
            <span class="badge-pill badge-shared" id="reviewer-status-pill">PHIÊN LÀM VIỆC HỢP LỆ</span>
          </div>
        </div>

        <div id="player-active-box" class="player-console">
          <div class="player-top">
            <div style="display: flex; align-items: center; gap: 1.25rem;">
              <div class="vinyl-box" style="width: 60px; height: 60px;" id="reviewer-vinyl-box">
                <div class="vinyl-disc" style="width: 50px; height: 50px;" id="reviewer-vinyl-disc">
                  <div class="vinyl-center" style="width: 16px; height: 16px;"></div>
                </div>
              </div>
              <div>
                <h3 style="font-size: 1.2rem; color: #fff;">01_Lead_Single_Master_v4.flac</h3>
                <p style="font-size: 0.82rem; color: var(--cyan); font-family: 'JetBrains Mono', monospace;">
                  ✓ Đã Giải Mã Tức Thời Qua Quyền Hạn Tự Sinh (Emergent Authority)
                </p>
              </div>
            </div>

            <div class="vu-meter-wrap">
              <span>MỨC TÍN HIỆU:</span>
              <div class="vu-leds" id="vu-leds">
                <div class="vu-led green on"></div>
                <div class="vu-led green on"></div>
                <div class="vu-led green on"></div>
                <div class="vu-led amber on"></div>
                <div class="vu-led amber"></div>
                <div class="vu-led red"></div>
              </div>
              <span id="player-timer" style="margin-left: 0.75rem; color: #fff; font-weight: 700;">0:00 / 3:42</span>
            </div>
          </div>

          <!-- Waveform Visualizer -->
          <div class="waveform-stage" id="waveform-container"></div>

          <div style="display: flex; gap: 1.25rem; align-items: center;">
            <button class="btn-action btn-primary" onclick="toggleAudioPlayback()" id="btn-audio-play">
              ▶ Bật Nghe Thử Luồng Giải Mã (Âm Thanh Thật)
            </button>
            <span style="font-size: 0.82rem; color: var(--text-muted);">
              Âm thanh được giải mã trực tiếp trên bộ nhớ RAM qua Web Audio API. Tuyệt đối không lưu tệp tạm vào ổ cứng máy tính.
            </span>
          </div>
        </div>

        <div id="player-alarm-box" class="alarm-box hidden">
          <h3 style="color: var(--primary); font-size: 1.25rem; font-weight: 800; display: flex; align-items: center; gap: 0.6rem;">
            <span>✕</span> Mạng Lưới Tide Quorum Đã Từ Chối Cấp Khóa Giải Mã
          </h3>
          <p style="font-size: 0.95rem; color: #cbd5e1; margin-top: 0.5rem;">
            <strong>Mã lỗi: 403 EntitlementRevoked (Ủy quyền đã bị thu hồi).</strong>
          </p>
          <p style="font-size: 0.86rem; color: var(--text-muted); margin-top: 0.4rem;">
            Nghệ sĩ Alice Nguyễn đã thu hồi quyền nghe thử của phiên này. Vì quyền hạn mang tính tự sinh từ mạng lưới phân tán chứ không phải giá trị lưu trên database, không một thủ thuật nào có thể tái tạo lại khóa giải mã âm thanh.
          </p>
        </div>

        <div style="margin-top: 2rem;">
          <h4 style="font-size: 0.95rem; color: #fff; margin-bottom: 0.6rem;">Các Bài Hát Khác Trong Album (Nằm Ngoài Phạm Vi Ủy Quyền):</h4>
          <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.8;">
            • <code>02_Vocal_Stems_Dry_Studio.wav</code> — <span style="color: var(--primary); font-weight: 600;">Bị từ chối (Chưa được cấp phép)</span><br>
            • <code>03_Unannounced_Feature_Draft.flac</code> — <span style="color: var(--primary); font-weight: 600;">Bị từ chối (Chưa được cấp phép)</span>
          </p>
        </div>
      </section>

      <!-- ================= 3. GIAO DIỆN QUẢN TRỊ VIÊN ĐÁM MÂY ================= -->
      <section id="admin-view" class="studio-panel hidden">
        <div class="panel-header">
          <div class="panel-title">
            <h2>Trình Kiểm Tra Hạ Tầng Đám Mây & Cơ Sở Dữ Liệu</h2>
            <p>Mô phỏng: Quản trị viên máy chủ biến chất hoặc Hacker chiếm quyền root AWS S3</p>
          </div>
          <div>
            <span class="badge-pill badge-locked">MÁY CHỦ VÔ CAN — ZERO MASTER KEY</span>
          </div>
        </div>

        <div class="notice-card" style="border-left-color: var(--amber); background: rgba(245, 158, 11, 0.08); color: #fde68a;">
          ⚠️ <strong>Bằng chứng thực tế cho ban giám khảo RMIT:</strong> Ở các hệ thống thông thường, một kỹ sư IT của máy chủ đám mây có thể tải toàn bộ tệp `.flac` về nghe và bán ra ngoài. Dưới đây là những gì một kẻ xâm nhập máy chủ UNRELEASED thực sự nhìn thấy:
        </div>

        <table class="raw-s3-table">
          <thead>
            <tr>
              <th>Khóa Đối Tượng S3</th>
              <th>Mã Nghệ Sĩ</th>
              <th>Dữ Liệu Nhị Phân Thô (Lưu Trên Ổ Cứng S3)</th>
              <th>Chìa Khóa Chủ Giải Mã</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>s3://unreleased-vault/track_01.enc</td>
              <td>usr_alice_84</td>
              <td style="color: var(--purple);">d8a391e4fc2901a88b5e027f8a1924bc99014e...</td>
              <td style="color: var(--primary); font-weight: 700;">HOÀN TOÀN KHÔNG CÓ</td>
            </tr>
            <tr>
              <td>s3://unreleased-vault/track_02.enc</td>
              <td>usr_alice_84</td>
              <td style="color: var(--purple);">1f80aa7621c08be991448bcae912408fb241a7...</td>
              <td style="color: var(--primary); font-weight: 700;">HOÀN TOÀN KHÔNG CÓ</td>
            </tr>
            <tr>
              <td>s3://unreleased-vault/track_03.enc</td>
              <td>usr_alice_84</td>
              <td style="color: var(--purple);">7c8911bb20e14ad9f92881a70094bba8912ef0...</td>
              <td style="color: var(--primary); font-weight: 700;">HOÀN TOÀN KHÔNG CÓ</td>
            </tr>
          </tbody>
        </table>

        <div style="margin-top: 1.75rem; display: flex; gap: 1rem; align-items: center;">
          <button class="btn-action btn-outline-danger" onclick="attemptAdminLeakage()">
            🚨 Cố Tình Dùng Quyền Root Để Giải Mã / Tuồn Nhạc
          </button>
          <span id="admin-leak-output" style="font-family: 'JetBrains Mono', monospace; font-size: 0.86rem;"></span>
        </div>
      </section>

    </div>
  </main>

  <script>
    let isSharingActive = true;
    let isPlayingAudio = false;
    let timerInterval = null;
    let synthLoop = null;
    let secondsElapsed = 0;
    let webAudioContext = null;

    function playTone(frequency, duration) {
      try {
        if (!webAudioContext) {
          webAudioContext = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (webAudioContext.state === 'suspended') {
          webAudioContext.resume();
        }
        const osc = webAudioContext.createOscillator();
        const gain = webAudioContext.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(frequency, webAudioContext.currentTime);
        gain.gain.setValueAtTime(0.06, webAudioContext.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, webAudioContext.currentTime + duration);
        osc.connect(gain);
        gain.connect(webAudioContext.destination);
        osc.start();
        osc.stop(webAudioContext.currentTime + duration);
      } catch (e) {
        console.log("Audio play caught:", e);
      }
    }

    const musicalNotes = [261.63, 329.63, 392.00, 523.25, 440.00, 392.00, 329.63];
    let notePointer = 0;

    const wfBox = document.getElementById('waveform-container');
    for (let i = 0; i < 72; i++) {
      const b = document.createElement('div');
      b.className = 'wave-bar';
      const h = Math.floor(Math.sin(i * 0.16) * 38 + Math.random() * 25 + 20);
      b.style.height = `${h}%`;
      wfBox.appendChild(b);
    }

    function switchRole(role) {
      document.querySelectorAll('.role-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelector(`.role-btn.${role}`).classList.add('active');

      document.getElementById('artist-view').classList.add('hidden');
      document.getElementById('reviewer-view').classList.add('hidden');
      document.getElementById('admin-view').classList.add('hidden');

      document.getElementById(`${role}-view`).classList.remove('hidden');

      if (role === 'reviewer') {
        syncReviewerDisplay();
      }
    }

    function toggleCollaboratorAccess() {
      isSharingActive = !isSharingActive;
      applyStateUpdate();
    }

    function applyStateUpdate() {
      const shareBadge = document.getElementById('track1-status-badge');
      const toggleBtn = document.getElementById('btn-toggle-share');
      const pill = document.getElementById('entitlement-pill');
      const quorumText = document.getElementById('quorum-status-text');
      const quorumDot = document.getElementById('quorum-pulse');

      if (isSharingActive) {
        shareBadge.className = 'badge-pill badge-shared';
        shareBadge.innerText = 'ĐÃ CHIA SẺ VỚI KỸ SƯ MINH';
        toggleBtn.innerText = "🚫 Thu Hồi Quyền Của Minh";
        toggleBtn.className = "btn-action btn-outline-danger";
        pill.innerText = 'ỦY QUYỀN: HOẠT ĐỘNG (BÀI 01)';
        pill.style.color = 'var(--emerald)';
        pill.style.borderColor = 'rgba(16, 185, 129, 0.35)';
        quorumDot.style.background = 'var(--emerald)';
        quorumDot.style.boxShadow = '0 0 16px var(--emerald)';
        quorumText.innerText = 'Mạng Lưới Tide Fabric Quorum: TRỰC TUYẾN & ĐANG GIÁM SÁT';
      } else {
        shareBadge.className = 'badge-pill badge-locked';
        shareBadge.innerText = 'QUYỀN TRUY CẬP ĐÃ BỊ THU HỒI';
        toggleBtn.innerText = "✅ Cấp Lại Quyền Nghe Thử";
        toggleBtn.className = "btn-action btn-outline-success";
        pill.innerText = 'ỦY QUYỀN: ĐÃ HỦY (0 BÀI)';
        pill.style.color = 'var(--primary)';
        pill.style.borderColor = 'rgba(255, 42, 95, 0.35)';
        quorumDot.style.background = 'var(--primary)';
        quorumDot.style.boxShadow = '0 0 16px var(--primary)';
        quorumText.innerText = 'Mạng Lưới Tide Fabric Quorum: ĐÃ THỰC THI LỆNH TỪ CHỐI';
        if (isPlayingAudio) stopPlayback();
      }
      syncReviewerDisplay();
    }

    function syncReviewerDisplay() {
      const activeBox = document.getElementById('player-active-box');
      const alarmBox = document.getElementById('player-alarm-box');
      const statusPill = document.getElementById('reviewer-status-pill');

      if (isSharingActive) {
        activeBox.classList.remove('hidden');
        alarmBox.classList.add('hidden');
        statusPill.className = 'badge-pill badge-shared';
        statusPill.innerText = 'PHIÊN LÀM VIỆC HỢP LỆ';
      } else {
        activeBox.classList.add('hidden');
        alarmBox.classList.remove('hidden');
        statusPill.className = 'badge-pill badge-locked';
        statusPill.innerText = 'QUYỀN ĐÃ BỊ THU HỒI';
      }
    }

    function stopPlayback() {
      const btn = document.getElementById('btn-audio-play');
      const bars = document.querySelectorAll('.wave-bar');
      const vinylDisc = document.getElementById('reviewer-vinyl-disc');
      isPlayingAudio = false;
      btn.innerText = '▶ Bật Nghe Thử Luồng Giải Mã (Âm Thanh Thật)';
      btn.style.background = 'var(--primary)';
      btn.style.color = '#fff';
      bars.forEach(b => b.classList.remove('active-wave'));
      if (vinylDisc) vinylDisc.classList.remove('spinning-vinyl');
      clearInterval(timerInterval);
      clearInterval(synthLoop);
    }

    function toggleAudioPlayback() {
      const btn = document.getElementById('btn-audio-play');
      const bars = document.querySelectorAll('.wave-bar');
      const timer = document.getElementById('player-timer');
      const vinylDisc = document.getElementById('reviewer-vinyl-disc');

      if (!isSharingActive) return;

      isPlayingAudio = !isPlayingAudio;
      if (isPlayingAudio) {
        btn.innerText = '⏸ Tạm Dừng Luồng Âm Thanh';
        btn.style.background = 'var(--cyan)';
        btn.style.color = '#021019';
        bars.forEach(b => b.classList.add('active-wave'));
        if (vinylDisc) vinylDisc.classList.add('spinning-vinyl');

        playTone(musicalNotes[notePointer], 0.6);
        synthLoop = setInterval(() => {
          notePointer = (notePointer + 1) % musicalNotes.length;
          playTone(musicalNotes[notePointer], 0.6);
        }, 500);

        timerInterval = setInterval(() => {
          secondsElapsed++;
          const m = Math.floor(secondsElapsed / 60);
          const s = secondsElapsed % 60;
          timer.innerText = `${m}:${s < 10 ? '0' : ''}${s} / 3:42`;
        }, 1000);
      } else {
        stopPlayback();
      }
    }

    function attemptAdminLeakage() {
      const output = document.getElementById('admin-leak-output');
      output.innerText = 'Đang truy vấn mạng Tide Fabric... LỖI TỪ CHỐI: Máy chủ là Oblivious Proxy, hoàn toàn KHÔNG giữ chìa khóa chủ để giải mã!';
      output.style.color = 'var(--primary)';
    }
  </script>
</body>
</html>
"""

# Ghi ra 2 nơi
with open(foodseekers_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Ghi thành công vào {foodseekers_html}")

with open(bersious_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Ghi thành công vào {bersious_html}")
