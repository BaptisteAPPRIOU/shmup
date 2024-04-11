import pygame
from lifeboat import Lifeboat
from sloop import Sloop
from enemy_wave import Wave
from ship import Ship
from pirate import Pirate
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
        self.total_score = 0
        self.timer = 0
        self.health = 100
        self.life = 3
        # SPRITE GROUPS
        self.vessels = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.pirate_group = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.cannon_ball_enemies = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.poison_gas = pygame.sprite.Group()
        # SOUNDS
        self.coin_sound = pygame.mixer.Sound("sounds/coins.mp3")
        # FONTS AND LABELS
        self.font = pygame.font.Font("Fonts/Minecraft.ttf", 15) 
        self.user_label = self.font.render("User: user", 1, (0, 255, 255))
        self.score_label = self.font.render("SCORE : ", 1, (0, 255, 255))
        self.score_label2 = self.font.render(str(self.total_score), 1, (0, 255, 255))
        self.health_label = self.font.render("HEALTH : ", 1, (0, 255, 255))
        self.health = self.font.render(str(self.health), 1, (0, 255, 255))
        self.life_label = self.font.render("LIVES : ", 1, (0, 255, 255))
        self.life = self.font.render(str(self.life), 1, (0, 255, 255))
        # IMAGES
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

        self.pirate = Pirate(self.pirate_group, self.bullets, self.vessels,self.zombies, self.cannon_ball_enemies,self.screen.get_width(), self.screen.get_height())    # Create player pirate instance and add it to sprite group
        self.pirate_group.add(self.pirate)

    def run(self):                                                                                                              # Main game loop
        waves = [                                                                                                               # List of waves
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Lifeboat], [2], 5, self.explosions),
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Sloop], [3], 5, self.explosions),
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Ship], [5], 5, self.explosions),
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Lifeboat], [8], 5, self.explosions),
        ]

        clock = pygame.time.Clock()
        running = True
        current_wave = 0
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
            self.poison_gas.update()
            self.poison_gas.draw(self.screen)
            self.cannon_ball_enemies.update()                                                                                      # Update cannon ball enemy sprites
            self.cannon_ball_enemies.draw(self.screen)                                                                             # Draw cannon ball enemy sprites
            self.coins.update() 
            self.coins.draw(self.screen) 

            self.timer += dt
            
            for vessel in self.vessels:                                                                                             # Loop through all vessels
                if not isinstance(vessel, Explosion):
                    vessel.move()                                                              # Move the vessel
                    self.screen.blit(vessel.image, vessel.rect)
                    if vessel.get_spawn_value() == True:
                        if self.timer >= 4:
                            lucky_number = random.randint(1, 5)
                            if lucky_number == (1 or 2 or 3 or 4):
                                SpawnZombie(vessel.rect.centerx, vessel.rect.bottom, self.zombies, 1, self.poison_gas)
                            elif lucky_number == 5:
                                SpawnZombie(vessel.rect.centerx, vessel.rect.bottom, self.zombies, 2, self.poison_gas)
                    if isinstance(vessel, Lifeboat) or isinstance(vessel, Sloop) or isinstance(vessel, Ship):
                        vessel.attack()
            
            if self.timer >= 4:
                self.timer -= 4

            for explosion in self.explosions.copy():
                explosion.update()
                self.screen.blit(explosion.image, explosion.rect)
                if explosion.type == "lifeboat":
                    self.total_score += 5
                elif explosion.type == "sloop":
                    self.total_score += 10
                elif explosion.type == "ship":
                    self.total_score += 15
                self.score_label2 = self.font.render(str(self.total_score), 1, (0, 255, 255))

            for bullet in self.cannon_ball_enemies:
                if pygame.sprite.collide_mask(bullet, self.pirate):
                    self.pirate.health -= 10
                    bullet.kill()
                    if self.pirate.health <= 0:
                        self.pirate.life -= 1
                        self.pirate.health = 100
                        if self.pirate.life == 0:
                            self.pirate.kill()
                            print("Game Over")
                            running = False
            self.health = self.font.render(str(self.pirate.health), 1, (0, 255, 255))
            self.life = self.font.render(str(self.pirate.life), 1, (0, 255, 255))
            
            for gas in self.poison_gas:
                if pygame.sprite.collide_mask(gas, self.pirate):
                    self.pirate.health -= 10
                    gas.kill()  
                    if self.pirate.health <= 0:
                        self.pirate.life -= 1
                        self.pirate.health = 100
                        if self.pirate.life == 0:
                            self.pirate.kill()
                            print("Game Over")
                            running = False

            # for coin in self.coins.copy():                                                                                          # Check collision between coins and pirate using masks
            #     if pygame.sprite.collide_mask(coin, self.pirate):
            #         self.score_label2 = self.font.render(str(self.total_score), 1, (0, 255, 255))                                    # Update score label
            #         self.coins.remove(coin)
            #         self.coin_sound.play()
            #         self.total_score += coin_value
            #         # print("Total score",self.total_score)

            self.screen.blit(self.user_label, (10, 50))
            self.screen.blit(self.score_label, (10, 100))
            self.screen.blit(self.score_label2, (10, 130))
            self.screen.blit(self.health_label, (10, 160))
            self.screen.blit(self.health, (10, 190))
            self.screen.blit(self.life_label, (10, 220))
            self.screen.blit(self.life, (10, 250))

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