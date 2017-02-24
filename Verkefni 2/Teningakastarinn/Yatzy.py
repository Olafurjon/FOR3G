#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Höfundur - Ólafur Jón Valgeirsson

import pygame
import random

pygame.init()
black = (0,0,0)
resW = 800
resH = 600
RED = (255, 0, 0)
white = (255,255,255)
LEFT_BUTTON = 1

myfont = pygame.font.SysFont("Arial",30)
gameDisplay = pygame.display.set_mode((resW,resH))
pygame.display.set_caption('Teningakastarinn')
background = pygame.image.load('img/yatzybord.jpg')
rects = [
    pygame.draw.rect(gameDisplay,(0,0,255),(320,250,60,60)),
    pygame.draw.rect(gameDisplay,(0,0,255),(400,250,60,60)),
    pygame.draw.rect(gameDisplay,(0,0,255),(440,330,60,60)),
    pygame.draw.rect(gameDisplay,(0,0,255),(360,330,60,60)),
    pygame.draw.rect(gameDisplay,(0,0,255),(280,330,60,60))]

clock = pygame.time.Clock()
clock.tick(60)
crashed = False

diceIMG0 = pygame.image.load('img/teningar/t0.png')  #dúndra inn myndunum sem ég nota
diceIMG1 = pygame.image.load('img/teningar/t1.png')
diceIMG2 = pygame.image.load('img/teningar/t2.png')
diceIMG3 = pygame.image.load('img/teningar/t3.png')
diceIMG4 = pygame.image.load('img/teningar/t4.png')
diceIMG5 = pygame.image.load('img/teningar/t5.png')
diceIMG6 = pygame.image.load('img/teningar/t6.png')

diceIMGY = pygame.image.load('img/teningar/tY.png')
diceIMGA = pygame.image.load('img/teningar/tA.png')
diceIMGT = pygame.image.load('img/teningar/tT.png')
diceIMGZ = pygame.image.load('img/teningar/tZ.png')

teningar = [diceIMG1,diceIMG2,diceIMG3,diceIMG4,diceIMG5,diceIMG6]  #mun nýta mér þetta síðar

takki = pygame.image.load('img/takki.jpg')
hendaaftur = pygame.image.load('img/kastaaftur.jpg')
byrjanytt = pygame.image.load('img/restart.jpg')


restart = pygame.draw.rect(gameDisplay, (255, 255, 0), (295, 440, 200, 100))
pressaftur = pygame.draw.rect(gameDisplay, (255, 255, 0), (295, 440, 200, 100))
press =  pygame.draw.rect(gameDisplay, (255, 255, 0), (295, 440, 200, 100))


kast = 0
tabordi = []
kastaftur = []

t1 = rects[0]
t2 = rects[1]
t3 = rects[2]
t4 = rects[3]
t5 = rects[4]

