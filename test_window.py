
import pygame
import sys
import gui

pygame.init()

# Variables for pygame window
res = pygame.Vector2(816,459) #16:9
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()
deltaTime = clock.tick(60)/1000
run = True
backgroundColour = (0, 0, 0)

# Text
testText = gui.Text(150, 300, "TEST TEXT", fontSize=40)
texts = [testText]

# Buttons
testButtonText1 = gui.Text(res.x/2, res.y/4, "Test")
testButton1 = gui.Button(testButtonText1)
testButtonText2 = gui.Text(res.x/2, res.y/2, "Second Test", textCol="dark gray", fontSize=40, fontStyle="arial")
testButton2 = gui.Button(testButtonText2, buttonCol="white")
testButtonTextQ = gui.Text(80, 80, "Q", fontSize=150)
testButtonQ = gui.Button(testButtonTextQ)
testButtonText3 = gui.Text(res.x/2, 3*res.y/4, "THIRD TEST", fontSize=15, bold=True)
testButton3 = gui.Button(testButtonText3)

buttons = [testButton1, testButton2, testButton3, testButtonQ]

# Graph
def create_graph():
    testGraph = gui.Graph([1,9], [1,2])

pygame.display.set_caption("Test screen")

while True:
    surface.fill(backgroundColour)

    for element in buttons + texts:
        element.update(surface)

    # Functions for each button
    if testButton1.check_click():
        print("Test button 1 clicked")

    if testButton2.check_click():
        print("Test button 2 clicked")

    if testButton3.check_click():
        print("Test button 3 clicked")

    if testButtonQ.check_click():
        create_graph()

    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)