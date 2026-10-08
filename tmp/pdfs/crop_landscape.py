import pymupdf
from pathlib import Path
src=pymupdf.open('assets/uav-landscape.png')
d=pymupdf.open('pdf',src.convert_to_pdf())
p=d[0]
scale=p.rect.width/2347
pix=p.get_pixmap(matrix=pymupdf.Matrix(1/scale,1/scale),clip=pymupdf.Rect(752*scale,304*scale,1809*scale,1015*scale))
pix.save('assets/uav-landscape-crop.png')
f=Path('index.html')
s=f.read_text(encoding='utf-8-sig').replace('assets/uav-landscape.png" width="2347" height="1115','assets/uav-landscape-crop.png" width="1057" height="711').replace('From the original research portfolio, p. 1','Cropped from the research portfolio, p. 1')
f.write_text(s,encoding='utf-8')
