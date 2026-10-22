/**
 * UNRELEASED — Oblivious Proxy API Server
 * Built with standard Node.js HTTP module (Zero external dependencies).
 * Proves that the server acts as an oblivious proxy and holds ZERO master keys.
 */

const http = require('http');
const emergentAuthority = require('../sdk/tidecloak/emergent_authority');
const CryptoEngine = require('../sdk/tidecloak/crypto_engine');
const crypto = require('crypto');

const PORT = process.env.PORT || 4000;

// Simulated storage bucket holding encrypted audio chunks
const mockAudioDatabase = [
  {
    trackId: 'track_01',
    title: '01_Lead_Single_Master_v4.flac',
    artist: 'Alice Nguyen',
    encryptedPayload: 'd8a391e4fc2901a88b5e027f8a1924bc99014efa78...',
    iv: 'a1b2c3d4e5f6071829304152',
    tag: 'f1e2d3c4b5a697887766554433221100',
    sharedWith: ['usr_minh_mix']
  },
  {
    trackId: 'track_02',
    title: '02_Vocal_Stems_Dry_Studio.wav',
    artist: 'Alice Nguyen',
    encryptedPayload: '1f80aa7621c08be991448bcae912408fb241a7bc81...',
    iv: 'b2c3d4e5f607182930415263',
    tag: 'e2d3c4b5a697887766554433221100ff',
    sharedWith: []
  },
  {
    trackId: 'track_03',
    title: '03_Unannounced_Feature_Draft.flac',
    artist: 'Alice Nguyen',
    encryptedPayload: '7c8911bb20e14ad9f92881a70094bba8912ef0aa32...',
    iv: 'c3d4e5f60718293041526374',
    tag: 'd3c4b5a697887766554433221100ffee',
    sharedWith: []
  }
];

// Initialize default active sharing policy for Track 1
emergentAuthority.grantEntitlement('track_01', 'usr_alice_84', 'usr_minh_mix', 86400);

const server = http.createServer((req, res) => {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    return res.end();
  }

  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);

  // 1. List all album tracks (Metadata + Encrypted state)
  if (req.method === 'GET' && parsedUrl.pathname === '/api/tracks') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({
      success: true,
      album: 'MIDNIGHT CIPHER (Pre-release)',
      tracks: mockAudioDatabase.map(t => ({
        trackId: t.trackId,
        title: t.title,
        artist: t.artist,
        isShared: t.sharedWith.includes('usr_minh_mix'),
        hasServerMasterKey: false
      }))
    }));
  }

  // 2. Request Emergent Playback Key (Evaluated at Tide Quorum)
  if (req.method === 'POST' && parsedUrl.pathname === '/api/stream/request-key') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      const data = JSON.parse(body || '{}');
      const trackId = data.trackId || 'track_01';
      const userId = data.userId || 'usr_minh_mix';

      const evalResult = emergentAuthority.requestEmergentKey(trackId, userId);
      if (evalResult.allowed) {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        return res.end(JSON.stringify({
          success: true,
          status: 'EMERGENT_KEY_GENERATED',
          expiresIn: evalResult.expiresIn,
          ephemeralToken: evalResult.ephemeralKey.toString('hex')
        }));
      } else {
        res.writeHead(403, { 'Content-Type': 'application/json' });
        return res.end(JSON.stringify({
          success: false,
          status: 'TIDE_QUORUM_REFUSED',
          error: evalResult.error
        }));
      }
    });
    return;
  }

  // 3. Artist Revocation Action
  if (req.method === 'POST' && parsedUrl.pathname === '/api/artist/revoke') {
    emergentAuthority.revokeEntitlement('track_01', 'usr_minh_mix');
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({
      success: true,
      status: 'ENTITLEMENT_REVOKED_ACROSS_TIDE_FABRIC'
    }));
  }

  // 4. Rogue Admin S3 Bucket Dump Exploit Attempt (Demonstrating Oblivious Proxy)
  if (req.method === 'POST' && parsedUrl.pathname === '/api/admin/dump-raw-s3') {
    res.writeHead(403, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({
      success: false,
      code: 'UNILATERAL_DECRYPTION_FORBIDDEN',
      error: 'CRITICAL SECURITY ENFORCEMENT: Server is an Oblivious Proxy. No master decryption key exists in this environment or database.',
      storedCiphertextSample: mockAudioDatabase[0].encryptedPayload
    }));
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

if (require.main === module) {
  server.listen(PORT, () => {
    console.log(`[+] UNRELEASED Oblivious Proxy Server listening on port ${PORT}`);
    console.log(`[*] Tide Fabric Quorum Simulation: ONLINE & ZERO-CUSTODY ACTIVE`);
  });
}

module.exports = server;
