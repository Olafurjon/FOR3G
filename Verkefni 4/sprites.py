import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self,width,height,resw,resh):
        super(Enemy,self).__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Tiefightersmall.png').convert_alpha()
        self.rect = self.image.get_rect()
    def move(self,arg):
        if arg == "right":
            self.rect.x += 1
        if arg == "left":
            self.rect.x -= 1
        if arg == "down":
            self.rect.y += 10

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










