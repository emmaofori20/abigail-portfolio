from pathlib import Path
import functools, hashlib, http.server, threading, json
from playwright.sync_api import sync_playwright
root = Path(__file__).resolve().parents[2]
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f'http://127.0.0.1:{server.server_port}/index.html'
results = []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', headless=True)
    page = browser.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    for width, height in [(1440, 1000), (390, 844), (320, 740)]:
        page.set_viewport_size({'width': width, 'height': height})
        page.goto(url)
        page.evaluate('document.fonts.ready')
        assert page.locator('h1').count() == 1
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Overflow at {width}'
        for img in page.locator('img').all():
            img.scroll_into_view_if_needed()
            page.wait_for_function('(e) => e.complete && e.naturalWidth > 0', arg=img.element_handle())
        for link in page.locator('nav a').all():
            target = link.get_attribute('href')
            assert page.locator(target).count() == 1
            link.click()
            page.wait_for_timeout(450)
            assert page.evaluate('location.hash') == target
        page.goto(url)
        page.keyboard.press('Tab')
        assert page.locator(':focus').inner_text() == 'Skip to content'
        assert page.locator(':focus').evaluate('(e) => e.getBoundingClientRect().top >= 0')
        page.keyboard.press('Enter')
        assert page.locator(':focus').get_attribute('id') == 'main'
        page.keyboard.press('Tab')
        assert page.locator(':focus').evaluate('(e) => getComputedStyle(e).outlineStyle') == 'solid'
        page.goto(url)
        page.screenshot(path=str(root / 'tmp/pdfs' / f'portfolio-{width}.png'), full_page=True)
        results.append({'width':width,'height':height,'overflow':False,'image_loaded':True,'navigation': 'all 6 anchors passed','keyboard':'skip link and visible link focus passed'})
    with page.expect_download() as event:
        page.locator('.portfolio-link[download]').click()
    download = event.value
    assert download.suggested_filename == 'Abigail-Adjetey-Bisa-Research-Portfolio.pdf'
    assert hashlib.sha256(Path(download.path()).read_bytes()).digest() == hashlib.sha256((root/'source/research-portfolio.pdf').read_bytes()).digest()
    assert page.locator('a[href^="mailto:"]').get_attribute('href') == 'mailto:abigailadjeleyadjeteybisa@gmail.com'
    page.emulate_media(reduced_motion='reduce')
    assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior') == 'auto'
    assert not errors, errors
    print(json.dumps({'viewports': results, 'pdf_download':'byte-identical to original', 'mailto':'passed', 'reduced_motion':'passed', 'page_errors':errors}, indent=2))
    browser.close()
server.shutdown()
