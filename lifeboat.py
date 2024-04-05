from enemy import Enemy
import pygame
import random

class Lifeboat(Enemy):
    def __init__(self, screen, hit_points, damage, speed, value):
        self.screen = screen
        self.width = 30
        self.height = 45
        self.speed = speed
        self.spawn()

    def spawn(self):
        self.x = random.randint(80, 520 - self.width)                                   # Ensure lifeboat is fully visible within screen width
        self.y = -self.height                                                           # Spawn from the top of the screen

    def check_overlap(self, other_lifeboats):                                           # Check if lifeboats overlap       
        for boat in other_lifeboats:
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                pygame.Rect(boat.x, boat.y, boat.width, boat.height)):
                return True
        return False

    def attack(self):
        pass

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
