# Imports
import sys
import pygame
import random

#Constants
black = (0, 0, 0)
yellow = (255,255,0)
white = (255,255,255)

#Variables for pygame window
res = pygame.Vector2(816,459) #16:9
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()
deltaTime = clock.tick(60)/1000
backgroundColour = black

#Constants
foodAmount = 5
consumerAmount = 3
margin = 50

#Food and creatures will inherit from entity class
class Entity:
  def __init__(self, col, size):
    #Spawn with a random position on the screen, 
    self.pos = randomVector()
    self.col = col
    self.size = size
    
  def draw(self):
    # Draws the objects on the pygame screen
    pygame.draw.circle(surface, self.col, self.pos, self.size)

class Consumer(Entity):
  def __init__(self):
    super().__init__(white, 10) # Attributes shared by classes

class Food(Entity):
  def __init__(self):
    super().__init__(yellow, 10)

def randomVector():
  # Generates a random vector position within the window
  return pygame.Vector2(random.randint(margin, int(res.x) - margin), random.randint(margin, int(res.y - margin)))

#Initial lists
foods = [Food() for _ in range(foodAmount)]
consumers = [Consumer() for _ in range(consumerAmount)]

#Set title of the window
pygame.display.set_caption("Simulation")

surface.fill(backgroundColour)

#Main Loop
while True:
  #Close window
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Combines the list of entities
  entities = foods + consumers # Add all future entities

  #Iterates through each entity
  for entity in entities:
    # Draws each entity
    entity.draw()

  pygame.display.update()
  clock.tick(60)
