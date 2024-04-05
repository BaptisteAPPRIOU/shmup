from enemy import Enemy
import pygame
import random

class Sloop(Enemy, pygame.sprite.Sprite):
    def __init__(self, screen, vessels, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 65))
        self.image.fill("BLUE")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speed = speed
        self.vessels = vessels
        self.spawn()

    def spawn(self):
        while True:
            self.rect.x = random.randint(80, 520 - self.rect.width)
            self.rect.y = random.randint(-1500, -300)
            if not self.check_overlap(self.vessels):
                break

    def check_overlap(self, other_ships):
        for ship in other_ships:
            if ship != self and self.rect.colliderect(ship.rect):
                return True
        return False  



    def move(self):
        self.rect.y += self.speed

    def attack(self):
        pass
