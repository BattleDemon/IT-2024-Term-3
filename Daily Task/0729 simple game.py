from typing import Any
import pygame
from pygame.locals import *

# Define a Player Class inheriting from Pygame's Sprite Class
class Player(pygame.sprite.Sprite):
    def __init__(self): 
        super(Player, self).__init__()
        self.height = 20 #Player Height
        self.width = 20 #PLayer Width
        self.surface = pygame.Surface((self.height,self.width))
        self.rect = self.surface.get_rect()
        self.surface.fill ("black") # Player Colour
        self.x = 300 # Player x
        self.y = 300 # Player y
        self.rect.center = [self.x,self.y] # Player Vector
    
    def update(self, keys_pressed): #
        if keys_pressed[K_UP]:
            self.rect.y -= 1
        if keys_pressed[K_DOWN]:
            self.rect.y += 1
        if keys_pressed[K_LEFT]:
            self.rect.x -= 1
        if keys_pressed[K_RIGHT]:
            self.rect.x += 1

pygame.init()

#Define Screen Size
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

clock = pygame.time.Clock()

player = Player()

#Finds all sprites and puts them in a list
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game Loop
running = True
while running: #Checks if game is running
    for event in pygame.event.get(): #Checks for events 
        if event.type == QUIT:
            running = False #Quits Loop
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False #Quits Loop

    keys = pygame.key.get_pressed() #Creates a Dictionary for every button / key and if its pressed
    for sprite in all_sprites:
        sprite.update(keys)

    screen.fill("white")

    for sprite in all_sprites: # Draws All Sprites onto the screen
        screen.blit(sprite.surface, sprite.rect)

    pygame.display.update() #Updates The Game Window
    clock.tick(60) # Creates a framerate

pygame.quit() #Quits Pygame When the Loop is Exited