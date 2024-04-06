import pygame
import random
from enemy import Enemy
import sys
import os

class Lifeboat(Enemy, pygame.sprite.Sprite):
    speed = 2
    width = 45
    height = 55

    def __init__(self, screen, vessels, speed, x, y):
        pygame.sprite.Sprite.__init__(self)
        lifeboat_image = pygame.image.load(os.path.join("images", "lifeboat.png")).convert_alpha()
        lifeboat_image = pygame.transform.scale(lifeboat_image, (45, 55))
        self.image = lifeboat_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speed = speed
        self.vessels = vessels
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.y += self.speed

    def attack(self):
        pass
