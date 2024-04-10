from enemy import Enemy
import pygame
import random
import os
import time
from cannon_ball_enemy import CannonBallEnemy
from explosion import Explosion 

class Ship(Enemy, pygame.sprite.Sprite):
    speed = 4
    width = 110
    height = 150
    value = 500

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
        self.mask = pygame.mask.from_surface(self.image)                                                                                    # Create a mask from the image to use for collision detection
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 1000
        self.hit_points = 600

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom >= 480:
            self.speed = 0

    def attack(self, y_offsets=[-20, 15, -20]):
        if self.rect.y >= 0:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.shoot_delay = random.randint(500, 2000)
                for i, offset in enumerate([-25, 0, 25]):
                    bullet = CannonBallEnemy(self.rect.centerx + offset, self.rect.bottom)
                    bullet.rect.centerx = self.rect.centerx + offset
                    bullet.rect.bottom = self.rect.bottom + y_offsets[i]
                    self.vessels.add(bullet)
                self.last_shot = now

    def update_hit_points(self, damage):                                                                                    # Method to update the hit points of the ship
        self.hit_points -= damage
        if self.hit_points <= 0:                                                                                            # Check if the hit points are less than or equal to zero
            self.destroy()

    def destroy(self):                                                                                                      # Method to destroy the ship
        explosion = Explosion(self.rect.centerx, self.rect.centery)
        self.vessels.add(explosion)                                                                                         # Add explosion to vessels group
        self.hit_points = 0                                                                                                 # Set hit points to zero to prevent further damage
        self.kill()