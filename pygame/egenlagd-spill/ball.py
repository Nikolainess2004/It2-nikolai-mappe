import pygame as pg

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.fart = -self.fart
    
    # Flytter ballen
    self.x += self.fart

# Lager et Ball-objekt
ball = Ball(250, 250, 0.1, 20, vindu)

