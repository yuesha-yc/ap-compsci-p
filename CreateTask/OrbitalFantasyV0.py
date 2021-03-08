# _*_ coding: utf-8 _*_

import math
from sys import exit

import numpy as np
import pygame
from pygame.locals import *

# Initialize Constants
# pi
pi = 3.14159
# gravitational constant AU^2/kg s^2
G = 1.976e-44
# Astronomical Unit per meter
auperm = 1. / 1.496e11
# mass of common stars in kg
mSun = 1.98e30
# mass of common planets in kg
mJupiter = 1.90e27
mEarth = 5.97e24
# orbital distance of common planets in AU
rJupiter = 778330000000 * auperm  # 5.202 AU
# rJupiter = 1.1
rEarth = 1.

# Initialize PyGame
pygame.init()

# Initialize Files
background_image_filename = 'starfield.png'
mouse_image_filename = 'mouse.png'
star_image_filename = 'transparent/arcturus.png'
planet_p_image_filename = 'earthlike.png'
planet_q_image_filename = 'gasgiantblue.png'

# Initialize Texts
my_font = pygame.font.SysFont("arial", 40)
title = my_font.render("Orbital Fantasy V1.0 Beta\nDo not resize window!", True, (0, 0, 0), (255, 255, 255))

# Load Screen
SCREEN_SIZE = (800, 800)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
pygame.display.set_caption("Orbital Fantasy V1.0 Beta")

# Load images
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert()
star = pygame.image.load(star_image_filename).convert()
planet_p = pygame.image.load(planet_p_image_filename).convert()
planet_q = pygame.image.load(planet_q_image_filename).convert()

# mass of the star
ms = mSun
# mass of planet p
mp = mEarth
# mass of planet q
mq = mJupiter

# radius of planet p
rp = rEarth
# radius of planet q
rq = rJupiter

# Current coordination of the planet p
xp1 = rp * 0.99
yp1 = rp * 0.01
zp1 = np.sqrt(rp ** 2 - xp1 ** 2 - yp1 ** 2)

# Current coordination of the planet q
xq1 = rq * 0.99
yq1 = rq * 0.01
zq1 = np.sqrt(rq ** 2 - xq1 ** 2 - yq1 ** 2)

# Current velocity of the planet p         vpy = sqrt(GM/4)
vpx = 0.
vpy = np.sqrt((G * ms) / rp) * 0.99
vpz = np.sqrt((G * ms) / rp - vpy ** 2)
vp = np.sqrt(vpx ** 2 + vpy ** 2 + vpz ** 2)

# Current velocity of the planet q         vpy = sqrt(GM/4)
vqx = 0.
vqy = np.sqrt((G * ms) / rq) * 0.99
vqz = np.sqrt((G * ms) / rq - vqy ** 2)
vq = np.sqrt(vqx ** 2 + vqy ** 2 + vqz ** 2)

# Specific Angular Momentum of planet P and Q
hp = np.sqrt((yp1 * vpz - vpy * zp1) ** 2 + (vpx * zp1 - xp1 * vpz) ** 2 + (xp1 * vpy - vpx * yp1) ** 2)
hq = np.sqrt((yq1 * vqz - vqy * zq1) ** 2 + (vqx * zq1 - xq1 * vqz) ** 2 + (xq1 * vqy - vqx * yq1) ** 2)

# Total energy of planet P and Q
Ep = 0.5 * mp * vp ** 2 - G * ms * mp / rp
Eq = 0.5 * mq * vq ** 2 - G * ms * mq / rq

# Time
t = 0.