class Yatzy:
    done = False
    location = [(310,240),(390,240),(430,320),(350,320),(270,320)]  #heldur um location á teningunum
    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(diceIMGY, (230, 160))
    gameDisplay.blit(diceIMGA, (290, 160))
    gameDisplay.blit(diceIMGT, (350, 160))
    gameDisplay.blit(diceIMGZ, (410, 160))
    gameDisplay.blit(diceIMGY, (470, 160))
    if kast == 0:
     gameDisplay.blit(takki, (295, 440))

    def ShowdDice(self):
        background = pygame.image.load('img/yatzybord2.jpg')
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(diceIMG1, Yatzy.location[0])
        gameDisplay.blit(diceIMG2, Yatzy.location[1])
        gameDisplay.blit(diceIMG3, Yatzy.location[2])
        gameDisplay.blit(diceIMG4, Yatzy.location[3])
        gameDisplay.blit(diceIMG5, Yatzy.location[4])

    def throwDice(self):
        global kast
        if kast == 0:
            background = pygame.image.load('img/yatzybord2.jpg')
            gameDisplay.blit(background, (0, 0))
            i = 0
            while i < 5:
                x = random.randint(0, 5)
                gameDisplay.blit(teningar[x], Yatzy.location[i])
                ten = teningar[x]
                tabordi.append(ten)
                i += 1
        kast += 1


    def kastaAftur(self):
        global kast,kastaftur
        background = pygame.image.load('img/yatzybord2.jpg')
        gameDisplay.blit(background, (0, 0))
        i = 0
        gameDisplay.blit(tabordi[0],Yatzy.location[0])
        gameDisplay.blit(tabordi[1],Yatzy.location[1])
        gameDisplay.blit(tabordi[2],Yatzy.location[2])
        gameDisplay.blit(tabordi[3],Yatzy.location[3])
        gameDisplay.blit(tabordi[4],Yatzy.location[4])
        while i < kastaftur.__len__():
            x = random.randint(0, 5)

            if kastaftur[i] == Yatzy.location[0]:
                gameDisplay.blit(teningar[x], Yatzy.location[0])
                tabordi[0] = teningar[x]
            if kastaftur[i] == Yatzy.location[1]:
                gameDisplay.blit(teningar[x], Yatzy.location[1])
                tabordi[1] = teningar[x]
            if kastaftur[i] == Yatzy.location[2]:
                gameDisplay.blit(teningar[x], Yatzy.location[2])
                tabordi[2] = teningar[x]
            if kastaftur[i] == Yatzy.location[3]:
                gameDisplay.blit(teningar[x], Yatzy.location[3])
                tabordi[3] = teningar[x]
            if kastaftur[i] == Yatzy.location[4]:
                gameDisplay.blit(teningar[x], Yatzy.location[4])
                tabordi[4] = teningar[x]
            i += 1

        kastaftur = []
        kast += 1

    def listener(self):
        global aftur,pressaftur,kast,tabordi
        if press.collidepoint(event.pos) and kast == 0:
            y.throwDice()
            pressaftur = pygame.draw.rect(gameDisplay, (255, 255, 0), (295, 440, 200, 100))
            aftur = gameDisplay.blit(hendaaftur, (295, 440))
        pygame.display.update()
        if rects[0].collidepoint(event.pos):
            kastaftur.append(y.location[0])
        if rects[1].collidepoint(event.pos):
            kastaftur.append(y.location[1])
        if rects[2].collidepoint(event.pos):
            kastaftur.append(y.location[2])
        if rects[3].collidepoint(event.pos):
            kastaftur.append(y.location[3])
        if rects[4].collidepoint(event.pos):
            kastaftur.append(y.location[4])

        if pressaftur.collidepoint(event.pos) and kast == 1:
            self.kastaAftur()

        elif pressaftur.collidepoint(event.pos) and kast == 2:
            self.kastaAftur()
            Yatzy.done = True
            if kast == 3 and Yatzy.done == True:
                gameDisplay.blit(byrjanytt, (295, 440))

        elif restart.collidepoint(event.pos) and Yatzy.done == True :
            kast = 0
            Yatzy.done = False
            tabordi = []
            background = pygame.image.load('img/yatzybord.jpg')
            gameDisplay.blit(background, (0, 0))
            gameDisplay.blit(diceIMGY, (230, 160))
            gameDisplay.blit(diceIMGA, (290, 160))
            gameDisplay.blit(diceIMGT, (350, 160))
            gameDisplay.blit(diceIMGZ, (410, 160))
            gameDisplay.blit(diceIMGY, (470, 160))
            if kast == 0:
                gameDisplay.blit(takki, (295, 440))





while not crashed:
    if kast >= 1 and kast < 3:
        pressaftur = pygame.draw.rect(gameDisplay, (255, 255, 0), (295, 440, 200, 100))
        aftur = gameDisplay.blit(hendaaftur, (295, 440))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_BUTTON:
            y = Yatzy()
            y.listener()

    pygame.display.update()
pygame.quit()

quit()