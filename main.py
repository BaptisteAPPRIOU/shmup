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
        self.surface = pygame.Surface((640, 1000),pygame.SRCALPHA) 
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
        self.blood = pygame.sprite.Group()
        self.static_coin = pygame.sprite.Group()
        # SOUNDS
        self.coin_sound = pygame.mixer.Sound("sounds/coins.mp3")
        # FONTS AND LABELS
        self.font = pygame.font.Font("Fonts/Minecraft.ttf", 17) 
        self.user_label = self.font.render("User: user", 1, (0, 0, 0))
        self.score_label = self.font.render("SCORE : ", 1, (0, 0, 0))
        self.score_label2 = self.font.render(str(self.total_score), 1, (0, 0, 0))
        # self.health_label = self.font.render("HEALTH : ", 1, (0, 0, 0))
        # self.health = self.font.render(str(self.health), 1, (0, 0, 0))
        # self.life_label = self.font.render("LIVES : ", 1, (0, 0, 0))
        # self.life = self.font.render(str(self.life), 1, (0, 0, 0))
        # IMAGES
        self.beach = pygame.image.load("images/beach.png").convert_alpha()
        self.dock = pygame.image.load("images/dock.png").convert_alpha()
        self.health_bar = pygame.image.load("images/health_10.png").convert_alpha()
        self.health_bar = pygame.transform.scale(self.health_bar, (100, 15))
        self.life_heart = pygame.image.load("images/life_3.png").convert_alpha()
        self.life_heart = pygame.transform.scale(self.life_heart, (96, 32))

        self.health_images = {
        100: pygame.transform.scale(pygame.image.load("images/health_10.png").convert_alpha(),(100, 15)),
        90: pygame.transform.scale(pygame.image.load("images/health_9.png").convert_alpha(),(100, 15)),
        80: pygame.transform.scale(pygame.image.load("images/health_8.png").convert_alpha(),(100, 15)),
        70: pygame.transform.scale(pygame.image.load("images/health_7.png").convert_alpha(),(100, 15)),
        60: pygame.transform.scale(pygame.image.load("images/health_6.png").convert_alpha(),(100, 15)),
        50: pygame.transform.scale(pygame.image.load("images/health_5.png").convert_alpha(),(100, 15)),
        40: pygame.transform.scale(pygame.image.load("images/health_4.png").convert_alpha(),(100, 15)),
        30: pygame.transform.scale(pygame.image.load("images/health_3.png").convert_alpha(),(100, 15)),
        20: pygame.transform.scale(pygame.image.load("images/health_2.png").convert_alpha(),(100, 15)),
        10: pygame.transform.scale(pygame.image.load("images/health_1.png").convert_alpha(),(100, 15)),
        110: pygame.transform.scale(pygame.image.load("images/health_immune.png").convert_alpha(),(100, 15))
    }
        self.life_images = {
            3: pygame.transform.scale(pygame.image.load("images/life_3.png").convert_alpha(), (96, 32)),
            2: pygame.transform.scale(pygame.image.load("images/life_2.png").convert_alpha(), (96, 32)),
            1: pygame.transform.scale(pygame.image.load("images/life_1.png").convert_alpha(), (96, 32)),
            0: pygame.transform.scale(pygame.image.load("images/life_0.png").convert_alpha(), (96, 32))
        }

        self.red_coin_images = [pygame.transform.scale(pygame.image.load(f"images/red_coin{i}.png").convert_alpha(), (32, 32)) for i in range(1, 7)]

        self.water_images = [
            pygame.transform.scale(pygame.image.load("images/water.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water1.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water2.png").convert_alpha(), (24, 24)),
            pygame.transform.scale(pygame.image.load("images/water3.png").convert_alpha(), (24, 24)),
        ]

        self.background_sprites = pygame.sprite.Group()
        for y in range(0, 540, 24):
            for x in range(0, 650, 24):                                                                                       # Loop through the screen width in steps of 24 and create water sprites
                water_sprite = Water(x, y, self.water_images)
                self.background_sprites.add(water_sprite)
  
        for y in range(540, 1000, self.beach.get_height()):                                                                     # Loop through the screen height in steps of the beach image height and create beach sprites
            for x in range(0, 640, self.beach.get_width()):
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

        self.pirate = Pirate(self.pirate_group, self.bullets, self.vessels,self.zombies, self.cannon_ball_enemies, 100,self.screen.get_width(), self.screen.get_height())    # Create player pirate instance and add it to sprite group    
        self.pirate_group.add(self.pirate)

        self.health_boost_duration = 0
        self.damage_boost_duration = 0
        self.speed_boost_duration = 0
        self.original_health = self.pirate.health
        self.original_damage = self.pirate.damage
        self.original_speed = 1
        self.speed = 1

    def run(self):                                                                                                              # Main game loop
        waves = [                                                                                                               # List of waves
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Lifeboat], [2], 5, self.explosions),
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Sloop], [3], 5, self.explosions),
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Ship], [5], 5, self.explosions),
            Wave(self.screen, self.vessels, self.cannon_ball_enemies, [Lifeboat], [10], 5, self.explosions),
        ]

        if not self.static_coin:
            static_coin =Coin(30,500)
            self.static_coin.add(static_coin)

        clock = pygame.time.Clock()
        running = True
        current_wave = 0
        self.score_label2 = self.font.render(str(self.total_score), 1, (0, 0, 0))
        while running:

            counter = 0
            dt = clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.pirate.shoot()

            waves[current_wave].spawn_waves(dt)                                                                                     # Spawn waves of enemies

            self.screen.fill((0, 0, 0))                                                                                             # Fill the screen with black color
            self.screen.blit(self.surface, (0, 0))                                                                                  # Blit the surface with transparency to the screen

            pygame.draw.rect(self.screen, "BLUE", self.wall)
            self.statiscs_bar = pygame.draw.rect(self.surface,(255,255,255,33),(0,0,100,1000))

            self.background_sprites.update()                                                                                        # Update water sprites
            self.background_sprites.draw(self.screen)                                                                               # Draw water sprite
            self.pirate_group.update(self.speed)                                                                                              # Update pirate sprite
            self.pirate_group.draw(self.screen)                                                                                     # Draw pirate sprites
            self.zombies.update(self.pirate.rect.centerx, self.pirate.rect.centery,self.blood)
            self.zombies.draw(self.screen)
            self.poison_gas.update()
            self.poison_gas.draw(self.screen)
            self.cannon_ball_enemies.update()                                                                                      # Update cannon ball enemy sprites
            self.cannon_ball_enemies.draw(self.screen)                                                                             # Draw cannon ball enemy sprites
            self.coins.update() 
            self.coins.draw(self.screen) 
            self.blood.update()
            self.blood.draw(self.screen)
            self.static_coin.update()
            self.static_coin.draw(self.screen)

            self.timer += dt
            
            for vessel in self.vessels:                                                                                             # Loop through all vessels
                if not isinstance(vessel, Explosion):
                    vessel.move()                                                              # Move the vessel
                    self.screen.blit(vessel.image, vessel.rect)
                    if vessel.get_spawn_value() == True:
                        if self.timer >= 4:
                            lucky_number = random.randint(1, 5)
                            if lucky_number == (1 or 2 or 3 or 4):
                                SpawnZombie(vessel.rect.centerx, vessel.rect.bottom, self.zombies, 1, self.poison_gas, self.blood)
                            elif lucky_number == 5:
                                SpawnZombie(vessel.rect.centerx, vessel.rect.bottom, self.zombies, 2, self.poison_gas, self.blood)
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
                self.score_label2 = self.font.render(str(self.total_score), 1, (0, 0, 0))

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
            # self.health = self.font.render(str(self.pirate.health), 1, (0, 0, 0))
            self.life = self.font.render(str(self.pirate.life), 1, (0, 0, 0))

            if self.pirate.health > 100:
                self.health_bar = self.health_images[110]
            elif self.pirate.health == 100:
                self.health_bar = self.health_images[100]
            elif self.pirate.health == 90:
                self.health_bar = self.health_images[90]
            elif self.pirate.health == 80:
                self.health_bar = self.health_images[80]
            elif self.pirate.health == 70:
                self.health_bar = self.health_images[70]
            elif self.pirate.health == 60:
                self.health_bar = self.health_images[60]
            elif self.pirate.health == 50:
                self.health_bar = self.health_images[50]
            elif self.pirate.health == 40:
                self.health_bar = self.health_images[40]
            elif self.pirate.health == 30:
                self.health_bar = self.health_images[30]
            elif self.pirate.health == 20:
                self.health_bar = self.health_images[20]
            elif self.pirate.health == 10:
                self.health_bar = self.health_images[10]

            if self.pirate.life == 3:
                self.life_heart = self.life_images[3]
            elif self.pirate.life == 2:
                self.life_heart = self.life_images[2]
            elif self.pirate.life == 1:
                self.life_heart = self.life_images[1]
            elif self.pirate.life == 0:
                self.life_heart = self.life_images[0]
            
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

            for vessel in self.vessels.copy():
                if isinstance(vessel, Coin):
                    if pygame.sprite.collide_mask(vessel, self.pirate):
                        print("Coin value", vessel.get_value())
                        if vessel.get_value() == 'blue':
                            print("Speed boost")
                            self.speed = 3
                            self.speed_boost_duration = 5
                        elif vessel.get_value() == 'red':
                            print("Damage boost")
                            self.pirate.damage += self.pirate.damage*4
                            self.damage_boost_duration = 5
                        elif vessel.get_value() == 'green':  
                            print("Health boost")
                            self.pirate.health += 50000  
                            self.health_boost_duration = 5
                        elif vessel.get_value() == 'black':
                            print("Poison gas")
                            for zombie in self.zombies:
                                zombie.die()
                            for gas in self.poison_gas:
                                gas.kill()
                        vessel.kill()
                        counter = 1
            
            if self.health_boost_duration > 0:
                self.health_boost_duration -= dt
                if self.health_boost_duration <= 0:
                    self.pirate.health = self.original_health    
                    self.health_boost_duration = 0
            
            if self.damage_boost_duration > 0:
                self.damage_boost_duration -= dt
                if self.damage_boost_duration <= 0:
                    self.pirate.damage = self.original_damage
                    self.damage_boost_duration = 0
            
            if self.speed_boost_duration > 0:
                self.speed_boost_duration -= dt
                if self.speed_boost_duration <= 0:
                    self.speed = 1
                    self.speed_boost_duration = 0

            self.screen.blit(self.user_label, (10, 50))
            self.screen.blit(self.score_label, (10, 100))
            self.screen.blit(self.score_label2, (10, 130))
            # self.screen.blit(self.health_label, (10, 160))
            # self.screen.blit(self.health, (10, 190))
            # self.screen.blit(self.life_label, (10, 220))
            # self.screen.blit(self.life, (10, 250))
            self.screen.blit(self.surface, (0, 0))
            self.screen.blit(self.health_bar, (2, 190))
            self.screen.blit(self.life_heart, (5, 210))
            

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