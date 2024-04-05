import pygame
import random
from enemy import Enemy

class Lifeboat(Enemy, pygame.sprite.Sprite):
    def __init__(self, screen, vessels, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 45))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speed = speed
        self.vessels = vessels
        self.spawn()

    def spawn(self):
        max_attempts = 100  # Limiting the number of attempts to avoid infinite loop
        for _ in range(max_attempts):
            self.rect.x = random.randint(80, 520 - self.rect.width)
            self.rect.y = random.randint(-1500, -300)
            if not self.check_overlap(self.vessels) and not self.check_pre_spawn():
                break
        else:
            print("Error: Could not spawn Lifeboat after", max_attempts, "attempts.")

    def check_overlap(self, other_ships):
        collisions = pygame.sprite.spritecollide(self, other_ships, False)
        return len(collisions) > 1

    def check_pre_spawn(self):
        for ship in self.vessels:
            if isinstance(ship, Lifeboat) and abs(ship.rect.centerx - self.rect.centerx) < self.rect.width + ship.rect.width and ship.rect.top < 320:
                return True
        return False 

    def move(self):
        self.rect.y += self.speed

    def attack(self):
        pass
