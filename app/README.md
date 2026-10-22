# UNRELEASED — Next.js + TideCloak Production App

This is the production-grade Next.js implementation of **UNRELEASED**, the zero-trust
creative audio preview studio for RMIT Hackathon 2026 Challenge 2.

> The judge-facing interactive demo lives in [`../prototype/index.html`](../prototype/index.html)
> and runs instantly in any browser with zero install. This `app/` folder holds the full
> Next.js + TideCloak integration intended for production deployment via the TideCloak Quickstart.

## Architecture

```
app/
├── package.json              # Next.js + @tidecloak/nextjs dependencies
├── src/
│   ├── app/                  # Next.js App Router pages
│   ├── components/           # Artist vault, Reviewer player, Admin inspector
│   └── lib/
│       └── tidecloak-client.js  # Client adapter to the Oblivious Proxy backend
└── public/
```

The backend Oblivious Proxy and the TideCloak SDK live in the repository root:
- `../src/backend/server.js` — zero-custody API server (run: `npm run server`)
- `../src/sdk/tidecloak/` — AES-256-GCM crypto engine + Emergent Authority quorum
- `../src/security/exploit_simulation.js` — automated security proof (run: `npm run test:security`)

## Local Development

```bash
# 1. Start the Oblivious Proxy backend (port 4000)
node ../src/backend/server.js

# 2. Install and run the Next.js studio (port 3000)
npm install
npm run dev
```

## TideCloak Production Integration

For a full emergent-authority deployment, initialize the TideCloak dev server and
template per the official Quickstart, then wire `src/lib/tidecloak-client.js` to the
TideCloak OIDC provider:

```bash
docker run --name mytidecloak -d -p 8080:8080 \
  -e KC_BOOTSTRAP_ADMIN_USERNAME=admin \
  -e KC_BOOTSTRAP_ADMIN_PASSWORD=password \
  tideorg/tidecloak-dev:latest

npm init @tidecloak/nextjs@latest
```
