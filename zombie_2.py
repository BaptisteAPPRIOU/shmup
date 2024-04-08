import pygame
import os
import math
import random
from poison_gas import PoisonGas


class Zombie_2(pygame.sprite.Sprite):
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

    def update(self, piratex, piratey):
        self.rect.y += self.speed
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        if self.rect.bottom > 900:
            self.rect.y = 0

        self.attack(piratex, piratey)

    def attack(self, piratex, piratey):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.shoot_delay = random.randint(1000, 3000)  # Randomize the shoot delay
            self.last_shot = now
            # self.shoot_poison_gas()
            self.aim_at_pirate(piratex, piratey)

    def shoot_poison_gas(self):
        poison_gas = PoisonGas(self.rect.centerx, self.rect.bottom)
        self.gas_sprites.add(poison_gas)

    def aim_at_pirate(self, pirate_x, pirate_y):
        target_x = pirate_x - self.rect.centerx
        target_y = pirate_y - self.rect.centery
        angle = math.atan2(target_y, target_x)
        poison_gas = PoisonGas(self.rect.centerx, self.rect.bottom)
        rotated_image = pygame.transform.rotate(self.images[self.index], math.degrees(angle))
        poison_gas.image = rotated_image
        poison_gas.change_x = math.cos(angle) * 5
        poison_gas.change_y = math.sin(angle) * 5
        
        # poison_gas = pygame.transform.rotate(self.images[self.index], math.degrees(angle))
        self.gas_sprites.add(poison_gas)