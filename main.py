import pygame
import os
from zombie import Zombie
from zombie_2 import Zombie_2
from pirate import Pirate

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 900), pygame.NOFRAME)
        self.statistics_bar = pygame.Rect(0, 0, 100, 900)
        self.wall = pygame.Rect(60, 800, 540, 10)
        self.gas_sprites = pygame.sprite.Group()                                            # Create a sprite group for gas_sprites
        self.all_sprites = pygame.sprite.Group()                                            # Create a sprite group for all sprites
        self.all_sprites2 = pygame.sprite.Group()                                           # Create sprite group        
        self.bullets = pygame.sprite.Group()                                                # Create bullet sprite group
        self.zombie = Zombie(300, 100, self.gas_sprites)                                    # Create a zombie instance
        self.zombie_2 = Zombie_2(500, 100, self.gas_sprites)                                # Create a zombie instance
        self.beach = pygame.image.load(os.path.join("images", "beach.png")).convert()
        self.water = pygame.image.load(os.path.join("images", "water.png")).convert()
        self.all_sprites.add(self.zombie)                                                   # Add the zombie to the sprite group
        self.all_sprites.add(self.zombie_2)                                                 # Add the zombie to the sprite group
        self.pirate = Pirate(self.all_sprites2, self.bullets, 640, 900)
        self.all_sprites2.add(self.pirate)   
        self.gas_timer = 0
        self.gas_interval = 2000  # 1 second interval
        self.font = pygame.font.Font("Fonts/Minecraft.ttf", 12)  # Create a font object
        self.user_label = self.font.render("User: user", 1, (0, 255, 255))
        self.score_label = self.font.render("Score : ", 1, (0, 255, 255))
        self.score_label2 = self.font.render(str(self.pirate.score), 1, (0, 255, 255))

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.pirate.score += 10
                        self.score_label2 = self.font.render(str(self.pirate.score), 1, (0, 255, 255))
                        self.pirate.shoot()
            # Update the zombie
            self.all_sprites.update(self.pirate.rect.centerx, self.pirate.rect.centery) 
            self.all_sprites2.update()
            self.bullets.update()
            self.gas_sprites.update()

            for y in range(0,900, self.water.get_height()):
                for x in range(0, 640, self.water.get_width()):
                    self.screen.blit(self.water, (x, y))

            for y in range(540, 900, self.beach.get_height()):
                for x in range(100, 640, self.beach.get_width()):
                    self.screen.blit(self.beach, (x, y))

            self.all_sprites.draw(self.screen)                                  # Draw all sprites
            self.gas_sprites.draw(self.screen)                                  # Draw gas_sprites
            self.all_sprites2.draw(self.screen)                                  # Draw all sprites
            self.bullets.draw(self.screen)                                      # Draw bullets
            pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
            pygame.draw.rect(self.screen, "BLUE", self.wall)
            self.screen.blit(self.user_label, (10, 10))
            self.screen.blit(self.score_label, (10, 30))
            self.screen.blit(self.score_label2, (10, 41))
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    Main().run()