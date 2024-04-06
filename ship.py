from enemy import Enemy
import pygame
import random
import os

class Ship(Enemy, pygame.sprite.Sprite):
    speed = 0.75
    width = 110
    height = 150

    def __init__(self, screen, vessels, speed, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((110, 150))
        ship_image = pygame.image.load(os.path.join("images", "ship.png")).convert_alpha()
        self.image = ship_image
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