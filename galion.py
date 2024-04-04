import enemy_creator
import random
import pygame

class Galion(enemy_creator.Enemy):
    
    def __init__(self, screen, hit_points, damage, speed, value):
        super().__init__(hit_points, damage, speed, value)
        self.screen = screen
        self.width = 440
        self.height = 440
        self.speed = speed
        self.spawned = False

    def spawn(self):
        self.x = random.randint(80, 520 - self.width)
        self.y = -self.height
        self.spawned = True

    def move(self):
        if self.spawned:
            self.y += self.speed
            if self.y == -300:
                self.speed = 0

    def draw(self):
        if self.spawned:
            pygame.draw.rect(self.screen, "RED", (self.x, self.y, self.width, self.height))

    def attack(self):
        pass

