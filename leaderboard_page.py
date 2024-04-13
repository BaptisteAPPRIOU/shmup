import pygame
import pygame_gui
from game_manager import GameManager

FPS = 60

class LeaderboardPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/leaderboard.png").convert_alpha()

    def run(self):
        clock = pygame.time.Clock()
        MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")
        
        button_back = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 930), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="back_button")
        
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
                        if button_back.rect.collidepoint(event.pos):
                            print("Back button clicked")
                            game_manager.show_landing_page()

                MANAGER.process_events(event)
            MANAGER.update(clock.tick(FPS))
            self.screen.blit(self.background, (0, 0))
            MANAGER.draw_ui(self.screen)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    leaderboard_page = LeaderboardPage()
    leaderboard_page.run()
