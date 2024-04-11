import pygame
import random


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"images/coin{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (32, 32))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        self.finished = False
        self.speed = 5
        self.mask = pygame.mask.from_surface(self.image)
        randomvalue = random.randint(1, 3)
        if randomvalue == 1:
            self.value = 'rouge'
        elif randomvalue == 2:
            self.value = 'vert'
        elif randomvalue == 3:
            self.value = 'bleu'

    def update(self):
        self.move()
        self.animate()

    def move(self):
        self.rect.y += self.speed
        self.animate()

    def animate(self):
        self.counter += 1
        if self.counter >= 3:  # Adjust the speed of animation by changing this value
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

    def get_coordinates(self, a, b):
        pass

    def get_value(self):
        return self.value
    
    def get_spawn_value(self):
        pass