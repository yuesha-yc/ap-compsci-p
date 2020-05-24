"""
|-------------------------------------------------------------------------------
| OrbitalFantasy.py
|-------------------------------------------------------------------------------
|
| Author:  Yichen Wang
| Created: May 25, 2020
|
| This is AP Computer Science Principles - Create Task Programming
| This is a game that allows you to customize three-body planetary motion at three-dimensional scale.
| Newtonian mechanics and gravitational mechanics are used to simulate the motion.
|
"""

import pygame
from pygame.locals import *
import numpy as np
import math

from sys import exit

# Initialize PyGame
pygame.init()

# Initialize Strings
log_message = "[Orbital Fantasy] "

print(
    log_message + "Welcome! Big thank for playing Orbital Fantasy.\n[Orbital Fantasy] Thanks to Python, PyGame and Numpy!")

print(log_message + "Game Initialization Starts...")
pygame.time.delay(100)
print(log_message + "Initializing Planetary Data...10%")
pygame.time.delay(100)
'''DATA'''
# pi
pi = 3.14159
# gravitational constant AU^2/kg s^2
G = 1.976e-44
# Astronomical Unit per meter
auperm = 1. / 1.496e11
# mass of common stars in kg
mSun = 1.98e30
mSirius = 2.06 * mSun
mArcturus = 1.10 * mSun
# radius of common stars in AU
rSun = 1.
rSirius = 1.
rArcturus = 1.
# mass of common planets in kg
mEarth = 5.97e24
mMercury = 0.0553 * mEarth
mVenus = 0.8150 * mEarth
mMars = 0.1074 * mEarth
mJupiter = 1.90e27
mSaturn = 5.68e26
mMoon = mEarth / 81
# orbital distance of common planets in AU
rEarth = 1.
rMercury = 57909100000 * auperm
rVenus = 108209184000 * auperm
rMars = 227936640000 * auperm
rJupiter = 778330000000 * auperm
rSaturn = 1433449370000 * auperm
rMoon = 384403000 * auperm
# images of planets
earth_image = 'transparent/earth-transparent.png'
jupiter_image = 'transparent/jupiter-transparent.png'
mars_image = 'transparent/mars-transparent.png'
mercury_image = 'transparent/mercury-transparent.png'
moon_image = 'transparent/moon-transparent.png'
saturn_image = 'transparent/saturn-transparent.png'
sun_image = 'transparent/sun.png'
venus_image = 'transparent/venus-transparent.png'
sirius_image = 'transparent/sirius.png'
arcturus_image = 'transparent/arcturus.png'

dataMercury = [mMercury, rMercury, mercury_image]
dataVenus = [mVenus, rVenus, venus_image]
dataEarth = [mEarth, rEarth, earth_image]
dataMars = [mMars, rMars, mars_image]
dataJupiter = [mJupiter, rJupiter, jupiter_image]
dataSaturn = [mSaturn, rSaturn, saturn_image]
dataMoon = [mMoon, rMoon, moon_image]
dataSun = [mSun, rSun, sun_image]
dataSirius = [mSirius, rSirius, sirius_image]
dataArcturus = [mArcturus, rArcturus, arcturus_image]

data = {'Mercury': dataMercury, 'Venus': dataVenus, 'Earth': dataEarth, 'Mars': dataMars, 'Jupiter': dataJupiter,
        'Saturn': dataSaturn, 'Moon': dataMoon, 'Sun': dataSun, 'Sirius': dataSirius, 'Arcturus': dataArcturus}

print(log_message + "Initializing images...20%")
pygame.time.delay(100)
# Initialize images
background_image = 'starfield.png'
mouse_image = 'mouse.png'
star_image = 'arcturus.png'
titlepic_image = 'titlepic.png'
button_quit_off_image = 'buttons/button_quit_off.png'
button_quit_on_image = 'buttons/button_quit_on.png'
button_start_off_image = 'buttons/button_start_off.png'
button_start_on_image = 'buttons/button_start_on.png'
button_stop_off_image = 'buttons/button_stop_off.png'
button_stop_on_image = 'buttons/button_stop_on.png'
button_earth_image = 'buttons/earth.png'
button_jupiter_image = 'buttons/jupiter.png'
button_mars_image = 'buttons/mars.png'
button_mercury_image = 'buttons/mercury.png'
button_moon_image = 'buttons/moon.png'
button_saturn_image = 'buttons/saturn.png'
button_sirius_image = 'buttons/sirius.png'
button_sun_image = 'buttons/sun.png'
button_venus_image = 'buttons/venus.png'
button_arcturus_image = 'buttons/arcturus.png'

