# Imports
import sys
import pygame

#Constants
black = (0, 0, 0)

#Variables for pygame window
res = pygame.Vector2(816,459) #16:9
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()
deltaTime = clock.tick(60)/1000
backgroundColour = black

surface.fill(backgroundColour)
#Main Loop
while True:
  #Close window
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  pygame.display.update()
  clock.tick(60)
