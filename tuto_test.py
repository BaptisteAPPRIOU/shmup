import pygame

class Tuto:
    def __init__(self,display,gameStateManager):
        pygame.init()
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        # pygame.init()
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('menu')