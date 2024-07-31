import pygame
from pygame.locals import *
import random

# Define a Player Class inheriting from Pygame's Sprite Class
class Player(pygame.sprite.Sprite):
    def __init__(self): 
        super(Player, self).__init__() #Get Super Class
        self.height = 20 #Player Height
        self.width = 20 #Player Width
        #self.surface = pygame.Surface((self.height,self.width)) # Create a surface for the Player
        self.surface = pygame.image.load("F5S4.png")
        self.surface = pygame.transform.scale(self.surface,(60,100))
        self.rect = self.surface.get_rect() #Turns the surface into a Rectangle 
        #self.surface.fill ("white") # Player Colour
        self.rect.center = [300,300] # Player Vector
        self.speed = 5
    
    def update(self, keys_pressed): #Player Update loop 
        
        # Player Inputs
        if keys_pressed[K_UP]: # Checks if the Player is pressing Up Arrow
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:# Checks if the Player is pressing Down Arrow
            self.rect.y += self.speed
        if keys_pressed[K_LEFT]:# Checks if the Player is pressing Left Arrow
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]:# Checks if the Player is pressing Right Arrow
            self.rect.x += self.speed

        # Border Checking
        if self.rect.top < 0: # Checks if the Player is off the Screen
            self.rect.top = 0 # Keeps Player of Screen
        elif self.rect.bottom > HEIGHT: # Checks if the Player is off the Screen
            self.rect.bottom = HEIGHT # Keeps Player of Screen
        if self.rect.left < 0: # Checks if the Player is off the Screen
            self.rect.left = 0 # Keeps Player of Screen
        elif self.rect.right > WIDTH: # Checks if the Player is off the Screen
            self.rect.right = WIDTH # Keeps Player of Screen


# Define an Enemy Class inheriting from Pygame's Sprite Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, center, speed): 
        super(Enemy, self).__init__() #Get Super Class
        self.height = 7 # Enemy Height
        self.width = 30 # Enemy Width
        #self.surface = pygame.Surface((self.height,self.width)) # Create a surface for the Enemy
        self.surface = pygame.image.load("Asteroids_32x32_002.png")
        self.surface = pygame.transform.scale(self.surface,(30,30))
        self.rect = self.surface.get_rect() #Turns the surface into a Rectangle 
        #self.surface.fill ("red") # Enemy Colour
        self.rect.center = center # Enemy Vector
        self.speed = speed
    
    def update(self, keys_pressed): #Enemy Update loop 

        # Enemy Movement
        self.rect.y -= self.speed
        if self.rect.top < 0:
            self.kill()

pygame.init()

#Define Screen Size
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

clock = pygame.time.Clock()

player = Player() # Initiate The Player

add_enemy = pygame.USEREVENT + 1 # Add the add_enemy event
pygame.time.set_timer(add_enemy, 100) # Create a timer so every .5 s the add_enemy event is broardcast

#Finds all sprites and puts them in a list
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Find All enemies and put them in a list
all_enemies = pygame.sprite.Group()

# Game Loop
running = True
while running: #Checks if game is running
    for event in pygame.event.get(): #Checks for events 
        if event.type == QUIT:
            running = False #Quits Loop
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False #Quits Loop
        if event.type == add_enemy:
            enemy = Enemy((random.randint(0,WIDTH),HEIGHT+100), random.randint(2,7))
            all_sprites.add(enemy)
            all_enemies.add(enemy)

    keys = pygame.key.get_pressed() #Creates a Dictionary for every button / key and if its pressed
    for sprite in all_sprites:
        sprite.update(keys)

    screen.fill("grey")

    for sprite in all_sprites: # Draws All Sprites onto the screen
        screen.blit(sprite.surface, sprite.rect)

    if pygame.sprite.spritecollideany(player,all_enemies):
        running = False

    pygame.display.update() #Updates The Game Window
    clock.tick(60) # Creates a framerate

pygame.quit() #Quits Pygame When the Loop is Exited