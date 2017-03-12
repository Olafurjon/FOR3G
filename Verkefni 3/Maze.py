#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Höfundur - Ólafur Jón Valgeirsson

import pygame
import random
import time
import Leidfinnur
from math import floor


pygame.init()
black = (0,0,0)
resW = 640
resH = 480
RED = (255, 0, 0)
white = (255,255,255)
LEFT_BUTTON = 1

myfont = pygame.font.SysFont("Arial",16)
gameDisplay = pygame.display.set_mode((resW,resH))
pygame.display.set_caption('Völundarhús')
walls = pygame.image.load('img/Walls.jpg')
HAL = pygame.image.load('img/player.jpg')
hero0 = pygame.image.load('img/hero.png')
hero1 = pygame.image.load('img/hero1.png')
hero2 = pygame.image.load('img/hero2.png')
bomb = pygame.image.load('img/bomb.png')
fata = pygame.image.load('img/fata2.png')
runni = pygame.image.load('img/runni.png')
skele1 = pygame.image.load('img/skellie1.png')
skele2 = pygame.image.load('img/skellie2.png')

skellies = [skele1,skele2]

clock = pygame.time.Clock()

# Holds the level layout in a list of strings.
maze2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W-------*-----------------------------CW",
    "W--------------LWWWW-WWWWWWWWWWWWWWWW--W",
    "WWWWWWWWWWWWWWWWW--WMWL------------+W--W",
    "WC-----------------W-W-C--------------*W",
    "W--WWWWWWWWWWWWWWWWW-WWWWWW-WWWWWWMWWWWW",
    "W--WC-------------*--W----W-W-L--------W",
    "W--WWWWWWWWWWWWWW----W-WMWW-WWWWWWWWWW-W",
    "WL-------------------W-W----M---L----W-W",
    "WWWWWWWWMWWWWWWWWMWWWW-W----WMWWWW---W-W",
    "W----------W---W--W----WWWWMW----W----MW",
    "WWWWWWW--L-W-W-W--W------LWLWWWWMWWMWWWW",
    "W------------W----M-------W--------*---W",
    "WWWWWWWWWWWWWWWWWWWWWWWWW-W------------W",
    "W-------+---------------WMW-L----------W",
    "W--WWWWWWWMWWWWWWWWWW-----WWWWWWWWWWWWMW",
    "W--W-L-------------*WWWWWWW-----*-----*W",
    "W--WWWWWWWWWWWWWWWWMW-----M-LWWWWWWWWWMW",
    "WL------W-L---+-----W-----WWWWL--------W",
    "WWWWWWWWWWWWWWWWWWMWW--------W---*-----W",
    "W-L-----------W-----W-------LWWWWWWWWWWW",
    "W------+------W--WWMWWWWWWWWWW--------CW",
    "W--WWWWWWWWWWWWWWW-------W-----WWW-----W",
    "W--WL--------------------W-----WLW-----W",
    "W--M-----C--------------LM-----WWW-----W",
    "WWWWWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWMW",
    "W---------------------------W------W--LW",
    "WWWWWWWWWWMWWWWWWWWWWWW-----W---WW-WWWWW",
    "WC----C--------------LW-----M---WL----ME",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
maze = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W----------------WWWWWWWWWWWWWWWWWWWW--W",
    "W--------------------------------------W",
    "W----------------WWWWWWWWWWWWWWWWWW----W",
    "W---------------------------------W----W",
    "WWWWWWWWWWWWWWWWWWWWWWW----W------W----W",
    "W---------------------W--W--W-----W----W",
    "W---------------------WWW----WWWWW-----W",
    "W--------------------------------------E",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
maze2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------W",
    "W--------------------------------------E",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

buckets = list()
bombs = list()
bricks = list()
skraut = list()
skraut2 = list()
gras = list()

leidfinnur = Leidfinnur.Leidfinnur()

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(84, 32, 14, 14)

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        # Move the rectangle
        self.rect.x += dx
        self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = brick.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = brick.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = brick.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = brick.rect.bottom


    # Nice class to hold a wall rectangle

class Stalker(object):
    def __init__(self):
        self.rect = pygame.Rect(4*16, 28*16, 16, 16)
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                if self.rect.x > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = brick.rect.left
                if self.rect.x < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = brick.rect.right
                if self.rect.y > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = brick.rect.top
                if self.rect.y < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = brick.rect.bottom


    def Stalkeron(self,path):
        if len(path) != 0:
            pos = leidfinnur.findcord(self.rect.x,self.rect.y)
            #print pos
            while pos == path[0]:
                path.pop(0)
                pos = leidfinnur.findcord(self.rect.x,self.rect.y)
                if len(path) == 0:
                    return
            pos = leidfinnur.findcord(self.rect.x, self.rect.y)

            th = leidfinnur.GetDirections(pos,path[0])
            self.rect.x += th[0] * 2
            self.rect.y += th[1] * 2

