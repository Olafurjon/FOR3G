#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Höfundur - Ólafur Jón Valgeirsson

import pygame
import sprites


pygame.init()
black = (0,0,0)
resW = 600
resH = 900
RED = (255, 0, 0)
white = (255,255,255)
LEFT_BUTTON = 1
myfont = pygame.font.SysFont("impact",48)
gameDisplay = pygame.display.set_mode((resW,resH))
pygame.display.set_caption("Verkefni 4")
clock = pygame.time.Clock()

fighters = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

tiefighters = list()
space = pygame.image.load('img/space1.jpg')
def mainmenu(gameDisplay,resW):
    myfont = pygame.font.SysFont("impact",48)
    playgametext = myfont.render("Play Game",1,(0,0,0))
    pygame.draw.rect(gameDisplay, (255, 255, 255), (resW / 4, 240, 300, 100))
    gameDisplay.blit(playgametext, (resW / 3, 260))

def readyfighters():
    x = 50
    y = 20
    k = 0
    for i in range(40):
        tie = sprites.Enemy(20,15,resW,resH)
        tiefighters.append(tie)
        tie.rect.x = x
        tie.rect.y = y
        fighters.add(tie)
        all_sprites.add(tie)
        x += 50
        k += 1
        if k == 10:
            y += 50
            x = 50
            k = 0

readyfighters()

Hero = sprites.Hero(50,50,resW,resH)
hero = pygame.sprite.GroupSingle()
all_sprites.add(Hero)
Hero.rect.x = 300
Hero.rect.y = 850



started  = False
crashed = False
arg = "right"
x= 0
while not crashed:
    clock.tick(60)
    x += 1
    if x == resH:
        x = 0
    gameDisplay.blit(space, (0, x))
    gameDisplay.blit(space, (0, x - resH))
    if started:
        all_sprites.draw(gameDisplay)

        if tiefighters[9].rect.x >= resW-30:
            arg = "left"
            for tie in fighters:
                tie.move("down")
        if tiefighters[0].rect.x <= 10:
            arg = "right"
            for tie in fighters:
                tie.move("down")
        for tie in fighters:
            tie.move(arg)

        pygame.display.update()
        pygame.display.flip()
    if not started:
        mainmenu(gameDisplay, resW)
        playgameclick = pygame.Rect(resW / 4, 240, 300, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    if event.type == pygame.KEYDOWN or pygame.KEYUP:  # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            Hero.move(-2, 0)
        if key[pygame.K_RIGHT]:
            Hero.move(2, 0)
        if key[pygame.K_UP]:
            Hero.move(0, -2)
        if key[pygame.K_DOWN]:
            Hero.move(0, 2)

        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_BUTTON:
            if playgameclick.collidepoint(event.pos):
                playgameclick.x = -1000000
                playgameclick.y = -1000000
                gameDisplay.blit(space, (0, x))
                gameDisplay.blit(space, (0, x - resH))
                started = True



        pygame.display.flip()
    pygame.display.update()
pygame.quit()
quit()