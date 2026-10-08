from pathlib import Path
p=Path('tmp/pdfs/check_portfolio.py')
s=p.read_text(encoding='utf-8-sig').replace("assert page.locator('img').evaluate('(e) => e.complete && e.naturalWidth > 0')", "for img in page.locator('img').all():\n            img.scroll_into_view_if_needed()\n            page.wait_for_function('(e) => e.complete && e.naturalWidth > 0', arg=img.element_handle())")
s=s.replace("'all 5 anchors passed'","'all 6 anchors passed'")
s=s.replace("page.locator('.button[download]').click()","page.locator('.button[download]').click()")
s=s.replace("page.screenshot(path=", "page.screenshot(path=")
p.write_text(s,encoding='utf-8')
