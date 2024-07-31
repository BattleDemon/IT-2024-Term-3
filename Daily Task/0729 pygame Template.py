import pygame
from pygame.locals import *

pygame.init()

#Define Screen Size
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

running = True

# Game Loop
while running: #Checks if game is running
    for event in pygame.event.get(): #Checks for events 
        if event.type == QUIT:
            running = False #Quits Loop
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False #Quits Loop
    screen.fill("white")

    pygame.display.update() #Updates The Game Window

pygame.quit() #Quits Pygame When the Loop is Exited