print(log_message + "Initializing Colors, colors and texts...40%")
pygame.time.delay(100)
# Initialize Colors
white = (0, 0, 0)
red = (128, 0, 0)
green = (0, 128, 0)
black = (255, 255, 255)
blue = (176, 196, 222)

print(log_message + "Initializing Fonts, colors and texts...60%")
pygame.time.delay(100)
# Initialize Fonts
font_30 = pygame.font.SysFont("arial", 30)
font_20 = pygame.font.SysFont("arial", 20)
font_50 = pygame.font.SysFont("arial", 50)
font_25 = pygame.font.SysFont("arial", 25)

print(log_message + "Initializing Texts, colors and texts...70%")
pygame.time.delay(100)
# Initializing Texts
title = font_50.render("Orbital Fantasy V1.5 | Do Not Resize Window!", True, white, black)
TitleX = font_20.render("X", True, black, white)
TitleY = font_20.render("Y", True, black, white)
TitleZ = font_20.render("Z", True, black, white)
choosing_tip1 = font_25.render("Click to Choose the first celestial body as your origin object", True, white, black)
choosing_tip2 = font_25.render("Then, Click to Choose the second celestial body as your first orbit object", True,
                               white, black)
choosing_tip3 = font_25.render("Then, Click to Choose the third celestial body as your second orbit object", True,
                               white, black)
choosing_tip4 = font_25.render("Don't click the same object twice, if you did re-enter the game", True, white, black)
choosing_tip5 = font_25.render("After you finish chosen three objects, the game will automatically start", True, white,
                               black)
choosing_tip6 = font_25.render("Remember you can only choose one star as the origin object or the game will crash!",
                               True, white, black)

print(log_message + "Setting up screen...80%")
pygame.time.delay(100)
# Loading Screen
SCREEN_SIZE = (900, 900)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
pygame.display.set_caption("Orbital Fantasy")

print(log_message + "Loading images...90%")
pygame.time.delay(100)
# Load images
titlepic = pygame.image.load(titlepic_image).convert()
background = pygame.image.load(background_image).convert()
button_quit_off = pygame.image.load(button_quit_off_image).convert()
button_quit_on = pygame.image.load(button_quit_on_image).convert()
button_start_off = pygame.image.load(button_start_off_image).convert()
button_start_on = pygame.image.load(button_start_on_image).convert()
button_stop_off = pygame.image.load(button_stop_off_image).convert()
button_stop_on = pygame.image.load(button_stop_on_image).convert()
button_earth = pygame.image.load(button_earth_image).convert()
button_jupiter = pygame.image.load(button_jupiter_image).convert()
button_mars = pygame.image.load(button_mars_image).convert()
button_mercury = pygame.image.load(button_mercury_image).convert()
button_moon = pygame.image.load(button_moon_image).convert()
button_saturn = pygame.image.load(button_saturn_image).convert()
button_sirius = pygame.image.load(button_sirius_image).convert()
button_sun = pygame.image.load(button_sun_image).convert()
button_venus = pygame.image.load(button_venus_image).convert()
button_arcturus = pygame.image.load(button_arcturus_image).convert()

chosen_planets = []


def drawBlueRect(rect):
    pygame.draw.rect(screen, blue, rect, 0)


def drawRedRect(rect):
    pygame.draw.rect(screen, red, rect, 0)


def quitGame():
    print(log_message + "Game Quited successfully... Thanks for playing Orbital Fantasy. \nFinished")
    pygame.quit()
    exit()


def startGame(switch):
    print(log_message + "Simulation Starts...")
    switch = False


