import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

for base in [FS_PROTO, BW_RMIT]:
    p = os.path.join(base, "2", "index.html")
    with open(p, "r", encoding="utf-8") as f:
        code = f.read()

    old_guard = """  const track=tracks.find(x=>x.id===activeTrackId);
  if(!track || !track.allowedUsers.includes(currentUser)) return;"""

    new_guard = """  const track=tracks.find(x=>x.id===activeTrackId);
  if(!track){
    alert('Vui lòng chọn một bài hát từ danh sách phía trên!');
    return;
  }
  const isAllowed = Array.isArray(track.allowedUsers) && track.allowedUsers.includes(currentUser);
  if(!isAllowed){
    alert(`Tác phẩm "${track.name}" đang bị khóa đối với tài khoản của bạn! Nhấn nút "Xin quyền nghe" để yêu cầu Nghệ Sĩ mở khóa.`);
    return;
  }"""

    if old_guard in code:
        code = code.replace(old_guard, new_guard)

    with open(p, "w", encoding="utf-8") as f:
        f.write(code)

print("Updated Page 2 locked track click alert.")
