import pygame as pg

from spiller import Spiller
from matbit import Matbit


pg.init()
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))

font = pg.font.SysFont("Arial", 24)

spiller1=Spiller()

matbiter=[]

for i in range(20):
    ny_matbit=Matbit()
    matbiter.append(ny_matbit)

fortsett=True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((135, 206, 235))
    
    #tegner alle matbiter
    for matbit in matbiter:
        matbit.tegn(vindu)
    #Oppdater posisjon til spiller
    musX, musY=pg.mouse.get_pos()
    spiller1.oppdater_posisjon(musX, musY)
    #Sjekk om spiller er over en av matbitene
    
    #Tegn spiller
    spiller1.tegn(vindu)

    pg.display.flip() #oppdaterer vinduet

pg.quit()