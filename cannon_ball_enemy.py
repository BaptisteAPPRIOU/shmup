import pygame
import os

class CannonBallEnemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "cannon_ball_enemies.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5

    def update(self):
        self.move()
        if self.rect.bottom < 0:
            self.kill()

    def move(self):
        self.rect.y += self.speed

    def get_coordinates(self, a, b):
        pass
    
    def get_spawn_value(self):
        pass