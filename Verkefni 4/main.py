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
hero = pygame.sprite.Group()
tiefighters = list()
tiefighters2 = list()
wave2 = pygame.sprite.Group()
space = pygame.image.load('img/space1.jpg')
def mainmenu(gameDisplay,resW):
    myfont = pygame.font.SysFont("impact",48)
    playgametext = myfont.render("Play Game",1,(0,0,0))
    pygame.draw.rect(gameDisplay, (255, 255, 255), (resW / 4, 240, 300, 100))
    gameDisplay.blit(playgametext, (resW / 3, 260))
def gameover(gameDisplay,resW):
    myfont = pygame.font.SysFont("impact",48)
    GameOver = myfont.render("Play Again?",1,(0,0,0))
    playgametext = myfont.render("Score:"+str(score), 1, (0, 0, 0))
    pygame.draw.rect(gameDisplay, (255, 255, 255), (resW / 4, 240, 300, 100))
    pygame.draw.rect(gameDisplay, (255, 255, 255), (resW / 4, 500, 300, 100))
    gameDisplay.blit(GameOver, (resW / 3, 260))
    gameDisplay.blit(playgametext, (resW / 3, 520))
def readyfighters():
    x = 50
    y = -150
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
    y = -10
    k = 0
    for i in range(r):
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
all_sprites.add(Hero)
Hero.rect.x = 300
Hero.rect.y = 850
lost = False
bullet = sprites.bullets(10, 10,Hero)
spawntime = 10



