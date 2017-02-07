#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import time


pygame.init()

displWidth = 800
displHeight = 600

window = gameDisplay = pygame.display.set_mode((displWidth,displHeight))
pygame.display.set_caption('Teningaleikur')
clock = pygame.time.Clock()
crashed = False
green = (98,244,66)
gameDisplay.fill(green)
RED = (255, 0, 0)
LEFT_BUTTON = 1

black = (0,0,0)
white = (255,255,255)

start = 0
myfont = pygame.font.SysFont("Arial",30)
Notandi = myfont.render("Notandi", 1, (0,0,0))
Tolva = myfont.render("Tolva", 1, (0,0,0))
crashed = False
play = False

pressplaybt = pygame.image.load('img/pressplay.jpg')
kastaaftur = pygame.image.load('img/kastaaftur.jpg')
kastalast = pygame.image.load('img/kastasidasta.jpg')
win = pygame.image.load('img/winner.png')
loss = pygame.image.load('img/gamover.png')
tie = pygame.image.load('img/tie.png')


pressplay = gameDisplay.blit(pressplaybt, (displWidth * 0.20, displHeight * 0.40))
gameDisplay.blit(Notandi, (displWidth * 0.1255, displHeight * 0.75))
gameDisplay.blit(Tolva, (displWidth * 0.12, displHeight * 0.15))

class diceGame():
    diceIMG0 = pygame.image.load('img/teningar/t0.png')
    diceIMG1 = pygame.image.load('img/teningar/t1.png')
    diceIMG2 = pygame.image.load('img/teningar/t2.png')
    diceIMG3 = pygame.image.load('img/teningar/t3.png')
    diceIMG4 = pygame.image.load('img/teningar/t4.png')
    diceIMG5 = pygame.image.load('img/teningar/t5.png')
    diceIMG6 = pygame.image.load('img/teningar/t6.png')
    xx = 0
    xy = 0

    compterdicepos1 = (displWidth * 0.12, displHeight * 0.2)
    compterdicepos2 = (displWidth * 0.19, displHeight * 0.2)
    compterdicepos3 = (displWidth * 0.26, displHeight * 0.2)
    compterdicepos4 = (displWidth * 0.33, displHeight * 0.2)
    compterdicepos5 = (displWidth * 0.40, displHeight * 0.2)
    compterdicepos6 = (displWidth * 0.47, displHeight * 0.2)

    userdicepos1 = (displWidth * 0.12, displHeight * 0.8)
    userdicepos2 = (displWidth * 0.19, displHeight * 0.8)
    userdicepos3 = (displWidth * 0.26, displHeight * 0.8)
    userdicepos4 = (displWidth * 0.33, displHeight * 0.8)
    userdicepos5 = (displWidth * 0.40, displHeight * 0.8)
    userdicepos6 = (displWidth * 0.47, displHeight * 0.8)

    def computerDice(self):
            gameDisplay.blit(diceGame.diceIMG1,diceGame.compterdicepos1)
            gameDisplay.blit(diceGame.diceIMG2, diceGame.compterdicepos2)
            gameDisplay.blit(diceGame.diceIMG3, diceGame.compterdicepos3)
            gameDisplay.blit(diceGame.diceIMG4, diceGame.compterdicepos4)
            gameDisplay.blit(diceGame.diceIMG5, diceGame.compterdicepos5)
            gameDisplay.blit(diceGame.diceIMG6, diceGame.compterdicepos6)


    def userDice(self):
            gameDisplay.blit(diceGame.diceIMG1, diceGame.userdicepos1)
            gameDisplay.blit(diceGame.diceIMG2, diceGame.userdicepos2)
            gameDisplay.blit(diceGame.diceIMG3, diceGame.userdicepos3)
            gameDisplay.blit(diceGame.diceIMG4, diceGame.userdicepos4)
            gameDisplay.blit(diceGame.diceIMG5, diceGame.userdicepos5)
            gameDisplay.blit(diceGame.diceIMG6, diceGame.userdicepos6)

    def shuffledice(self,x):
        position = (x)
        x = random.randint(1,6)
        pic = diceGame.diceIMG0
        if x == 1:
            pic = diceGame.diceIMG1
            diceGame.xx += 1
            diceGame.xy += 1
        elif x == 2:
            pic = diceGame.diceIMG2
            diceGame.xx += 2
            diceGame.xy += 2
        elif x == 3:
            pic = diceGame.diceIMG3
            diceGame.xx += 3
            diceGame.xy += 3
        elif x == 4:
            pic = diceGame.diceIMG4
            diceGame.xx += 4
            diceGame.xy += 4
        elif x == 5:
            pic = diceGame.diceIMG5
            diceGame.xx += 5
            diceGame.xy += 5
        elif x == 6:
            diceGame.xx += 6
            diceGame.xy += 6
            pic = diceGame.diceIMG6
        return gameDisplay.blit(pic,position)

    def returnpointsxx(self):
        return diceGame.xx

    def returnpointsxy(self):
        return diceGame.xx

    def resetpoints(self):
        diceGame.xx = 0
        diceGame.xy = 0

