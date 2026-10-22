import os

API_FILE = r"C:\Users\nguye\bersious-web\api\rmit-vault.ts"

with open(API_FILE, 'r', encoding='utf-8') as f:
    code = f.read()

target = "case 'SET_PREVIEW_LIMIT':"
new_snippet = """        case 'SET_WATERMARK_MODE': {
          const { trackId, mode } = body;
          const track = state.tracks.find((t: any) => t.id === trackId);
          if (track) {
            track.watermarkMode = mode || 'none';
            touch();
          }
          break;
        }

        case 'SET_PREVIEW_LIMIT':"""

if "case 'SET_WATERMARK_MODE':" not in code:
    code = code.replace(target, new_snippet)

with open(API_FILE, 'w', encoding='utf-8') as f:
    f.write(code)

print("Added SET_WATERMARK_MODE to api/rmit-vault.ts!")