def button(surface_on, surface_off, posX, posY, isPlanet, planet_name, action=None):
    click = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()

    # rect = [left, top, width, height]
    button_rect = surface_on.get_rect()
    left = button_rect[0]
    top = button_rect[1]
    width = button_rect[2]
    height = button_rect[3]

    pos_left = posX
    pos_right = posX + width
    pos_top = posY
    pos_bottom = posY + height

    screen.blit(surface_off, (int(posX), int(posY)))

    if pos_left <= x1 <= pos_right and pos_top <= y1 <= pos_bottom:
        screen.blit(surface_on, (int(posX), int(posY)))
        if isPlanet == True:
            if click[0] == 1:
                pygame.time.delay(500)
                screen.blit(surface_on, (int(posX), int(posY)))
                chosen_planets.append(planet_name)
            else:
                screen.blit(surface_off, (int(posX), int(posY)))
        else:
            if click[0] == 1 and action is not None:
                pygame.time.delay(500)
                screen.blit(surface_on, (int(posX), int(posY)))
                action()
                if action == "play":
                    action()
                if action == "quit":
                    action()
                if action == "choose_planet":
                    action()
            else:
                screen.blit(surface_off, (int(posX), int(posY)))


def getHalfSide(surface, indicator):
    rect = surface.get_rect()
    width = rect[2]
    height = rect[3]
    if indicator == "w":
        return width / 2
    elif indicator == "h":
        return height / 2
    else:
        print("[Orbtial Fantasy] FunctionError: Input string must be 'w' or 'h'!")


def planet_choose(chosen):
    print(log_message + "Entering planet choosing phase...")
    pygame.time.delay(100)

    s = chosen[0]
    p = chosen[1]
    q = chosen[2]

    # mass of the star
    ms = data[s][0]

    # mass of planet p
    mp = data[p][0]
    # mass of planet q
    mq = data[q][0]

    # radius of planet p
    rp = data[p][1]
    # radius of planet q
    rq = data[q][1]

    # image of planet p and q and s
    image_s = data[s][2]
    image_p = data[p][2]
    image_q = data[q][2]

    data_list = {'mp': mp, 'mq': mq, 'rp': rp, 'rq': rq, 'ms': ms, 'imgp': image_p, 'imgq': image_q, 'imgs': image_s,
                 's_name': s, 'p_name': p, 'q_name': q}

    return data_list


# Game Functions


def game_intro():
    print(log_message + "Game Started successfully...100%")
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                quitGame()

        screen.blit(background, (0, 0))  # draw the background
        screen.blit(title, (100, 100))  # draw the background
        screen.blit(titlepic, (int(450 - getHalfSide(titlepic, "w")),
                               int(300 - getHalfSide(titlepic, "h"))))  # draw the background

        button(button_quit_on, button_quit_off, 450 - getHalfSide(button_quit_on, "w"),
               450 - getHalfSide(button_quit_on, "h"), False, "", quitGame)
        button(button_start_on, button_start_off, 450 - getHalfSide(button_start_on, "w"),
               550 - getHalfSide(button_start_on, "h"), False, "", game_choose)

        pygame.display.update()


def game_choose():
    choose = True
    while choose:
        for event in pygame.event.get():
            if event.type == QUIT:
                quitGame()

        screen.blit(background, (0, 0))  # draw the background
        screen.blit(choosing_tip1, (240, 100))  # draw the background
        screen.blit(choosing_tip2, (240, 200))  # draw the background
        screen.blit(choosing_tip3, (240, 300))  # draw the background
        screen.blit(choosing_tip4, (240, 400))  # draw the background
        screen.blit(choosing_tip5, (240, 500))  # draw the background
        screen.blit(choosing_tip6, (240, 600))  # draw the background

        button(button_mercury, button_mercury, 120 - getHalfSide(button_mercury, "w"),
               100 - getHalfSide(button_mercury, "h"), True, "Mercury", None)
        button(button_venus, button_venus, 120 - getHalfSide(button_mercury, "w"),
               180 - getHalfSide(button_mercury, "h"), True, "Venus", None)
        button(button_earth, button_earth, 120 - getHalfSide(button_mercury, "w"),
               260 - getHalfSide(button_mercury, "h"), True, "Earth", None)
        button(button_mars, button_mars, 120 - getHalfSide(button_mercury, "w"),
               340 - getHalfSide(button_mercury, "h"), True, "Mars", None)
        button(button_jupiter, button_jupiter, 120 - getHalfSide(button_mercury, "w"),
               420 - getHalfSide(button_mercury, "h"), True, "Jupiter", None)
        button(button_saturn, button_saturn, 120 - getHalfSide(button_mercury, "w"),
               500 - getHalfSide(button_mercury, "h"), True, "Saturn", None)
        button(button_sun, button_sun, 120 - getHalfSide(button_mercury, "w"),
               580 - getHalfSide(button_mercury, "h"), True, "Sun", None)
        button(button_sirius, button_sirius, 120 - getHalfSide(button_mercury, "w"),
               660 - getHalfSide(button_mercury, "h"), True, "Sirius", None)
        button(button_arcturus, button_arcturus, 120 - getHalfSide(button_mercury, "w"),
               740 - getHalfSide(button_mercury, "h"), True, "Arcturus", None)

        if len(chosen_planets) == 3:
            game_loop()

        pygame.display.update()


