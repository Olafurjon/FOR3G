#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Höfundur - Ólafur Jón Valgeirsson

import pygame
import sprites
import time
import random
from math import floor


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
    y = -300
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
    y = -350
    k = 0
    for i in range(10):
        newtie = sprites.Enemy(20,15,resW,resH)
        tiefighters.append(newtie)
        newtie.rect.x = x
        newtie.rect.y = y
        wave2.add(newtie)
        all_sprites.add(newtie)
        x += 50
        k += 2
        if k == 10:
            y += 50
            x = 50
            k = 0

readyfighters()



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
    sek = int(floor(ms))
    print sek
    if sek == spawntime:
        readyfighters()
        t0 = time.time()
        t += 1
        if t == 5:
            if k != 2:
                k += 1
            if k > 2:
                k == 2
            if k == 2:
                spawntime = 20


            t = 0


    if started:

        all_sprites.draw(gameDisplay)

        for tie in fighters:
           if tie.rect.x >= (resW-30):
               print "snúavið"
               arg = "left"
               for tie in fighters:
                   tie.move("down",k)

           if tie.rect.x <= 0:
               arg = "right"
               print "snúavið"
               for tie in fighters:
                   tie.move("down",k)

        for newtie in wave2:
           if newtie.rect.x >= (resW-30):
               arg = "leftska"


           if newtie.rect.x <= 0:
               arg = "skaright"


        if clip.__len__() !=  0:
           for bullet in clip:
               bullet.rect.y -= 5
               if bullet.rect.y <= 0 or bullet.rect.y >= 900:
                   clip.remove(bullet)
                   print "bullet dead"
                   all_sprites.remove(bullet)

        for tie in fighters:
            tie.move(arg,k)
            if pygame.sprite.spritecollideany(tie, clip):
                for bullet in clip:
                    if bullet.rect.colliderect(tie):
                        all_sprites.remove(bullet)
                        clip.remove(bullet)
                all_sprites.remove(tie)
                fighters.remove(tie)

        for newtie in wave2:
            newtie.move(arg,k)
            if pygame.sprite.spritecollideany(newtie, clip):
                for bullet in clip:
                    if bullet.rect.colliderect(newtie):
                        all_sprites.remove(bullet)
                        clip.remove(bullet)
                all_sprites.remove(newtie)
                wave2.remove(newtie)



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
        if key[pygame.K_LEFT]:
            Hero.move(-2, 0)
        if key[pygame.K_RIGHT]:
            Hero.move(2, 0)
        if key[pygame.K_UP]:
            Hero.move(0, -2)
        if key[pygame.K_DOWN]:
            Hero.move(0, 2)
        if missile >= 20:
            missile = 0

        if key[pygame.K_SPACE] and missile == 0 :
            print "shoot"
            bullet = sprites.bullets(10, 10,Hero)
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