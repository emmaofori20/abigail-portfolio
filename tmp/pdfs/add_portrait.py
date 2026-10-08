from pathlib import Path
import re
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=re.sub(r'    <div class="portrait-placeholder".*?</div>\s*<!-- Replace.*?-->', '''    <figure class="portrait"><img src="assets/portrait.jpg" width="400" height="400" alt="Abigail A. Adjetey Bisa, seated with her arms folded, wearing a red top."></figure>''',s,flags=re.S)
p.write_text(s,encoding='utf-8')
p=Path('styles.css'); s=p.read_text(encoding='utf-8-sig').replace('--sage:#bcc9b6','--sage:#ef8791')
s+='''\n/* Actual researcher portrait: a small overlap with the display, clear of the introduction. */
.portrait{grid-column:1;grid-row:1;width:85%;margin-top:14rem;position:relative;z-index:1;border:1px solid #788174;overflow:hidden}
.portrait img{display:block;width:100%;height:auto;aspect-ratio:1;object-fit:cover}
@media(max-width:1050px) and (min-width:701px){.portrait{width:92%;margin-top:15rem}}
@media(max-width:700px){.portrait{width:100%;margin-top:0;flex-shrink:0}.portrait img{aspect-ratio:1}}
@media print{.portrait{display:none}}
'''
p.write_text(s,encoding='utf-8')
