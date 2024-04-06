from enemy import Enemy
import pygame
import random
import os

class Sloop(Enemy, pygame.sprite.Sprite):
    speed = 1.5
    width = 45
    height = 65

    def __init__(self, screen, vessels, speed, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 65))
        sloop_image = pygame.image.load(os.path.join("images", "sloop.png"))
        self.image = sloop_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speed = speed
        self.vessels = vessels
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.y += self.speed

    def attack(self):
        pass
