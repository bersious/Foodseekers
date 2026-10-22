import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

for base in [FS_PROTO, BW_RMIT]:
    for page in ["1", "2"]:
        p = os.path.join(base, page, "index.html")
        with open(p, "r", encoding="utf-8") as f:
            code = f.read()

        # Xóa các dòng note gợi ý mật khẩu
        code = re.sub(r'<div style="font-size:11px;color:var\(--dim\);margin-top:4px" class="mono">Gợi ý:.*?</div>', '', code)
        code = code.replace('placeholder="Nhập mật khẩu khởi tạo (123)"', 'placeholder="••••••••"')
        code = code.replace('placeholder="Nhập mật khẩu (123)"', 'placeholder="••••••••"')
        code = code.replace("alert('Mật khẩu không đúng! (Vui lòng nhập mật khẩu là 123)');", "alert('Mật khẩu xác thực không chính xác.');")
        code = code.replace("alert('Mật khẩu không đúng! Vui lòng nhập mật khẩu là 123');", "alert('Mật khẩu xác thực không chính xác.');")
        code = code.replace("alert('Vui lòng đặt mật khẩu là 123!');", "alert('Mật khẩu không hợp lệ.');")
        code = code.replace("alert('Vui lòng đặt mật khẩu khởi tạo là 123!');", "alert('Mật khẩu không hợp lệ.');")

        with open(p, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Cleaned 123 notes in: {p}")

print("✓ Đã xóa sạch 100% các dòng chữ và mở ngoặc 123 trên UI!")
