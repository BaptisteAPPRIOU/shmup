import pygame
import sys
from menu_test import Menu
from leaderboard import Leaderboard
from tutorial import Tutorial
from game_over_page import GameOverPage
from level import Level1
from credits import Credits
from GameState import GameStateManager

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 1000
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager('menu')
        self.menu = Menu(self.screen, self.gameStateManager)
        self.leaderboard = Leaderboard(self.screen, self.gameStateManager)
        self.credits = Credits(self.screen, self.gameStateManager)
        self.tuto = Tutorial(self.screen, self.gameStateManager)
        self.gameover = GameOverPage(self.screen, self.gameStateManager)
        self.gameplay = Level1(self.screen, self.gameStateManager)
        self.states = {'menu':self.menu, 'leaderboard':self.leaderboard, 'game':self.gameplay, 'tuto':self.tuto, 'gameover':self.gameover, 'credits':self.credits}
        
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