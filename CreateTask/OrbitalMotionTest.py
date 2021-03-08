# _*_ coding: utf-8 _*_

from sys import exit

import pygame
from pygame.locals import *

background_image_filename = 'background.jpeg'
mouse_image_filename = 'mouse.png'
star_image_filename = 'star.jpeg'
planet_p_image_filename = 'planet_p.png'

# Initialize PyGame
pygame.init()

# Set text
my_font = pygame.font.SysFont("arial", 40)
text_surface = my_font.render("Orbital Fantasy V1.0 Beta", True, (0, 0, 0), (255, 255, 255))
x = -text_surface.get_width()
y = 30

# Create Screen
SCREEN_SIZE = (800, 800)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
pygame.display.set_caption("Orbital Fantasy V1.0 Beta")

# Initialize the images
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert()
star = pygame.image.load(star_image_filename).convert()
player = pygame.image.load(planet_p_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))  # draw the background
    screen.blit(star, (380, 380))  # draw star

    position = player.get_rect()
    print(position)
    screen.blit(player, position)  # draw the player
    pygame.display.update()  # and show it all

    for x in range(100):  # animate 100 frames
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(background, (0, 0))  # erase
        screen.blit(star, (380, 380))  # draw star
        position = position.move(2, 0)  # move player
        screen.blit(player, position)  # draw new player
        pygame.display.update()  # and show it all
        pygame.time.delay(100)
