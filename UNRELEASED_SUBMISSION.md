[![Built with TideCloak](https://tide.org/badges/built-with-tidecloak.svg)](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked)

# 🎧 UNRELEASED — Zero-Trust Creative Audio Preview Studio

> **RMIT Hackathon 2026 · Challenge 2 (UNLOCKED by Tide)** — Team Foodseekers (UIT)
>
> 🌐 **Live Web App:** [https://bersious.io.vn/rmit](https://bersious.io.vn/rmit)
> 💻 **Local Interactive Demo:** open [`prototype/index.html`](./prototype/index.html) in any browser (zero install).
> 🎥 **Two-minute demo video:** [`demo/unreleased-demo.mp4`](./demo/).

## Project overview

**UNRELEASED** is a zero-trust creative collaboration studio that lets musicians share unreleased masters with external collaborators without ever handing cloud storage the power to read or leak them.

Built with [TideCloak](https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked).

### 1. Vision & originality
UNRELEASED transforms pre-release creative collaboration. Rather than trusting centralized cloud drives with multimillion-dollar unreleased album masters, UNRELEASED provides a cryptographically isolated preview studio where artists grant fine-grained, per-track listening entitlements without surrendering master-file access to the hosting platform.

### 2. Trust constraint insight
Today, creative pre-releases are crippled by leak anxiety. Sharing unmastered demos with session musicians, mixing engineers, or A&R reviewers forces artists to deposit plaintext audio into services (Dropbox, SoundCloud Private, Byta) where platform administrators and leaked storage buckets hold universal decryption keys. Watermarking only identifies a leaker *after* the damage is done. Removing unilateral server authority makes secure, friction-free collaboration finally possible.

### 3. Value & impact
Independent artists, record labels, and sound engineers collaborate seamlessly across borders while retaining sovereign control over their intellectual property. Leaks become structurally impossible, protecting multimillion-dollar launch campaigns, while collaborators enjoy instant, secure streaming previews with no NDAs or custody risk.

### 4. Why TideCloak matters
Conventional IAM (Auth0, standard Keycloak, cloud RBAC) keeps a master decryption key on the server, so any rogue admin or breached bucket exposes every track. UNRELEASED integrates TideCloak's **Emergent Authority**: audio stays unbreakable ciphertext in storage, and decryption keys never exist on our servers — they emerge just-in-time strictly inside the authorized reviewer's browser memory. When an artist revokes access, playback terminates instantly at the cryptographic quorum layer. Without TideCloak this guarantee is impossible.

### 5. Prototype & storytelling
Our working prototype demonstrates the full zero-trust workflow: Artist Alice shares Track 1 with reviewer Minh; Minh streams decrypted audio in-memory while Tracks 2–3 stay locked; a rogue cloud admin attempts a raw S3 master dump and is denied; Alice revokes access and Minh's stream dies instantly. Automated tests prove all five invariants (`npm run test:security`).

## Setup

```bash
# 1. Start the Oblivious Proxy backend (zero master keys, port 4000)
node src/backend/server.js

# 2a. Fastest path — open the interactive prototype directly
#     open prototype/index.html in Chrome/Edge

# 2b. Full Next.js studio
cd app && npm install && npm run dev   # http://localhost:3000

# 3. Run the automated security + E2E proof
node src/security/exploit_simulation.js
node src/security/e2e_integration_test.js
```

**Architecture:** `src/sdk/tidecloak/` (AES-256-GCM engine + Emergent Authority quorum) · `src/backend/server.js` (oblivious proxy API) · `src/security/` (exploit + E2E tests) · `prototype/index.html` (judge demo) · `app/` (Next.js production integration).
