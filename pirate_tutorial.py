import pygame
from bullet_tutorial import Bullet

class Pirate(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pirate_image = pygame.image.load("images/pirate.png")
        pirate_image = pygame.transform.scale(pirate_image, (64, 64))
        self.cannon_sound = pygame.mixer.Sound("sounds/pirate_cannon.mp3")
        self.cannon_sound.set_volume(0.1)


        self.image = pirate_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.WIDTH = WIDTH

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q] or keystate[pygame.K_LEFT]:         # Changed to allow the pirate to move with the keys "q" and "d"
            self.speedx = -8
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if self.rect.right > self.WIDTH:                            # Adjusted to allow the pirate to move up to x = 540
            self.rect.right = self.WIDTH
        elif self.rect.left < 60:                                   # Adjusted to start movement from x = 60
            self.rect.left = 60

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
        self.cannon_sound.play()
