import pygame
from pygame.locals import *
import random

'''---------------------------- Player Class ----------------------------'''
# Define a Player Class inheriting from Pygame's Sprite Class
class Player(pygame.sprite.Sprite):
    def __init__(self): 
        super(Player, self).__init__() #Get Super Class
        self.height = 20 #Player Height
        self.width = 20 #Player Width
        self.surface = pygame.image.load("F5S4.png") # load the image of a space ship
        self.surface = pygame.transform.scale(self.surface,(60,100)) # scales image to be the size of my player
        self.rect = self.surface.get_rect() #Turns the surface into a Rectangle 
        self.mask = pygame.mask.from_surface(self.surface) # Masks the surface to the player (allign collider with image)
        self.rect.center = [300,300] # Player Vector
        self.speed = 5 # Player speed 
    
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
        if keys_pressed[K_w]: # Checks if the Player is pressing W Key
            self.rect.y -= self.speed
        if keys_pressed[K_s]:# Checks if the Player is pressing S Key
            self.rect.y += self.speed
        if keys_pressed[K_a]:# Checks if the Player is pressing A Key
            self.rect.x -= self.speed
        if keys_pressed[K_d]:# Checks if the Player is pressing D Key
            self.rect.x += self.speed

        # Border Checking
        if self.rect.top < 0: # Checks if the Player is off the Screen
            self.rect.top = 0 # Keeps Player on Screen
        elif self.rect.bottom > HEIGHT: # Checks if the Player is off the Screen
            self.rect.bottom = HEIGHT # Keeps Player on Screen
        if self.rect.left < 0: # Checks if the Player is off the Screen
            self.rect.left = 0 # Keeps Player on Screen
        elif self.rect.right > WIDTH: # Checks if the Player is off the Screen
            self.rect.right = WIDTH # Keeps Player on Screen

    def fire(self): 
        target = pygame.Vector2(pygame.mouse.get_pos())
        center = pygame.Vector2(self.rect.center)
        diffirence = target-center
        speed = pygame.math.Vector2.normalize(diffirence)*10
        new_bullet = Bullet(self.rect.center,speed)
        all_sprites.add(new_bullet)
        all_bullets.add(new_bullet)

'''---------------------------- Enemy Class ----------------------------'''
# Define an Enemy Class inheriting from Pygame's Sprite Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, center, speed): 
        super(Enemy, self).__init__() #Get Super Class
        self.height = 7 # Enemy Height
        self.width = 30 # Enemy Width
        self.surface = pygame.image.load("Asteroids_32x32_002.png") # load the image of an asteroid
        self.surface = pygame.transform.scale(self.surface,(30,30)) # scales image to be the size of the enemy
        self.rect = self.surface.get_rect() #Turns the surface into a Rectangle 
        self.mask = pygame.mask.from_surface(self.surface) # Masks the surface to the player (allign collider with image)
        self.rect.center = center # Enemy Vector
        self.speed = speed # get the enemy speed
    
    def update(self, keys_pressed): #Enemy Update loop 

        # Enemy Movement
        self.rect.y -= self.speed
        if self.rect.top < 0: # Kills enemy after it leaves the screen 
            self.kill()

'''---------------------------- Bullet Class ---------------------------- '''
# Define a Bullet class inheriting from Pygame's Sprite Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, center, speed): 
        super(Bullet, self).__init__() #Get Super Class
        self.surface = pygame.Surface((5,5))
        self.rect = self.surface.get_rect() #Turns the surface into a Rectangle 
        self.surface.fill("black")
        self.rect.center = center # Bullet Vector
        self.speed = speed # get the Bullet speed

    def update(self, keys_pressed): #Bullet Update loop 
            # Bullet Movement
            self.rect.move_ip(self.speed) 
            if self.rect.bottom > HEIGHT or self.rect.top < 0 or self.rect.left > WIDTH or self.rect.right < 0: # Kills Bullet after it leaves the screen 
                self.kill()

pygame.init()

'''---------------------------- Define Variables ----------------------------'''
#Define Screen Size
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # define a screen with the predefined width and height
background = pygame.image.load("Purple Nebula 8 - 512x512.png") # define a background using the image of a purple nebula 
background = pygame.transform.scale(background,(WIDTH,HEIGHT)) # Scales the background to fill the screen

my_font = pygame.font.SysFont(pygame.font.get_default_font(), 50) # define a font to use for text
game_over_text = my_font.render('Game Over', False, (0, 0, 0)) # define my game over text 

clock = pygame.time.Clock() # define a clock to use ingame
explosion_sound = pygame.mixer.Sound("medium-explosion-40472.wav") # define an explosion sound 

player = Player() # Initiate The Player

add_enemy = pygame.USEREVENT + 1 # Add the add_enemy event
pygame.time.set_timer(add_enemy, 100) # Create a timer so every .5 s the add_enemy event is broardcast

#Finds all sprites and puts them in a list
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Find All enemies and put them in a list
all_enemies = pygame.sprite.Group()

# Find All bullers and put them in a list
all_bullets = pygame.sprite.Group()

'''---------------------------- Game Loop ----------------------------'''
running = True
waiting = True
while running: #Checks if game is running
    for event in pygame.event.get(): #Checks for events 
        if event.type == QUIT:
            running = False #Quits Loop
            waiting = False #Skips the end loop
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False #Quits Loop
                waiting = False #Skips the end loop
        if event.type == add_enemy:
            enemy = Enemy((random.randint(0,WIDTH),HEIGHT+100), random.randint(2,7)) 
            all_sprites.add(enemy) # add the enemy to the list of all sprites
            all_enemies.add(enemy) # add the enemy to the list of all enemies 
        if event.type == MOUSEBUTTONDOWN:
            player.fire()

    keys = pygame.key.get_pressed() #Creates a Dictionary for every button / key and if its pressed
    for sprite in all_sprites: # updates every sprite
        sprite.update(keys) 

    screen.blit(background,(0,0)) # loads the background 

    for sprite in all_sprites: # Draws All Sprites onto the screen
        screen.blit(sprite.surface, sprite.rect)

    if pygame.sprite.spritecollideany(player,all_enemies): # checks if the player is colliding with any asteroids 
        if pygame.sprite.spritecollide(player,all_enemies,False,pygame.sprite.collide_mask): # Checks if the player mask is overlaping with the asteroid mask 
            explosion_sound.play() # Plays the explosion sound
            running = False # Exits the game (game over)
    
    for enemy in all_enemies:
        if pygame.sprite.spritecollide(enemy,all_bullets,True,):
            explosion_sound.play()
            #enemy.kill()

            

    pygame.display.update() #Updates The Game Window
    clock.tick(60) # Creates a framerate

'''---------------------------- Game Over Process ----------------------------'''
while waiting: # wait for the player to quit the game
    for event in pygame.event.get(): # Checks if the player has pressed escape or the quit button
        if event.type == QUIT:
                waiting = False #Quits Loop
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                waiting = False #Quits Loop

    screen.blit(game_over_text, (WIDTH/2,HEIGHT/2)) # loads the game over text in the centre of the screen 
    pygame.display.update() 
pygame.quit() #Quits Pygame When the Loop is Exited
