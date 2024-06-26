import pygame
import os
from poison_gas import PoisonGas
import random
from blood import Blood
from pirate import Pirate

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

        self.blood_sound = pygame.mixer.Sound("sounds/blood.wav")
        self.blood_sound.set_volume(0.2)
        self.zombie_sound = pygame.mixer.Sound("sounds/zombie2.mp3")
        self.zombie_sound.set_volume(0.1)

    # Method to update the zombie movement, animation, and attack
    def update(self, player_x, player_y, blood):                                                                                   
        self.move()  
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.attack()

    # Method to move the zombie
    def move(self):                                                                                                         
        self.rect.y += self.speed                                                                                           # Update the y position of the zombie to move downward

    # Method to make the zombie attack
    def attack(self):                                                                                                       # Method to make the zombie attack             
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:                                                                         
            self.shoot_delay = random.randint(1000, 3000)
            self.last_shot = now
            self.shoot_poison_gas()
            self.zombie_sound.play()

    # Method to make the zombie shoot poison gas
    def shoot_poison_gas(self):                                                                                             
        poison_gas = PoisonGas(self.rect.centerx, self.rect.bottom)
        poison_gas.change_y = 5
        self.poison_gas.add(poison_gas)

    # Method to update the hit points of the zombie
    def update_hit_points(self, damage):                                                                                   
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.die()

    # Method to kill the zombie
    def die(self):                                                                                                      
        blood = Blood(self.rect.centerx, self.rect.centery)
        self.blood.add(blood)
        self.hit_points = 0
        self.kill()
        self.blood_sound.play()
        self.zombie_sound.stop()