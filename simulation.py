
# Imports
import sys
import pygame
import math
import random
import analysis

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

# Pygame event
CREATE_FOOD = pygame.USEREVENT + 1
COLLECT_DATA = pygame.USEREVENT + 2

#Food and creatures will inherit from entity class
class Entity:
  def __init__(self, col, size):
    #Spawn with a random position on the screen, 
    self.pos = random_vector()
    self.col = col
    self.size = size
    
  def draw(self):
    # Draws the objects on the pygame screen
    pygame.draw.circle(surface, self.col, self.pos, self.size)

class Consumer(Entity):
  def __init__(self, pos, speed, range, size):
    super().__init__((255, 255, 255), size + random.uniform(-sizeVariance,sizeVariance)) # Attributes shared by classes
    self.pos = pos
    self.path = random_vector()
    self.energy = 100

    # Initial traits
    self.speed = speed + random.randint(-speedVariance, speedVariance)
    self.range = range + random.randint(-senseVariance, senseVariance)


  def update(self):
    self.update_vel()
    self.update_pos()
    self.update_eating()
    self.update_energy()
      
  def update_vel(self):
    smallest = math.inf
    preyList = self.make_prey_list()

    # Check if creature has reached its destination
    if self.pos.distance_to(self.path) <= self.size:
      self.path = random_vector()
    
    # Check for closest thing to eat
    for food in foods:
      smallest = self.path_finding(food,smallest)
    for prey in preyList:
      smallest = self.path_finding(prey,smallest)

    # Calculate velocity
    self.vel = pygame.Vector2(self.path - self.pos).normalize()*self.speed*deltaTime

  def update_pos(self):
    # Changes the position based on the current velocity
    self.pos = self.pos + self.vel

  def path_finding(self, target: Entity, smallest):
    # Sets the path to the closest target
    distance = self.pos.distance_to(target.pos)
    if distance < smallest:
      smallest = distance
    if distance <= self.range and distance == smallest:
      self.path = target.pos
    return smallest

  def update_eating(self):
    # Check if food can be eaten
    for food in foods:
      if self.pos.distance_to(food.pos) <= self.size:
        foods.remove(food)
        self.consumer_ate()

    # Check if prey can be eaten
    preyList = self.make_prey_list()
    for prey in preyList:
      if self.pos.distance_to(prey.pos) <= self.size:
        consumers.remove(prey)
        self.consumer_ate()

  def make_prey_list(self): 
    # Adds the creatures that are small enough to the list to be eaten
    preyList = []
    for consumer in consumers:
      if self.size > 1.25 * consumer.size:
        preyList.append(consumer)
    return preyList

  def consumer_ate(self):
    # Replenish some energy
    self.energy += 50
    # Might create a new creature
    if random.randint(1,reproductionChance) == 1:
      consumers.append(Consumer(self.pos, self.speed, self.range, self.size))

  def update_energy(self):
    # Decrease energy over time
    self.energy -= 0.25

    # Kills creature
    if self.energy <= 0:
      consumers.remove(self)

class Food(Entity):
  def __init__(self):
    super().__init__(yellow, 10)

def random_vector():
  # Generates a random vector position within the window
  return pygame.Vector2(random.randint(margin, int(res.x) - margin), random.randint(margin, int(res.y - margin)))

def average_trait(trait):
  total = sum(getattr(consumer, trait) for consumer in consumers)
  averageValue = total/len(consumers)
  roundedValue = round(averageValue, -int(math.floor(math.log10(averageValue))) + 2)
  return roundedValue

def main(startSpeed, startRange, startSize, startSpeedVariance, startSenseVariance, startSizeVariance, startReproductionChance= 2, consumerAmount=5, foodAmount=5):
  global foods, consumers, speedVariance, senseVariance, sizeVariance, reproductionChance # Add all future global variables
  speedVariance = startSpeedVariance
  senseVariance = startSenseVariance
  sizeVariance = startSizeVariance
  reproductionChance = startReproductionChance # 1 / reproductionChance

  # Event Delays
  foodDelay = 1000
  dataDelay = 1000

  # Analysis Lists
  averageSpeeds = []
  averageSizes = []
  averageRanges = []

  run = True

  # Creates the inital list for creatures and food
  foods = [Food() for _ in range(foodAmount)]
  consumers = [Consumer(random_vector(), startSpeed, startRange, startSize) for _ in range(consumerAmount)]

  # Start pygame events

  # Food generation
  pygame.time.set_timer(CREATE_FOOD, foodDelay)
  # Data collection
  pygame.event.post(pygame.event.Event(COLLECT_DATA))

  #Set title of the window
  pygame.display.set_caption("Simulation")

  #Main Loop
  while run == True:
    surface.fill(backgroundColour)

    #Close window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      # Continues generating food every so often
      if event.type == CREATE_FOOD:
        foods.append(Food())
        foodDelay += 10
        pygame.time.set_timer(CREATE_FOOD, foodDelay)

      # Collect the mean value of each trait every so often
      if event.type == COLLECT_DATA:
        averageSpeeds.append(average_trait("speed"))
        averageSizes.append(average_trait("size"))
        averageRanges.append(average_trait("range"))

        pygame.time.set_timer(COLLECT_DATA, dataDelay)

    # Combines the list of entities
    entities = foods + consumers # Add all future entities

    # Check if all creatures died
    if len(consumers) == 0:
      run = False
      analysis.main(averageSpeeds, averageSizes, averageRanges, dataDelay)

    #Iterates through each entity
    for entity in entities:
      # Draws each entity
      entity.draw()
      
      #For each consumer
      if type(entity) == Consumer:
        entity.update()

    pygame.display.update()
    clock.tick(60)
