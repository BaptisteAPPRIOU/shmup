import pygame
import pygame_gui
from game_manager import GameManager

FPS = 60

class LandingPage: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/splash_art.png").convert_alpha()
        self.new_cursor = pygame.image.load("images/mouse_cursor.png").convert_alpha()
        pygame.mouse.set_visible(False)

    def run(self):
        clock = pygame.time.Clock()
        MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")
        # Create buttons
        button_play = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 480), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="play_button"
            )
        button_leaderboard = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 530), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="leaderboard_button")
        button_credits = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 580), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="credits_button")
        button_quit = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 630), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="quit_button")
        
        game_manager = GameManager()  
        
        running = True   
        while running:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_play:
                            game_manager.show_tutorial_page()
                        elif event.ui_element == button_leaderboard:
                            game_manager.show_leaderboard_page()
                        elif event.ui_element == button_credits:
                            game_manager.show_credits_page()
                        elif event.ui_element == button_quit:
                            running = False
                            pygame.quit()

                MANAGER.process_events(event)
            MANAGER.update(clock.tick(FPS))
            self.screen.blit(self.background, (0, 0))
            MANAGER.draw_ui(self.screen)
            self.screen.blit(self.new_cursor, pos)

            pygame.display.flip()
        # pygame.quit()

if __name__ == "__main__":
    landing_page = LandingPage()
    landing_page.run()
