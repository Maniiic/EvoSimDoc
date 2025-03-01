
#Imports
import pygame
import sys
import gui

#Constants
black = (0, 0, 0)
yellow = (255,255,0)
white = (255,255,255)

#Variables for pygame window
res = pygame.Vector2(816,459) #16:9
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()
backgroundColour = black



# Text
titleText = gui.Text(res.x/2, res.y/10, "Analysis", fontSize=50)
texts = [titleText]

# Buttons

buttons = []

# Sliders

sliders = []


def main():
  run = True

  #Set title of the window
  pygame.display.set_caption("Analysis")

  while run == True:
    surface.fill(backgroundColour)

    # Draw GUI elements
    for element in texts + buttons + sliders:
      element.update(surface)
      if type(element) == gui.Slider:
        if element.check_click():
          element.change_pos()

    #Close window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)



