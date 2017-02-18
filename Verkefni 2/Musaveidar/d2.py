import pygame
import random

pygame.init()

LEFT_BUTTON = 1
WINDOW_SIZE = (545, 485)
BACKGROUND = (50,50,50)
HOLE_COLOR = (182,109,13)
MOUSE = (87, 184, 255)
CAT = (254, 104, 71)
font = pygame.font.Font(None, 30)

hole_index_number = 0
counter = 0
limit = 4900
life = 6
score = 0
it_is_a_cat = False

window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(BACKGROUND)

# a list to keep the holes in
holes = list()

running = True

class Holes: #Class for everything
    def create(self): #Creates the holes
        for i in range(5, 440, 55):
            for n in range(5, 440, 55):
                holes.append(pygame.Rect(n, i, 50, 50))
    def Draw(self): #Draws them on the screen
        for hole in holes:
            pygame.draw.rect(window, HOLE_COLOR, hole)

       # highscore = font.render("High Score: Alexander: 174", 1, (255, 255, 255))
        #pygame.Surface.blit(window, highscore, (0, 460))

    def CatMouse(self): #This does almost everything
        global hole_index_number, it_is_a_cat, limit, counter, score
        if(limit <= 1900): #if the timer is less than 1900 starting lowering it faster
            limit -= 10
        elif(score % 10 == 0 and limit > 1700): #Else lower it slow and steady
            limit -= 300
        counter = 0
        if random.randint(1, 10) < 3: #Random factor to show the red square you shouldn't push
            it_is_a_cat = True
        else:
            it_is_a_cat = False
        pygame.draw.rect(window, HOLE_COLOR, holes[hole_index_number])
        # now we need to "find a hole" for the animal to appear in.
        # in this case it's a number between 0 and 63 corresponding to the
        # elements in the holes-list
        hole_index_number = random.randrange(0, 63)
        # and finally we draw the animal in the chosen hole.
        if it_is_a_cat:
            pygame.draw.rect(window, CAT, holes[hole_index_number])
        else:
            pygame.draw.rect(window, MOUSE, holes[hole_index_number])

    def ScoreBoard(self, score): #Draws the score board
        global life
        scoretext = font.render("Score:" + str(score), 1, (255,255,255))
        lifetext = font.render("life:" + str(life), 1, (255,255,255))
        pygame.draw.rect(window, BACKGROUND, (445, 10, 100, 60))
        pygame.Surface.blit(window, scoretext, (445,10))
        pygame.Surface.blit(window, lifetext, (445,35))

Whacker = Holes()
Whacker.create() #Creates the squares
Whacker.Draw() #Draws them
Whacker.CatMouse() #Picks a hole to show the mouse
Whacker.ScoreBoard(score) #Prints the scoreboard
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        for hole in holes:
            if hole.collidepoint(event.pos):
                # if there is a collision the index number of that list element(hole)
                # is compared with the value in the hole_index_number to see if there
                # is an animal there. If it turns out to be the cat, some text is printed
                # on the screen and if it is a mouse, something else is printed.
                if holes.index(hole) == hole_index_number: #If you clicked the hole with the mouse/cat
                    if it_is_a_cat: #If it was a red square (bad)
                        life -= 1
                        Whacker.CatMouse()
                        Whacker.ScoreBoard(score)
                    else: #Else good job, give him a point
                        score += 1
                        Whacker.CatMouse()
                        Whacker.ScoreBoard(score)
    if counter == limit and it_is_a_cat == False: #If the timer is finished and you didn't press the blue square
        life -= 1
        Whacker.CatMouse()
        Whacker.ScoreBoard(score)
    elif counter == 3000 and it_is_a_cat == True: #If the timer is finished and you didn't press the red square
        score += 1
        Whacker.CatMouse()
        Whacker.ScoreBoard(score)
    else: #Else raise the counter (timer)
        counter += 1

    if life == 0: #If you finished your life you loose
        counter = 0
        Whacker.Draw()
        print(score)
        running = False

    pygame.display.flip()