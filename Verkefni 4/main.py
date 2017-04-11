#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Höfundur - Ólafur Jón Valgeirsson

import pygame
import sprites
import time
import random
import math


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
r = random.randint(15, 50)
fighters = pygame.sprite.Group()
clip = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

tiefighters = list()
tiefighters2 = list()
wave2 = pygame.sprite.Group()
space = pygame.image.load('img/space1.jpg')
def mainmenu(gameDisplay,resW):
    myfont = pygame.font.SysFont("impact",48)
    playgametext = myfont.render("Play Game",1,(0,0,0))
    pygame.draw.rect(gameDisplay, (255, 255, 255), (resW / 4, 240, 300, 100))
    gameDisplay.blit(playgametext, (resW / 3, 260))
spawntime = 10
def readyfighters():
    x = 50
    y = 0
    k = 0
    for i in range(r):
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

def fighters2():
    x = 50
    y = 50
    k = 0
    for i in range(10):
        tie = sprites.Enemy2(20,15,resW,resH)
        tiefighters.append(tie)
        tie.rect.x = x
        tie.rect.y = y
        wave2.add(tie)
        all_sprites.add(tie)
        x += 50
        k += 1
        if k == 10:
            y += 50
            x = 50
            k = 0
readyfighters()
fighters2()



Hero = sprites.Hero(50,50,resW,resH)
hero = pygame.sprite.GroupSingle()
bullet = sprites.bullets(10, 10,Hero)
all_sprites.add(Hero)
Hero.rect.x = 300
Hero.rect.y = 850
missile = 0
shoot = True
started  = False
crashed = False
arg = "right"
t0 = time.time()
x= 0
t = 0
k = 1
while not crashed:
    if x == resH:
        x = 0
    x+= 1
    gameDisplay.blit(space, (0, x))
    gameDisplay.blit(space, (0, x - resH))
    clock.tick(60)
    t1 = time.time()
    time_Start = True
    ms = t1 - t0
    sek = int(math.floor(ms))
    #print sek



    if started:

        all_sprites.draw(gameDisplay)
        for tie in fighters:
            tie.update1()

        for tie in wave2:
            tie.update2()

        for tie in tiefighters:
            if pygame.sprite.spritecollideany(tie, clip):
                for bullet in clip:
                    if bullet.rect.colliderect(tie):
                        all_sprites.remove(bullet)
                        clip.remove(bullet)
                all_sprites.remove(tie)
                tiefighters.remove(tie)



        if clip.__len__() != 0:
            for bullet in clip:
                if bullet.type == "straight":
                    bullet.rect.y -= 5
                if bullet.type == "rightska":
                    bullet.rect.y -= 5
                    bullet.rect.x += 2
                if bullet.type == "leftska":
                    bullet.rect.y -= 5
                    bullet.rect.x -= 2
                if bullet.rect.y <= 0 or bullet.rect.y >= 900:
                    clip.remove(bullet)
                    print "bullet dead"
                    all_sprites.remove(bullet)






        pygame.display.update()
        pygame.display.flip()
    if not started:
        mainmenu(gameDisplay, resW)
        playgameclick = pygame.Rect(resW / 4, 240, 300, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    missile += 1
    if event.type == pygame.KEYDOWN or pygame.KEYUP:  # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        Hero.keylistener()
        if missile >= 20:
            missile = 0

        if key[pygame.K_SPACE] and missile == 0 :
            print "shoot"
            bullet = sprites.bullets(10, 10,Hero)
            if Hero.angle < 20 and Hero.angle > -20:
                bullet.rect.y = Hero.rect.y - 27
                bullet.rect.x = Hero.rect.x + 12
                bullet.type = "straight"
            if Hero.angle < -20 and Hero.angle > -70:
                bullet.rect.y = Hero.rect.y - 27
                bullet.rect.x = Hero.rect.x + 30
                bullet.type = "rightska"
            if Hero.angle < 70 and Hero.angle > 20:
                bullet.rect.y = Hero.rect.y - 27
                bullet.rect.x = Hero.rect.x - 5
                bullet.type = "leftska"

            all_sprites.add(bullet)
            clip.add(bullet)


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