class Things(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


clock = pygame.time.Clock()

player = Player()
stalker = Stalker()
hero = 1
haswater = False

if haswater == True:
    bucket = "Yes"
else:
    bucket = "No"


x = 0
y = 0
c = 0
ma = {}

for rowx,row in enumerate(maze):
    for coly,col in enumerate(row):
        ma[(coly, rowx)] = col
        if col == "L":
            water = Things((x, y))
            buckets.append(water)
        if col == "*":
            Orn = Things((x, y))
            skraut.append(Orn)
        if col == "+":
            Orn = Things((x, y))
            skraut2.append(Orn)
        if col == "C":
            grodur = Things((x, y))
            gras.append(grodur)
        if col == "W":
            bricks.append(Things((x, y)))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        #if col == "M":
           #magic_rect = Things((x, y))
            #bombs.append(magic_rect)

        x += 16

    y += 16
    x = 0


t0 = time.time()
relax = 5000000
timelast = pygame.time.get_ticks()
crashed = False
time_Start = False
points = 3

getpoints = myfont.render(str(points),1,(0,0,0))
while not crashed:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    print "player pos:" + str(player.rect[0] / 16) + " " + str(player.rect[1]/16)
    print "Stalker pos:" + str(stalker.rect[0] / 16) + " " + str(stalker.rect[1]/16)
        #print(event)

    if event.type == pygame.KEYDOWN or pygame.KEYUP:  # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)

        if points < 35 and player.rect.colliderect(end_rect):
            player.rect.right = player.rect.left
        if player.rect.colliderect(end_rect) and points >= 35:
            raise SystemExit, 'You win!'
        for b in bombs:
            if player.rect.colliderect(b.rect):
                if haswater == True:
                    bombs.remove(b.rect)
                    points += 5
                    haswater = False

                else:
                    raise SystemExit, "You Lose"

        for bs in buckets:
            if player.rect.colliderect(bs.rect):
                if haswater == False:
                    points -= 3
                    buckets.remove(bs.rect)
                    haswater = True
                    pygame.display.flip()

        # Draw the scene
        gameDisplay.fill((43, 42, 38))
        # every brick in the walls is drawn
        timenow = pygame.time.get_ticks()
        if timenow - timelast >= relax:
            raise SystemExit, "Þú tapaðir, tíminn búinn"


        for brick in bricks:
            gameDisplay.blit(walls, brick.rect)

        for buck in buckets:
            gameDisplay.blit(fata, buck.rect)

        for gra in gras:
            gameDisplay.blit(runni,gra.rect)

        for ment in skraut:
            gameDisplay.blit(skellies[0],ment.rect)
        for ment in skraut2:
            gameDisplay.blit(skellies[1],ment.rect)

        if points < 35:
            pygame.draw.rect(gameDisplay, (255, 0, 0), end_rect)
        else:
            pygame.draw.rect(gameDisplay, (0, 255, 0), end_rect)

        for b in bombs:
            gameDisplay.blit(bomb, b.rect)

        gameDisplay.blit(hero0, player.rect)
        gameDisplay.blit(HAL, (stalker.rect.x, stalker.rect.y, stalker.rect.width, stalker.rect.height))
        ok = leidfinnur.findcord(stalker.rect.x,stalker.rect.y)
        path = leidfinnur.pathfinding(ma,ok,leidfinnur.findcord(player.rect.x,player.rect.y),40,30)
        #print(path)

        stalker.Stalkeron(path)
        #print (stalker.rect.x / 16, stalker.rect.y / 16)



        if hero == 1:
            gameDisplay.blit(hero0, player.rect)
            hero = 2
        elif hero == 2 and event.type == pygame.KEYDOWN:
            gameDisplay.blit(hero1, player.rect)
            hero = 3
        elif hero == 3 and event.type == pygame.KEYDOWN:
            gameDisplay.blit(hero2, player.rect)
            hero = 1
        if haswater == True:
            bucket = "Yes"
        else:
            bucket = "No"
        pygame.draw.rect(gameDisplay, (255, 255, 255), (0, 0, 80, 64))
        #print (player.rect.x /16 , player.rect.y /16)
        if player.rect != (84,32,16,16):
            t1 = time.time()
            time_Start = True
            ms = t1-t0
            sek = int(floor(ms))
            timi = myfont.render("Time: " + str(sek) + "/50", 1, (0, 0, 0))
        elif time_Start == False:
            timi = myfont.render("Time: 0/50", 1, (0, 0, 0))

        gameDisplay.blit(timi, (0, -3))
        getpoints = myfont.render("Points: "+ str(points)+"/35", 1, (0, 0, 0))
        gameDisplay.blit(getpoints, (0, 17))
        hefurfotu = myfont.render("Bucket: " + str(bucket), 1, (0, 0, 0))
        gameDisplay.blit(hefurfotu, (0, 36))



        pygame.display.flip()
    pygame.display.flip()
pygame.quit()
quit()