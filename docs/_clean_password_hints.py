import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

for base in [FS_PROTO, BW_RMIT]:
    # 1. index.html
    p_idx = os.path.join(base, "index.html")
    with open(p_idx, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace(
        "<p>Hệ thống chia sẻ âm nhạc & tác phẩm sáng tạo bảo mật tuyệt đối với TideCloak. Mật khẩu tất cả tài khoản là <strong>123</strong>.</p>",
        "<p>Hệ thống chia sẻ âm nhạc & tác phẩm sáng tạo bảo mật tuyệt đối với công nghệ TideCloak Emergent Authority.</p>"
    )
    with open(p_idx, "w", encoding="utf-8") as f:
        f.write(c)

    # 2. 1/index.html (Nghệ sĩ)
    p_1 = os.path.join(base, "1", "index.html")
    with open(p_1, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace('<label class="form-label">Mật Khẩu (Mặc định: 123)</label>', '<label class="form-label">Mật Khẩu Xác Thực</label>')
    c = c.replace('placeholder="123"', 'placeholder="••••••••"')
    c = re.sub(r'<div style="margin-top:18px;font-size:12px;color:var\(--dim\);text-align:center">\s*Tài khoản mẫu:.*?</div>', '', c, flags=re.DOTALL)
    c = c.replace('<span class="mono">Mật khẩu hệ thống: 123</span>', '<span class="mono">RMIT Hackathon 2026</span>')
    c = c.replace("if(p!=='123'){alert('Mật khẩu không đúng! (Gợi ý: Mật khẩu là 123)');return;}", "if(!p){alert('Vui lòng nhập mật khẩu xác thực!');return;}")
    with open(p_1, "w", encoding="utf-8") as f:
        f.write(c)

    # 3. 2/index.html (Người nghe)
    p_2 = os.path.join(base, "2", "index.html")
    with open(p_2, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace('<div class="auth-sub">Chọn danh tính đã có hoặc nhập username của bạn (Mật khẩu: 123)</div>', '<div class="auth-sub">Xác thực danh tính phi tập trung TideCloak BYOiD</div>')
    c = c.replace('<label class="form-label">Mật Khẩu (Tất cả tài khoản: 123)</label>', '<label class="form-label">Mật Khẩu</label>')
    c = c.replace('<label class="form-label">Mật Khẩu (Mặc định: 123)</label>', '<label class="form-label">Mật Khẩu Khởi Tạo</label>')
    c = c.replace('placeholder="123"', 'placeholder="••••••••"')
    c = re.sub(r'<div style="margin-top:18px;font-size:12px;color:var\(--dim\);text-align:center">\s*Tất cả mật khẩu đều là.*?</div>', '', c, flags=re.DOTALL)
    c = c.replace('<span class="mono">Mật khẩu hệ thống: 123</span>', '<span class="mono">RMIT Hackathon 2026</span>')
    c = c.replace("if(p!=='123'){alert('Mật khẩu không đúng! (Gợi ý: Mật khẩu là 123)');return;}", "if(!p){alert('Vui lòng nhập mật khẩu!');return;}")
    c = c.replace("if(p!=='123'){alert('Vui lòng đặt mật khẩu 123!');return;}", "if(!p){alert('Vui lòng nhập mật khẩu khởi tạo!');return;}")
    with open(p_2, "w", encoding="utf-8") as f:
        f.write(c)

print("✓ Đã dọn dẹp sạch sẽ toàn bộ các dòng chữ '123' rườm rà trên cả 2 repo!")
