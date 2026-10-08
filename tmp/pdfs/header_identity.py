from pathlib import Path
p=Path('index.html'); s=p.read_text(encoding='utf-8'); old='Abigail A. Adjetey Bisa<span>Research portfolio</span>'; assert old in s; s=s.replace(old,'Abigail A. Adjetey Bisa',1); p.write_text(s,encoding='utf-8')
p=Path('styles.css'); s=p.read_text(encoding='utf-8'); s+='\n/* Single-line header identity. */\n.site-header{padding-block:1.25rem}\n.identity{line-height:1.4}\n@media(max-width:700px){.site-header{padding-block:1rem}nav{margin-top:.75rem}}\n'; p.write_text(s,encoding='utf-8')
assert '<span>Research portfolio</span>' not in Path('index.html').read_text(encoding='utf-8')
print('Header subtitle removed; hero heading retained.')
