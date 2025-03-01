
#Imports
import pygame
import sys
import gui
import matplotlib.pyplot as plt
import numpy as np


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

# # Buttons
# generateSpeedGraphText = gui.Text(res.x/3, res.y/3, "Speed Graph", fontSize=40, textCol="black")
# generateSpeedGraphButton = gui.Button(generateSpeedGraphText, buttonCol="green")
# generateSizeGraphText = gui.Text(2*res.x/3, res.y/3, "Size Graph", fontSize=40, textCol="black")
# generateSizeGraphButton = gui.Button(generateSizeGraphText, buttonCol="lightblue")
# generateRangeGraphText = gui.Text(res.x/2, 2*res.y/3, "Range Graph", fontSize=40, textCol="black")
# generateRangeGraphButton = gui.Button(generateRangeGraphText, buttonCol="yellow")
# buttons = [generateSpeedGraphButton, generateSizeGraphButton, generateRangeGraphButton]

# Buttons

buttons = []

def graph(yPoints, yAxis, dataDelay):
  xPoints = []
  for n in range(len(yPoints)):
    xPoints.append(dataDelay*n/1000)
  yPoints = np.array(yPoints)
  xPoints = np.array(xPoints)

  # Find line of best fit
  m, c = np.polyfit(xPoints, yPoints, 1)

  plt.scatter(xPoints, yPoints)
  plt.plot(xPoints, m*xPoints+c)
  plt.xlabel("Time / s")
  plt.ylabel(yAxis)
  plt.show()


def main(speeds, sizes, ranges, dataDelay):
  run = True

  # Graphs
  graph(speeds, "Speed", dataDelay)
  graph(sizes, "Size", dataDelay)
  graph(ranges, "Range", dataDelay)


  #Set title of the window
  pygame.display.set_caption("Analysis")

  while run == True:
    surface.fill(backgroundColour)

    # Draw GUI elements
    for element in texts + buttons:
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
