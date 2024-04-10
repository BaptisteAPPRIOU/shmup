import pygame
import os
from poison_gas import PoisonGas
import random

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, vessels):
        super().__init__()
        self.images = [pygame.image.load(f"images/zombie1_{i}.png").convert_alpha() for i in range(1, 5)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.animation_delay = 5
        self.animation_counter = 0
        self.vessels = vessels
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 2000  # 2 seconds interval for shooting gas

    def update(self, player_x, player_y):
        self.move()  # Call the move method in the update method
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        if self.rect.bottom > 900:
            self.kill()
        self.attack()

    def move(self):
        self.rect.y += self.speed  # Update the y position of the zombie to move downward

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.shoot_delay = random.randint(1000, 3000)
            self.last_shot = now
            self.shoot_poison_gas()

    def shoot_poison_gas(self):
        poison_gas = PoisonGas(self.rect.centerx, self.rect.bottom)
        poison_gas.change_y = 5
        self.vessels.add(poison_gas)