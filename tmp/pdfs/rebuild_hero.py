from pathlib import Path
import re
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=s.replace('<h1 id="profile-title">Abigail A. Adjetey Bisa</h1>','<h1 id="profile-title">Abigail A.<br>Adjetey Bisa</h1>')
s=s.replace('My research combines remote sensing, GIS and artificial intelligence for agricultural and environmental applications. I work with field observations, UAV imagery and satellite data to assess crop nutrients, characterise cocoa agroforestry, and map land cover and deforestation.','I use remote sensing, GIS and AI to study agricultural and environmental landscapes. My work spans cocoa nutrient assessment, agroforestry shade characterisation, and satellite-based land-cover and deforestation monitoring.')
s=s.replace('class="button button-outline"','class="portfolio-link"')
s=s.replace('<figure class="portrait">','<figure class="portrait"><span class="portrait-type" aria-hidden="true">Research</span>')
s=s.replace('    <p class="hero-focus">Agricultural &amp; environmental applications</p>\n','')
s=re.sub(r'<p class="source">.*?</p>','',s,flags=re.S)
s=re.sub(r'<span>Research portfolio, p\. \d+</span>','',s)
s=s.replace('Publication statuses are reported as listed in the research portfolio.','Published work and manuscripts in progress.')
start=s.index('    <div><p class="lead">',s.index('id="about"'))
end=s.index('</div>',start)+6
s=s[:start]+'''    <div><p class="lead">My research experience connects fieldwork, spatial analysis and collaborative landscape research in Ghana.</p><p>Within the Deforestation-Free Cocoa Project, I led field-data collection, supervised training-coordinate collection for historical mapping, and developed Python machine-learning and CNN classifiers. I also constructed physical 3D landscape models for stakeholder communication.</p><p>Through FRAME-Cocoa research, I contributed to soil and foliar sampling, multispectral predictor development, and GIS-based characterisation of shade conditions in cocoa farms. My work distinguishes these individual contributions from the broader teams’ agroforestry and landscape research.</p></div>'''+s[end:]
p.write_text(s,encoding='utf-8')
p=Path('styles.css'); s=p.read_text(encoding='utf-8')
s=s.replace('--text:#182538','--text:#142033')
s+='''
/* Portrait-led white hero: introduction left, genuine cutout right. */
.hero-shell{background:var(--background);color:var(--text)}
.site-header{padding-block:1.6rem}
.identity span{color:var(--text)}
.hero-shell a:hover{color:var(--accent)}
.hero-shell a:focus-visible{outline-color:var(--accent)}
.hero{border:0;grid-template-columns:1.12fr 1fr;grid-template-rows:auto;gap:3rem;align-items:center;padding:2.8rem 0 3rem;isolation:isolate}
.hero-copy{grid-column:1;grid-row:1;z-index:2;align-self:center;padding:0}
.hero-copy h1{font-size:clamp(3rem,5.8vw,5.3rem);line-height:1.03;max-width:none;margin-bottom:1.5rem;letter-spacing:-.055em}
.role{color:var(--accent);font-size:1.05rem;line-height:1.5;font-weight:600}
.hero-copy>p:last-of-type{color:var(--text);font-size:1.1rem;margin-top:1.5rem;max-width:49ch}
.actions{gap:1.5rem;margin-top:2rem}
.button{border-radius:3px;padding:.9rem 1.3rem}
.button:hover,.hero-shell .button:hover{background:var(--text);color:var(--text-on-dark);border-color:var(--text)}
.button:focus-visible{outline-color:var(--accent)}
.portfolio-link{font-size:.96rem;padding:.7rem 0;text-decoration:underline;text-underline-offset:.35em}
.portrait{grid-column:2;grid-row:1;width:100%;max-width:none;margin:0;position:relative;border:0;overflow:visible;isolation:isolate;align-self:end}
.portrait img{position:relative;z-index:1;display:block;width:100%;height:590px;max-height:none;aspect-ratio:auto;object-fit:contain;object-position:center bottom;border:0;filter:none}
.portrait-type{position:absolute;z-index:0;left:-.15em;bottom:.65em;font-size:clamp(5rem,9vw,9rem);font-weight:650;line-height:1;letter-spacing:-.065em;color:var(--surface);pointer-events:none}
.about{border-top:1px solid var(--border)}
@media(max-width:1050px) and (min-width:701px){.hero{gap:2rem;grid-template-columns:1.15fr 1fr}.hero-copy h1{font-size:5.8vw}.portrait img{height:480px}.role{font-size:.95rem}.hero-copy>p:last-of-type{font-size:1rem}}
@media(max-width:700px){.hero{display:flex;flex-direction:column;padding:2rem 0 0;gap:2rem;align-items:stretch}.hero-copy{order:0}.hero-copy h1{font-size:clamp(2.7rem,11vw,4.3rem)}.role{font-size:.98rem}.hero-copy>p:last-of-type{font-size:1.05rem}.portrait{order:1;width:min(100%,460px);margin-inline:auto}.portrait img{height:auto;max-height:490px;width:100%;object-fit:contain}.portrait-type{font-size:18vw;left:0;bottom:.8em}.hero-shell:has(.hero){padding-bottom:0}.actions{gap:1.1rem}}
@media(max-width:360px){.hero-copy h1{font-size:11vw}.role{font-size:.9rem}}
@media print{.portrait{display:none}.hero{display:block}.hero-copy h1{font-size:3rem}}
'''
p.write_text(s,encoding='utf-8')
