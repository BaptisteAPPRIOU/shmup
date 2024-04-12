import pygame

class Leaderboard:
    def __init__(self,display,gameStateManager):
        pygame.init()
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('menu')