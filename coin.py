import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        randomvalue = random.randint(1, 10)
        print(randomvalue)
        if randomvalue in [1 , 2 , 3]:
            self.value = 'red'
            for num in range(1, 7):
                img = pygame.image.load(f"images/red_coin{num}.png").convert_alpha()
                img = pygame.transform.scale(img, (32, 32))
                self.images.append(img)
        elif randomvalue in [4 , 5 , 6]:
            self.value = 'green'
            for num in range(1, 7):
                img = pygame.image.load(f"images/green_coin{num}.png").convert_alpha()
                img = pygame.transform.scale(img, (32, 32))
                self.images.append(img)
        elif randomvalue in [7 , 8 , 9]:
            self.value = 'blue'
            for num in range(1, 7):
                img = pygame.image.load(f"images/blue_coin{num}.png").convert_alpha()
                img = pygame.transform.scale(img, (32, 32))
                self.images.append(img)
        elif randomvalue in [10]:
            self.value = 'black'
            for num in range(1, 7):
                img = pygame.image.load(f"images/black_coin{num}.png").convert_alpha()
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

    # Method to update the coin animation and movement
    def update(self):
        self.move()
        self.animate()

    # Method to move the coin
    def move(self):
        self.rect.y += self.speed
        self.animate()

    # Method to animate the coin
    def animate(self):
        self.counter += 1
        if self.counter >= 3: 
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