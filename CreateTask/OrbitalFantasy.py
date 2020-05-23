# _*_ coding: utf-8 _*_

import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
import numpy as np
import math
import time

from sys import exit

'''Constants'''
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
mNeptune = 1.0247e26
mSaturn = 5.6846e26
# orbital distance of common planets in AU
rJupiter = 778330000000 * auperm  # 5.202 AU
rNeptune = 4503443661000 * auperm
rSaturn = 1433449370000 * auperm
rEarth = 1.

# Initialize PyGame
pygame.init()

# Initialize Files
background_image = 'starfield1000.png'
mouse_image = 'mouse.png'
star_image = 'sun.png'
earthlike_image = 'earthlike.png'
gasgiantblue_image = 'gasgiantblue.png'

earth_image = 'transparent/earth-transparent.png'
jupiter_image = 'transparent/jupiter-transparent.png'
mars_image = 'transparent/mars-transparent.png'
mercury_image = 'transparent/mercury-transparent.png'
moon_image = 'transparent/moon-transparent.png'
neptune_image = 'transparent/neptune-transparent.png'
saturn_image = 'transparent/saturn-transparent.png'
sun_image = 'transparent/sun-transparent.png'
uranus_image = 'transparent/uranus-transparent.png'
venus_image = 'transparent/venus-transparent.png'

# Initialize Colors
white = (0, 0, 0)
red = (128, 0, 0)
green = (0, 128, 0)
black = (255, 255, 255)
blue = (176, 196, 222)

# Initialize Texts
font_30 = pygame.font.SysFont("arial", 30)
font_20 = pygame.font.SysFont("arial", 20)
font_50 = pygame.font.SysFont("arial", 50)

title = font_30.render("Orbital Fantasy V1.1", True, white, black)

# Load Screen
SCREEN_SIZE = (900, 900)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
pygame.display.set_caption("Orbital Fantasy")

# Load images
background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert()
star = pygame.image.load(star_image).convert()
planet_p = pygame.image.load(mercury_image).convert()
planet_q = pygame.image.load(jupiter_image).convert()

# Rects of images
rect_star = star.get_rect()
rect_planet_p = planet_p.get_rect()
rect_planet_q = planet_q.get_rect()

# Side length of images
side_star = rect_star[3]
side_planet_p = rect_planet_p[3]
side_planet_q = rect_planet_q[3]
print(side_star)

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

def drawRectangle(rect):
    pygame.draw.rect(screen, blue, rect, 0)

