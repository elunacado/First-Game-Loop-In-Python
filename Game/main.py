import pygame

# Initialize the Game
pygame.init()

# create screen
screen = pygame.display.set_mode((600,600))

#Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY= 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop so the window wont close
running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    #RGB - Red-Green-Blue
    screen.fill((0, 0, 0))

    player()
    pygame.display.update()
