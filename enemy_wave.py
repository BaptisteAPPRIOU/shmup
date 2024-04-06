import pygame
import random
from enemy import Enemy
import sys
import os
from lifeboat_test import Lifeboat
from sloop_test import Sloop

class Wave:
    def __init__(self, screen, vessels, enemy_types, counts, pause_duration):
        self.screen = screen
        self.vessels = vessels
        self.enemy_types = enemy_types
        self.counts = counts
        self.pause_duration = pause_duration
        self.timer = 0
        self.current_wave = 0

    def update(self, dt):
        if self.current_wave < len(self.enemy_types):
            enemy_type = self.enemy_types[self.current_wave]
            count = self.counts[self.current_wave]
            if count > 0:
                self.timer += dt
                if self.timer >= 3:  # Delay in seconds between enemy spawns
                    self.timer = 0
                    x = random.randint(80, 520 - enemy_type.width)
                    y = random.randint(-1500, -300)
                    while self.check_overlap(x, y, enemy_type):
                        x = random.randint(80, 520 - enemy_type.width)
                        y = random.randint(-1500, -300)
                    enemy = enemy_type(self.screen, self.vessels, speed=enemy_type.speed, x=x, y=y)
                    self.vessels.add(enemy)
                    self.counts[self.current_wave] -= 1
            else:
                self.timer += dt  # Increment timer during pause
                if self.timer >= self.pause_duration:  # Delay in seconds between waves
                    self.timer = 0
                    self.current_wave += 1

    def check_overlap(self, x, y, enemy_type):
        for vessel in self.vessels:
            if isinstance(vessel, enemy_type) and vessel.rect.colliderect(pygame.Rect(x, y, enemy_type.width, enemy_type.height)):
                return True
        return False