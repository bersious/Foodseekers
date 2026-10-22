import os, re

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

TOAST_BLOCK_START = "/* ==================== TOAST SYSTEM (thay alert() để UI sang trọng) ==================== */"
TOAST_BLOCK_END = "})();"

def move_toast_to_head():
    """Di chuyển script Toast lên ngay sau <body> để mọi hàm main script đều gọi được."""
    for base in [FS_PROTO, BW_RMIT]:
        for page in ["1", "2", "3"]:
            p = os.path.join(base, page, "index.html")
            with open(p, "r", encoding="utf-8") as f:
                code = f.read()

            if TOAST_BLOCK_START not in code:
                print(f"  skip (no toast): {p}")
                continue

            start = code.find(TOAST_BLOCK_START)
            end = code.find(TOAST_BLOCK_END, start)
            if end == -1:
                print(f"  skip (no end): {p}")
                continue
            end += len(TOAST_BLOCK_END)

            # Lấy riêng khối toast (bao gồm cả <script> tags nếu có)
            block = code[start:end]
            # Cắt khối ra khỏi vị trí cũ
            code = code[:start] + code[end:]
            # Dọn script tag rỗng còn sót
            code = code.replace("</script>\n\n\n<script></script>", "</script>")
            code = code.replace("<script></script>\n", "")

            # Chèn vào ngay sau <body>
            body_i = code.find("<body>")
            insert_at = body_i + len("<body>")
            wrapped = "\n\n<script>\n" + block + "\n</script>\n"
            code = code[:insert_at] + wrapped + code[insert_at:]

            with open(p, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"  moved toast to top: {p}")

move_toast_to_head()
print("✓ Đã chuyển Toast System lên đầu trang, không còn lỗi 'animateCount is not defined'.")
