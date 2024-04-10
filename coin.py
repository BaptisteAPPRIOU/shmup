import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, value):
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
        self.value = value
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.move()
        self.animate()

    def move(self):
        self.rect.y += self.speed

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
