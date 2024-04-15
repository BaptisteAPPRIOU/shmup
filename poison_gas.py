import pygame

class PoisonGas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(f"images/gas{i}.png").convert_alpha(), (32, 32)) for i in range(1, 9)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4
        self.animation_delay = 3
        self.animation_counter = 0
        self.change_x = 0
        self.change_y = 0

    # Method to update the poison gas animation
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        if self.rect.top > 1000 or self.rect.left < 100 or self.rect.right > 640:
            self.kill()

    def get_coordinates(self, a, b):
        pass

    def update_hit_points(self, damage):
        pass