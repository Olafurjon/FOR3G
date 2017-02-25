#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import time


pygame.init()
black = (0,0,0)
resW = 800
resH = 600
myfont = pygame.font.SysFont("Arial",30)
gameDisplay = pygame.display.set_mode((resW,resH))
pygame.display.set_caption('Músaveiðar')
background = pygame.image.load('img/bakgrunnur.jpg')
hola = pygame.image.load('img/musahola.png')
jenni = pygame.image.load('img/jennihola.png')
tommi = pygame.image.load('img/tommihola.png')
cheesescore = pygame.image.load('img/cheesescoreboard.png')
jennipoints = 0
clock = pygame.time.Clock()
crashed = False
gameDisplay.blit(background, (0, 0))
NotandiScore = 0
Scoreboard = myfont.render("Stig: " + str(NotandiScore), 1, (0, 0, 0))
Scoreboard2 = myfont.render("Jenni Stig: " + str(jennipoints), 1, (0, 0, 0))

gameDisplay.blit(cheesescore, (52,5))
gameDisplay.blit(cheesescore, (752,5))
gameDisplay.blit(Scoreboard2, (635, 0))
gameDisplay.blit(Scoreboard, (0, 0))
NotandiScore = 0
holur = []
location = []
rects = []


X = -240
Y = 250
J = 145
K = 550
i = 0
x = 0
while i != 64:

    x += 1

    holumaker = gameDisplay.blit(hola, (X, Y))
    holur.append(holumaker)
    location.append((X, Y))
    rect = pygame.draw.rect(gameDisplay, (0, 0, 255), (J, K, 35, 36), 0)
    rects.append(rect)

    Y -= 65
    K -= 65
    i += 1
    if x == 8:
        X += 65
        J += 65
        x = 0
        Y = 250
        K = 550


i = 0
while i != 7:
    pygame.event.get()
    t = random.randint(0,10)
    M = random.randint(0, 63)
    rx = location[M][0]
    ry = location[M][1]
    x = 1
    if t < 2:
        tommimynd = gameDisplay.blit(tommi,location[M])
        tommirekt = rects[M]
    else:
        activejenni = gameDisplay.blit(jenni,location[M])
        jennirect = rects[M]
    pygame
    pygame.display.flip()
    gameDisplay.blit(hola,location[M])

    i += 1
    if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30:
        x -= 0.4

    pygame.display.flip()




RED = (255, 0, 0)
LEFT_BUTTON = 1


white = (255,255,255)


def playerStig(notandiscore):
    notandiscore += 1
    Scoreboard = myfont.render("Stig: " + str(notandiscore), 1, (0, 0, 0))
    gameDisplay.blit(cheesescore, (52, 5))
    gameDisplay.blit(Scoreboard, (0, 0))
    pygame.display.flip()
    return notandiscore

def jennistig(jenniscore):
    jenniscore += 1
    Scoreboard2 = myfont.render("Jenni Stig: " + str(jenniscore), 1, (0, 0, 0))
    gameDisplay.blit(cheesescore, (752, 5))
    gameDisplay.blit(Scoreboard2, (635, 0))
    pygame.display.flip()
    return jenniscore

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            if  jennirect.collidepoint(event.pos):
                NotandiScore = playerStig(NotandiScore)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

quit()
