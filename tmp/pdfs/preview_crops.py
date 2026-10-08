import pymupdf
for width in [1440,390]:
    src=pymupdf.open(f'tmp/pdfs/portfolio-{width}.png')
    d=pymupdf.open('pdf',src.convert_to_pdf())
    p=d[0]
    scale=p.rect.width/width
    p.get_pixmap(matrix=pymupdf.Matrix(1/scale,1/scale),clip=pymupdf.Rect(0,0,p.rect.width,1200*scale)).save(f'tmp/pdfs/preview-{width}.png')
