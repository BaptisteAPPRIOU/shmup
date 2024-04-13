import pygame
import pygame_gui
from game_manager import GameManager

FPS = 60

class LandingPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/splash_art.png").convert_alpha()

    def run(self):
        clock = pygame.time.Clock()
        MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")

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
        
        game_manager = GameManager()  # Create an instance of GameManager
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if button_play.rect.collidepoint(event.pos):
                            print("Play button clicked")
                            game_manager.show_tutorial_page()
                        elif button_leaderboard.rect.collidepoint(event.pos):
                            print("Leaderboard button clicked")
                            game_manager.show_leaderboard_page()

                            # Perform action for leaderboard button click
                        elif button_credits.rect.collidepoint(event.pos):
                            print("Credits button clicked")
                            # Perform action for credits button click
                        elif button_quit.rect.collidepoint(event.pos):
                            print("Quit button clicked")
                            running = False
                            pygame.quit()

                MANAGER.process_events(event)
            MANAGER.update(clock.tick(FPS))
            self.screen.blit(self.background, (0, 0))
            MANAGER.draw_ui(self.screen)
            pygame.display.flip()
        # pygame.quit()

if __name__ == "__main__":
    landing_page = LandingPage()
    landing_page.run()
