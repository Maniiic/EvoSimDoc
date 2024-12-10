
import pygame

pygame.init()

class Text():
  def __init__(self, xPos, yPos, textInput, textCol = "white", fontSize = 25, fontStyle = "cambira", bold = False):
    # Initialises attributes
    self.xPos = xPos
    self.yPos = yPos
    self.textInput = textInput
    self.textCol = textCol
    self.fontSize = fontSize
    self.fontStyle = fontStyle
    self.bold = bold
    self.font = pygame.font.SysFont(self.fontStyle, self.fontSize, bold = self.bold)

    # Creates a rectangle for the text contained in the button
    self.text = self.font.render(self.textInput, True, self.textCol)
    self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))
  
  def update(self, screen: pygame.surface.Surface):
    screen.blit(self.text, self.textRect)
    

class Button():
  def __init__(self, textObj: Text, width=0 , height=0, buttonCol = "dark gray"):
    # Initialises attributes
    self.textObj = textObj
    self.buttonCol = buttonCol
    self.font = pygame.font.SysFont(self.textObj.fontStyle, self.textObj.fontSize, bold = self.textObj.bold)

    # Sets the width to be based on the length of the text if not specified
    if width == 0:
      width = self.textObj.fontSize/2 * len(self.textObj.textInput)
    if height == 0:
      height = self.textObj.fontSize + 10
    self.width = width
    self.height = height

    # Creates a rectangle for the background of the button
    self.rect = pygame.Rect(self.textObj.xPos, self.textObj.yPos, self.width, self.height)
    self.rect.center = (self.textObj.xPos, self.textObj.yPos)

    # Used to check if mouse is clicked once
    self.canClick = True
  
  def update(self, screen: pygame.surface):
    # Draw the button when it is updated
    pygame.draw.rect(screen, self.buttonCol, self.rect, 0, 5)
    screen.blit(self.textObj.text, self.textObj.textRect)
  
  def check_hover(self):
    # Check when the position of the mouse is above the button
    mousePos = pygame.mouse.get_pos()
    if self.rect.collidepoint(mousePos):
      return True
    else:
      return False
    
  def check_click(self):
    # Check when the the button is clicked
    leftClick = pygame.mouse.get_pressed()[0]
    if self.check_hover():
      if leftClick:
        if self.canClick: # Needed to prevent holding the mouse button repeatedly activating function
          self.canClick = False
          return True
        else:
          return False
      else:
        self.canClick = True


class Slider():
  def __init__(self, xPos, yPos, min, max, step=1, width=100 , height=20):
    #Initialises attributes
    self.xPos = xPos
    self.yPos = yPos
    self.min = min
    self.max = max
    self.step = step
    trackWidth = width
    trackHeight = height
    thumbWidth = trackWidth / 10
    thumbHeight = trackHeight

    # Creates a rectangle for the track
    self.rectTrack = pygame.Rect(self.xPos, self.yPos, trackWidth, trackHeight) 
    self.rectTrack.center = (self.xPos, self.yPos)

    # Creates a rectangle for the thumb
    self.rectThumb = pygame.Rect(self.xPos, self.yPos, thumbWidth, thumbHeight)
    self.rectThumb.center = (self.xPos, self.yPos)

  def update(self, screen):
    # Draw the slider when it is updated
    pygame.draw.rect(screen, "dark gray", self.rectTrack)
    pygame.draw.rect(screen, "blue", self.rectThumb)

  def check_click(self):
    # Moves the slider when clicked / dragged
    mousePos = pygame.mouse.get_pos()
    leftClick = pygame.mouse.get_pressed()[0]

    # Check when its clicked
    if self.rectTrack.collidepoint(mousePos) and leftClick:
      return True

  def change_pos(self):
    mousePos = pygame.mouse.get_pos()

    # Gets the position of each side of the thumb
    rightAdjustedPos = [mousePos[0] + self.rectThumb.width/2, mousePos[1]]
    leftAdjustedPos = [mousePos[0] - self.rectThumb.width/2, mousePos[1]]

    # Moves thumb depending on mouse position
    if self.rectTrack.collidepoint(rightAdjustedPos) == False:
      self.rectThumb.centerx = self.rectTrack.right - self.rectThumb.width/2
    elif self.rectTrack.collidepoint(leftAdjustedPos) == False:
      self.rectThumb.centerx = self.rectTrack.left + self.rectThumb.width/2
    else:
      self.rectThumb.centerx = mousePos[0]  
      
    return self.change_val()

  def change_val(self):
    # Update the current value
    range = self.max - self.min
    effectiveWidth = self.rectTrack.width - self.rectThumb.width
    distance = self.rectThumb.left - self.rectTrack.left
    scale = distance / effectiveWidth
    value = self.min + scale * range
    self.currentVal = self.step * round(value / self.step)
    return self.currentVal
