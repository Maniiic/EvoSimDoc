
import pygame

pygame.init()

class Button():
  def __init__(self, xPos, yPos, textInput, width=0 , height=60, textCol = "white", buttonCol = "dark gray", fontSize = 25, fontStyle = "cambira", bold = False):
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
    self.width = width
    self.height = height

    # Creates a rectangle for the background of the button
    self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
    self.rect.center = (self.xPos, self.yPos)

    # Creates a rectangle for the text contained in the button
    self.textInput = textInput
    self.text = self.font.render(self.textInput, True, self.textCol)
    self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))
  
  def update(self, screen):
    # Draw the button when it is updated
    pygame.draw.rect(screen, self.buttonCol, self.rect, 0, 5)
    screen.blit(self.text, self.textRect)

