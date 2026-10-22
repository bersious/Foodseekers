/**
 * UNRELEASED — Full End-to-End Integration Test
 * Boots the Oblivious Proxy server and exercises every API endpoint to prove
 * the complete zero-trust workflow: share -> stream -> admin-denied -> revoke -> blocked.
 */

const http = require('http');
const server = require('../backend/server');

const PORT = 4100;

function request(method, path, body) {
  return new Promise((resolve, reject) => {
    const data = body ? JSON.stringify(body) : null;
    const req = http.request(
      { hostname: 'localhost', port: PORT, path, method, headers: { 'Content-Type': 'application/json' } },
      (res) => {
        let raw = '';
        res.on('data', (c) => (raw += c));
        res.on('end', () => resolve({ status: res.statusCode, body: JSON.parse(raw) }));
      }
    );
    req.on('error', reject);
    if (data) req.write(data);
    req.end();
  });
}

async function runE2E() {
  console.log('================================================================');
  console.log('🔗  UNRELEASED — FULL END-TO-END INTEGRATION TEST');
  console.log('================================================================\n');

  let pass = 0;
  const total = 5;

  // 1. List album tracks
  const tracks = await request('GET', '/api/tracks');
  if (tracks.body.success && tracks.body.tracks.length === 3 && tracks.body.tracks.every(t => !t.hasServerMasterKey)) {
    console.log('[1/5] ✓ Album loaded: 3 tracks, server holds ZERO master keys.');
    pass++;
  } else console.log('[1/5] ✕ Album load failed.');

  // 2. Reviewer Minh requests emergent key (allowed)
  const key1 = await request('POST', '/api/stream/request-key', { trackId: 'track_01', userId: 'usr_minh_mix' });
  if (key1.status === 200 && key1.body.success && key1.body.ephemeralToken) {
    console.log('[2/5] ✓ Emergent key generated just-in-time for authorized reviewer Minh.');
    pass++;
  } else console.log('[2/5] ✕ Authorized key request failed.');

  // 3. Rogue admin dump attempt (must be denied 403)
  const dump = await request('POST', '/api/admin/dump-raw-s3');
  if (dump.status === 403 && dump.body.code === 'UNILATERAL_DECRYPTION_FORBIDDEN') {
    console.log('[3/5] ✓ Rogue admin S3 dump BLOCKED — oblivious proxy holds no keys.');
    pass++;
  } else console.log('[3/5] ✕ Admin dump was not blocked!');

  // 4. Artist revokes access
  const revoke = await request('POST', '/api/artist/revoke');
  if (revoke.status === 200 && revoke.body.status === 'ENTITLEMENT_REVOKED_ACROSS_TIDE_FABRIC') {
    console.log('[4/5] ✓ Artist revocation propagated instantly across Tide Fabric.');
    pass++;
  } else console.log('[4/5] ✕ Revocation failed.');

  // 5. Reviewer attempts playback after revoke (must be denied)
  const key2 = await request('POST', '/api/stream/request-key', { trackId: 'track_01', userId: 'usr_minh_mix' });
  if (key2.status === 403 && key2.body.status === 'TIDE_QUORUM_REFUSED') {
    console.log('[5/5] ✓ Post-revoke playback DENIED — stream terminates immediately.');
    pass++;
  } else console.log('[5/5] ✕ Post-revoke access was not denied!');

  console.log('\n================================================================');
  console.log(`🎯 E2E RESULT: ${pass}/${total} PASSED`);
  console.log('================================================================');

  server.close();
  process.exit(pass === total ? 0 : 1);
}

server.listen(PORT, () => {
  console.log(`[*] Test server booted on port ${PORT}\n`);
  runE2E();
});
