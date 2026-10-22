import subprocess, os

demo_dir = r"C:\Users\nguye\Foodseekers\demo"
os.makedirs(demo_dir, exist_ok=True)
out_file = os.path.join(demo_dir, "unreleased-demo.mp4")

# Viết filter graph ra file để tránh escape issue trên Windows
filter_path = os.path.join(demo_dir, "filter.txt")
filter_content = """
drawtext=text='UNRELEASED':fontsize=64:fontcolor=white:x=(w-text_w)/2:y=200:enable='between(t,0,24)',
drawtext=text='Zero-Trust Creative Audio Preview Studio':fontsize=32:fontcolor=0xf43f5e:x=(w-text_w)/2:y=280:enable='between(t,0,24)',
drawtext=text='RMIT Hackathon 2026 | Challenge 2 by Tide':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=340:enable='between(t,0,24)',
drawtext=text='Live at: https://bersious.io.vn/rmit':fontsize=28:fontcolor=0x38bdf8:x=(w-text_w)/2:y=500:enable='between(t,0,24)',

drawtext=text='STEP 1: ARTIST SOVEREIGN VAULT':fontsize=54:fontcolor=white:x=(w-text_w)/2:y=200:enable='between(t,24,48)',
drawtext=text='3 Album Masters Encrypted with Client-Side AES-256-GCM':fontsize=28:fontcolor=0x10b981:x=(w-text_w)/2:y=280:enable='between(t,24,48)',
drawtext=text='Alice grants Track 1 entitlement to Reviewer Minh':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=360:enable='between(t,24,48)',
drawtext=text='Tracks 2 and 3 stay strictly locked. Zero master keys on server.':fontsize=24:fontcolor=0xf43f5e:x=(w-text_w)/2:y=420:enable='between(t,24,48)',

drawtext=text='STEP 2: COLLABORATOR IN-MEMORY PLAYBACK':fontsize=54:fontcolor=white:x=(w-text_w)/2:y=200:enable='between(t,48,72)',
drawtext=text='Minh Authenticates via TideCloak BYOiD':fontsize=28:fontcolor=0x38bdf8:x=(w-text_w)/2:y=280:enable='between(t,48,72)',
drawtext=text='Tide Quorum verifies policy -> Decryption key emerges just-in-time':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=360:enable='between(t,48,72)',
drawtext=text='Audio stream plays via Web Audio API. Zero local files cached.':fontsize=24:fontcolor=0x10b981:x=(w-text_w)/2:y=420:enable='between(t,48,72)',

drawtext=text='STEP 3: CLOUD STORAGE INSPECTOR (OBLIVIOUS PROXY)':fontsize=54:fontcolor=white:x=(w-text_w)/2:y=200:enable='between(t,72,96)',
drawtext=text='Simulating Rogue Cloud Admin or Breached S3 Bucket':fontsize=28:fontcolor=0xf59e0b:x=(w-text_w)/2:y=280:enable='between(t,72,96)',
drawtext=text='Storage holds only raw encrypted binary chunk blobs (.enc)':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=360:enable='between(t,72,96)',
drawtext=text='Admin leak attempt: DENIED BY TIDE QUORUM (Oblivious proxy)':fontsize=24:fontcolor=0xf43f5e:x=(w-text_w)/2:y=420:enable='between(t,72,96)',

drawtext=text='STEP 4: INSTANT QUORUM REVOCATION':fontsize=54:fontcolor=white:x=(w-text_w)/2:y=200:enable='between(t,96,120)',
drawtext=text='Alice Revokes Minh Access -> Stream Dies in 0.069 ms':fontsize=28:fontcolor=0xf43f5e:x=(w-text_w)/2:y=280:enable='between(t,96,120)',
drawtext=text='Authority is emergent: no cached token can reconstruct decryption keys':fontsize=24:fontcolor=0x94a3b8:x=(w-text_w)/2:y=360:enable='between(t,96,120)',
drawtext=text='Built by Team Foodseekers (UIT) | Powered by TideCloak':fontsize=28:fontcolor=white:x=(w-text_w)/2:y=500:enable='between(t,96,120)'
""".replace('\n', ' ').strip()

with open(filter_path, 'w', encoding='utf-8') as f:
    f.write(filter_content)

cmd = f'ffmpeg -y -f lavfi -i color=c=0x070a13:s=1920x1080:d=120:r=30 -f lavfi -i sine=f=220:b=4:d=120 -filter_script:v "{filter_path}" -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 64k -shortest "{out_file}"'
print("Running command...")
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
if res.returncode == 0:
    size = os.path.getsize(out_file) / (1024 * 1024)
    print(f"SUCCESS: Video rendered: {size:.2f} MB")
else:
    print("Error:", res.stderr[-400:])
