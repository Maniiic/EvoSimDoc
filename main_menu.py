
import pygame
import sys
import gui

# Variables for pygame window
res = pygame.Vector2(816,459) #16:9
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()
deltaTime = clock.tick(60)/1000
run = True
backgroundColour = (0, 0, 0)

# Buttons
testButton1 = gui.Button(res.x/2, res.y/4, "Test")
testButton2 = gui.Button(res.x/2, res.y/2, "Second Test")

def main_menu():
  pygame.display.set_caption("Test screen")

  while True:
    surface.fill(backgroundColour)
    testButton1.update(surface)

    for event in pygame.event.get():
      # Close window
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)

