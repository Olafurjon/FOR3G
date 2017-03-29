import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self,width,height):
        super(Enemy,self).__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Tiefightersmall.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self,k,resw,resh):
        self.rect.x += k
        k += 1







