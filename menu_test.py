import pygame
import pygame_gui

FPS = 60

class Menu:
    def __init__(self,display,gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        clock = pygame.time.Clock()
        self.display.fill('white')
        MANAGER = pygame_gui.UIManager((540, 640), "theme.json")
        button_play = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((125, 70), (290, 100)),
        text="PLAY",manager=MANAGER,object_id="button",tool_tip_text="Play")
        button_leaderboard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 290), (200, 60)),
        text="LEADERBOARD",manager=MANAGER,object_id="button",tool_tip_text="Leaderboard")
        button_quit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((195, 580), (150, 40)),
        text="QUIT",manager=MANAGER,object_id="button",tool_tip_text="Quit")
        keys = pygame.key.get_pressed()
        running = True
        while running == True:
            for event in pygame.event.get():
                if keys[pygame.K_a]:
                    self.gameStateManager.set_state('tuto')
                    running = False
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
                            self.gameStateManager.set_state('tuto')
                            running = False
                        elif event.ui_element == button_quit:
                            print("Quit button clicked")
                            running = False
                            pygame.quit()
                MANAGER.process_events(event)
            MANAGER.update(clock.tick(60))
            self.display.fill((255, 255, 255))
            MANAGER.draw_ui(self.display)
            pygame.display.flip()
        
        
        