import enemy_creator
import pygame
import random

class Sloop(enemy_creator.Enemy):
    def __init__(self, screen, hit_points, damage, speed, value):
        self.screen = screen
        self.speed = speed
        self.width = 45
        self.height = 65
        self.spawn()

    def spawn(self):
        self.x = random.randint(80, 520 - self.width)
        self.y = -self.height

    def check_overlap(self, other_sloops):
        for sloop in other_sloops:
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                pygame.Rect(sloop.x, sloop.y, sloop.width, sloop.height)):
                return True
        return False

    def attack(self):
        pass

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, "BLUE", (self.x, self.y, self.width, self.height))