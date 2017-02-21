#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
pygame.display.set_caption('Músaveiðar')
background = pygame.image.load('img/bakgrunnur.jpg')
jenniwin = pygame.image.load('img/jennivannback.jpg')
tommivann = pygame.image.load('img/tommivann.jpg')
thuvannst = pygame.image.load('img/thuvannst.jpg')
spilaaftur = pygame.image.load('img/spilaaftur.png')
playagain = gameDisplay.blit(spilaaftur, (135, 210))
playagainrect = pygame.draw.rect(gameDisplay, (0, 0, 255,), (330, 430, 150, 90), 0)
gameDisplay.blit(background, (0, 0))

hola = pygame.image.load('img/musahola.png')
jenni = pygame.image.load('img/jennihola.png')
tommi = pygame.image.load('img/tommihola.png')
cheesescore = pygame.image.load('img/cheesescoreboard.png')


clock = pygame.time.Clock()
crashed = False

totalpoints = 0
jennipoints = 0
NotandiScore = 0
tommiscore = 0
Scoreboard = myfont.render("Stig: " + str(NotandiScore), 1, (0, 0, 0))
Scoreboard2 = myfont.render("Jenni Stig: " + str(jennipoints), 1, (0, 0, 0))
Scoreboard3 = myfont.render("Tommi: " + str(tommiscore), 1, (0, 0, 0))

gameDisplay.blit(cheesescore, (52,5))
gameDisplay.blit(cheesescore, (752,5))
gameDisplay.blit(Scoreboard2, (635, 0))
gameDisplay.blit(Scoreboard, (0, 0))
gameDisplay.blit(cheesescore, (750,555))
gameDisplay.blit(Scoreboard3, (668, 555))


field = []
rects = []
holur = []
location = []
clock.tick(60)
class Musaleikur: #Bý tíl músaleik klasa til að auðvelda meðhöndlun
    def geraholur(self): #býr til allar músarholurnar, bæði með holunum og gerir rect á bakvið til að meðhöndla click betur
        X = -240
        Y = 250
        J = 145
        K = 550
        i = 0
        x = 0
        while i != 64:
            x += 1

            holumaker = gameDisplay.blit(hola, (X, Y)) #býr til holur
            holur.append(holumaker)
            location.append((X, Y))
            rect = pygame.draw.rect(gameDisplay, (0, 0, 0,), (J, K, 36, 36), 0) #býr til rects
            rects.append(rect)


            Y -= 65
            K -= 65
            i += 1
            if x == 8:
                X += 65
                J += 65
                x = 0
                Y = 250
                K = 550 #

    def playerStig(self): #þegar kallað er í þetta uppfærir það töfluna með playernum og bætir við hann stigi
        global NotandiScore,pressed
        NotandiScore += 1
        Scoreboard = myfont.render("Stig: " + str(NotandiScore), 1, (0, 0, 0))
        gameDisplay.blit(cheesescore, (52, 5))
        gameDisplay.blit(Scoreboard, (0, 0))
    def jennistig(self): #sama og playerstig nema bara með jenna
        global jennipoints,pressed
        jennipoints += 1
        Scoreboard2 = myfont.render("Jenni Stig: " + str(jennipoints), 1, (0, 0, 0))
        gameDisplay.blit(cheesescore, (752, 5))
        gameDisplay.blit(Scoreboard2, (635, 0))

    def musedakottur(self):
        t = random.randint(0, 10)
        M = random.randint(0, 63)
        returns = []
        if t < 2:
            jenni_active = False
            returns.append(jenni_active)
        else:
            jenni_active = True
            returns.append(jenni_active)
        if jenni_active == True:
            gameDisplay.blit(jenni,location[M])
            returns.append(rects[M])
        else:
            gameDisplay.blit(tommi,location[M])
            returns.append(rects[M])
        return returns

    def tommibad(self): #sama og playerstig nema bara með tomma og tekur öll stig af Notanda og núllstillir
        global tommiscore, NotandiScore, relax
        tommiscore += NotandiScore
        NotandiScore = 0
        relax = 2000
        Scoreboard3 = myfont.render("Tommi: " + str(tommiscore), 1, (0, 0, 0))
        gameDisplay.blit(cheesescore, (750, 555))
        gameDisplay.blit(Scoreboard3, (668, 555))
        Scoreboard = myfont.render("Stig: " + str(NotandiScore), 1, (0, 0, 0))
        gameDisplay.blit(cheesescore, (52, 5))
        gameDisplay.blit(Scoreboard, (0, 0))

    def playagain(self):
        global endgame,NotandiScore,jennipoints,tommiscore,totalpoints
        endgame = 70
        NotandiScore = 0
        jennipoints = 0
        tommiscore = 0
        totalpoints = 0 #í vinnslu, á að leyfa manni að spila aftur án þess að þurfa endurræsa leikinn

