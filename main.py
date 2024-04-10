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
from spawn import SpawnZombie
import random

class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.statistics_bar = pygame.Rect(0, 0, 100, 900)
        self.wall = pygame.Rect(60, 800, 540, 10)
        self.total_score = 57
        self.timer = 0

        self.vessels = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.pirate_group = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.cannon_ball_enemies = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()

        self.coin_sound = pygame.mixer.Sound("sounds/coins.mp3")

        self.font = pygame.font.Font("Fonts/Minecraft.ttf", 15)  # Create a font object
        self.user_label = self.font.render("User: user", 1, (0, 255, 255))
        self.score_label = self.font.render("SCORE : ", 1, (0, 255, 255))
        self.score_label2 = self.font.render(str(self.total_score), 1, (0, 255, 255))

        self.beach = pygame.image.load("images/beach.png").convert_alpha()
        self.dock = pygame.image.load("images/dock.png").convert_alpha()

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

        self.pirate = Pirate(self.pirate_group, self.bullets, self.vessels,self.screen.get_width(), self.screen.get_height())    # Create player pirate instance and add it to sprite group
        self.pirate_group.add(self.pirate)

    def run(self):                                                                                                              # Main game loop
        waves = [                                                                                                               # List of waves
            Wave(self.screen, self.vessels, [Lifeboat], [2], 5),
            Wave(self.screen, self.vessels, [Lifeboat], [3], 5),
            Wave(self.screen, self.vessels, [Lifeboat], [5], 5),
            Wave(self.screen, self.vessels, [Lifeboat], [8], 5),
            #Wave(self.screen, self.vessels, [Sloop], [10], 5),

        ]

        clock = pygame.time.Clock()
        running = True
        current_wave = 0
        # coin = Coin(-100, -100, 0)
        self.score_label2 = self.font.render(str(self.total_score), 1, (0, 255, 255))
        while running:

            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.pirate.shoot()

            waves[current_wave].spawn_waves(dt)                                                                                     # Spawn waves of enemies

            self.background_sprites.update()                                                                                        # Update water sprites
            self.screen.fill((0, 0, 0))                                                                                             # Fill the screen with black color

            pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
            pygame.draw.rect(self.screen, "BLUE", self.wall)

            self.background_sprites.draw(self.screen)                                                                               # Draw water sprites

            self.pirate_group.update()                                                                                              # Update pirate sprite
            self.pirate_group.draw(self.screen)                                                                                     # Draw pirate sprites
            self.zombies.update(self.pirate.rect.centerx, self.pirate.rect.centery)
            self.zombies.draw(self.screen)

            self.timer += dt
            
                
            for vessel in self.vessels:                                                                                             # Loop through all vessels
                #print (vessel)
                if not isinstance(vessel, Explosion):
                    vessel.move()                                                              # Move the vessel
                    vessel.get_coordinates(self.pirate.rect.centerx, self.pirate.rect.centery)
                    self.screen.blit(vessel.image, vessel.rect)
                    if vessel.get_spawn_value() == True:
                        print("Spawn can zombie")
                        if self.timer >= 4:
                            lucky_number = random.randint(1, 5)
                            print(self.timer)
                            if lucky_number == (1 or 2 or 3 or 4):
                                SpawnZombie(vessel.rect.centerx, vessel.rect.bottom, self.zombies, 1)
                            elif lucky_number == 5:
                                SpawnZombie(vessel.rect.centerx, vessel.rect.bottom, self.zombies, 2)
                            print (self.timer)
                    if isinstance(vessel, Lifeboat) or isinstance(vessel, Sloop) or isinstance(vessel, Ship):
                        vessel.attack()
            
            if self.timer >= 4:
                self.timer -= 4

            for explosion in self.vessels.copy():                                                                                   # Use copy() to avoid modifying the original while iterating
                if isinstance(explosion, Explosion):
                    explosion.update()
                    self.screen.blit(explosion.image, explosion.rect)
                    if explosion.finished:                                                                                          # Check if explosion animation has finished
                        for vessel in self.vessels:
                            if isinstance(vessel, Ship) or isinstance(vessel, Sloop) or isinstance(vessel, Lifeboat):
                                if vessel.rect.colliderect(explosion.rect):
                                    self.vessels.remove(vessel)
                                    self.vessels.remove(explosion)
                                    coin_value = 0
                                if isinstance(vessel, Lifeboat):
                                    coin_value = 100
                                    # print("Coin value",coin_value)
                                elif isinstance(vessel, Sloop):
                                    coin_value = 300
                                elif isinstance(vessel, Ship):
                                    coin_value = 500
                                coin = Coin(explosion.rect.centerx, explosion.rect.centery, coin_value)
                                self.coins.add(coin)
                                # print(coin_value)
                            else:
                                pass

            for coin in self.coins.copy():                                                                                          # Check collision between coins and pirate using masks
                if pygame.sprite.collide_mask(coin, self.pirate):
                    self.score_label2 = self.font.render(str(self.total_score), 1, (0, 255, 255))                                    # Update score label
                    self.coins.remove(coin)
                    self.coin_sound.play()
                    self.total_score += coin_value
                    # print("Total score",self.total_score)

            for vessel in self.vessels:
                if isinstance(vessel, Lifeboat):
                    if isinstance(vessel, Lifeboat):
                        if pygame.sprite.collide_rect(self.pirate, vessel):
                            self.pirate.health -= 10
                            if self.pirate.health <= 0:
                                self.pirate.kill()
                                print("Game Over")
                                running = False
                            print("Lifeboat collision")
                    
                # if pygame.sprite.collide_rect(self.pirate, poison_gas):
                #     print("hit")

            self.coins.update()  # Update coin sprites
            self.coins.draw(self.screen)  # Draw coin sprites

            self.screen.blit(self.user_label, (10, 50))
            self.screen.blit(self.score_label, (10, 100))
            self.screen.blit(self.score_label2, (10, 130))

            pygame.display.flip()
            pygame.time.Clock().tick(60)

            if all(count == 0 for count in waves[current_wave].counts):  # Check if all enemies in the current wave have been spawned
                current_wave += 1

            if current_wave == len(waves):  # Check if all waves have been spawned
                if any(w.current_wave < len(w.enemy_types) for w in waves):  # Check if there are more waves to spawn
                    current_wave -= 1
                else:
                    print("Game Over")
                    break

        pygame.quit()

if __name__ == "__main__":
    Main().run()
