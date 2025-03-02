
#Imports
import pygame
import sys
import main_menu
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

# Buttons
generateSpeedGraphText = gui.Text(res.x/3, res.y/3, "Speed Graph", fontSize=40, textCol="black")
generateSpeedGraphButton = gui.Button(generateSpeedGraphText, buttonCol="green", width=220, height=50)
generateSizeGraphText = gui.Text(2*res.x/3, res.y/3, "Size Graph", fontSize=40, textCol="black")
generateSizeGraphButton = gui.Button(generateSizeGraphText, buttonCol="cyan", width=220, height=50)
generateRangeGraphText = gui.Text(res.x/3, 2*res.y/3, "Range Graph", fontSize=40, textCol="black")
generateRangeGraphButton = gui.Button(generateRangeGraphText, buttonCol="yellow", width=220, height=50)
restartText = gui.Text(2*res.x/3, 2*res.y/3, "Restart", fontSize=40, textCol="black")
restartButton = gui.Button(restartText, buttonCol="white", width=220, height=50)
buttons = [generateSpeedGraphButton, generateSizeGraphButton, generateRangeGraphButton, restartButton]


def graph(yPoints, yAxis, dataDelay):
  xPoints = []
  for n in range(len(yPoints)):
    xPoints.append(dataDelay*n/1000)
  yPoints = np.array(yPoints)
  xPoints = np.array(xPoints)

  # Find line of best fit
  m, c = np.polyfit(xPoints, yPoints, 1)

  plt.figure(num=(yAxis + " vs Time"))
  plt.scatter(xPoints, yPoints)
  plt.plot(xPoints, m*xPoints+c)
  plt.xlabel("Time / s")
  plt.ylabel(yAxis)
  plt.show()


def main(speeds, sizes, ranges, dataDelay):
  run = True

  #Set title of the window
  pygame.display.set_caption("Analysis")

  while run == True:
    surface.fill(backgroundColour)

    # Draw GUI elements
    for element in texts + buttons:
      element.update(surface)

    # Button checks
    if generateSpeedGraphButton.check_click():
      graph(speeds, "Speed", dataDelay)
    if generateSizeGraphButton.check_click():
      graph(sizes, "Size", dataDelay)
    if generateRangeGraphButton.check_click():
      graph(ranges, "Range", dataDelay)
    if restartButton.check_click():
      main_menu.main()

    #Close window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)
