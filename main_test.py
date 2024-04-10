import pygame
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)

        self.states = {'start':self.start, 'level':self.level}
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #    if event.type == pygame.KEYDOWN:
            #       if event.key == pygame.K_SPACE:
            #             if self.gameStateManager.get_state() == 'start':
            #                 self.gameStateManager.set_state('level')
            #             else:
            #                 self.gameStateManager.set_state('start')
            self.states[self.gameStateManager.get_state()].run()
            
            pygame.display.update()
            self.clock.tick(FPS)
            
class Level:
    def __init__(self,display,gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('blue')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.gameStateManager.set_state('start')
    
class Start:
    def __init__(self,display,gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('level')
        
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state
            
if __name__ == '__main__':
    game = Game()
    game.run()