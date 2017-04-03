import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self,width,height,resw,resh):
        super(Enemy,self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Tiefightersmall.png').convert_alpha()
        self.rect = self.image.get_rect()


    def move(self,arg,k):
        if arg == "right":
            self.rect.x += k
        if arg == "left":
            self.rect.x -= k
        if arg == "leftska":
            self.rect.x -= 1
            self.rect.y += 1
        if arg == "rightska":
            self.rect.x += 1
            self.rect.y += 1
        if arg == "down":
            i = 0
            while i < 10:
                self.rect.y += 1
                i+=1

class bullets(pygame.sprite.Sprite):
    def __init__(self,width,height,Hero):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/skot1.png')
        self.rect = self.image.get_rect()
        self.rect.y = Hero.rect.y - 27
        self.rect.x = Hero.rect.x + 12





class Hero(pygame.sprite.Sprite):

    def __init__(self,width,height,resw,resh):
        super(Hero,self).__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/serenitysmall.png')
        self.rect = self.image.get_rect()


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
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 850:
            self.rect.y = 850
        if self.rect.x >= 600:
            self.rect.x = -30
        if self.rect.x <= -40:
            self.rect.x = 580












