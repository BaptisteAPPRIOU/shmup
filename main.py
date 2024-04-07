import pygame
from lifeboat import Lifeboat
from sloop import Sloop
from enemy_wave import Wave
from ship import Ship
from pirate import Pirate
from bullet import Bullet
import time
from explosion import Explosion
from water import Water
from coin import Coin
  
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.statistics_bar = pygame.Rect(0, 0, 100, 900)
        self.wall = pygame.Rect(60, 800, 540, 10)
        self.vessels = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group() 
        self.beach = pygame.image.load("images/beach.png")
        self.dock = pygame.image.load("images/dock.png")

        self.water_images = [
            pygame.transform.scale(pygame.image.load("images/water.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water1.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water2.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water3.png").convert_alpha(), (24, 24)),
        ]

        self.background_sprites = pygame.sprite.Group()
        for y in range(0, 540, 24):                                                                                            
            for x in range(112, 650, 24):                                                                                       # Loop through the screen width in steps of 24 and create water sprites
                water_sprite = Water(x, y, self.water_images)
                self.background_sprites.add(water_sprite)
        
        for y in range(540, 1000, self.beach.get_height()):                                                                     # Loop through the screen height in steps of the beach image height and create beach sprites    
            for x in range(100, 640, self.beach.get_width()):  
                beach_sprite = pygame.sprite.Sprite()
                beach_sprite.image = self.beach
                beach_sprite.rect = beach_sprite.image.get_rect(topleft=(x, y))
                self.background_sprites.add(beach_sprite)

        dock_width = self.dock.get_width()
        for x in range(100, 640, dock_width):                                                                                   # Loop through the screen width in steps of the dock image width and create dock sprites               
            dock_sprite = pygame.sprite.Sprite()
            dock_sprite.image = self.dock
            dock_sprite.rect = dock_sprite.image.get_rect(topleft=(x, 480))
            self.background_sprites.add(dock_sprite)

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.pirate = Pirate(self.all_sprites, self.bullets, self.vessels,self.screen.get_width(), self.screen.get_height())    # Create player pirate instance and add it to sprite group
        self.all_sprites.add(self.pirate)

    def run(self):                                                                                                              # Main game loop
        waves = [                                                                                                               # List of waves
            Wave(self.screen, self.vessels, [Lifeboat], [5], 5),                        
            Wave(self.screen, self.vessels, [Lifeboat], [5], 5), 
            Wave(self.screen, self.vessels, [Lifeboat], [10], 5),
            Wave(self.screen, self.vessels, [Lifeboat], [20], 5),
            Wave(self.screen, self.vessels, [Sloop], [3], 5)
        ]

        clock = pygame.time.Clock()
        running = True
        current_wave = 0
        while running:
            dt = clock.tick(60) / 1000                                                                                          # Convert milliseconds to seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.pirate.shoot()

            waves[current_wave].spawn_waves(dt)                                 # Spawn waves of enemies

            self.background_sprites.update()                                         # Update water sprites

            pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
            pygame.draw.rect(self.screen, "BLUE", self.wall)

            self.background_sprites.draw(self.screen)                                # Draw water sprites   

            self.all_sprites.update()                                           # Update all sprites
            self.all_sprites.draw(self.screen)                                  # Draw all sprites

            for vessel in self.vessels:
                if not isinstance(vessel, Explosion):
                    vessel.move()
                    self.screen.blit(vessel.image, vessel.rect)
                    if isinstance(vessel, Lifeboat) or isinstance(vessel, Sloop) or isinstance(vessel, Ship):
                        vessel.attack()

            for explosion in self.vessels.copy():                                   # Use copy() to avoid modifying the original while iterating
                if isinstance(explosion, Explosion):
                    explosion.update()
                    self.screen.blit(explosion.image, explosion.rect)
                    if explosion.finished:                                          # Check if explosion animation has finished
                        for vessel in self.vessels:
                            if vessel.rect.colliderect(explosion.rect):
                                self.vessels.remove(vessel)
                                self.vessels.remove(explosion)
                                coin = Coin(explosion.rect.centerx, explosion.rect.centery, 100)
                                self.coins.add(coin)
                                break  # Break the loop after adding the coin
                        break  # Break the loop after processing the explosion

            self.coins.update()                                                     # Update coin sprites
            self.coins.draw(self.screen)                                            # Draw coin sprites

            pygame.display.flip()
            pygame.time.Clock().tick(60)

            if all(count == 0 for count in waves[current_wave].counts):             # Check if all enemies in the current wave have been spawned
                current_wave += 1

            if current_wave == len(waves):                                          # Check if all waves have been spawned
                if any(w.current_wave < len(w.enemy_types) for w in waves):         # Check if there are more waves to spawn
                    current_wave -= 1
                else:
                    break

        pygame.quit()
if __name__ == "__main__":
    Main().run()