tstep = 1.
tsteps = 86400. * tstep
tlimit = math.floor(365. / tstep)  # floor() 10.234 -> 10

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))  # draw the background
    screen.blit(title, (0, 0))  # draw the text
    screen.blit(star, (380, 380))  # draw star

    positionp = planet_p.get_rect()
    screen.blit(planet_p, positionp)  # draw the player

    positionq = planet_q.get_rect()
    screen.blit(planet_q, positionq)  # draw the player

    pygame.display.update()  # and show it all

    for x in range(0, tlimit, 1):  # animate 100 frames

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # Distance from P to S
        Dps = np.sqrt(xp1 ** 2 + yp1 ** 2 + zp1 ** 2)
        # Distance from P to Q
        Dpq = np.sqrt((xp1 - xq1) ** 2 + (yp1 - yq1) ** 2 + (zp1 - zq1) ** 2)
        # Distance from Q to S
        Dqs = np.sqrt(xq1 ** 2 + yq1 ** 2 + zq1 ** 2)

        # Update acc of planet P due to S and Q
        aPs = G * ms / Dps ** 2
        aPq = G * mq / Dpq ** 2

        # Update acc components of planet P
        aPx = -aPs * xp1 / Dps - aPq * (xp1 - xq1) / Dpq
        aPy = -aPs * yp1 / Dps - aPq * (yp1 - yq1) / Dpq
        aPz = -aPs * zp1 / Dps - aPq * (zp1 - zq1) / Dpq

        # Update acc of planet Q due to S and P
        aQs = G * ms / Dqs ** 2
        aQp = G * mp / Dpq ** 2

        # Update acc components of planet Q
        aQx = -aQs * xq1 / Dqs - aQp * (xq1 - xp1) / Dpq
        aQy = -aQs * yq1 / Dqs - aQp * (yq1 - yp1) / Dpq
        aQz = -aQs * zq1 / Dqs - aQp * (zq1 - zp1) / Dpq

        # Update velocity components of planet P
        vpx = vpx + aPx * tsteps
        vpy = vpy + aPy * tsteps
        vpz = vpz + aPz * tsteps

        # Update velocity components of planet Q
        vqx = vqx + aQx * tsteps
        vqy = vqy + aQy * tsteps
        vqz = vqz + aQz * tsteps

        # Update position components of planet P
        xp1 = xp1 + vpx * tsteps
        yp1 = yp1 + vpy * tsteps
        zp1 = zp1 + vpz * tsteps

        # Update position components of planet Q
        xq1 = xq1 + vqx * tsteps
        yq1 = yq1 + vqy * tsteps
        zq1 = zq1 + vqz * tsteps

        # Update combine velocity of planet P and Q
        vp = np.sqrt(vpx ** 2 + vpy ** 2 + vpz ** 2)
        vq = np.sqrt(vqx ** 2 + vqy ** 2 + vqz ** 2)

        # Update radius of orbit of planet P and Q
        rp = np.sqrt(xp1 ** 2 + yp1 ** 2 + zp1 ** 2)
        rq = np.sqrt(xq1 ** 2 + yq1 ** 2 + zq1 ** 2)

        # Update total energy of planet P and Q
        Ep = 0.5 * mp * vp ** 2 - G * ms * mp / rp
        Eq = 0.5 * mq * vq ** 2 - G * ms * mq / rq

        # Update specific angular momentum of planet P and Q , h = v x r
        hp = np.sqrt((yp1 * vpz - vpy * zp1) ** 2 + (vpx * zp1 - xp1 * vpz) ** 2 + (xp1 * vpy - vpx * yp1) ** 2)
        hq = np.sqrt((yq1 * vqz - vqy * zq1) ** 2 + (vqx * zq1 - xq1 * vqz) ** 2 + (xq1 * vqy - vqx * yq1) ** 2)

        # Update Time
        t += tsteps

        screen.blit(background, (0, 0))  # erase
        screen.blit(star, (380, 380))  # draw star
        screen.blit(title, (0, 0))  # draw the text
        positionp = (int(xp1 * 50 + 400 - 5), int(yp1 * 50 + 400 - 5))  # move player
        positionq = (int(xq1 * 50 + 400 - 5), int(yq1 * 50 + 400 - 5))  # move player

        screen.blit(planet_p, positionp)  # draw new player
        screen.blit(planet_q, positionq)  # draw new player

        pygame.display.update()  # and show it all
        pygame.time.delay(5)
