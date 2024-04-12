import pygame
import sys
from menu_test import Menu
from tuto_test import Tuto
from GameState import GameStateManager

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager('tuto')
        self.menu = Menu(self.screen, self.gameStateManager)
        self.tuto = Tuto(self.screen, self.gameStateManager)
        self.states = {'menu':self.menu, 'tuto':self.tuto}
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()