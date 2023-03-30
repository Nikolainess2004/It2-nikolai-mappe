import pygame as pg
from ball import Ball

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen hvit
    vindu.fill((255, 255, 255))

    # Tegner en sirkel
    pg.draw.circle(vindu, (255, 0, 0), (100, 250), 50)
    # Tegner et rektangel
    pg.draw.rect(vindu, (0, 255, 0), (200, 250, 70, 90))
    # Tegner en ellipse
    pg.draw.ellipse(vindu, (0, 0, 255), (300, 250, 90, 60))
    # Tegner en linje
    pg.draw.line(vindu, (200, 0, 200), (400, 100), (420, 400), 5)

    # Lager en tekst i form av et bilde og legger til bildet i vinduet
    bilde = font.render("Heisann!", True, (50, 50, 50))
    vindu.blit(bilde, (400, 20))

    # Tegner og flytter ballen
    ball.tegn()
    ball.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()



import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_x = 50
player_y = 100

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", (player_x, player_y), 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()




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