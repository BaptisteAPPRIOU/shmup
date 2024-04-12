import pygame
from bullet import Bullet

class Pirate(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets,vessels,zombies,cannon_ball_enemy,damage, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        pirate_image = pygame.image.load("images/pirate.png").convert_alpha()
        pirate_image = pygame.transform.scale(pirate_image, (64, 64))

        self.image = pirate_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.health = 100
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.WIDTH = WIDTH
        self.damage = damage
        self.vessels = vessels
        self.zombies = zombies
        self.cannon_ball_enemy = cannon_ball_enemy
        self.life = 3

    def update(self,i):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q] or keystate[pygame.K_LEFT]:                     # Changed to allow the pirate to move with the keys "q" and "d"
            self.speedx = -(8*i)
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:                    # Changed to allow the pirate to move with the keys "q" and "d"     
            self.speedx = 8*i
        self.rect.x += self.speedx

        if self.rect.right > self.WIDTH:                                        # Adjusted to allow the pirate to move up to x = 540
            self.rect.right = self.WIDTH
        elif self.rect.left < 100:                                               # Adjusted to start movement from x = 60
            self.rect.left = 100

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.vessels, self.zombies, self.cannon_ball_enemy, self.damage)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)