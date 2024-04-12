import pygame

class UI():
    def __init__(self):

        self.image_red_coin = pygame.Surface((32, 32))
        self.rect = self.image_red_coin.get_rect()
        self.image_yellow_coin = pygame.Surface((32, 32))
        self.rect = self.image_yellow_coin.get_rect() 
        self.image_green_coin = pygame.Surface((32, 32))
        self.rect = self.image_green_coin.get_rect() 
        self.image_blue_coin = pygame.Surface((32, 32))
        self.rect = self.image_blue_coin.get_rect() 
        self.image_black_coin = pygame.Surface((32, 32))
        self.rect = self.image_black_coin.get_rect()

        # Coin images
        self.red_coin_images = [pygame.transform.scale(pygame.image.load(f"images/red_coin{i}.png").convert_alpha(), (32, 32)) for i in range(1, 7)]
        self.green_coin_images = [pygame.transform.scale(pygame.image.load(f"images/green_coin{i}.png").convert_alpha(), (32, 32)) for i in range(1, 7)]
        self.blue_coin_images = [pygame.transform.scale(pygame.image.load(f"images/blue_coin{i}.png").convert_alpha(), (32, 32)) for i in range(1, 7)]
        self.black_coin_images = [pygame.transform.scale(pygame.image.load(f"images/black_coin{i}.png").convert_alpha(), (32, 32)) for i in range(1, 7)]
        self.yellow_coin_images = [pygame.transform.scale(pygame.image.load(f"images/yellow_coin{i}.png").convert_alpha(), (32, 32)) for i in range(1, 7)]

        # Indexes for each type of coin
        self.red_coin_index = 0
        self.green_coin_index = 0
        self.blue_coin_index = 0
        self.black_coin_index = 0
        self.yellow_coin_index = 0

        # Initial positions for each type of coin
        self.red_coin_rect = pygame.Rect(2, 300, 32, 32)
        self.green_coin_rect = pygame.Rect(2, 330, 32, 32)
        self.blue_coin_rect = pygame.Rect(2, 360, 32, 32)
        self.black_coin_rect = pygame.Rect(2, 390, 32, 32)
        self.yellow_coin_rect = pygame.Rect(77, 120, 32, 32)

        # Counters for animation
        self.red_coin_counter = 0
        self.green_coin_counter = 0
        self.blue_coin_counter = 0
        self.black_coin_counter = 0
        self.yellow_coin_counter = 0

        self.animation_speed = 5

    def show(self, screen):
        screen.blit(self.image_red_coin, self.red_coin_rect)
        screen.blit(self.image_green_coin, self.green_coin_rect)
        screen.blit(self.image_blue_coin, self.blue_coin_rect)
        screen.blit(self.image_black_coin, self.black_coin_rect)
        screen.blit(self.image_yellow_coin, self.yellow_coin_rect)
 
    def update(self):
        self.animate_red()
        self.animate_green()
        self.animate_blue()
        self.animate_black()
        self.animate_yellow()

    def animate_red(self):
        self.red_coin_counter += 1
        if self.red_coin_counter >= self.animation_speed:
            self.red_coin_counter = 0
            self.red_coin_index = (self.red_coin_index + 1) % len(self.red_coin_images)
            self.image_red_coin = self.red_coin_images[self.red_coin_index]
            self.rect = self.red_coin_rect

    def animate_green(self):
        self.green_coin_counter += 1
        if self.green_coin_counter >= self.animation_speed:
            self.green_coin_counter = 0
            self.green_coin_index = (self.green_coin_index + 1) % len(self.green_coin_images)
            self.image_green_coin = self.green_coin_images[self.green_coin_index]
            self.rect = self.green_coin_rect

    def animate_blue(self):
        self.blue_coin_counter += 1
        if self.blue_coin_counter >= self.animation_speed:
            self.blue_coin_counter = 0
            self.blue_coin_index = (self.blue_coin_index + 1) % len(self.blue_coin_images)
            self.image_blue_coin = self.blue_coin_images[self.blue_coin_index]
            self.rect = self.blue_coin_rect

    def animate_black(self):
        self.black_coin_counter += 1
        if self.black_coin_counter >= self.animation_speed:
            self.black_coin_counter = 0
            self.black_coin_index = (self.black_coin_index + 1) % len(self.black_coin_images)
            self.image_black_coin = self.black_coin_images[self.black_coin_index]
            self.rect = self.black_coin_rect

    def animate_yellow(self):
        self.yellow_coin_counter += 1
        if self.yellow_coin_counter >= self.animation_speed:
            self.yellow_coin_counter = 0
            self.yellow_coin_index = (self.yellow_coin_index + 1) % len(self.yellow_coin_images)
            self.image_yellow_coin = self.yellow_coin_images[self.yellow_coin_index]
            self.rect = self.yellow_coin_rect