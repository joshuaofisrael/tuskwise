from PIL import Image, ImageDraw, ImageFont
def font(sz,bold=True):
    for f in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        try: return ImageFont.truetype(f,sz)
        except Exception: pass
    return ImageFont.load_default()
def logo(d,cx,cy,s):
    e=lambda x,y,rx,ry,c: d.ellipse([cx+(x-32)*s-rx*s,cy+(y-32)*s-ry*s,cx+(x-32)*s+rx*s,cy+(y-32)*s+ry*s],fill=c)
    e(17,28,13,16,"#7d8b99"); e(47,28,13,16,"#7d8b99"); e(32,26,15,15,"#b8c6d4")
    pts=[(32,34),(32,40),(31.5,46),(33,50),(36,53),(40,53),(43,50)]
    d.line([(cx+(x-32)*s,cy+(y-32)*s) for x,y in pts],fill="#b8c6d4",width=int(7*s),joint="curve")
    for x in (26,38): e(x,24,2,2,"#15191e")
im=Image.new("RGB",(1200,630),"#15191e"); d=ImageDraw.Draw(im)
d.rectangle([0,560,1200,630],fill="#1d232a")
logo(d,230,300,6)
d.text((440,190),"TuskWise",font=font(92),fill="#dbe5ef")
d.text((444,310),"Elephant facts, species, behavior,",font=font(40,False),fill="#c3ccd5")
d.text((444,362),"conservation and ethical viewing",font=font(40,False),fill="#c3ccd5")
d.text((444,440),"Sourced from IUCN, WWF, zoos and research",font=font(28,False),fill="#e3c58a")
d.text((40,578),"Operated by Joshua Israel Ventures LLC",font=font(24,False),fill="#94a1ae")
im.save("og-image.png",optimize=True)
lg=Image.new("RGB",(512,512),"#15191e"); logo(ImageDraw.Draw(lg),256,256,7); lg.save("logo.png",optimize=True)
print("ok")
