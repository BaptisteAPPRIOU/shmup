import pygame

class PoisonGas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load poison gas images
        self.images = [pygame.transform.scale(pygame.image.load(f"images/gas{i}.png").convert_alpha(), (32, 32)) for i in range(1, 9)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4
        self.animation_delay = 3
        self.animation_counter = 0

    def update(self):
        self.rect.y += self.speed
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        if self.rect.top > 900:
            self.kill()  # Remove the poison gas sprite when it goes off-screen