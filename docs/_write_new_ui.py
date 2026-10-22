#!/usr/bin/env python3
# Ghi giao diện mới (tối giản, cao cấp) cho prototype UNRELEASED Challenge 2
import io

HTML = r'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UNRELEASED - Zero-Trust Audio Vault - Foodseekers x RMIT 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#08090d;--surface:rgba(255,255,255,.025);--surface-2:rgba(255,255,255,.045);
  --line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.14);
  --fg:#f4f5f7;--muted:#8b8fa0;--dim:#5a5e6e;
  --accent:#d4ff3f;--accent-dim:rgba(212,255,63,.12);
  --danger:#ff4d6d;--danger-dim:rgba(255,77,109,.1);
  --ok:#3ee88f;--ok-dim:rgba(62,232,143,.1);--radius:18px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--fg);font-family:'Space Grotesk',sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased;overflow-x:hidden;min-height:100vh}
body::before{content:'';position:fixed;inset:0;z-index:-2;background:radial-gradient(900px 500px at 78% -5%,rgba(212,255,63,.07),transparent 60%),radial-gradient(700px 500px at 0% 100%,rgba(90,110,255,.06),transparent 55%)}
body::after{content:'';position:fixed;inset:0;z-index:-1;opacity:.4;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:64px 64px;-webkit-mask-image:radial-gradient(circle at 50% 40%,#000 0%,transparent 80%);mask-image:radial-gradient(circle at 50% 40%,#000 0%,transparent 80%)}
.mono{font-family:'JetBrains Mono',monospace}
.topbar{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:18px 36px;backdrop-filter:blur(18px);background:rgba(8,9,13,.6);border-bottom:1px solid var(--line)}
.logo{display:flex;align-items:center;gap:12px;font-weight:700;letter-spacing:-.02em}
.logo .dot{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 14px var(--accent)}
.logo small{display:block;font-size:11px;color:var(--muted);font-weight:400;letter-spacing:.04em}
.topbar .right{display:flex;align-items:center;gap:14px}
.ghost-link{font-size:13px;color:var(--muted);text-decoration:none;border:1px solid var(--line);padding:8px 14px;border-radius:999px;transition:.2s;display:inline-flex;gap:7px;align-items:center}
.ghost-link:hover{color:var(--fg);border-color:var(--line-strong);background:var(--surface)}
.tide-chip{font-size:12px;font-weight:600;color:#0a0b0e;background:var(--accent);padding:8px 14px;border-radius:999px}
.hero{max-width:1120px;margin:0 auto;padding:64px 36px 32px;text-align:center}
.kicker{display:inline-flex;align-items:center;gap:9px;font-size:12px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase;border:1px solid var(--line);border-radius:999px;padding:7px 16px;margin-bottom:28px}
.kicker .pulse{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 10px var(--ok);animation:pulse 1.8s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
.hero h1{font-size:clamp(38px,6vw,68px);line-height:1.02;letter-spacing:-.04em;font-weight:700}
.hero h1 .glow{color:var(--accent);text-shadow:0 0 40px rgba(212,255,63,.35)}
.hero p{max-width:560px;margin:22px auto 0;color:var(--muted);font-size:17px}
.hero .cta{display:flex;gap:14px;justify-content:center;margin-top:36px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;padding:13px 24px;border-radius:12px;border:1px solid transparent;transition:.2s;display:inline-flex;align-items:center;gap:9px;text-decoration:none}
.btn-accent{background:var(--accent);color:#0a0b0e}
.btn-accent:hover{filter:brightness(1.08);transform:translateY(-1px)}
.btn-ghost{background:var(--surface);border-color:var(--line-strong);color:var(--fg)}
.btn-ghost:hover{background:var(--surface-2)}
.stats{max-width:1120px;margin:40px auto 0;padding:0 36px;display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.stat{background:var(--bg);padding:22px 24px}
.stat .n{font-size:26px;font-weight:700;letter-spacing:-.02em}
.stat .n.accent{color:var(--accent)}
.stat .l{font-size:12px;color:var(--dim);margin-top:4px}
.app{max-width:1120px;margin:56px auto 80px;padding:0 36px}
.app-head{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:20px;gap:20px;flex-wrap:wrap}
.app-head h2{font-size:22px;letter-spacing:-.02em}
.app-head p{color:var(--dim);font-size:13px;margin-top:4px}
.tabs{display:flex;gap:6px;background:var(--surface);border:1px solid var(--line);padding:5px;border-radius:14px}
.tab{font-family:inherit;font-size:13px;font-weight:500;color:var(--muted);cursor:pointer;background:transparent;border:none;padding:10px 16px;border-radius:10px;transition:.18s;display:flex;align-items:center;gap:8px}
.tab:hover{color:var(--fg)}
.tab.active{background:var(--fg);color:#0a0b0e;font-weight:600}
.stage{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:30px;min-height:420px;position:relative;overflow:hidden}
.vault-top{display:flex;align-items:center;gap:20px;padding-bottom:24px;border-bottom:1px solid var(--line);margin-bottom:24px}
.cover{width:78px;height:78px;border-radius:14px;flex-shrink:0;background:conic-gradient(from 210deg,#1b1d26,#2a2d3a,#15161d,#1b1d26);border:1px solid var(--line-strong);position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.cover::after{content:'';position:absolute;width:26px;height:26px;border-radius:50%;background:var(--accent);filter:blur(1px);opacity:.9;box-shadow:0 0 30px var(--accent)}
.vault-meta h3{font-size:19px;letter-spacing:-.01em}
.vault-meta .sub{color:var(--muted);font-size:13px;margin-top:3px}
.vault-meta .tags{display:flex;gap:7px;margin-top:10px}
.tg{font-size:11px;color:var(--muted);border:1px solid var(--line);border-radius:7px;padding:3px 9px}
.track{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:16px 18px;border:1px solid var(--line);border-radius:14px;margin-bottom:10px;transition:.18s;background:var(--bg)}
.track:hover{border-color:var(--line-strong)}
.track .lead{display:flex;align-items:center;gap:16px;min-width:0}
.track .idx{font-size:13px;color:var(--dim);width:22px;font-weight:500}
.track .name{font-size:14px;font-weight:500}
.track .hash{font-size:11px;color:var(--dim);margin-top:2px}
.state{font-size:11px;font-weight:600;padding:6px 11px;border-radius:999px;white-space:nowrap}
.state.shared{color:var(--ok);background:var(--ok-dim)}
.state.locked{color:var(--danger);background:var(--danger-dim)}
.state.sealed{color:var(--muted);background:var(--surface-2)}
.mini-btn{font-family:inherit;font-size:12px;font-weight:600;cursor:pointer;transition:.18s;padding:8px 14px;border-radius:9px;border:1px solid var(--line-strong);background:transparent;color:var(--fg);display:inline-flex;align-items:center;gap:7px}
.mini-btn.danger{color:var(--danger);border-color:rgba(255,77,109,.3)}
.mini-btn.danger:hover{background:var(--danger-dim)}
.mini-btn.ok{color:var(--ok);border-color:rgba(62,232,143,.3)}
.mini-btn.ok:hover{background:var(--ok-dim)}
.player{display:flex;flex-direction:column;gap:22px}
.now-playing{display:flex;align-items:center;gap:18px}
.disc{width:72px;height:72px;border-radius:50%;flex-shrink:0;background:repeating-radial-gradient(#0c0d12,#0c0d12 2px,#17181f 3px,#0c0d12 4px);border:1px solid var(--line-strong);position:relative;display:flex;align-items:center;justify-content:center}
.disc::after{content:'';width:18px;height:18px;border-radius:50%;background:var(--accent)}
.disc.spin{animation:spin 3s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.np-info .t{font-size:16px;font-weight:600}
.np-info .s{font-size:12px;color:var(--ok);margin-top:3px;display:flex;align-items:center;gap:6px}
.visualizer{height:96px;display:flex;align-items:flex-end;gap:3px;border:1px solid var(--line);border-radius:14px;background:linear-gradient(180deg,transparent,rgba(212,255,63,.015));overflow:hidden;padding:14px}
.bar{flex:1;background:var(--line-strong);border-radius:3px;height:10%;transition:height .1s ease}
.bar.on{background:linear-gradient(180deg,var(--accent),rgba(212,255,63,.3))}
.player-controls{display:flex;align-items:center;gap:16px}
.play-btn{width:54px;height:54px;border-radius:50%;flex-shrink:0;cursor:pointer;border:none;background:var(--accent);color:#0a0b0e;font-size:19px;transition:.2s;display:flex;align-items:center;justify-content:center}
.play-btn:hover{transform:scale(1.05)}
.timebar{flex:1}
.timebar .track-line{height:5px;border-radius:999px;background:var(--surface-2);overflow:hidden}
.timebar .fill{height:100%;width:0%;background:var(--accent);transition:width .25s linear}
.timebar .times{display:flex;justify-content:space-between;font-size:11px;color:var(--dim);margin-top:7px}
.denied{text-align:center;padding:50px 20px;border:1px solid rgba(255,77,109,.25);border-radius:16px;background:var(--danger-dim)}
.denied .big{font-size:40px}
.denied h3{color:var(--danger);font-size:19px;margin-top:14px}
.denied p{color:var(--muted);font-size:13px;margin-top:8px;max-width:420px;margin-left:auto;margin-right:auto}
.denied .code{font-size:12px;color:var(--danger);margin-top:16px;border:1px solid rgba(255,77,109,.25);display:inline-block;padding:6px 14px;border-radius:8px}
.inspector-note{display:flex;gap:12px;align-items:flex-start;background:var(--surface-2);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-bottom:20px;font-size:13px;color:var(--muted)}
.inspector-note .ic{color:var(--accent);flex-shrink:0;font-size:16px;margin-top:1px}
.blob-row{display:grid;grid-template-columns:1.1fr 2fr .9fr;gap:14px;align-items:center;padding:14px 16px;border:1px solid var(--line);border-radius:12px;margin-bottom:9px;background:var(--bg)}
.blob-row .key{font-size:12px;color:var(--muted)}
.blob-row .cipher{font-size:12px;color:#7b6fff;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.blob-row .keyval{font-size:11px;font-weight:700;color:var(--danger);text-align:right}
.hack-row{display:flex;align-items:center;gap:16px;margin-top:22px;flex-wrap:wrap}
.hack-out{font-size:12px;color:var(--danger);flex:1;min-width:240px}
.hidden{display:none!important}
.footer{max-width:1120px;margin:0 auto;padding:30px 36px 50px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;color:var(--dim);font-size:12px}
@media(max-width:780px){.stats{grid-template-columns:repeat(2,1fr)}.topbar{padding:16px 20px}.hero,.app,.stats,.footer{padding-left:20px;padding-right:20px}.blob-row{grid-template-columns:1fr;gap:6px}.blob-row .cipher,.blob-row .keyval{text-align:left}}
</style>
</head>
<body>
<header class="topbar">
  <div class="logo"><span class="dot"></span><div>UNRELEASED<small>Zero-Trust Audio Vault</small></div></div>
  <div class="right">
    <a class="ghost-link" href="https://github.com/bersious/Foodseekers" target="_blank">&#9670; Source</a>
    <span class="tide-chip">Powered by TideCloak</span>
  </div>
</header>

<section class="hero">
  <div class="kicker"><span class="pulse"></span> RMIT Hackathon 2026 &middot; Challenge 2 &middot; Team Foodseekers</div>
  <h1>Chia s&#7867; b&#7843;n thu<br><span class="glow">kh&#244;ng c&#7847;n tin ai c&#7843;.</span></h1>
  <p>Nghe th&#7917; nh&#7841;c ch&#432;a ph&#225;t h&#224;nh m&#224; kh&#244;ng m&#7897;t m&#225;y ch&#7911;, qu&#7843;n tr&#7883; vi&#234;n hay hacker n&#224;o ch&#7841;m &#273;&#432;&#7907;c t&#7899;i file g&#7889;c. Ch&#236;a kh&#243;a kh&#244;ng t&#7891;n t&#7841;i &#8212; cho &#273;&#7871;n &#273;&#250;ng kho&#7843;nh kh&#7855;c &#273;&#432;&#7907;c ph&#233;p.</p>
  <div class="cta">
    <a href="#demo" class="btn btn-accent">&#9654; Tr&#7843;i nghi&#7879;m demo</a>
    <a href="https://github.com/bersious/Foodseekers" target="_blank" class="btn btn-ghost">Xem ki&#7871;n tr&#250;c</a>
  </div>
</section>

<div class="stats">
  <div class="stat"><div class="n accent">0</div><div class="l">ch&#236;a kh&#243;a ch&#7911; l&#432;u tr&#234;n m&#225;y ch&#7911;</div></div>
  <div class="stat"><div class="n">AES-256</div><div class="l">m&#227; h&#243;a &#273;&#7847;u cu&#7889;i ph&#237;a client</div></div>
  <div class="stat"><div class="n">0.069<span style="font-size:14px">ms</span></div><div class="l">t&#7889;c &#273;&#7897; thu h&#7891;i quy&#7873;n</div></div>
  <div class="stat"><div class="n accent">&#8734;</div><div class="l">l&#7847;n admin th&#7917; &amp; th&#7845;t b&#7841;i</div></div>
</div>

<section class="app" id="demo">
  <div class="app-head">
    <div><h2>Ph&#242;ng demo tr&#7921;c ti&#7871;p</h2><p>Chuy&#7875;n vai &#273;&#7875; th&#7845;y c&#249;ng m&#7897;t file &#273;&#432;&#7907;c b&#7843;o v&#7879; ra sao t&#7915; ba g&#243;c nh&#236;n.</p></div>
    <div class="tabs">
      <button class="tab active" data-role="artist" onclick="go('artist')">&#127911; Ngh&#7879; s&#297;</button>
      <button class="tab" data-role="reviewer" onclick="go('reviewer')">&#127897; Ng&#432;&#7901;i nghe th&#7917;</button>
      <button class="tab" data-role="admin" onclick="go('admin')">&#9888; Qu&#7843;n tr&#7883; m&#225;y ch&#7911;</button>
    </div>
  </div>

  <div class="stage">
    <div id="view-artist">
      <div class="vault-top">
        <div class="cover"></div>
        <div class="vault-meta">
          <h3>MIDNIGHT CIPHER</h3>
          <div class="sub">Alice Nguy&#7877;n &middot; album ch&#432;a ph&#225;t h&#224;nh &middot; 3 b&#7843;n thu</div>
          <div class="tags"><span class="tg">FLAC 24-bit</span><span class="tg">Zero-Custody</span><span class="tg">Client-side AES</span></div>
        </div>
      </div>
      <div class="track">
        <div class="lead"><span class="idx">01</span><div><div class="name">Lead Single &#8212; Master v4</div><div class="hash mono">sha256 &middot; b79a4e&#8230;</div></div></div>
        <div style="display:flex;align-items:center;gap:12px">
          <span class="state shared" id="t1-state">&#272;&#227; c&#7845;p cho Minh</span>
          <button class="mini-btn danger" id="t1-btn" onclick="toggleShare()">Thu h&#7891;i quy&#7873;n</button>
        </div>
      </div>
      <div class="track">
        <div class="lead"><span class="idx">02</span><div><div class="name">Vocal Stems &#8212; Dry</div><div class="hash mono">sha256 &middot; 82f10a&#8230;</div></div></div>
        <span class="state sealed">&#128274; Ni&#234;m phong</span>
      </div>
      <div class="track">
        <div class="lead"><span class="idx">03</span><div><div class="name">Feature Draft &#8212; K&#237;n</div><div class="hash mono">sha256 &middot; 11ce9d&#8230;</div></div></div>
        <span class="state sealed">&#128274; Ni&#234;m phong</span>
      </div>
    </div>

    <div id="view-reviewer" class="hidden">
      <div id="player-ok" class="player">
        <div class="now-playing">
          <div class="disc" id="disc"></div>
          <div class="np-info"><div class="t">Lead Single &#8212; Master v4</div><div class="s">&#9679; gi&#7843;i m&#227; t&#7913;c th&#7901;i tr&#234;n RAM &middot; kh&#244;ng l&#432;u &#7893; c&#7913;ng</div></div>
        </div>
        <div class="visualizer" id="viz"></div>
        <div class="player-controls">
          <button class="play-btn" id="play" onclick="togglePlay()">&#9654;</button>
          <div class="timebar">
            <div class="track-line"><div class="fill" id="fill"></div></div>
            <div class="times mono"><span id="cur">0:00</span><span>3:42</span></div>
          </div>
        </div>
      </div>
      <div id="player-denied" class="denied hidden">
        <div class="big">&#9940;</div>
        <h3>Quy&#7873;n truy c&#7853;p &#273;&#227; b&#7883; thu h&#7891;i</h3>
        <p>Alice v&#7915;a r&#250;t quy&#7873;n. V&#236; ch&#236;a kh&#243;a l&#224; quy&#7873;n h&#7841;n t&#7921; sinh t&#7915; m&#7841;ng Quorum &#8212; kh&#244;ng ph&#7843;i gi&#225; tr&#7883; l&#432;u &#273;&#226;u &#273;&#243; &#8212; kh&#244;ng token c&#361; hay b&#7843;n cache n&#224;o t&#225;i t&#7841;o l&#7841;i &#273;&#432;&#7907;c.</p>
        <div class="code mono">403 &middot; EntitlementRevoked</div>
      </div>
    </div>

    <div id="view-admin" class="hidden">
      <div class="inspector-note"><span class="ic">&#9670;</span><div>&#272;&#226;y l&#224; t&#7845;t c&#7843; nh&#7919;ng g&#236; m&#7897;t qu&#7843;n tr&#7883; vi&#234;n m&#225;y ch&#7911; (ho&#7863;c k&#7867; chi&#7871;m &#273;&#432;&#7907;c quy&#7873;n root S3) nh&#236;n th&#7845;y. To&#224;n b&#7897; ch&#7881; l&#224; kh&#7889;i nh&#7883; ph&#226;n m&#227; h&#243;a &#8212; kh&#244;ng k&#232;m ch&#236;a kh&#243;a.</div></div>
      <div class="blob-row"><div class="key mono">track_01.enc</div><div class="cipher mono">d8a391e4fc2901a88b5e027f8a1924bc99014e&#8230;</div><div class="keyval">KEY: &#8709;</div></div>
      <div class="blob-row"><div class="key mono">track_02.enc</div><div class="cipher mono">1f80aa7621c08be991448bcae912408fb241a7&#8230;</div><div class="keyval">KEY: &#8709;</div></div>
      <div class="blob-row"><div class="key mono">track_03.enc</div><div class="cipher mono">7c8911bb20e14ad9f92881a70094bba8912ef0&#8230;</div><div class="keyval">KEY: &#8709;</div></div>
      <div class="hack-row">
        <button class="mini-btn danger" onclick="tryLeak()">&#128680; Th&#7917; d&#249;ng quy&#7873;n root &#273;&#7875; gi&#7843;i m&#227;</button>
        <span class="hack-out mono" id="leak-out"></span>
      </div>
    </div>
  </div>
</section>

<footer class="footer">
  <span>UNRELEASED &middot; Team Foodseekers (UIT)</span>
  <span class="mono">RMIT Hackathon 2026 &#8212; Security x GenAI</span>
</footer>

<script>
let sharing=true,playing=false,t=0,timer=null,synth=null,ctx=null,note=0;
const notes=[261.63,329.63,392,523.25,440,392,329.63,293.66];
const viz=document.getElementById('viz');
for(let i=0;i<60;i++){const b=document.createElement('div');b.className='bar';viz.appendChild(b)}
const bars=[...document.querySelectorAll('.bar')];
function go(role){
  document.querySelectorAll('.tab').forEach(x=>x.classList.toggle('active',x.dataset.role===role));
  ['artist','reviewer','admin'].forEach(r=>document.getElementById('view-'+r).classList.toggle('hidden',r!==role));
  if(role==='reviewer')syncReviewer();
}
function toggleShare(){sharing=!sharing;render()}
function render(){
  const st=document.getElementById('t1-state'),btn=document.getElementById('t1-btn');
  if(sharing){st.className='state shared';st.textContent='\u0110\u00e3 c\u1ea5p cho Minh';btn.className='mini-btn danger';btn.textContent='Thu h\u1ed3i quy\u1ec1n';}
  else{st.className='state locked';st.textContent='\u0110\u00e3 thu h\u1ed3i';btn.className='mini-btn ok';btn.textContent='C\u1ea5p l\u1ea1i quy\u1ec1n';if(playing)stop();}
  syncReviewer();
}
function syncReviewer(){
  document.getElementById('player-ok').classList.toggle('hidden',!sharing);
  document.getElementById('player-denied').classList.toggle('hidden',sharing);
}
function tone(f){try{if(!ctx)ctx=new(window.AudioContext||window.webkitAudioContext)();if(ctx.state==='suspended')ctx.resume();const o=ctx.createOscillator(),g=ctx.createGain();o.type='triangle';o.frequency.value=f;g.gain.setValueAtTime(.05,ctx.currentTime);g.gain.exponentialRampToValueAtTime(.0001,ctx.currentTime+.5);o.connect(g);g.connect(ctx.destination);o.start();o.stop(ctx.currentTime+.5);}catch(e){}}
function stop(){playing=false;document.getElementById('play').textContent='\u25b6';document.getElementById('disc').classList.remove('spin');bars.forEach(b=>{b.classList.remove('on');b.style.height='10%'});clearInterval(timer);clearInterval(synth);}
function togglePlay(){
  if(!sharing)return;
  playing=!playing;
  const disc=document.getElementById('disc'),play=document.getElementById('play');
  if(playing){play.textContent='\u23f8';disc.classList.add('spin');tone(notes[note]);
    synth=setInterval(()=>{note=(note+1)%notes.length;tone(notes[note]);bars.forEach(b=>b.style.height=(15+Math.random()*80)+'%');bars.forEach(b=>b.classList.toggle('on',Math.random()>.25));},200);
    timer=setInterval(()=>{t++;document.getElementById('cur').textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0');document.getElementById('fill').style.width=Math.min(t/222*100,100)+'%';},1000);
  }else stop();
}
function tryLeak(){const o=document.getElementById('leak-out');o.textContent='';const msg='> querying Tide Fabric\u2026 DENIED \u2014 server holds zero master keys. Decryption impossible.';let i=0;const ty=setInterval(()=>{o.textContent=msg.slice(0,++i);if(i>=msg.length)clearInterval(ty)},18);}
</script>
</body>
</html>
'''

with io.open(r"C:\Users\nguye\Foodseekers\prototype\index.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("Wrote prototype/index.html:", len(HTML), "chars")
