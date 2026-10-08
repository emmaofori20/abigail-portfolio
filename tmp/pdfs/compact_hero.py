from pathlib import Path
p=Path('index.html'); s=p.read_text(encoding='utf-8').replace('<h1 id="profile-title" class="editorial-title"><span>EXPLORE MY</span><span>RESEARCH</span></h1>','<h1 id="profile-title" class="editorial-title">Research portfolio</h1>'); p.write_text(s,encoding='utf-8')
p=Path('styles.css'); s=p.read_text(encoding='utf-8'); s+='''
/* Compact refinement of the existing editorial layout. */
.editorial-hero{padding-top:1.5rem}
.editorial-title{font-size:clamp(2.4rem,5.5vw,5rem);line-height:1.15;font-weight:400;letter-spacing:-.045em;white-space:nowrap}
.editorial-hero .hero-copy{padding-top:1rem}
.editorial-hero .hero-copy h2{font-size:clamp(2rem,3.2vw,2.85rem);line-height:1.1;font-weight:600}
.editorial-hero .portrait{margin-top:-.7rem}
@media(max-width:1050px) and (min-width:701px){.editorial-hero .hero-copy h2{font-size:2.15rem}}
@media(max-width:700px){.editorial-hero{padding-top:1.3rem;gap:1.3rem}.editorial-title{font-size:clamp(1.8rem,7.6vw,3rem);line-height:1.15;white-space:normal}.editorial-hero .portrait{margin-top:-1rem}.editorial-hero .hero-copy{padding-top:0}.editorial-hero .hero-copy h2{font-size:clamp(2rem,9vw,2.6rem)}}
'''; p.write_text(s,encoding='utf-8')