# def changeScientific(num):
#     if num < 1:
#         print("Error: num smaller than 1")
#     numstr = str(num)
#     deci_index = numstr.find(".")
#     int_part = numstr[0:deci_index]
#     exponent = len(int_part) - 1
#     lowered_num = float(int_part[0] + "." + int_part[1:-1] + numstr[deci_index+1, -1])
#     final = float(str(round(lowered_num, 2)) + "e" + str(exponent))
#     return final

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # The Canvas

    screen.blit(background, (0, 0))  # draw the background
    # screen.blit(title, (10, 0))
    # rect = [left, top, width, height]
    rect_1 = [0, 0, 10, 900]
    rect_2 = [10, 0, 880, 10]
    rect_3 = [10, 890, 880, 10]
    rect_4 = [890, 0, 10, 900]
    rect_5 = [440, 10, 10, 880]
    rect_6 = [10, 440, 880, 10]

    drawRectangle(rect_1)
    drawRectangle(rect_2)
    drawRectangle(rect_3)
    drawRectangle(rect_4)
    drawRectangle(rect_5)
    drawRectangle(rect_6)

    screen.blit(star, (int(230 - side_star / 2), int(230 - side_star / 2)))  # draw XY star
    screen.blit(star, (int(230 - side_star / 2), int(680 - side_star / 2)))  # draw XY star
    screen.blit(star, (int(680 - side_star / 2), int(230 - side_star / 2)))  # draw XY star

    # The texts

    TitleP = font_20.render("Planet P:", True, white, blue)
    TitleQ = font_20.render("Planet Q:", True, white, blue)
    TitleStop = font_20.render("STOP SIMULATION", True, white, red)

    screen.blit(TitleP, (460, 460))
    screen.blit(TitleQ, (460, 640))
    screen.blit(TitleStop, (460, 870))

    screen.blit(planet_p, (460 + 180, 460))
    screen.blit(planet_q, (460 + 180, 640))

    # positionp = planet_p.get_rect()
    # screen.blit(planet_p, positionp)
    # positionq = planet_q.get_rect()
    # screen.blit(planet_q, positionq)

    pygame.display.update()  # and show it all

    tstep = 1.
    tsteps = 86400. * tstep
    tlimit = math.floor(365. / tstep)  # floor() 10.234 -> 10

    for x in range(0, tlimit, 1):

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

        # Update combine acceleration of planet P and Q
        ap = np.sqrt(aPx ** 2 + aPy ** 2 + aPz ** 2)
        aq = np.sqrt(aQx ** 2 + aQy ** 2 + aQz ** 2)

        # Update combine velocity of planet P and Q
        vp = np.sqrt(vpx ** 2 + vpy ** 2 + vpz ** 2)
        vq = np.sqrt(vqx ** 2 + vqy ** 2 + vqz ** 2)

        # Update radius of orbit of planet P and Q
        rp = np.sqrt(xp1 ** 2 + yp1 ** 2 + zp1 ** 2)
        rq = np.sqrt(xq1 ** 2 + yq1 ** 2 + zq1 ** 2)

        # Update net force on planet P and Q
        Fp = ap * mp
        Fq = aq * mq

        # Update total energy of planet P and Q
        Ep = 0.5 * mp * vp ** 2 - G * ms * mp / rp
        Eq = 0.5 * mq * vq ** 2 - G * ms * mq / rq

        # Update specific angular momentum of planet P and Q , h = v x r
        hp = np.sqrt((yp1 * vpz - vpy * zp1) ** 2 + (vpx * zp1 - xp1 * vpz) ** 2 + (xp1 * vpy - vpx * yp1) ** 2)
        hq = np.sqrt((yq1 * vqz - vqy * zq1) ** 2 + (vqx * zq1 - xq1 * vqz) ** 2 + (xq1 * vqy - vqx * yq1) ** 2)

        # Update inclination
        ip = np.arctan(zp1 / np.sqrt(xp1 * xp1 + yp1 * yp1))*180/pi
        iq = np.arctan(zq1 / np.sqrt(xq1 * xq1 + yq1 * yq1))*180/pi

        # Update Eccentricity
        ep = np.sqrt(1 + (2 * (0.5 * vp ** 2 - G * ms / rp)) * (hp / (G * ms)) ** 2)
        eq = np.sqrt(1 + (2 * (0.5 * vq ** 2 - G * ms / rq)) * (hq / (G * ms)) ** 2)

        # Update Time
        t += tsteps

        '''Pygame methods start'''

        # Erase and Re-Draw Canvas
        screen.blit(background, (0, 0))
        # rect = [left, top, width, height]
        rect_1 = [0, 0, 10, 900]
        rect_2 = [10, 0, 880, 10]
        rect_3 = [10, 890, 880, 10]
        rect_4 = [890, 0, 10, 900]
        rect_5 = [440, 10, 10, 880]
        rect_6 = [10, 440, 880, 10]

        drawRectangle(rect_1)
        drawRectangle(rect_2)
        drawRectangle(rect_3)
        drawRectangle(rect_4)
        drawRectangle(rect_5)
        drawRectangle(rect_6)

        screen.blit(star, (int(230 - side_star / 2), int(230 - side_star / 2)))  # draw XY star
        screen.blit(star, (int(230 - side_star / 2), int(680 - side_star / 2)))  # draw XY star
        screen.blit(star, (int(680 - side_star / 2), int(230 - side_star / 2)))  # draw XY star

        screen.blit(TitleP, (460, 460))
        screen.blit(TitleQ, (460, 640))
        screen.blit(TitleStop, (460, 870))

        screen.blit(planet_p, (460 + 180, 460))
        screen.blit(planet_q, (460 + 180, 640))

        #Data
        Mass_P = font_20.render("Mass="+str(round(mp, 2))+"kg", True, white, black)
        Radius_P = font_20.render("Radius="+str(round(rp, 2))+"AU", True, white, black)
        Velocity_P = font_20.render("Velocity="+str(vp)+"AU/s", True, white, black)
        Acceleration_P = font_20.render("Acceleration="+str(ap)+"AU/s^2", True, white, black)
        Force_P = font_20.render("Force="+str(round(Fp, 2))+"kg*AU/s^2", True, white, black)
        Inclination_P = font_20.render("Inclination="+str(round(ip, 4))+"Degrees", True, white, black)
        Eccentricity_P = font_20.render("Eccentricity="+str(round(ep, 4)), True, white, black)
        if Ep < 0:
            TotalEnergy_P = font_20.render("TotalEnergy="+str(round(Ep, 2))+"kg*AU^2/s^2 PLANET IN BOUND!", True, white, black)
        else:
            TotalEnergy_P = font_20.render("TotalEnergy="+str(round(Ep, 2))+"kg*AU^2/s^2 PLANET OUT OF BOUND!", True, white, black)

        Mass_Q = font_20.render("Mass=" + str(round(mp, 2)) + "kg", True, white, black)
        Radius_Q = font_20.render("Radius=" + str(round(rp, 2)) + "AU", True, white, black)
        Velocity_Q = font_20.render("Velocity=" + str(vp) + "AU/day", True, white, black)
        Acceleration_Q = font_20.render("Acceleration=" + str(ap) + "AU/day^2", True, white, black)
        Force_Q = font_20.render("Force=" + str(round(Fp, 2)) + "kg*AU/day^2", True, white, black)
        Inclination_Q = font_20.render("Inclination=" + str(round(ip, 4)) + "Degrees", True, white, black)
        Eccentricity_Q = font_20.render("Eccentricity=" + str(round(ep, 4)), True, white, black)
        if Eq < 0:
            TotalEnergy_Q = font_20.render("TotalEnergy="+str(round(Eq, 2))+"kg*AU^2/s^2 PLANET IN BOUND!", True, white, black)
        else:
            TotalEnergy_Q = font_20.render("TotalEnergy="+str(round(Eq, 2))+"kg*AU^2/s^2 PLANET OUT OF BOUND!", True, white, black)

        screen.blit(Mass_P, (460, 480))
        screen.blit(Radius_P, (460, 500))
        screen.blit(Velocity_P, (460, 520))
        screen.blit(Acceleration_P, (460, 540))
        screen.blit(Force_P, (460, 560))
        screen.blit(Inclination_P, (460, 580))
        screen.blit(Eccentricity_P, (460, 600))
        screen.blit(TotalEnergy_P, (460, 620))

        screen.blit(Mass_Q, (460, 660))
        screen.blit(Radius_Q, (460, 680))
        screen.blit(Velocity_Q, (460, 700))
        screen.blit(Acceleration_Q, (460, 720))
        screen.blit(Force_Q, (460, 740))
        screen.blit(Inclination_Q, (460, 760))
        screen.blit(Eccentricity_Q, (460, 780))
        screen.blit(TotalEnergy_Q, (460, 800))

        positionp_xy = (int(xp1 * 20 + 230 - side_planet_p / 2), int(yp1 * 20 + 230 - side_planet_p / 2))  # move planet
        positionq_xy = (int(xq1 * 20 + 230 - side_planet_q / 2), int(yq1 * 20 + 230 - side_planet_q / 2))  # move planet

        positionp_xz = (int(xp1 * 20 + 230 - side_planet_p / 2), int(zp1 * 20 + 680 - side_planet_p / 2))  # move planet
        positionq_xz = (int(xq1 * 20 + 230 - side_planet_q / 2), int(zq1 * 20 + 680 - side_planet_q / 2))  # move planet

        positionp_yz = (int(yp1 * 20 + 680 - side_planet_p / 2), int(zp1 * 20 + 230 - side_planet_p / 2))  # move planet
        positionq_yz = (int(yq1 * 20 + 680 - side_planet_q / 2), int(zq1 * 20 + 230 - side_planet_q / 2))  # move planet

        screen.blit(planet_p, positionp_xy)  # draw new planet
        screen.blit(planet_q, positionq_xy)  # draw new planet

        screen.blit(planet_p, positionp_xz)  # draw new planet
        screen.blit(planet_q, positionq_xz)  # draw new planet

        screen.blit(planet_p, positionp_yz)  # draw new planet
        screen.blit(planet_q, positionq_yz)  # draw new planet

        pygame.display.update()  # and show it all
        pygame.time.delay(10)
