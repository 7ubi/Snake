import pygame
import random

pygame.init()

rows = 20
cols = 20
gridS = 30

width = rows * gridS
height = cols * gridS

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

snakes = []
apple = None

class Food:
    def __init__(self):
        self.x = random.randint(0, rows - 1) * gridS
        self.y = random.randint(0, cols - 1) * gridS
    
    def show(self):
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.x, self.y, gridS, gridS))

class snake:
    def __init__(self):
        self.x = rows/2 * gridS
        self.y = cols/2 * gridS
        self.dirX = 1
        self.dirY = 0
  
    def updateHead(self):
        self.x += self.dirX * gridS
        self.y += self.dirY * gridS

    def updateTale(self, newX, newY):
        self.x = newX
        self.y = newY
    
    def show(self):
        pygame.draw.rect(screen, pygame.Color(0, 255, 0), (self.x, self.y, gridS, gridS), 0)

def gameLoop():
    snakes = []
    snakes.append(snake())
    apple = Food()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snakes[0].dirX = 0
                    snakes[0].dirY = -1
                if event.key == pygame.K_s:
                    snakes[0].dirX = 0
                    snakes[0].dirY = 1
                if event.key == pygame.K_d:
                    snakes[0].dirX = 1
                    snakes[0].dirY = 0
                if event.key == pygame.K_a:
                    snakes[0].dirX = -1
                    snakes[0].dirY = 0

        screen.fill(pygame.Color(125, 125, 125))

        if len(snakes) > 1:
            for i in range(len(snakes) - 1, 0, -1):
                snakes[i].updateTale(snakes[i - 1].x, snakes[i - 1].y)
                snakes[i].show()
        snakes[0].updateHead()
        snakes[0].show()
        
        if snakes[0].x == apple.x and snakes[0].y == apple.y:
            snakes.append(snake())
            apple = Food()

        #check for collision
        for i in range(1, len(snakes)):
            if snakes[0].x == snakes[i].x and snakes[0].y == snakes[i].y:
                gameLoop()
        
        if snakes[0].x < -gridS or snakes[0].x > width or snakes[0].y < -gridS or snakes[0].y > height:
            gameLoop()

        apple.show()

        pygame.display.update()
        clock.tick(5)



gameLoop()