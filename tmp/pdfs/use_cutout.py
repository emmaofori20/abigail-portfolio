from pathlib import Path
p=Path('index.html'); s=p.read_text(encoding='utf-8').replace('src="assets/portrait.jpg" width="400" height="400"','src="assets/portrait-cutout.png" width="1254" height="1254"').replace('alt="Abigail A. Adjetey Bisa, seated with her arms folded, wearing a red top."','alt="Abigail A. Adjetey Bisa with her arms folded, wearing a red top."'); p.write_text(s,encoding='utf-8')
assert 'class="source"' not in s
assert 'Remote Sensing · GIS · Geospatial AI' in s
