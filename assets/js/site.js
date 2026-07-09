/* ============================================================
   Inspire Arts Software — shared canvas animations
   One starfield (always) + a reusable hero animation chosen by
   the page via <canvas id="heroCanvas" data-anim="...">.
   Animations: waveform | spectrum | orbit | matrix | particles
   Accent colours are read from CSS variables on <body>.
   ============================================================ */
(function(){
  const css = getComputedStyle(document.body);
  function v(name, fb){ const c = css.getPropertyValue(name).trim(); return c || fb; }
  const ACCENT_A = v('--accent-a', '#3A86FF');
  const ACCENT_B = v('--accent-b', '#33E0FF');
  const ACCENT_C = v('--accent-c', '#C77DFF');
  const DPR = Math.min(window.devicePixelRatio || 1, 2);

  /* ---- starfield (every page) ---- */
  const sc = document.getElementById('stars');
  let stars = [], sctx = sc ? sc.getContext('2d') : null;
  function buildStars(){
    if(!sc) return;
    sc.width = innerWidth; sc.height = innerHeight;
    stars = Array.from({length:130},()=>({
      x:Math.random()*sc.width, y:Math.random()*sc.height,
      r:Math.random()*1.3+.3, p:Math.random()*Math.PI*2, s:.4+Math.random()*1.2
    }));
  }
  function drawStars(t){
    if(!sctx) return;
    sctx.clearRect(0,0,sc.width,sc.height);
    for(const st of stars){
      const a = .15 + .35*(0.5+0.5*Math.sin(t*.001*st.s + st.p));
      sctx.fillStyle = `rgba(255,255,255,${a})`;
      sctx.beginPath(); sctx.arc(st.x,st.y,st.r,0,7); sctx.fill();
    }
  }
  buildStars(); addEventListener('resize', buildStars);

  /* ---- hero canvas ---- */
  const hc = document.getElementById('heroCanvas');
  const hctx = hc ? hc.getContext('2d') : null;
  const anim = hc ? (hc.dataset.anim || 'waveform') : null;
  function sizeHero(){ if(!hc) return; hc.width = hc.clientWidth*DPR; hc.height = hc.clientHeight*DPR; }
  sizeHero(); addEventListener('resize', sizeHero);

  // helpers
  function hueShift(t){ return (t*0.012) % 360; }

  function drawWaveform(t){
    const w=hc.width,h=hc.height,mid=h/2;
    hctx.clearRect(0,0,w,h);
    const phase=t*0.0016, hue=(200+t*0.012)%360;
    for(let layer=0;layer<3;layer++){
      hctx.beginPath();
      const amp=(h*0.30)*(1-layer*0.28), sp=.012+layer*.005, ph=phase*(1+layer*.4);
      for(let x=0;x<=w;x+=3){
        const env=Math.exp(-((x-w/2)**2)/(2*(w*0.26)**2));
        const y=mid+(Math.sin(x*sp+ph)*amp+Math.sin(x*sp*0.45-ph*0.6)*amp*0.35)*env;
        x===0?hctx.moveTo(x,y):hctx.lineTo(x,y);
      }
      const g=hctx.createLinearGradient(0,0,w,0);
      g.addColorStop(0,`hsla(${hue},90%,60%,0)`);
      g.addColorStop(.3,`hsla(${hue},90%,62%,${.65-layer*.18})`);
      g.addColorStop(.5,`hsla(${(hue+70)%360},85%,68%,${.85-layer*.22})`);
      g.addColorStop(.7,`hsla(${hue},90%,62%,${.65-layer*.18})`);
      g.addColorStop(1,`hsla(${hue},90%,60%,0)`);
      hctx.strokeStyle=g; hctx.lineWidth=(3-layer)*DPR;
      hctx.shadowColor=`hsla(${(hue+40)%360},90%,65%,.8)`; hctx.shadowBlur=14;
      hctx.stroke();
    }
    hctx.shadowBlur=0;
  }

  function drawSpectrum(t){
    const w=hc.width,h=hc.height, bars=46, bw=w/bars;
    hctx.clearRect(0,0,w,h);
    for(let i=0;i<bars;i++){
      const n=Math.abs(Math.sin(i*0.5+t*0.003))*0.6+Math.abs(Math.sin(i*0.17+t*0.0021))*0.4;
      const bh=n*h*0.92, x=i*bw+bw*0.15, bwi=bw*0.7;
      const g=hctx.createLinearGradient(0,h,0,h-bh);
      g.addColorStop(0,ACCENT_A); g.addColorStop(.6,ACCENT_B); g.addColorStop(1,ACCENT_C);
      hctx.fillStyle=g; hctx.shadowColor=ACCENT_B; hctx.shadowBlur=12;
      hctx.fillRect(x,h-bh,bwi,bh);
    }
    hctx.shadowBlur=0;
  }

  function drawOrbit(t){
    const w=hc.width,h=hc.height,cx=w/2,cy=h/2;
    hctx.clearRect(0,0,w,h);
    for(let ring=0;ring<3;ring++){
      const R=(Math.min(w,h)*0.16)*(ring+1), n=10+ring*6;
      for(let i=0;i<n;i++){
        const a=(i/n)*Math.PI*2 + t*(0.0004+ring*0.0002)*(ring%2?1:-1);
        const x=cx+Math.cos(a)*R*1.7, y=cy+Math.sin(a)*R*0.7;
        const col=[ACCENT_A,ACCENT_B,ACCENT_C][(i+ring)%3];
        hctx.fillStyle=col; hctx.shadowColor=col; hctx.shadowBlur=10;
        hctx.beginPath(); hctx.arc(x,y,(2.2-ring*0.4)*DPR,0,7); hctx.fill();
      }
    }
    hctx.shadowBlur=0;
  }

  let mrops=null;
  function drawMatrix(t){
    const w=hc.width,h=hc.height, fs=14*DPR, cols=Math.floor(w/fs);
    if(!mrops||mrops.length!==cols){ mrops=Array.from({length:cols},()=>Math.random()*-30); }
    hctx.fillStyle='rgba(7,7,26,0.18)'; hctx.fillRect(0,0,w,h);
    hctx.font=fs+'px Consolas, monospace';
    for(let i=0;i<cols;i++){
      const ch=String.fromCharCode(0x30A0+Math.floor(Math.random()*60));
      const y=mrops[i]*fs;
      hctx.fillStyle=ACCENT_B; hctx.shadowColor=ACCENT_B; hctx.shadowBlur=8;
      hctx.fillText(ch, i*fs, y);
      hctx.shadowBlur=0;
      if(y>h && Math.random()>0.975) mrops[i]=0; else mrops[i]+=0.5;
    }
  }

  let parts=null;
  function drawParticles(t){
    const w=hc.width,h=hc.height,cx=w/2,cy=h/2;
    if(!parts){ parts=Array.from({length:90},()=>({a:Math.random()*7,r:Math.random(),s:0.2+Math.random()*0.8,sz:Math.random()*2+1})); }
    hctx.clearRect(0,0,w,h);
    const pulse=0.5+0.5*Math.sin(t*0.003);
    for(const p of parts){
      const rad=p.r*Math.min(w,h)*0.5*(0.6+pulse*0.6);
      const ang=p.a + t*0.0006*p.s;
      const x=cx+Math.cos(ang)*rad*1.6, y=cy+Math.sin(ang)*rad*0.8;
      const col=[ACCENT_A,ACCENT_B,ACCENT_C][Math.floor(p.a)%3];
      hctx.fillStyle=col; hctx.shadowColor=col; hctx.shadowBlur=10;
      hctx.beginPath(); hctx.arc(x,y,p.sz*DPR,0,7); hctx.fill();
    }
    hctx.shadowBlur=0;
  }

  const renderers={waveform:drawWaveform,spectrum:drawSpectrum,orbit:drawOrbit,matrix:drawMatrix,particles:drawParticles};
  const hero = hctx ? (renderers[anim]||drawWaveform) : null;

  function loop(t){
    drawStars(t);
    if(hero) hero(t);
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