tolva = diceGame()
notandi = diceGame()
i = 0

notandi.userDice()
tolva.computerDice()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        if pressplay.collidepoint(event.pos) and start == 0:
            time.sleep(0.5)
            gameDisplay.fill(green)
            gameDisplay.blit(Notandi, (displWidth * 0.1255, displHeight * 0.75))
            gameDisplay.blit(Tolva, (displWidth * 0.12, displHeight * 0.15))
            play = True
            start = 10
            notandi.shuffledice(notandi.userdicepos1)
            notandi.shuffledice(notandi.userdicepos2)
            notandi.shuffledice(notandi.userdicepos3)
            notandi.shuffledice(notandi.userdicepos4)
            notandi.shuffledice(notandi.userdicepos5)
            gameDisplay.blit(diceGame.diceIMG0 , diceGame.userdicepos6)
            notandipoints = notandi.returnpointsxx()
            upoints = int(notandi.returnpointsxy())
            userpoints = myfont.render(str(notandipoints), 1, (0, 0, 0))
            gameDisplay.blit(userpoints, (displWidth * 0.8, displHeight * 0.8))
            tolva.resetpoints()
            kastaaftur = gameDisplay.blit(kastaaftur, (displWidth * 0.05, displHeight * 0.40))
            kastalast = gameDisplay.blit(kastalast, (displWidth * 0.35, displHeight * 0.40))
            tolva.shuffledice(tolva.compterdicepos1)
            tolva.shuffledice(tolva.compterdicepos2)
            tolva.shuffledice(tolva.compterdicepos3)
            tolva.shuffledice(tolva.compterdicepos4)
            tolva.shuffledice(tolva.compterdicepos5)
            tolva.shuffledice(tolva.compterdicepos6)
            tolvapoints = tolva.returnpointsxy()
            cpoints = int(tolva.returnpointsxy())
            cpupoints = myfont.render(str(tolvapoints), 1, (0, 0, 0))
            gameDisplay.blit(cpupoints, (displWidth * 0.8, displHeight * 0.20))
            tolva.resetpoints()
            pygame.display.update()
            while not crashed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        crashed = True
                    print(event)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
                    if kastaaftur.collidepoint(event.pos) and start == 10:
                        start = 20
                        notandi.shuffledice(notandi.userdicepos1)
                        notandi.shuffledice(notandi.userdicepos2)
                        notandi.shuffledice(notandi.userdicepos3)
                        notandi.shuffledice(notandi.userdicepos4)
                        notandi.shuffledice(notandi.userdicepos5)
                        notandi.shuffledice(notandi.userdicepos6)
                        pygame.draw.rect(gameDisplay,green,(displWidth * 0.8, displHeight * 0.8,100,100))
                        userpoints = myfont.render(str(notandipoints), 1, (0, 0, 0))
                        notandipoints = notandi.returnpointsxx()
                        upoints = int(notandi.returnpointsxx())
                        userpoints = myfont.render(str(notandipoints), 1, (0, 0, 0))
                        gameDisplay.blit(userpoints, (displWidth * 0.8, displHeight * 0.8))
                        pygame.draw.rect(gameDisplay, green, (displWidth * 0.05, displHeight * 0.40, 500, 200))
                        if upoints > cpoints:
                            gameDisplay.blit(win, (displWidth * 0.20, displHeight * 0.10))
                        elif upoints == cpoints:
                            gameDisplay.blit(tie, (displWidth * 0.20, displHeight * 0.30))
                        else:
                            gameDisplay.blit(loss, (displWidth * 0.20, displHeight * 0.30))


                        pygame.display.update()
                    elif kastalast.collidepoint(event.pos) and start == 10:
                        start = 20
                        notandi.shuffledice(notandi.userdicepos6)
                        pygame.draw.rect(gameDisplay,green,(displWidth * 0.8, displHeight * 0.8,100,100))
                        upoints += int(notandi.returnpointsxy())
                        notandipoints += notandi.returnpointsxx()
                        userpoints = myfont.render(str(notandipoints), 1, (0, 0, 0))
                        gameDisplay.blit(userpoints, (displWidth * 0.8, displHeight * 0.8))
                        pygame.draw.rect(gameDisplay, green, (displWidth * 0.05, displHeight * 0.40, 500, 200))
                        if upoints > cpoints:
                            gameDisplay.blit(win, (displWidth * 0.20, displHeight * 0.10))
                        elif upoints == cpoints:
                            gameDisplay.blit(tie, (displWidth * 0.20, displHeight * 0.30))
                        else:
                            gameDisplay.blit(loss, (displWidth * 0.20, displHeight * 0.30))


                        pygame.display.update()











    pygame.display.update()
    clock.tick(60)
pygame.quit()

quit()
