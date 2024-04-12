import pygame
import pygame_gui

FPS = 60

class Menu:
    def __init__(self,screen,gameStateManager):
        pygame.init()
        self.screen = screen
        self.gameStateManager = gameStateManager
    def run(self):
        clock = pygame.time.Clock()
        self.screen.blit(pygame.image.load("images/splash_art.png").convert_alpha(), (0, 0))
        MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")
        self.background = pygame.image.load("images/splash_art.png").convert_alpha()
        button_play = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 480), (100, 50)),
        text="PLAY",manager=MANAGER,object_id="button",tool_tip_text="Play the game")
        button_leaderboard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 530), (200, 50)),
        text="LEADERBOARD",manager=MANAGER,object_id="button",tool_tip_text="View the leaderboard")
        button_credits = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((245, 580), (150, 50)),
        text="CREDITS",manager=MANAGER,object_id="button",tool_tip_text="Show credits")
        button_quit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((245, 630), (150, 50)),
        text="QUIT",manager=MANAGER,object_id="button",tool_tip_text="Exit the game")
        keys = pygame.key.get_pressed()
        running = True
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_play:
                            print("Play button clicked")
                            self.gameStateManager.set_state('tuto')
                            running = False
                        elif event.ui_element == button_leaderboard:
                            print("Leaderboard button clicked")
                            self.gameStateManager.set_state('leaderboard')
                            running = False
                        elif event.ui_element == button_credits:
                            print("Credits button clicked")
                            self.gameStateManager.set_state('credits')
                            running = False
                        elif event.ui_element == button_quit:
                            print("Quit button clicked")
                            running = False
                            pygame.quit()
                MANAGER.process_events(event)
            MANAGER.update(clock.tick(60))
            self.screen.blit(pygame.image.load("images/splash_art.png").convert_alpha(), (0, 0))
            MANAGER.draw_ui(self.screen)
            pygame.display.flip()
        
        
        