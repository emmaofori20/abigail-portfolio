from pathlib import Path
import re
p=Path('index.html'); s=p.read_text(encoding='utf-8')
start=s.index('  <section class="hero wrap"'); end=s.index('  </section>',start)+len('  </section>')
s=s[:start]+'''  <section class="hero wrap editorial-hero" id="profile" aria-labelledby="profile-title">
    <h1 id="profile-title" class="editorial-title"><span>EXPLORE MY</span><span>RESEARCH</span></h1>
    <figure class="portrait"><img src="assets/portrait-cutout.png" width="1254" height="1254" alt="Abigail A. Adjetey Bisa with her arms folded, wearing a red top."></figure>
    <div class="hero-copy">
      <h2>Abigail A.<br>Adjetey Bisa</h2>
      <p>I use remote sensing, GIS and AI to study agricultural and environmental landscapes. My work spans cocoa nutrient assessment, agroforestry shade characterisation, and satellite-based land-cover and deforestation monitoring.</p>
    </div>
    <ul class="hero-disciplines" aria-label="Research disciplines"><li>Remote Sensing</li><li>GIS</li><li>Geospatial AI</li></ul>
    <div class="actions"><a class="button" href="#projects">Explore Research</a><a class="portfolio-link" href="source/research-portfolio.pdf" download="Abigail-Adjetey-Bisa-Research-Portfolio.pdf">Download Portfolio <span>(PDF)</span></a></div>
  </section>'''+s[end:]
p.write_text(s,encoding='utf-8')
p=Path('styles.css'); s=p.read_text(encoding='utf-8')
s+='''
/* Centred editorial composition; portrait overlap uses its transparent upper margin. */
.site-header{border-bottom:1px solid var(--border)}
nav{gap:.5rem}
nav a{border:1px solid var(--border);border-radius:999px;padding:.4rem .95rem;font-size:.85rem;line-height:1.5;min-height:36px}
nav a:hover{border-color:var(--accent);background:var(--surface)}
.editorial-hero{display:grid;grid-template-columns:1fr 1.5fr .65fr;grid-template-rows:auto 1fr auto;gap:0 2rem;padding:3rem 0 0;align-items:center}
.editorial-title{grid-column:1/-1;grid-row:1;text-align:center;font-size:clamp(4rem,11vw,10rem);line-height:.87;font-weight:650;letter-spacing:-.065em;margin:0;position:relative;z-index:2}
.editorial-title span{display:block}
.editorial-hero .portrait{grid-column:2;grid-row:2 / span 2;margin-top:-1.8rem;align-self:end;width:100%;position:relative;z-index:1}
.editorial-hero .portrait img{height:540px;width:100%;object-fit:contain;object-position:center bottom}
.editorial-hero .hero-copy{grid-column:1;grid-row:2;align-self:center;padding-top:2rem}
.editorial-hero .hero-copy h2{font-size:clamp(1.6rem,2.35vw,2.1rem);line-height:1.12;font-weight:600;margin-bottom:1rem;letter-spacing:-.035em}
.editorial-hero .hero-copy>p{font-size:.98rem;line-height:1.75;margin:0;max-width:36ch}
.hero-disciplines{grid-column:3;grid-row:2;list-style:none;padding:0;margin:2rem 0 0;align-self:center;font-size:1rem;font-weight:500;line-height:1.5}
.hero-disciplines li{padding:.75rem 0;border-bottom:1px solid var(--border)}
.hero-disciplines li:first-child{border-top:1px solid var(--border)}
.editorial-hero>.actions{grid-column:1;grid-row:3;align-self:start;flex-direction:column;align-items:start;gap:.5rem;margin:0 0 2rem}
.about>h2{font-size:clamp(2.6rem,5vw,4.5rem);line-height:1.05}
@media(max-width:1050px) and (min-width:701px){.editorial-hero{grid-template-columns:1fr 1.3fr .7fr;gap:0 1.5rem}.editorial-hero .portrait img{height:460px}.editorial-hero .hero-copy>p{font-size:.9rem}.hero-disciplines{font-size:.9rem}.editorial-hero .hero-copy h2{font-size:1.6rem}}
@media(max-width:700px){.editorial-hero{display:flex;flex-direction:column;align-items:stretch;padding:2.2rem 0 2rem;gap:1.7rem}.editorial-title{order:0;font-size:clamp(2.8rem,11.5vw,5rem);line-height:.9;margin:0}.editorial-hero .portrait{order:1;margin-top:-2.1rem;width:min(100%,420px);align-self:center}.editorial-hero .portrait img{height:auto;max-height:440px}.editorial-hero .hero-copy{order:2;padding:0;align-self:stretch}.editorial-hero .hero-copy h2{font-size:2rem;margin-bottom:.8rem}.editorial-hero .hero-copy>p{font-size:1rem;max-width:none}.hero-disciplines{order:3;margin:0;font-size:1rem}.hero-disciplines li{padding:.55rem 0}.editorial-hero>.actions{order:4;margin:0;flex-direction:row;align-items:center;gap:1rem}.about>h2{font-size:2.6rem}nav a{min-height:40px;padding:.45rem .85rem}nav{gap:.5rem}}
@media(max-width:360px){.editorial-title{font-size:11.5vw}.editorial-hero>.actions{gap:.7rem}}
@media print{.editorial-hero{display:block}.editorial-title{font-size:3rem;margin-bottom:1rem}.hero-disciplines{margin-top:1rem}}
'''
p.write_text(s,encoding='utf-8')