score = 0
missile = 0
shoot = True
lost = False
started  = False
crashed = False
arg = "right"
t0 = time.time()
spawn = False
x= 0
t = 0
k = 1
while not crashed:
    if x == resH*-1:
        x = 0
    x-= 1
    gameDisplay.blit(space, (0, x))
    gameDisplay.blit(space, (0, x + resH))
    clock.tick(60)
    t1 = time.time()
    time_Start = True
    ms = t1 - t0
    sek = int(math.floor(ms))


    if started == True:
        if sek == spawntime:
            t0 = time.time()
            t += 1
            if t % 5 == 1:
                for tie in fighters:
                    tie.speedx += 1
                    tie.speedy += 3
                readyfighters()
            else:

                for tie in wave2:
                    tie.speedx += 5
                    tie.speedy += 5
                fighters2()
            k += 1
            if k == 10 and spawntime != 3:
                if spawntime < 3:
                    spawntime = 3
                else:
                    spawntime = - 2
                k = 0



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
                        score += 1
                        pygame.display.set_caption("Verkefni 4 stig:" + str(score))
                all_sprites.remove(tie)
                tiefighters.remove(tie)

        for tie in tiefighters:
            if pygame.sprite.spritecollideany(Hero,tiefighters):
                print "ouch"
                gameover(gameDisplay, resW)
                lost = True
                started = False




        if clip.__len__() != 0:
            for bullet in clip:
                if bullet.counter >= 3:
                    clip.remove(bullet)
                    all_sprites.remove(bullet)
                if bullet.type == "straight":
                    bullet.rect.y -= 5
                if bullet.type == "down":
                    bullet.rect.y += 5
                if bullet.type == "rightska":
                    bullet.rect.y -= 5
                    bullet.rect.x += 2
                if bullet.type == "downright":
                    bullet.rect.y += 10
                    bullet.rect.x += 2
                if bullet.type == "leftska":
                    bullet.rect.y -= 5
                    bullet.rect.x -= 2
                if bullet.type == "downleft":
                    bullet.rect.y += 5
                    bullet.rect.x -= 2
                if bullet.type == "left":
                    bullet.rect.x -= 5
                if bullet.type == "right":
                    bullet.rect.x += 5
                if bullet.rect.y <= 0 or bullet.rect.y >= 900:
                    clip.remove(bullet)
                    print "bullet dead"
                    all_sprites.remove(bullet)

        pygame.display.update()
        pygame.display.flip()
    if not started:
        mainmenu(gameDisplay, resW)
        playgameclick = pygame.Rect(resW / 4, 240, 300, 100)
    if not started and lost == True:
        if x == resH * -1:
            x = 0
        x -= 1
        gameDisplay.blit(space, (0, x))
        gameDisplay.blit(space, (0, x + resH))
        gameover(gameDisplay, resW)
        playgameclick = pygame.Rect(resW / 4, 240, 300, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    missile += 1
    key = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN or pygame.KEYUP and started:  # Move the player if an arrow key is pressed
        if started:
            Hero.keylistener()
        if missile >= 20:
            missile = 0

        if key[pygame.K_SPACE] and missile == 0 and started :
            print "shoot"
            bullet = sprites.bullets(10, 10,Hero)
            if Hero.angle < 20 and Hero.angle >= -20 or Hero.angle < -340 or Hero.angle >= 330:
                bullet.rect.y = Hero.rect.y - 27
                bullet.rect.x = Hero.rect.x + 12
                if started == True:
                    started = False
                if started == False:
                    started = True
                bullet.type = "straight"
            elif Hero.angle < -20 and Hero.angle >= -80 or Hero.angle < 330 and Hero.angle >= 290:
                bullet.rect.y = Hero.rect.y - 27
                bullet.rect.x = Hero.rect.x + 30
                bullet.image = pygame.transform.rotate(bullet.image, -15)
                bullet.type = "rightska"
            elif Hero.angle < 80 and Hero.angle >= 20 or Hero.angle < -290 and Hero.angle >= -340:
                bullet.rect.y = Hero.rect.y - 30
                bullet.rect.x = Hero.rect.x - 10
                bullet.image = pygame.transform.rotate(bullet.image, 15)
                bullet.type = "leftska"
            elif Hero.angle < 120 and Hero.angle >= 80 or Hero.angle < -250 and Hero.angle >= -290:
                bullet.rect.y = Hero.rect.y + 12
                bullet.rect.x = Hero.rect.x - 30
                bullet.image = pygame.transform.rotate(bullet.image,90)
                bullet.type = "left"
            elif Hero.angle < -80 and Hero.angle >= -120 or Hero.angle < 300 and Hero.angle >= 240:
                bullet.rect.y = Hero.rect.y + 12
                bullet.rect.x = Hero.rect.x + 30
                bullet.image = pygame.transform.rotate(bullet.image,90)
                bullet.type = "right"
            elif Hero.angle < -120 and Hero.angle >= -150 or Hero.angle < 240 and Hero.angle >= 215:
                bullet.rect.y = Hero.rect.y + 12
                bullet.rect.x = Hero.rect.x + 8
                bullet.image = pygame.transform.rotate(bullet.image,45)
                bullet.type = "downright"
                bullet.type = "right"
            elif Hero.angle < 180 and Hero.angle >= 120 or Hero.angle < -220 and Hero.angle >= -250:
                bullet.rect.y = Hero.rect.y + 12
                bullet.rect.x = Hero.rect.x - 10
                bullet.image = pygame.transform.rotate(bullet.image,-45)
                bullet.type = "downleft"
            elif Hero.angle < 215 and Hero.angle >= 180 or Hero.angle < -150 and Hero.angle >= -220:
                bullet.rect.y = Hero.rect.y + 27
                bullet.rect.x = Hero.rect.x + 12
                bullet.type = "down"

            else:
                Hero.angle + 180


            all_sprites.add(bullet)
            clip.add(bullet)



    if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_BUTTON:
        if playgameclick.collidepoint(event.pos):
            if lost == True:
                playgameclick.x = -1000000
                playgameclick.y = -1000000
                gameDisplay.blit(space, (0, x))
                t0 = time.time()
                gameDisplay.blit(space, (0, x - resH))
                all_sprites.empty()
                fighters.empty()
                tiefighters = 0
                tiefighters = list()
                wave2.empty()
                clip.empty()
                readyfighters()
                fighters2()
                Hero = sprites.Hero(50, 50, resW, resH)
                all_sprites.add(Hero)
                Hero.rect.x = 300
                Hero.rect.y = 850
                lost = False
                started = True
                score = 0
                pygame.display.set_caption("Verkefni 4")



            else:
                playgameclick.x = -1000000
                playgameclick.y = -1000000
                gameDisplay.blit(space, (0, x))
                gameDisplay.blit(space, (0, x - resH))
                started = True



        pygame.display.flip()
    pygame.display.update()
pygame.quit()
quit()