import pygame
import random
from enemy import Enemy
import sys
import os

class Wave:
    def __init__(self, screen, vessels,cannon_ball_enemy, enemy_types, counts, pause_duration, explosions):                       
        self.screen = screen
        self.vessels = vessels
        self.cannon_ball_enemy = cannon_ball_enemy
        self.enemy_types = enemy_types
        self.counts = counts
        self.pause_duration = pause_duration
        self.explosions = explosions
        self.timer = 0
        self.current_wave = 0

    # Method to spawn waves of enemies
    def spawn_waves(self, dt):                                                      # Spawn waves of enemies
        if self.current_wave < len(self.enemy_types):                               # Check if there are more waves to spawn
            enemy_type = self.enemy_types[self.current_wave]                        # Get the enemy type for the current wave       
            count = self.counts[self.current_wave]                                  # Get the number of enemies to spawn for the current wave

            if count > 0:                                                           # Check if there are enemies left to spawn
                self.timer += dt                                                    # Increment timer during enemy spawn 
                               
                if self.timer >= 3:                                                 # Delay in seconds between enemy spawns
                    self.timer = 0                                                  # Reset timer             
                    x = random.randint(120, 520 - enemy_type.width)                  # Random x-coordinate for enemy spawn       
                    y = random.randint(-1500, -300)                                 # Random y-coordinate for enemy spawn
                    
                    while self.check_overlap(x, y, enemy_type):                     # Check if the enemy overlaps with other enemies
                        x = random.randint(120, 520 - enemy_type.width)              # Random x-coordinate for enemy spawn
                        y = random.randint(-1500, -300)                             # Random y-coordinate for enemy spawn
                    enemy = enemy_type(self.screen, self.vessels, self.cannon_ball_enemy,self.explosions, speed=enemy_type.speed, x=x, y=y)             # Create an enemy object
                    
                    self.vessels.add(enemy)                                         # Add the enemy to the vessels group
                    self.counts[self.current_wave] -= 1                             # Decrement the number of enemies left to spawn
            else:
                self.timer += dt                                                    # Increment timer during pause
                if self.timer >= self.pause_duration:                               # Delay in seconds between waves
                    self.timer = 0
                    self.current_wave += 1

    # Method to check if enemies overlap
    def check_overlap(self, x, y, enemy_type):
        for vessel in self.vessels:
            if isinstance(vessel, enemy_type) and vessel.rect.colliderect(pygame.Rect(x, y, enemy_type.width, enemy_type.height)):
                return True
        return False