from pathlib import Path
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=s.replace('    <h1 id="profile-title" class="discipline">Remote<br>sensing</h1>\n','')
s=s.replace('<h2>Abigail A.<br>Adjetey Bisa</h2>','<h1 id="profile-title">Abigail A. Adjetey Bisa</h1>')
s=s.replace('Remote sensing, GIS &amp; geospatial AI research','Remote Sensing · GIS · Geospatial AI')
s=s.replace('I connect field observations, UAV imagery and satellite data to study crop nutrition, cocoa agroforestry and environmental change.','My research combines remote sensing, GIS and artificial intelligence for agricultural and environmental applications. I work with field observations, UAV imagery and satellite data to assess crop nutrients, characterise cocoa agroforestry, and map land cover and deforestation.')
s=s.replace('Earth observation and geospatial analysis for agricultural and environmental decision-making.','Remote sensing, spatial analysis and AI applied to crop nutrition, agroforestry, precision agriculture and environmental monitoring.')
p.write_text(s,encoding='utf-8')
p=Path('styles.css'); s=p.read_text(encoding='utf-8')
s+='''
/* The researcher, rather than a single discipline, leads the introduction. */
.hero{grid-template-rows:auto auto;align-items:center}
.portrait{grid-row:1}
.hero-copy{grid-row:1;align-self:center;padding:0}
.hero-copy h1{font-size:clamp(2.8rem,4.7vw,4.4rem);line-height:1.07;letter-spacing:-.04em;font-weight:600;max-width:14ch;margin-bottom:1.3rem}
.role{max-width:none}
.hero-focus{grid-row:2}
@media(max-width:700px){.hero-copy h1{font-size:clamp(2.3rem,9.8vw,3.3rem);max-width:none}.hero-copy{padding:0}}
'''
p.write_text(s,encoding='utf-8')
assert s.count('--background:#FFFFFF')==1
assert 'class="discipline"' not in Path('index.html').read_text(encoding='utf-8')
