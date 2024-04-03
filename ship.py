import enemy_creator
import pygame
import random

class Ship(enemy_creator.Enemy):

    def __init__(self, screen, hit_points, damage, speed, value):
        self.screen = screen
        self.speed = speed
        self.width = 65
        self.height = 100
        self.spawn()

    def spawn(self):
        self.x = random.randint(80, 520 - self.width)
        self.y = -self.height

    def check_overlap(self, other_ships):
        for ship in other_ships:
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                pygame.Rect(ship.x, ship.y, ship.width, ship.height)):
                return True
        return False    

    def attack(self):
        pass

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, "GREEN", (self.x, self.y, self.width, self.height))