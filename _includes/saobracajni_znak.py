# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300)
prozor = pygamebg.open_window(sirina, visina, "Saobraćajni znak")

def jednakostranicni(cx, cy, h, boja):
    a = int(h * 2 / math.sqrt(3))
    A = (cx - a//2, cy + h//3)
    B = (cx + a//2, cy + h//3)
    C = (cx, cy - 2*h//3)
    pg.draw.polygon(prozor, boja, [A, B, C])

prozor.fill(pg.Color("white"))
(cx, cy) = (sirina // 2, 2 *  visina // 3)
jednakostranicni(cx, cy, round(0.8*visina), pg.Color("red"))
jednakostranicni(cx, cy, round(0.55*visina), pg.Color("yellow"))
    
# -*- acsection: main -*-
mis_x, mis_y = 0, 0

def tekst(s, x, y):
    # font kojim će biti prikazan tekst
    font = pg.font.SysFont("Arial", 25)
    tekst = font.render(s, True, pg.Color("black"))
    # određujemo veličinu tog teksta (da bismo mogli da ga centriramo)
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    # položaj određujemo tako da tekst bude centriran
    (x, y) = (x - sirina_teksta * (x / sirina), y - visina_teksta * (y / visina))
    # prikazujemo sličicu na odgovarajućem mestu na ekranu
    prozor.blit(tekst, (x, y))

    
def crtanje():
    prozor.fill(pg.Color("white"))
    (cx, cy) = (sirina // 2, 2 *  visina // 3)
    jednakostranicni(cx, cy, round(0.8*visina), pg.Color("red"))
    jednakostranicni(cx, cy, round(0.55*visina), pg.Color("yellow"))
    pg.draw.line(prozor, pg.Color("black"), (cx-30,cy-30), (cx+30, cy+30), 20)
    pg.draw.line(prozor, pg.Color("black"), (cx-30,cy+30), (cx+30, cy-30), 20)

    pg.draw.line(prozor, pg.Color("black"), (mis_x, 0), (mis_x, visina)) 
    pg.draw.line(prozor, pg.Color("black"), (0, mis_y), (sirina, mis_y)) 
    s = "(" + str(mis_x) + ", " + str(mis_y) + ")"
    pg.display.set_caption(s)

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y
    if dogadjaj.type == pg.MOUSEMOTION:   # miš je pomeren
        mis_x, mis_y = dogadjaj.pos
        return True                         # ponovo iscrtavamo scenu
    return False                            # nema potrebe da iscrtavamo scenu

treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:    # ako je potrebno nacrtati lopticu
        crtanje()
        pg.display.update()        # ažuriramo prikaz sadržaja prozora
        treba_crtati = False

    dogadjaj = pg.event.wait()     # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:   # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

# Zavrsetak skrivenog progrma, koji radi kao primer
pg.time.set_timer(pg.QUIT,50)
pg.time.wait(70)
pg.time.set_timer(pg.QUIT,0)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
