#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Höfundur - Ólafur Jón Valgeirsson

import pygame
import random

pygame.init()
black = (0,0,0)
resW = 640
resH = 480
RED = (255, 0, 0)
white = (255,255,255)
LEFT_BUTTON = 1

myfont = pygame.font.SysFont("Arial",30)
gameDisplay = pygame.display.set_mode((resW,resH))
pygame.display.set_caption('Völundarhús')
walls = pygame.image.load('img/Walls.jpg')
HAL = pygame.image.load('img/player.jpg')
hero0 = pygame.image.load('img/hero.png')
hero1 = pygame.image.load('img/hero1.png')
hero2 = pygame.image.load('img/hero2.png')
bomb = pygame.image.load('img/bomb.png')
fata = pygame.image.load('img/fata2.png')
clock = pygame.time.Clock()
clock.tick(60)


class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)


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
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = brick.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = brick.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = brick.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = brick.rect.bottom


# Nice class to hold a wall rectangle
class Brick(object):

    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# A class to hold the magic rectangle
class MagicBox(object):

    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class WaterBucket(object):

    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)



buckets = list()
clock = pygame.time.Clock()
bombs = list()
bricks = list()     # List to hold the walls
player = Player()   # Create the player
hero = 1
haswater = False
# Holds the level layout in a list of strings.
maze = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W---------------L-W----W-------------W-W",
"W-----------------W------------------W-W",
"WWWWWWWWWWWWWwww--W-WWWWWW-----------W-W",
"W---M-------------WMW----------------W-W",
"W---W---------------W----------------W-W",
"W---WWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWW-W-W",
"W---------------------------W------W-W-W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWW------W-W-W",
"W-------------W--------------------W-W-W",
"W-------W-----W---------W----------W-W-W",
"WWWWWWWWW-----WWWWWWWWW-W----------W-W-W",
"W-------------W---------W----------W---W",
"W---------------WWWWWWW-W----------WWWWW",
"W--------WWWWWW---------W--------------W",
"W-------------WWWW-WWWWWWWWWWWWWWWWWWWWW",
"W--------W-----------W-----------------W",
"W--------W----WWWW-WWWWWWWWWWWW--------W",
"WWWW-WWWWWWW-WW----------W-------------W",
"W-------W----------------W----W--------W",
"W-------WWWWWWWWWWWWWWW--W----W--------W",
"W-------W----------------WWWWWWWWWWWWW-W",
"WWWWWW--W-------WWWWWWW--W-------------W",
"W-------W-------W-----W--W-------------W",
"W-------WWWWWWWWW-----W--WWW-WWWW-WWWWWW",
"W-------W-------W-----W------W---------W",
"W-------W-------W-----W------W---------W",
"WWWWW-WWW-------WWWWWWW----W-WWWWWWW-WWW",
"W------------------------W-W-----------E",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# Parse the maze string above. W = wall, E = exit, M = magic box
x = 0
y = 0
for row in maze:
    for col in row:
        if col == "L":
            water = WaterBucket((x,y))
            buckets.append(water)
        if col == "W":
            bricks.append(Brick((x, y)))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        if col == "M":
            magic_rect = MagicBox((x, y))
            bombs.append(magic_rect)

        x += 16
    y += 16
    x = 0

crashed = False
points = 3
getpoints = myfont.render(str(points),1,(0,0,0))

while not crashed:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    if event.type == pygame.KEYDOWN or pygame.KEYUP:    # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)

        if player.rect.colliderect(end_rect):
            raise SystemExit, 'You win!'
        for b in bombs:
            if player.rect.colliderect(b.rect):
                if haswater == True:
                    bombs.remove(b.rect)
                    points += 5
                    haswater = False
                else:
                    raise SystemExit, 'You lose!'
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
        for brick in bricks:
            gameDisplay.blit(walls,brick.rect)

        for buck in buckets:
            gameDisplay.blit(fata,buck.rect)

        if points < 27:
            pygame.draw.rect(gameDisplay, (255, 0, 0), end_rect)
        else:
            pygame.draw.rect(gameDisplay, (0, 255, 0), end_rect)

        for b in bombs:
            gameDisplay.blit(bomb,b.rect)
        gameDisplay.blit(hero0, player.rect)
        if hero == 1:
            gameDisplay.blit(hero0,player.rect)
            hero = 2
        elif hero == 2 and event.type == pygame.KEYDOWN:
            gameDisplay.blit(hero1, player.rect)
            hero = 3
        elif hero == 3 and event.type == pygame.KEYDOWN:
            gameDisplay.blit(hero2, player.rect)
            hero = 1
        pygame.draw.rect(gameDisplay,(0,255,255),(0,0,15,30))
        getpoints = myfont.render(str(points), 1, (0, 0, 0))
        gameDisplay.blit(getpoints, (0, 0))

        pygame.display.flip()
    pygame.display.flip()
pygame.quit()

quit()