timelast = pygame.time.get_ticks() #Meðhöndlar hvíldartímann
m = Musaleikur()
m.geraholur()
click = 0
relax = 2000 #relax minnkar eftir því sem leikurinn er spilaður meira, hægt er að hækka þessa tölu til að gera hann auðveldari í lengri tíma eða lækka til að gera han erfiðari
endgame = 50 #Leikurinn ákvarðar sigurvegara eftir að spilað hefur verið fyrir 70 stig
pressed = 0
def play():
    global field,timelast,click,relax
    timenow = pygame.time.get_ticks()
    if timenow - timelast >= relax:
        timelast = timenow
        m.geraholur()
        field = m.musedakottur()  # meöhöndlar spilun #meöhöndlar spilun

def replay():
    global timelast,click,relax,pressed,playagain,endgame
    timelast = pygame.time.get_ticks()  # Meðhöndlar hvíldartímann
    m = Musaleikur()
    m.geraholur()
    click = 0
    relax = 2000  # relax minnkar eftir því sem leikurinn er spilaður meira, hægt er að hækka þessa tölu til að gera hann auðveldari í lengri tíma eða lækka til að gera han erfiðari
    endgame = 0  # Leikurinn ákvarðar sigurvegara eftir að spilað hefur verið fyrir 70 stig
    pressed = 0
    while not crashed:
        totalpoints = NotandiScore + tommiscore + jennipoints
        if totalpoints < endgame:  # svolengi sem að engameinu er ekki náð heldur þetta áfram
            pressed = 0
            play()
            if field.__len__() != 0:
                if  event.button != 1:
                    m.jennistig()
        else:
            points = [NotandiScore, tommiscore, jennipoints]  # hver vann
            if max(points) == NotandiScore:
                gameDisplay.blit(thuvannst, (0, 0))
                playagain = gameDisplay.blit(spilaaftur, (135, 210))
            elif max(points) == tommiscore:
                gameDisplay.blit(tommivann, (0, 0))
                playagain = gameDisplay.blit(spilaaftur, (135, 210))
            elif max(points) == jennipoints:
                gameDisplay.blit(jenniwin, (0, 0))
                playagain = gameDisplay.blit(spilaaftur, (135, 210))
            pygame.display.flip()

while not crashed:
    totalpoints = NotandiScore + tommiscore + jennipoints
    if totalpoints < endgame: #svolengi sem að engameinu er ekki náð heldur þetta áfram
        pressed = 0
        play()
    else:
        points = [NotandiScore,tommiscore,jennipoints]  # hver vann
        if max(points) == NotandiScore:
            gameDisplay.blit(thuvannst, (0, 0))
            playagainrect = pygame.draw.rect(gameDisplay, (0, 0, 255,), (330, 430, 150, 90), 0)
            playagain = gameDisplay.blit(spilaaftur, (135, 210))
        elif max(points) == tommiscore:
            gameDisplay.blit(tommivann, (0, 0))
            playagain = gameDisplay.blit(spilaaftur, (135, 210))
            playagainrect = pygame.draw.rect(gameDisplay, (0, 0, 255,), (330, 430, 150, 90), 0)
        elif max(points) == jennipoints:
            gameDisplay.blit(jenniwin, (0, 0))
            playagain = gameDisplay.blit(spilaaftur, (135, 210))
            playagainrect = pygame.draw.rect(gameDisplay, (0, 0, 255,), (330, 430, 150, 90), 0)
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            if field.__len__() != 0: # kemur í veg fyrir error er ýtt er á reit áður en að mynd er birtuð
                click += 1
                if click == 10:
                    if relax > 500:
                        relax -= 200
                        click = 0
                if field[1].collidepoint(event.pos) and field[0] == True and pressed == 0: # gefur þér stig ef þú hittir á Jenna
                    if totalpoints < endgame:
                        if pressed == 0:
                            m.playerStig()
                            timelast = pygame.time.get_ticks()
                            field[0] = "inactive"
                            m.geraholur()
                            play()
                            pressed = 1

                elif field[1].collidepoint(event.pos) != pygame.mouse.get_cursor() and field[0] == True:  # gefur jenna stig ef þú klikkar og hittir ekki á jenna meðan jenni er þarna
                    if totalpoints < endgame:
                        if pressed == 0:
                            m.jennistig()
                            pressed = 1
                elif field[1].collidepoint(event.pos) and field[0] == False:  # Tommi stelur stigunum þínum ef þú klikkar á hann
                    if totalpoints < endgame:
                        if pressed == 0:
                            m.tommibad()
                            pressed = 1
                elif totalpoints > endgame and playagainrect.collidepoint(event.pos):
                    replay()
                    pygame.display.flip()
    pygame.display.flip()
pygame.quit()

quit()
