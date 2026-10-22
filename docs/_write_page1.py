import os

# Ghi đè file trang 1 - cả 2 nơi
content_new = open('C:/Users/nguye/Foodseekers/docs/_page1_new.html', 'r', encoding='utf-8').read()
for base in [r'C:\Users\nguye\Foodseekers\prototype', r'C:\Users\nguye\bersious-web\rmit']:
    path = os.path.join(base, '1', 'index.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content_new)
    print(f'Đã ghi: {path} ({len(content_new)} bytes)')
