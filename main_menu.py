
import pygame
import sys
import gui
import simulation

pygame.init()

# Variables for pygame window
res = pygame.Vector2(816,459) #16:9
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()
deltaTime = clock.tick(60)/1000
run = True
backgroundColour = (0, 0, 0)

# Text
titleText = gui.Text(5*res.x/16, res.y/10, "Evolution Simulator", fontSize=50)
speedText = gui.Text(2*res.x/16, 4*res.y/10, "Speed:")
rangeText = gui.Text(2*res.x/16, 6*res.y/10, "Range:")
sizeText = gui.Text(2*res.x/16, 8*res.y/10, "Size:")
valueText = gui.Text(4*res.x/16, 3*res.y/10, "Value")
varianceText = gui.Text(7*res.x/16, 3*res.y/10, "Variance")
texts = [titleText, speedText, rangeText, sizeText, valueText, varianceText]

# Buttons
startButtonText = gui.Text(12*res.x/16, 2*res.y/5, "Start Simulation")
startButton = gui.Button(startButtonText)
quitButtonText = gui.Text(12*res.x/16, 3*res.y/5, "Quit")
quitButton = gui.Button(quitButtonText)
buttons = [startButton, quitButton]

# Sliders
startSpeedSlider = gui.Slider(4*res.x/16, 2*res.y/5, 50, 200)
startRangeSlider = gui.Slider(4*res.x/16, 3*res.y/5, 30, 120)
startSizeSlider = gui.Slider(4*res.x/16, 4*res.y/5, 3, 15)
speedVarianceSlider = gui.Slider(7*res.x/16, 2*res.y/5, 1, 10)
rangeVarianceSlider = gui.Slider(7*res.x/16, 3*res.y/5, 1, 10)
sizeVarianceSlider = gui.Slider(7*res.x/16, 4*res.y/5, 0.2, 2, step=0.2)
sliders = [startSpeedSlider, startRangeSlider, startSizeSlider, speedVarianceSlider, rangeVarianceSlider, sizeVarianceSlider]


def main_menu():
  pygame.display.set_caption("Main Menu")

  while True:
    surface.fill(backgroundColour)
    
    for element in texts + buttons + sliders:
      element.update(surface)
      if type(element) == gui.Slider:
        if element.check_click():
          element.change_pos()

    # Functions for each button
    if startButton.check_click():
      simulation.main()
    
    if quitButton.check_click():
      # Close window
      pygame.quit()
      sys.exit()

    for event in pygame.event.get():
      # Close window
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)



