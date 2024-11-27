
import pygame

pygame.init()

# Creates default font
main_font = pygame.font.SysFont("cambira", 25)

class Button():
  def __init__(self, xPos, yPos, textInput, width=60 , height=60, textCol = "white", buttonCol = "dark gray", font = main_font):
    # Initialises attributes
    self.xPos = xPos
    self.yPos = yPos
    self.textCol = textCol
    self.buttonCol = buttonCol
    self.font = font
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

