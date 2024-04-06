import pygame
from pygame.sprite import Sprite

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vessels):
        pygame.sprite.Sprite.__init__(self)
        cannon_ball = pygame.image.load("images/cannon_ball.png")
        self.image = cannon_ball
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.vessels = vessels
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

        collisions = pygame.sprite.spritecollide(self, self.vessels, True, pygame.sprite.collide_mask)
        if collisions:
            for collision in collisions:
                collision.kill()
            self.kill()

    