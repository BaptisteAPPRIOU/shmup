import pygame
import time

class mapGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
        self.screen.fill((255, 255, 255))
        self.statistics_bar = pygame.Rect(0, 0, 60, 640)
        self.beach = pygame.Rect(60, 550, 480, 90)
        self.clock = pygame.time.Clock()

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
        pygame.draw.rect(self.screen, "YELLOW", self.beach)

    def update_display(self):
        pygame.display.flip()
        self.clock.tick(60)

    def quit(self):
        pygame.quit()
