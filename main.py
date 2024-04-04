import pygame
import random
from pirate import Pirate
from map_game import mapGame

class Main:
    def __init__(self):
        pygame.init()
        self.map_game = mapGame()
        self.map_game.draw()

        screen_width = self.map_game.screen.get_width()
        screen_height = self.map_game.screen.get_height()

        self.all_sprites = pygame.sprite.Group()                                            # Create sprite group        
        self.bullets = pygame.sprite.Group()                                                # Create bullet sprite group        
        
        self.pirate = Pirate(self.all_sprites, self.bullets, screen_width, screen_height)   # Create player pirate instance and add it to sprite group
        self.all_sprites.add(self.pirate)
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.pirate.shoot()

                        
            self.map_game.screen.fill((255,255,255))
            self.map_game.draw()
            self.all_sprites.update()
            self.all_sprites.draw(self.map_game.screen)
            self.map_game.update_display()
            
        self.map_game.quit()

if __name__ == "__main__":
    main = Main()
    main.run()