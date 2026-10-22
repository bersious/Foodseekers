import os

FS_PROTO = r"C:\Users\nguye\Foodseekers\prototype"
BW_RMIT = r"C:\Users\nguye\bersious-web\rmit"

for base in [FS_PROTO, BW_RMIT]:
    # Page 1
    p1 = os.path.join(base, "1", "index.html")
    with open(p1, "r", encoding="utf-8") as f:
        c1 = f.read()
    c1 = c1.replace("updateArtistLoginSelect();", "")
    c1 = c1.replace("""function updateArtistLoginSelect(){
  const artists = getStoredArtists();
  const select = document.getElementById('quick-artist-login-select');
  if(select && artists.length){
    select.innerHTML = artists.map(a => `<option value="${a.username}">${a.name} (@${a.username})</option>`).join('');
  }
}""", "")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(c1)

    # Page 2
    p2 = os.path.join(base, "2", "index.html")
    with open(p2, "r", encoding="utf-8") as f:
        c2 = f.read()
    c2 = c2.replace("renderUserSelect();", "")
    c2 = c2.replace("""function renderUserSelect(){
  const users = getStoredUsers();
  const select = document.getElementById('quick-user-select');
  const input = document.getElementById('reviewer-login-user');
  if(!select) return;

  if(!users || !users.length){
    select.innerHTML = '<option value="">(Đang tải danh sách từ Cloud...)</option>';
    return;
  }

  const currentVal = input ? input.value : '';
  select.innerHTML = users.map(u => `<option value="${u.username}" ${u.username===currentVal?'selected':''}>👤 ${u.name||u.username} (@${u.username})</option>`).join('');
  if(!currentVal && users.length && input){
    input.value = users[0].username;
  }
}""", "")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(c2)

print("Cleaned dead JS references to login select dropdowns.")
