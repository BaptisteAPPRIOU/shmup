import pygame

class Blood(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 8):
            img = pygame.image.load(f"images/blood_splatter{num}.png").convert_alpha()
            # img = pygame.transform.scale(img, (50, 50))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        self.finished = False

    def update(self):
        blood_speed = 4
        self.counter += 1

        if self.counter >= blood_speed and self.index < len(self.images) - 1:                           # Check if the counter is greater than or equal to the explosion speed and the index is less than the length of the images list minus 1
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= blood_speed:                          # Check if the index is greater than or equal to the length of the images list minus 1 and the counter is greater than or equal to the explosion speed
            self.finished = True
            self.kill()