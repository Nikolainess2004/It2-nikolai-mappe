from random import randint
import pygame as pg

class Matbit:
    def __init__(self):
        self.x = randint(0,400)
        self.y = randint(0,400)
        self.radius=randint(1,5)
    
    def tegn(self, vindu):
        pg.draw.circle(vindu, (255,0,0), (self.x, self.y), self.radius)