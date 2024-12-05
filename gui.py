
import pygame

pygame.init()

class Button():
  def __init__(self, xPos, yPos, textInput, width=0 , height=0, textCol = "white", buttonCol = "dark gray", fontSize = 25, fontStyle = "cambira", bold = False):
    # Initialises attributes
    self.xPos = xPos
    self.yPos = yPos
    self.textCol = textCol
    self.buttonCol = buttonCol
    self.fontSize = fontSize
    self.fontStyle = fontStyle
    self.bold = bold
    self.font = pygame.font.SysFont(self.fontStyle, self.fontSize, bold = self.bold)

    # Sets the width to be based on the length of the text if not specified
    if width == 0:
      width = self.fontSize/2 * len(textInput)
    if height == 0:
      height = self.fontSize + 10
    self.width = width
    self.height = height

    # Creates a rectangle for the background of the button
    self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
    self.rect.center = (self.xPos, self.yPos)

    # Creates a rectangle for the text contained in the button
    self.textInput = textInput
    self.text = self.font.render(self.textInput, True, self.textCol)
    self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))

    # Used to check if mouse is clicked once
    self.canClick = True
  
  def update(self, screen):
    # Draw the button when it is updated
    pygame.draw.rect(screen, self.buttonCol, self.rect, 0, 5)
    screen.blit(self.text, self.textRect)
  
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
  def __init__(self, xPos, yPos, min, max, width=100 , height=20):
    #Initialises attributes
    self.xPos = xPos
    self.yPos = yPos
    self.min = min
    self.max = max
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

  def checkHover(self):
    mousePos = pygame.mouse.get_pos()

    # Returns True when cursor is over track
    if self.rectTrack.collidepoint(mousePos):
      return True

  def move(self):
    # Moves the slider when clicked / dragged
    mousePos = pygame.mouse.get_pos()
    leftClick = pygame.mouse.get_pressed()[0]

    # Gets the position of each side of the thumb
    rightAdjustedPos = [mousePos[0] + self.rectThumb.width/2, mousePos[1]]
    leftAdjustedPos = [mousePos[0] - self.rectThumb.width/2, mousePos[1]]

    # Check where its clicked and move thumb
    if self.checkHover() and leftClick:
      if self.rectTrack.collidepoint(rightAdjustedPos) == False:
        self.rectThumb.centerx = self.rectTrack.right - self.rectThumb.width/2
      elif self.rectTrack.collidepoint(leftAdjustedPos) == False:
        self.rectThumb.centerx = self.rectTrack.left + self.rectThumb.width/2
      else:
        self.rectThumb.centerx = mousePos[0]
      
      print(self.changeVal())

  def changeVal(self):
    # Update the current value
    range = self.max - self.min
    effectiveWidth = self.rectTrack.width - self.rectThumb.width
    distance = self.rectThumb.left - self.rectTrack.left
    scale = distance / effectiveWidth
    self.currentVal = self.min + scale * range
    return self.currentVal


