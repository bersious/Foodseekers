import os, re

FS = r"C:\Users\nguye\Foodseekers"
BW = r"C:\Users\nguye\bersious-web"

# Danh sách các tệp cần đổi tên thương hiệu sang SONARA
files_to_update = [
    os.path.join(FS, "README.md"),
    os.path.join(FS, "UNRELEASED_SUBMISSION.md"),
    os.path.join(FS, "package.json"),
    os.path.join(FS, "index.html"),
    os.path.join(FS, "prototype", "index.html"),
    os.path.join(FS, "prototype", "1", "index.html"),
    os.path.join(FS, "prototype", "2", "index.html"),
    os.path.join(FS, "prototype", "3", "index.html"),
    os.path.join(BW, "rmit", "index.html"),
    os.path.join(BW, "rmit", "1", "index.html"),
    os.path.join(BW, "rmit", "2", "index.html"),
    os.path.join(BW, "rmit", "3", "index.html"),
]

# Các quy tắc thay thế:
# SONORA -> SONARA
# UNRELEASED -> SONARA
replacements = [
    ("SONORA", "SONARA"),
    ("Sonora", "Sonara"),
    ("sonora", "sonara"),
    ("UNRELEASED", "SONARA"),
    ("Unreleased", "Sonara"),
    ("unreleased", "sonara")
]

for p in files_to_update:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(p, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated brand to SONARA in: {p}")

print("✓ Hoàn tất đổi tên sản phẩm thành SONARA trên toàn bộ website và tài liệu!")
