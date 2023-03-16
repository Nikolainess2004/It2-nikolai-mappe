import pygame as pg
from spiller import Spiller 
from hinder import Hinder
import time

spiller1=Spiller()
hindere=[]

for i in range(3):
    nytt_hinder=Hinder()
    hindere.append(nytt_hinder)

pg.init()
VINDU_BREDDE=500
VINDU_HOYDE=500
vindu=pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

fortsett=True
while fortsett:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            fortsett=False
    
    vindu.fill((255,255,255)) # Farger bakgrunnen hvit

    pg.draw.rect(vindu, (180,40,70), (0,0,200,100))

    for hinder in hindere:
        hinder.flytt_venstre()
        hinder.tegn(vindu)
    spiller1.tegn(vindu)
    pg.display.flip() # Oppdaterer pygame-vinduet, denne MÅ være med
    time.sleep(1/60)
pg.quit() # avslutter pygame
print("Ferdig")

#vindu.fill((rød,grønn,blå)) #andel rød, grønn, blå mellom 0-255

#pg.draw.circle(vindu, (rød,grønn,blå), (x,y), radius)

#pg.draw.rect(vindu, (rød,grønn,blå), (x,y,bredde,høyde))