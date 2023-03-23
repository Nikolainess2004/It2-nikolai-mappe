import pygame as pg

class Spiller:
    def __init__(self):
        self._x=20
        self._y=20

    def tegn(self, vindu):
            pg.draw.circle(vindu, (100,50,140), (100,200), 25)