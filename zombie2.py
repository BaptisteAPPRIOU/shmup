import pygame
import os
import math
import random
from poison_gas import PoisonGas
from blood import Blood
from pirate import Pirate

class Zombie_2(pygame.sprite.Sprite):
    def __init__(self, x, y, zombies, poison_gas,blood):
        super().__init__()
        pygame.mixer.init()
        self.images = [pygame.image.load(f"images/zombie2_{i}.png").convert_alpha() for i in range(1, 5)]   # Load zombie images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.animation_delay = 5
        self.animation_counter = 0
        self.zombies = zombies
        self.poison_gas = poison_gas
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 2000  # 2 seconds interval for shooting gas
        self.hit_points = 350
        self.mask = pygame.mask.from_surface(self.image)                                                                    # Create a mask from the image to use for collision detection
        self.hit_points = 350
        self.mask = pygame.mask.from_surface(self.image)                                                                    # Create a mask from the image to use for collision detection
        self.blood = blood
        self.blood_sound = pygame.mixer.Sound("sounds/blood.mp3")

    def update(self, pirate_x, pirate_y, blood):                                 # Update the zombie and attack
        self.rect.y += self.speed
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.attack(pirate_x, pirate_y)

    def update_hit_points(self, damage):                                # Update the hit points of the zombie
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.kill()

    def attack(self, pirate_x, pirate_y):                                 # Attack the player
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.shoot_delay = random.randint(1000, 3000)               # Randomize the shoot delay
            self.last_shot = now
            self.shoot_poison_gas(pirate_x, pirate_y)

    def shoot_poison_gas(self, pirate_x, pirate_y):                     # Shoot poison gas
        target_x = pirate_x - self.rect.centerx
        target_y = pirate_y - self.rect.centery
        angle = math.atan2(target_y, target_x)
        poison_gas = PoisonGas(self.rect.centerx, self.rect.bottom)
        poison_gas.change_x = math.cos(angle) * 5
        poison_gas.change_y = math.sin(angle) * 5
        self.poison_gas.add(poison_gas)

    def update_hit_points(self, damage):                                # Update the hit points of the zombie
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.die()

    def die(self):                                                                                                      # Method to destroy the zombie
        blood = Blood(self.rect.centerx, self.rect.centery)
        self.blood.add(blood)
        self.hit_points = 0
        self.kill()
        self.blood_sound.play()
