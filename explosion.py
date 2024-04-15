import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"images/exp{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (50, 50))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        self.finished = False
        self.type = type
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.mp3")
        self.explosion_sound.set_volume(0.1)

    # Method to update the explosion animation
    def update(self):
        self.explosion_sound.play()
        explosion_speed = 4
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:                           # Check if the counter is greater than or equal to the explosion speed and the index is less than the length of the images list minus 1
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:                          # Check if the index is greater than or equal to the length of the images list minus 1 and the counter is greater than or equal to the explosion speed
            self.finished = True
            self.kill()

    # Method to get the type of explosion
    def get_type(self):
        return self.type
