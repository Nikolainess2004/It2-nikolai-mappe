from random import randint
import pygame as pg

class Spiller:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.fartX = 0
        self.fartY = 0
        self.radius=20
    def beveg_opp(self):
        self.y += 1
    def beveg_ned(self):
        self.y -= 1
    def beveg_venstre(self):
        self.x -= 1
    def beveg_hoyre(self):
        self.x += 1
    def tegn(self, vindu):
        pg.draw.circle(vindu, (0,255,0), (self.x, self.y), self.radius)
        bilde=pg.image.load("agario/durek.png")
        bilde=pg.transform.scale(bilde, (40,40))
        vindu.blit(bilde, (self.x, self.y))

    def oppdater_posisjon(self, musX, musY):
        print(musX, musY)
        avstandX=musX-self.x
        avstandY=musY-self.y

        self.fartX=avstandX*0.01
        self.fartY=avstandY*0.01

        self.x+=self.fartX
        self.y+=self.fartY