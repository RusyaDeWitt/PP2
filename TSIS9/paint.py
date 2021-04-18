import pygame

pygame.init()

width = 1000
height = 1000

color = (0, 255, 0)
BLACK = (0, 0, 0)


surface = pygame.display.set_mode((width,height))

isPressed = False
prevPoint = (0, 0)
currentPoint = (0, 0)

#0 - eraser , 1 - circle , 2 - rectangle
currentTool = 1
toolCount = 3

#0 - GREEN , 1 - BLUE , 2 - RED
currentColor = 1
colorCount = 3

def drawRectangle(surface, x,y, width, height):
    pygame.draw.rect(surface, color, [x,y, width, height], 5)

def drawCircle(surface, x,y):
    pygame.draw.circle(surface, color, (x,y), 5)

def Eraser(surface, x,y):
    pygame.draw.circle(surface, BLACK, (x,y), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                currentTool = (currentTool + 1) % toolCount
            if event.key == pygame.K_c:
                currentColor = (currentColor + 1) % colorCount
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPoint = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            prevPoint = currentPoint
            currentPoint = pygame.mouse.get_pos()

        if currentTool == 0:
            Eraser(surface, prevPoint[0], prevPoint[1])
        elif currentTool == 1:
            drawCircle(surface, prevPoint[0], prevPoint[1])
        elif currentTool == 2:
            drawRectangle(surface, prevPoint[0], prevPoint[1], 50, 50)

        if currentColor == 0:
            color = (0, 255, 0)
        elif currentColor == 1:
            color = (0, 0, 255)
        elif currentColor == 2:
            color = (255, 0, 0)
        pygame.display.flip()