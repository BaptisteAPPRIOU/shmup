import pygame
from bullet import Bullet
import sys
import os

class Pirate(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets,vessels, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        pirate_image = pygame.image.load("images/pirate.png").convert_alpha()
        pirate_image = pygame.transform.scale(pirate_image, (64, 64))

        self.image = pirate_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.WIDTH = WIDTH
        self.vessels = vessels

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q] or keystate[pygame.K_LEFT]:                     # Changed to allow the pirate to move with the keys "q" and "d"
            self.speedx = -8
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:                    # Changed to allow the pirate to move with the keys "q" and "d"     
            self.speedx = 8
        self.rect.x += self.speedx

        if self.rect.right > self.WIDTH:                                        # Adjusted to allow the pirate to move up to x = 540
            self.rect.right = self.WIDTH
        elif self.rect.left < 100:                                               # Adjusted to start movement from x = 60
            self.rect.left = 100

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.vessels)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)