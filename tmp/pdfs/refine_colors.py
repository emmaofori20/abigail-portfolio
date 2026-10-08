from pathlib import Path
import re,hashlib
p=Path('styles.css'); s=p.read_text(encoding='utf-8')
root=''' :root{--background:#FFFFFF;--surface:#F1F5F9;--hero-background:#101D35;--text:#182538;--text-on-dark:#FFFFFF;--accent:#B42342;--accent-on-dark:#FDA4AF;--border:#D8E0EA;--body:"Segoe UI",Calibri,Arial,sans-serif}'''.strip()
s=re.sub(r':root\{[^}]+\}',root,s,count=1)
for old,new in {'--white':'--background','--ink':'--text','--dark':'--hero-background','--deep':'--surface','--sage':'--accent-on-dark','--muted':'--border','--line':'--border'}.items(): s=s.replace('var('+old+')','var('+new+')')
for c in ['#60665d','#506548','#587447']: s=s.replace(c,'var(--text)' if c=='#60665d' else 'var(--accent)')
for c in ['#bfc3b9','#788174']: s=s.replace(c,'var(--border)')
s=re.sub(r'\.portrait-placeholder[^{}]*\{[^}]*\}','',s)
s=s[:s.index('/* Keep the discipline readable')]
s+='''
/* The display and photograph occupy separate rows; the name begins beside the display. */
.hero{min-height:0;grid-template-columns:1fr 1fr;grid-template-rows:auto auto auto;align-items:start;gap:2rem 4rem;padding:3rem}
.discipline{position:static;grid-column:1;grid-row:1;z-index:auto;font-size:clamp(3.5rem,6.4vw,5.6rem);line-height:.98;letter-spacing:-.05em}
.portrait{grid-column:1;grid-row:2;width:100%;max-width:500px;margin:0;border:1px solid var(--border);overflow:hidden}
.portrait img{display:block;width:100%;height:auto;aspect-ratio:1;object-fit:cover;filter:none}
.hero-copy{grid-column:2;grid-row:1 / span 2;align-self:start;padding:1rem 0 0}
.hero-copy h2{font-size:clamp(2.5rem,4.2vw,4rem)}
.hero-focus{grid-row:3;margin-top:0}
.hero-shell{background:var(--hero-background);color:var(--text-on-dark)}
.role{color:var(--accent-on-dark)}
.button,.button-outline{background:var(--accent);color:var(--text-on-dark);border-color:var(--accent)}
.button:hover,.button-outline:hover{background:var(--text-on-dark);color:var(--accent);border-color:var(--text-on-dark);text-decoration:none}
.button:focus-visible{outline-color:var(--accent-on-dark)}
a:hover{color:var(--accent)}
.hero-shell a:hover,footer a:hover{color:var(--accent-on-dark)}
.hero-shell .button:hover{color:var(--accent)}
a:focus-visible{outline-color:var(--accent)}
.hero-shell a:focus-visible,footer a:focus-visible{outline-color:var(--accent-on-dark)}
.research-band,.contact-band{background:var(--surface);color:var(--text)}
.research-band .section-intro>p,.research-band .source,.themes p,.contact-band .source{color:var(--text)}
.publications-band{background:var(--background);color:var(--text)}
.publications-band .section-intro>p,.publications-band .source,.publication div>p{color:var(--text)}
.publication-status,.context,.status{color:var(--accent)}
.research-band a:focus-visible,.publications-band a:focus-visible,.contact-band a:focus-visible{outline-color:var(--accent)}
footer.wrap{width:100%;padding-inline:max(48px,calc((100% - 1240px)/2));background:var(--hero-background);color:var(--text-on-dark)}
@media(max-width:1050px){.hero{padding:2rem;gap:1.8rem 2.5rem}.hero-copy{padding:.5rem 0 0}.discipline{font-size:clamp(3.1rem,6.4vw,5.6rem)}}
@media(max-width:700px){.hero{padding:1.4rem;gap:1.5rem}.discipline{font-size:clamp(2.9rem,12vw,4.2rem)}.hero-copy{padding:0}.hero-copy h2{font-size:2.5rem}.portrait{max-width:none}.hero-focus{margin-top:0}footer.wrap{padding-inline:20px}}
@media(max-width:360px){.hero{padding:1rem}.discipline{font-size:12vw}footer.wrap{padding-inline:14px}}
@media print{.portrait{display:none}.hero{display:block}.hero-copy{padding:1rem 0}.hero-shell,footer.wrap{background:var(--background);color:var(--text)}}
'''
p.write_text(s,encoding='utf-8')
