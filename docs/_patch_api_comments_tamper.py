import os

API_FILE = r"C:\Users\nguye\bersious-web\api\rmit-vault.ts"

with open(API_FILE, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Thêm comments vào DEFAULT_STATE
old_def = "  requests: [],\n  settings: { autoApprove: false },"
new_def = "  requests: [],\n  comments: [],\n  settings: { autoApprove: false },"
if old_def in code:
    code = code.replace(old_def, new_def)

# 2. Thêm comments vào normalizeState
old_norm = "    requests: Array.isArray(s.requests) \n      ? s.requests.filter((r: any) => !r.trackId.startsWith('track_0'))\n      : [],"
new_norm = """    requests: Array.isArray(s.requests) 
      ? s.requests.filter((r: any) => !r.trackId.startsWith('track_0'))
      : [],
    comments: Array.isArray(s.comments) ? s.comments : [],"""
if old_norm in code:
    code = code.replace(old_norm, new_norm)

# 3. Thêm actions: ADD_COMMENT và SET_TAMPER_PROTECTION
cases = """        case 'ADD_COMMENT': {
          const { trackId, username, text } = body;
          if (trackId && username && text) {
            if (!Array.isArray(state.comments)) state.comments = [];
            state.comments.unshift({
              id: `cmt_${Date.now()}_${Math.random().toString(16).slice(2, 6)}`,
              trackId,
              username,
              text: String(text).trim(),
              createdAt: new Date().toISOString()
            });
            touch();
          }
          break;
        }

        case 'SET_TAMPER_PROTECTION': {
          const { trackId, enabled } = body;
          const track = state.tracks.find((t: any) => t.id === trackId);
          if (track) {
            track.tamperProtection = !!enabled;
            touch();
          }
          break;
        }
"""
if "case 'ADD_COMMENT':" not in code:
    code = code.replace("case 'SET_WATERMARK_MODE':", f"{cases}\n        case 'SET_WATERMARK_MODE':")

with open(API_FILE, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated api/rmit-vault.ts with comments & tamper protection!")
