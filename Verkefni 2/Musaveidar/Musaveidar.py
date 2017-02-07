#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import time


pygame.init()

resW = 800
resH = 600

gameDisplay = pygame.display.set_mode((resW,resH))
pygame.display.set_caption('Músaveiðar')
background = pygame.image.load('img/bakgrunnur.jpg')
hola = pygame.image.load('img/musahola.png')
jenni = pygame.image.load('img/jennihola.png')
tommi = pygame.image.load('img/tommihola.png')
clock = pygame.time.Clock()
crashed = False
gameDisplay.blit(background,(0,0))
holur = []
location = []
X = -240
Y = 250
i = 0
x = 0
while i != 64:
    x += 1
    holumaker = gameDisplay.blit(hola,(X,Y))
    holur.append(holumaker)
    location.append((X,Y))
    Y -= 65
    i += 1
    if x == 8:
        X += 65
        x = 0
        Y = 250

i = 0
while i != 10:
    pygame.event.wait()
    t = random.randint(0,10);
    M = random.randint(0, 63)
    if t < 2:
        tommimynd = gameDisplay.blit(tommi,location[M])
    else:
        jennimynd = gameDisplay.blit(jenni,location[M])
    time.sleep(1)
    pygame.display.update()
    gameDisplay.blit(hola,location[M])
    time.sleep(1)
    i += 1
    pygame.display.update()




RED = (255, 0, 0)
LEFT_BUTTON = 1

black = (0,0,0)
white = (255,255,255)



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)


    pygame.display.update()
    clock.tick(60)
pygame.quit()

quit()