def game_loop():
    print(log_message + "Loading Planetary Data...")

    dataset = planet_choose(chosen_planets)

    star = pygame.image.load(dataset['imgs']).convert()
    planet_p = pygame.image.load(dataset['imgp']).convert()
    planet_q = pygame.image.load(dataset['imgq']).convert()

    ms = dataset['ms']
    mp = dataset['mp']
    mq = dataset['mq']
    rp = dataset['rp']
    rq = dataset['rq']

    s_name = dataset['s_name']
    p_name = dataset['p_name']
    q_name = dataset['q_name']

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

    print(log_message + "Simulation Starts")
    switch2 = True
    while switch2:

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

        drawBlueRect(rect_1)
        drawBlueRect(rect_2)
        drawBlueRect(rect_3)
        drawBlueRect(rect_4)
        drawBlueRect(rect_5)
        drawBlueRect(rect_6)

        screen.blit(star, (int(230 - getHalfSide(star, "w")), int(230 - getHalfSide(star, "h"))))  # draw XY star
        screen.blit(star, (int(230 - getHalfSide(star, "w")), int(680 - getHalfSide(star, "h"))))  # draw XY star
        screen.blit(star, (int(680 - getHalfSide(star, "w")), int(230 - getHalfSide(star, "h"))))  # draw XY star

        # The texts

        TitleP = font_20.render(p_name, True, white, blue)
        TitleQ = font_20.render(q_name, True, white, blue)
        TitleS = font_20.render(s_name, True, white, blue)

        screen.blit(TitleP, (460, 460))
        screen.blit(TitleQ, (460, 640))
        screen.blit(TitleS, (460, 820))

        screen.blit(planet_p, (460 + 180, 460))
        screen.blit(planet_q, (460 + 180, 640))
        screen.blit(star, (460 + 180, 820))

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
                    quitGame()

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
            ip = np.arctan(zp1 / np.sqrt(xp1 * xp1 + yp1 * yp1)) * 180 / pi
            iq = np.arctan(zq1 / np.sqrt(xq1 * xq1 + yq1 * yq1)) * 180 / pi

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

            drawBlueRect(rect_1)
            drawBlueRect(rect_2)
            drawBlueRect(rect_3)
            drawBlueRect(rect_4)
            drawBlueRect(rect_5)
            drawBlueRect(rect_6)

            screen.blit(star, (int(230 - getHalfSide(star, 'w')), int(230 - getHalfSide(star, 'w'))))  # draw XY star
            screen.blit(star, (int(230 - getHalfSide(star, 'w')), int(680 - getHalfSide(star, 'w'))))  # draw XZ star
            screen.blit(star, (int(680 - getHalfSide(star, 'w')), int(230 - getHalfSide(star, 'w'))))  # draw YZ star

            screen.blit(TitleP, (460, 460))
            screen.blit(TitleQ, (460, 640))
            screen.blit(TitleS, (460, 820))

            screen.blit(planet_p, (460 + 180, 460))
            screen.blit(planet_q, (460 + 180, 640))
            screen.blit(star, (460 + 180, 820))

            screen.blit(TitleX, (220, 420))
            screen.blit(TitleY, (20, 230))

            screen.blit(TitleX, (220, 870))
            screen.blit(TitleZ, (20, 680))

            screen.blit(TitleY, (670, 420))
            screen.blit(TitleZ, (460, 230))

            # Data
            Clock = font_30.render("Time Elapsed: " + str(round(t / 86400 / 365, 2)) + "years", True, white, blue)
            Mass_P = font_20.render("Mass=" + str(round(mp, 2)) + "kg", True, white, black)
            Radius_P = font_20.render("Radius=" + str(round(rp, 2)) + "AU", True, white, black)
            Velocity_P = font_20.render("Velocity=" + str(vp / auperm / 24 / 3600) + "m/s", True, white, black)
            Acceleration_P = font_20.render("Acceleration=" + str(ap / auperm / 24 / 3600 / 24 / 3600) + "m/s^2", True,
                                            white, black)
            Force_P = font_20.render("Force=" + str(round(Fp / auperm / 24 / 3600 / 24 / 3600, 2)) + "N", True, white,
                                     black)
            Inclination_P = font_20.render("Inclination=" + str(round(ip, 4)) + "Degrees", True, white, black)
            Eccentricity_P = font_20.render("Eccentricity=" + str(round(ep, 4)), True, white, black)
            if Ep < 0:
                TotalEnergy_P = font_20.render("TotalEnergy=" + str(
                    round(Ep / auperm / auperm / 24 / 3600 / 24 / 3600, 2)) + "J, PLANET IN BOUND!",
                                               True, white, black)
            else:
                TotalEnergy_P = font_20.render(
                    "TotalEnergy=" + str(
                        round(Ep / auperm / auperm / 24 / 3600 / 24 / 3600, 2)) + "J, PLANET OUT OF BOUND!",
                    True, white, black)

            Mass_Q = font_20.render("Mass=" + str(round(mq, 2)) + "kg", True, white, black)
            Radius_Q = font_20.render("Radius=" + str(round(rq, 2)) + "AU", True, white, black)
            Velocity_Q = font_20.render("Velocity=" + str(vq / auperm / 24 / 3600) + "m/s", True, white, black)
            Acceleration_Q = font_20.render("Acceleration=" + str(aq / auperm / 24 / 3600 / 24 / 3600) + "m/s^2", True,
                                            white, black)
            Force_Q = font_20.render("Force=" + str(round(Fq / auperm / 24 / 3600 / 24 / 3600, 2)) + "N", True, white,
                                     black)
            Inclination_Q = font_20.render("Inclination=" + str(round(iq, 4)) + "Degrees", True, white, black)
            Eccentricity_Q = font_20.render("Eccentricity=" + str(round(eq, 4)), True, white, black)
            if Eq < 0:
                TotalEnergy_Q = font_20.render("TotalEnergy=" + str(
                    round(Eq / auperm / auperm / 24 / 3600 / 24 / 3600, 2)) + "J, PLANET IN BOUND!",
                                               True, white, black)
            else:
                TotalEnergy_Q = font_20.render(
                    "TotalEnergy=" + str(
                        round(Eq / auperm / auperm / 24 / 3600 / 24 / 3600, 2)) + "J, PLANET OUT OF BOUND!",
                    True, white, black)

            Mass_S = font_20.render("Mass=" + str(round(ms, 2)) + "kg", True, white, black)

            screen.blit(Clock, (350, 10))
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

            screen.blit(Mass_S, (460, 840))

            positionp_xy = (
                int(xp1 * 20 + 230 - getHalfSide(planet_p, 'w')),
                int(yp1 * 20 + 230 - getHalfSide(planet_p, 'w')))  # move planet
            positionq_xy = (
                int(xq1 * 20 + 230 - getHalfSide(planet_q, 'w')),
                int(yq1 * 20 + 230 - getHalfSide(planet_q, 'w')))  # move planet

            positionp_xz = (
                int(xp1 * 20 + 230 - getHalfSide(planet_p, 'w')),
                int(zp1 * 20 + 680 - getHalfSide(planet_p, 'w')))  # move planet
            positionq_xz = (
                int(xq1 * 20 + 230 - getHalfSide(planet_q, 'w')),
                int(zq1 * 20 + 680 - getHalfSide(planet_q, 'w')))  # move planet

            positionp_yz = (
                int(yp1 * 20 + 680 - getHalfSide(planet_p, 'w')),
                int(zp1 * 20 + 230 - getHalfSide(planet_p, 'w')))  # move planet
            positionq_yz = (
                int(yq1 * 20 + 680 - getHalfSide(planet_q, 'w')),
                int(zq1 * 20 + 230 - getHalfSide(planet_q, 'w')))  # move planet

            screen.blit(planet_p, positionp_xy)  # draw new planet
            screen.blit(planet_q, positionq_xy)  # draw new planet

            screen.blit(planet_p, positionp_xz)  # draw new planet
            screen.blit(planet_q, positionq_xz)  # draw new planet

            screen.blit(planet_p, positionp_yz)  # draw new planet
            screen.blit(planet_q, positionq_yz)  # draw new planet

            pygame.display.update()  # and show it all
            pygame.time.delay(1)


game_intro()
