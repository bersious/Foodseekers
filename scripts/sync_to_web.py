import os, subprocess

FOODSEEKERS_DIR = r"C:\Users\nguye\Foodseekers"
BERSIOUS_WEB_DIR = r"C:\Users\nguye\bersious-web"

src_proto = os.path.join(FOODSEEKERS_DIR, "prototype", "index.html")
dst_proto = os.path.join(BERSIOUS_WEB_DIR, "rmit", "index.html")

print(f"[*] Đồng bộ từ {src_proto} sang {dst_proto}...")
with open(src_proto, "r", encoding="utf-8") as f:
    content = f.read()

os.makedirs(os.path.dirname(dst_proto), exist_ok=True)
with open(dst_proto, "w", encoding="utf-8") as f:
    f.write(content)

print("[*] Đã ghi đè file rmit/index.html thành công.")

# Git status check on bersious-web
res = subprocess.run(["git", "-C", BERSIOUS_WEB_DIR, "status", "--porcelain"], capture_output=True, text=True)
if res.stdout.strip():
    print("[*] Phát hiện thay đổi mới, đang commit và push lên bersious-web...")
    subprocess.run(["git", "-C", BERSIOUS_WEB_DIR, "add", "rmit/index.html"], check=True)
    subprocess.run(["git", "-C", BERSIOUS_WEB_DIR, "commit", "-m", "chore(sync): auto-sync UNRELEASED prototype from Foodseekers"], check=True)
    subprocess.run(["git", "-C", BERSIOUS_WEB_DIR, "push", "origin", "main"], check=True)
    print("[✓] Đã đẩy lên GitHub bersious/bersious-web! Vercel sẽ tự động deploy trong vài giây.")
else:
    print("[✓] rmit/index.html trên bersious-web đã hoàn toàn đồng bộ với Foodseekers, không cần commit lại.")
