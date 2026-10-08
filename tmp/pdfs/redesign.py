from pathlib import Path
import re, pymupdf
root=Path('.')
doc=pymupdf.open('source/research-portfolio.pdf')
for page,name in [(4,'nutrient-study'),(10,'shade-canopy'),(12,'historical-landcover'),(14,'classifier-comparison')]:
    x=doc[page].get_images()[0][0]
    pymupdf.Pixmap(doc,x).save(f'assets/{name}.png')
f=Path('index.html'); s=f.read_text(encoding='utf-8-sig')
s=s.replace('<body>','<body>\n<div class="hero-shell">')
s=s.replace('<a href="#research">Research</a>','<a href="#about">About</a><a href="#research">Research</a>')
start=s.index('  <section class="hero wrap"')
end=s.index('  <section class="research-band"',start)
s=s[:start]+'''  <section class="hero wrap" id="profile" aria-labelledby="profile-title">
    <h1 id="profile-title" class="discipline">Remote<br>sensing</h1>
    <div class="portrait-placeholder" role="img" aria-label="The researcher's portrait is not yet available">
      <p>Researcher’s portrait</p><span>Photo not yet supplied</span>
    </div>
    <!-- Replace the labelled placeholder above with the actual researcher photograph at assets/portrait.jpg. Do not substitute another person. -->
    <div class="hero-copy">
      <h2>Abigail A.<br>Adjetey Bisa</h2>
      <p class="role">Remote sensing, GIS &amp; geospatial AI research</p>
      <p>I connect field observations, UAV imagery and satellite data to study crop nutrition, cocoa agroforestry and environmental change.</p>
      <div class="actions"><a class="button" href="#projects">Explore Research</a><a class="button button-outline" href="source/research-portfolio.pdf" download="Abigail-Adjetey-Bisa-Research-Portfolio.pdf">Download Portfolio <span>(PDF)</span></a></div>
    </div>
    <p class="hero-focus">Agricultural &amp; environmental applications</p>
  </section>
  </div>
  <section class="wrap section about" id="about" aria-labelledby="about-title">
    <h2 id="about-title">About the researcher</h2>
    <div><p class="lead">My research lies at the intersection of remote sensing, geographic information science and artificial intelligence.</p><p>My experience includes UAV multispectral crop nutrient assessment, satellite land-use and land-cover classification, deep learning for satellite imagery, and GIS analysis of cocoa agroforestry landscapes.</p><p>Across these projects, I work with field and reference data, spatial processing and predictive models to produce agricultural and environmental decision-support outputs.</p><p class="source">Research portfolio, pp. 1–3</p></div>
  </section>
''' +s[end:]
# Main extends through the hero; hero-shell is a purely visual wrapper around header and main's first section.
s=s.replace('<main id="main" tabindex="-1">','</div>\n<main id="main" tabindex="-1">\n<div class="hero-shell">')
figures=[('nutrient-study','Study-area map and UAV orthomosaic for the cocoa nutrient study.','Study area and UAV orthomosaic','5'),('shade-canopy','Juaboso landscape land-cover map showing cocoa shade canopy variations.','Cocoa shade canopy variations','11'),('historical-landcover','Historical landscape maps comparing land cover in 2015, 2020 and 2024.','Historical landscape classification, 2015–2024','13'),('classifier-comparison','Juaboso-Bia land-cover maps comparing Random Forest, SVM and CNN classifications.','Landsat 9 L2 classifier comparison','15')]
idx=0
def add_figure(m):
    global idx
    name,alt,caption,page=figures[idx]; idx+=1
    return m.group(0).replace('</article>',f'<figure class="project-figure"><a href="source/research-portfolio.pdf#page={page}" aria-label="View {caption.lower()} in the original PDF"><img src="assets/{name}.png" alt="{alt}" loading="lazy"></a><figcaption>{caption}<span>Research portfolio, p. {page}</span></figcaption></figure></article>')
s=re.sub(r'<article class="project(?: featured)?">.*?</article>',add_figure,s,flags=re.S)
s=s.replace('<section class="wrap section" id="projects"','<section class="wrap section projects-section" id="projects"')
s=s.replace('<footer class="wrap">','<footer class="wrap">')
f.write_text(s,encoding='utf-8')
