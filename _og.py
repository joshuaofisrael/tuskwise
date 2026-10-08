"""Regenerates og-image.png and logo.png (run from the repo root). Same drawing as LOGO in _build.py and favicon.svg."""
from PIL import Image, ImageDraw, ImageFont
def font(sz,bold=True):
    try: return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""),sz)
    except Exception: return ImageFont.load_default()
def bez(p0,p1,p2,p3,n=120):
    return [tuple((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t**2*c+t**3*d for a,b,c,d in zip(p0,p1,p2,p3)) for t in [i/n for i in range(n+1)]]
def stroke(d,pts,w,c):
    for x,y in pts: d.ellipse([x-w/2,y-w/2,x+w/2,y+w/2],fill=c)
def logo(d,cx,cy,s):
    P=lambda x,y:(cx+(x-32)*s,cy+(y-32)*s)
    e=lambda x,y,rx,ry,c: d.ellipse([*P(x-rx,y-ry),*P(x+rx,y+ry)],fill=c)
    e(17,28,13,16,"#7d8b99"); e(47,28,13,16,"#7d8b99"); e(32,26,15,15,"#b8c6d4")
    # tusks (ivory): same curves as the SVG paths M26 35 C25 41 22 45 18 44 and its mirror
    stroke(d,[P(*q) for q in bez((26,35),(25,41),(22,45),(18,44))],3.6*s,"#f1e6cf")
    stroke(d,[P(*q) for q in bez((38,35),(39,41),(42,45),(46,44))],3.6*s,"#f1e6cf")
    # trunk: M32 34c0 9-1 15 4 19 3 2 7 0 7-3
    tr=bez((32,34),(32,43),(31,49),(36,53))+bez((36,53),(39,55),(43,53),(43,50))[1:]
    stroke(d,[P(*q) for q in tr],7*s,"#b8c6d4")
    for x in (26,38): e(x,24,2,2,"#15191e")
if __name__=="__main__":
    S=3  # supersample for smooth edges
    im=Image.new("RGB",(1200*S,630*S),"#15191e"); d=ImageDraw.Draw(im)
    d.rectangle([0,560*S,1200*S,630*S],fill="#1d232a")
    logo(d,230*S,300*S,6*S)
    d.text((440*S,190*S),"TuskWise",font=font(92*S),fill="#dbe5ef")
    d.text((444*S,310*S),"Elephant facts, species, behavior,",font=font(40*S,False),fill="#c3ccd5")
    d.text((444*S,362*S),"conservation and ethical viewing",font=font(40*S,False),fill="#c3ccd5")
    d.text((444*S,440*S),"Sourced from IUCN, WWF, zoos and research",font=font(28*S,False),fill="#e3c58a")
    d.text((40*S,578*S),"Operated by Joshua Israel Ventures LLC",font=font(24*S,False),fill="#94a1ae")
    im.resize((1200,630),Image.LANCZOS).save("og-image.png",optimize=True)
    lg=Image.new("RGB",(512*S,512*S),"#15191e"); logo(ImageDraw.Draw(lg),256*S,256*S,7*S)
    lg=lg.resize((512,512),Image.LANCZOS); lg.save("logo.png",optimize=True)
    lg.resize((64,64),Image.LANCZOS).save("/tmp/tw_fav_preview.png")
    print("ok")
