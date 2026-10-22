import os

API_FILE = r"C:\Users\nguye\bersious-web\api\rmit-vault.ts"

with open(API_FILE, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Clean stale requests in normalizeState
old_norm = "requests: Array.isArray(s.requests) ? s.requests : DEFAULT_STATE.requests,"
new_norm = """requests: Array.isArray(s.requests) 
      ? s.requests.filter((r: any) => !r.trackId.startsWith('track_0'))
      : [],"""

if old_norm in code:
    code = code.replace(old_norm, new_norm)

# 2. Add SET_PREVIEW_LIMIT action
action_snippet = """        case 'SET_PREVIEW_LIMIT': {
          const { trackId, limitSeconds } = body;
          const track = state.tracks.find((t: any) => t.id === trackId);
          if (track) {
            track.previewLimitSeconds = Number(limitSeconds) || 0;
            touch();
          }
          break;
        }
"""

if "case 'SET_PREVIEW_LIMIT':" not in code:
    code = code.replace("case 'SET_AUTO_APPROVE':", f"{action_snippet}\n        case 'SET_AUTO_APPROVE':")

with open(API_FILE, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated api/rmit-vault.ts with SET_PREVIEW_LIMIT support!")
