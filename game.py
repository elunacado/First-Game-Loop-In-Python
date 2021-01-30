import pygame

# Initialize the Game
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# Game Loop so the window wont close 
running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False