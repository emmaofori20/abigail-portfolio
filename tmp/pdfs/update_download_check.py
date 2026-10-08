from pathlib import Path
p=Path('tmp/pdfs/check_portfolio.py')
s=p.read_text(encoding='utf-8').replace("page.locator('.button[download]').click()","page.locator('.portfolio-link[download]').click()")
p.write_text(s,encoding='utf-8')
