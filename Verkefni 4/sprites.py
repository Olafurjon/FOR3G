#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Höfundur - Ólafur Jón Valgeirsson

import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):

    def __init__(self,width,height,resw,resh):
        super(Enemy,self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.boomimage = pygame.image.load('img/Boom.png').convert_alpha()
        self.image = pygame.image.load('img/Tiefightersmall.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speedx = 1
        self.speedy = 9
        self.spacewidth = resw
        self.arg = "right"
        self.rect.x = 50
        self.rect.x += self.speedx
        self.down = False
        self.counter = 0
    def update1(self):
        self.move(self.arg,1)
        if self.rect.x >= (self.spacewidth - 30):
                self.arg = "left"
                self.move("down",self.speedy)
                self.counter += 1
                self.move(self.arg,self.speedx)

        if self.rect.x <= 0:
            self.arg = "right"
            self.move("down",self.speedy)
            self.counter += 1
            self.move(self.arg,self.speedx)

        if self.counter >= 5:
            self.speedx += 1
            self.speedy += 1
            self.counter = 0
        if self.rect.y > 900:
            self.kill()
            print "tie die"

    def update2(self):
        self.move(self.arg,2)
        if self.rect.x >= (self.spacewidth - 30):
            self.arg = "left"
            self.move("down",21)
            self.move(self.arg,2)

        if self.rect.x <= 0:
            self.arg = "right"
            self.move("down",21)
            self.move(self.arg,2)

        if self.rect.y > 900:
            self.kill()
            print "tie die"




    def move(self,arg,k):
        if arg == "right":
            self.rect.x += int(k)
        if arg == "left":
            self.rect.x -= k
        if arg == "leftska":
            self.rect.x -= k
            self.rect.y += k
        if arg == "rightska":
            self.rect.x += k
            self.rect.y += k
        if arg == "down":
            self.rect.y += k+9

class Enemy2(pygame.sprite.Sprite):

    def __init__(self,width,height,resw,resh):
        super(Enemy2,self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.boomimage = pygame.image.load('img/Boom.png').convert_alpha()
        self.image = pygame.image.load('img/dtiefighter2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speedx = 1
        self.speedy = 21
        self.spacewidth = resw
        self.arg = "right"
        self.rect.x = 50
        self.rect.x += self.speedx
        self.down = False





    def update1(self):
        self.move(self.arg,1)
        if self.rect.x >= (self.spacewidth - 30):
                self.arg = "left"
                self.move("down",self.speedy)
                self.move(self.arg,1)

        if self.rect.x <= 0:
            self.arg = "right"
            self.move("down",self.speedy)
            self.move(self.arg,1)


        if self.rect.y > 900:
            self.kill()
            print "tie die"

    def update2(self):
        self.move(self.arg,2)
        if self.rect.x >= (self.spacewidth - 30):
            print "snúavið"
            self.arg = "left"
            self.move("down",self.speedy)
            self.move(self.arg,self.speedx+1)

        if self.rect.x <= 0:
            self.arg = "right"
            print "snúavið"
            self.move("down",self.speedy)
            self.move(self.arg,self.speedx+1)

        if self.rect.y > 900:
            self.kill()
            print "tie die"




    def move(self,arg,k):
        if arg == "right":
            self.rect.x += int(k)
        if arg == "left":
            self.rect.x -= k
        if arg == "leftska":
            self.rect.x -= k
            self.rect.y += k
        if arg == "rightska":
            self.rect.x += k
            self.rect.y += k
        if arg == "down":
            self.rect.y += k+9

class bullets(pygame.sprite.Sprite):
    def __init__(self,width,height,Hero):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/skot1.png')
        self.rect = self.image.get_rect()
        self.counter = 0
        self.type = "straight"






class Hero(pygame.sprite.Sprite):

    def __init__(self,width,height,resw,resh):
        super(Hero,self).__init__()

        pygame.sprite.Sprite.__init__(self)
        self.imageMaster = pygame.image.load('img/serenitysmall.png')
        self.imageMaster = self.imageMaster
        self.image = self.imageMaster
        self.rect = self.image.get_rect()
        self.orig_rect = self.image.get_rect()
        self.movement = 200
        self.width = width
        self.height = height
        self.i = 0
        self.deg = 0
        self.off = 0
        self.rotator = 45
        self.angle = 0
        self.spin = 0
        self.rotate_speed = 3
        self.floating = (0,0)
        self.angle %= 360



    def turns(self,degrees, offset):
        rads = math.radians(float(degrees))
        x = math.cos(rads) * offset;
        y = math.sin(rads) * offset;
        return x, y

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def rotate(self):
        oldcenter = self.rect.center
        self.image = pygame.transform.rotate(self.imageMaster, self.angle)
        rot_rect = self.orig_rect.copy()
        rot_rect.center = self.image.get_rect().center
        self.image = self.image.subsurface(rot_rect).copy()
        self.rect.center = oldcenter

    def move_single_axis(self, dx, dy):
        # Move the rectangle
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 850:
            self.rect.y = 850
        if self.rect.x >= 600:
            self.rect.x = -30
        if self.rect.x <= -40:
            self.rect.x = 580

    def keylistener(self):
            key = pygame.key.get_pressed()
            #self.angle = math.degrees(math.atan2(self.rect.x + (self.width / 2) - self.rect.x, self.rect.y + (self.height / 2) - self.rect.y))
            if key[pygame.K_LEFT]:
                self.move(self.movement/100 * -1 , 0)
                self.floating = (-1,0)

            if  key[pygame.K_a]:
                self.angle += 5
                self.rotate()

            if key[pygame.K_RIGHT]:
                self.move(self.movement/100 , 0)
                self.floating = (1, 0)

            if key[pygame.K_d]:
                self.angle -= 5
                self.rotate()

            if key[pygame.K_RIGHT] and key[pygame.K_LEFT]:
                self.floating = (0,0)
            if key[pygame.K_UP]:
                self.move(0, (self.movement * -1) / 100)
                self.floating = (0, -1)
            if key[pygame.K_DOWN]:
                self.move(0, self.movement / 100 )
                self.floating = (0, 1)

            #print self.angle

            self.move(self.floating[0],self.floating[1])
            if self.angle > 360:
                self.angle = 0
            if self.angle < -360:
                self.angle = 0



            #self.rect.x = newX
            #self.rect.y = newY
            #print (newX,newY)










