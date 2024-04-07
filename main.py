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
  
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 900), pygame.NOFRAME)
        self.statistics_bar = pygame.Rect(0, 0, 100, 900)
        self.wall = pygame.Rect(60, 800, 540, 10)
        self.vessels = pygame.sprite.Group()
        self.beach = pygame.image.load("images/beach.png")

        self.water_images = [
            pygame.transform.scale(pygame.image.load("images/water.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water1.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water2.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water3.png").convert_alpha(), (24, 24)),
        ]
        self.water_sprites = pygame.sprite.Group()
        for y in range(0, 540, 24):                                                                                             # Use the height of your water images
            for x in range(112, 650, 24):                                                                                        # Use the width of your water images
                water_sprite = Water(x, y, self.water_images)
                self.water_sprites.add(water_sprite)

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
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

            self.water_sprites.update()                                         # Update water sprites

            pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
            pygame.draw.rect(self.screen, "BLUE", self.wall)

            self.water_sprites.draw(self.screen)                                # Draw water sprites   

            for y in range(540, 900, self.beach.get_height()):                  # Draw beach  
                for x in range(100, 640, self.beach.get_width()):  
                    self.screen.blit(self.beach, (x, y))

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
                         self.vessels.remove(explosion)
                         self.vessels.remove(Lifeboat)

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
