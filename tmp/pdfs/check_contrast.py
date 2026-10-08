from pathlib import Path
import json
colors={'background':'FFFFFF','surface':'F1F5F9','hero':'101D35','text':'182538','white':'FFFFFF','accent':'B42342','rose':'FDA4AF','border':'D8E0EA'}
def lum(h):
    a=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    a=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in a]
    return sum(v*w for v,w in zip(a,[.2126,.7152,.0722]))
def ratio(a,b):
    x,y=sorted([lum(colors[a]),lum(colors[b])]);return (y+.05)/(x+.05)
for name,a,b,minimum in [('Body on white','text','background',4.5),('Body on grey','text','surface',4.5),('Hero/footer text','white','hero',4.5),('Button text','white','accent',4.5),('Button hover text','accent','white',4.5),('Light-section link hover','accent','surface',4.5),('Dark highlight/hover','rose','hero',4.5),('Light focus','accent','background',3),('Grey focus','accent','surface',3),('Dark focus','rose','hero',3),('Muted hero text','border','hero',4.5)]:
    r=ratio(a,b);assert r>=minimum,(name,r);print(f'{name}: {r:.2f}:1 PASS')
