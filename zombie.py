import pygame
import os
from poison_gas import PoisonGas
import random
from blood import Blood

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, zombies, poison_gas, blood):
        super().__init__()
        pygame.mixer.init()
        self.images = [pygame.image.load(f"images/zombie1_{i}.png").convert_alpha() for i in range(1, 5)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.animation_delay = 5
        self.animation_counter = 0
        self.zombies = zombies
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 2000                                                                                             # Interval for shooting gas
        self.hit_points = 150
        self.mask = pygame.mask.from_surface(self.image)                                                                    # Create a mask from the image to use for collision detection
        self.poison_gas = poison_gas
        self.blood = blood

        self.blood_sound = pygame.mixer.Sound("sounds/blood.mp3")

    def update(self, player_x, player_y, blood):                                                                                   # Method to update the zombie
        self.move()  
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        if self.rect.bottom > 1000:
            self.kill()
        self.attack()

    def move(self):                                                                                                         # Method to move the zombie
        self.rect.y += self.speed                                                                                           # Update the y position of the zombie to move downward

    def attack(self):                                                                                                       # Method to make the zombie attack             
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:                                                                         
            self.shoot_delay = random.randint(1000, 3000)
            self.last_shot = now
            self.shoot_poison_gas()

    def shoot_poison_gas(self):                                                                                             # Method to make the zombie shoot poison gas
        poison_gas = PoisonGas(self.rect.centerx, self.rect.bottom)
        poison_gas.change_y = 5
        self.poison_gas.add(poison_gas)

    def update_hit_points(self, damage):                                                                                    # Method to update the hit points of the zombie
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.die()

    def die(self):                                                                                                      # Method to destroy the zombie
        blood = Blood(self.rect.centerx, self.rect.centery)
        self.blood.add(blood)
        self.hit_points = 0
        self.kill()
        self.blood_sound.play()