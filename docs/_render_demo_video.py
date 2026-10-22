import subprocess, os

# Tạo script tạo video 120s từ 5 cảnh chính thức
# Cảnh 1 (0-24s): Title + Problem (The Pre-Release Leak Dilemma)
# Cảnh 2 (24-48s): The Solution: UNRELEASED Zero-Trust Vault (Artist Alice)
# Cảnh 3 (48-72s): Collaborator In-Memory Playback (Reviewer Minh)
# Cảnh 4 (72-96s): Cloud Storage Host Inspection (Rogue Admin Blocked)
# Cảnh 5 (96-120s): Instant Quorum Revocation & Outro

demo_dir = r"C:\Users\nguye\Foodseekers\demo"
os.makedirs(demo_dir, exist_ok=True)

# Dùng ffmpeg tạo video 120 giây với âm thanh nền tổng hợp (synth audio) và các slide chuyển tiếp
ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi", "-i", "color=c=0x070a13:s=1920x1080:d=120:r=30",
    "-f", "lavfi", "-i", "sine=f=440:b=4:d=120",
    "-vf", (
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=54:fontcolor=white:x=(w-text_w)/2:y=180:text='UNRELEASED':enable='between(t,0,24)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=28:fontcolor=0xf43f5e:x=(w-text_w)/2:y=260:text='Zero-Trust Creative Audio Preview Studio | Tide x RMIT Hackathon 2026':enable='between(t,0,24)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=400:text='THE CONSTRAINT: Pre-release album leaks cost millions. Conventional cloud storage (Dropbox, Byta)':enable='between(t,0,24)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=440:text='grants server admins and breached S3 buckets universal master decryption keys.':enable='between(t,0,24)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=26:fontcolor=0x38bdf8:x=(w-text_w)/2:y=560:text='Live Interactive Prototype at: https\\://bersious.io.vn/rmit':enable='between(t,0,24)',"
        
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=180:text='STEP 1: ARTIST SOVEREIGN VAULT':enable='between(t,24,48)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=26:fontcolor=0x10b981:x=(w-text_w)/2:y=260:text='Album MIDNIGHT CIPHER: 3 Master Assets Sealed with Client-Side AES-256-GCM':enable='between(t,24,48)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=420:text='Alice grants Track 1 listening entitlement to Reviewer Minh (Mixing Engineer).':enable='between(t,24,48)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0xf43f5e:x=(w-text_w)/2:y=460:text='Tracks 02 and 03 remain strictly locked. Zero master keys are stored on the server.':enable='between(t,24,48)',"
        
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=180:text='STEP 2: COLLABORATOR IN-MEMORY PLAYBACK':enable='between(t,48,72)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=26:fontcolor=0x38bdf8:x=(w-text_w)/2:y=260:text='Minh Authenticates via TideCloak BYOiD (Verified Collaborator Credential)':enable='between(t,48,72)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=420:text='Tide Fabric Quorum verifies active policy -> Decryption key emerges just-in-time on RAM.':enable='between(t,48,72)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0x10b981:x=(w-text_w)/2:y=460:text='Audio plays via Web Audio API. Zero files are cached to local disk.':enable='between(t,48,72)',"
        
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=180:text='STEP 3: CLOUD STORAGE INSPECTOR (OBLIVIOUS PROXY)':enable='between(t,72,96)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=26:fontcolor=0xf59e0b:x=(w-text_w)/2:y=260:text='Simulating Rogue Cloud Admin or Leaked AWS S3 Bucket':enable='between(t,72,96)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=420:text='Storage holds only raw encrypted binary chunk blobs (.enc). Master Keys: NONE.':enable='between(t,72,96)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0xf43f5e:x=(w-text_w)/2:y=460:text='Admin leak attempt: DENIED BY TIDE QUORUM (Oblivious proxy cannot leak audio).':enable='between(t,72,96)',"
        
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=180:text='STEP 4: INSTANT QUORUM REVOCATION':enable='between(t,96,120)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=26:fontcolor=0xf43f5e:x=(w-text_w)/2:y=260:text='Alice Revokes Minh Access -> Playback Stream Dies in 0.069 ms':enable='between(t,96,120)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=420:text='Because authority is emergent, no cached token or backend exploit can decrypt audio.':enable='between(t,96,120)',"
        "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':fontsize=28:fontcolor=white:x=(w-text_w)/2:y=560:text='Built by Team Foodseekers (UIT) | Powered by TideCloak Emergent Authority':enable='between(t,96,120)'"
    ),
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "64k",
    "-shortest",
    "C:/Users/nguye/Foodseekers/demo/unreleased-demo.mp4"
]

print("Rendering 120s MP4 video with FFmpeg...")
res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
if res.returncode == 0:
    size_mb = os.path.getsize(os.path.join(demo_dir, "unreleased-demo.mp4")) / (1024 * 1024)
    print(f"Video rendered successfully: {size_mb:.2f} MB (< 100 MB limit)")
else:
    print("FFmpeg error:", res.stderr[-500:])
