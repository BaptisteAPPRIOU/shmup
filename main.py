import pygame
import os
from zombie import Zombie


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 900), pygame.NOFRAME)
        self.statistics_bar = pygame.Rect(0, 0, 100, 900)
        self.wall = pygame.Rect(60, 800, 540, 10)
        self.gas_sprites = pygame.sprite.Group()  # Create a sprite group for gas_sprites
        self.all_sprites = pygame.sprite.Group()  # Create a sprite group for all sprites
        self.zombie = Zombie(300, 100, self.gas_sprites)  # Create a zombie instance
        self.beach = pygame.image.load(os.path.join("images", "beach.png")).convert()
        self.water = pygame.image.load(os.path.join("images", "water.png")).convert()
        self.all_sprites.add(self.zombie)  # Add the zombie to the sprite group

        self.gas_timer = 0
        self.gas_interval = 2000  # 1 second interval


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

            # Update the zombie
            self.all_sprites.update()
            self.gas_sprites.update()

            self.gas_timer += dt 
            if self.gas_timer >= self.gas_interval:
                self.zombie.shoot_poison_gas()
                self.gas_timer = 0

            for y in range(0,900, self.water.get_height()):
                for x in range(0, 640, self.water.get_width()):
                    self.screen.blit(self.water, (x, y))

            for y in range(540, 900, self.beach.get_height()):
                for x in range(100, 640, self.beach.get_width()):
                    self.screen.blit(self.beach, (x, y))

            self.all_sprites.draw(self.screen)                                  # Draw all sprites
            self.gas_sprites.draw(self.screen)                                  # Draw gas_sprites

            pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
            pygame.draw.rect(self.screen, "BLUE", self.wall)

            # Draw the zombie
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    Main().run()
