import pygame
import os
from poison_gas import PoisonGas
import random

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, gas_sprites):
        super().__init__()
        # Load zombie images
        self.images = [pygame.image.load(f"images/zombie1_{i}.png").convert_alpha() for i in range(1, 5)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.animation_delay = 5
        self.animation_counter = 0
        self.gas_sprites = gas_sprites
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 2000  # 2 seconds interval for shooting gas

    def update(self, player_x, player_y):
        self.rect.y += self.speed
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        if self.rect.bottom > 900:
            self.rect.y = 0

        self.attack()

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.shoot_delay = random.randint(1000, 3000)  # Randomize the shoot delay
            self.last_shot = now
            self.shoot_poison_gas()

    def shoot_poison_gas(self):
        poison_gas = PoisonGas(self.rect.centerx, self.rect.bottom)
        poison_gas.change_y = 5
        self.gas_sprites.add(poison_gas)
