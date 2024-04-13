import pygame
import pygame_gui
from game_manager import GameManager
import json

FPS = 60

class LeaderboardPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/leaderboard.png").convert_alpha()
        self.font = pygame.font.Font("fonts/Minecraft.ttf", 25)
        self.new_cursor = pygame.image.load("images/mouse_cursor.png").convert_alpha()
        pygame.mouse.set_visible(False)

        
    def display_leaderboard(self):
        try:
            with open("leaderboard.json", "r") as file:
                leaderboard_data = json.load(file)
        except FileNotFoundError:
            leaderboard_data = []

        leaderboard_data.sort(key=lambda x: x["score"], reverse=True)

        for i, entry in enumerate(leaderboard_data[:5]):  # Display top 5 scores
            username = entry["username"]
            score = entry["score"]
            username_text = self.font.render(username, True, (255, 255, 255))
            score_text = self.font.render(str(score), True, (255, 255, 255))

            username_position = (180, 477 + i * 63)  
            score_position = (360, 477 + i * 63)     

            self.screen.blit(username_text, username_position)
            self.screen.blit(score_text, score_position)
    
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
            pos = pygame.mouse.get_pos()
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
            self.display_leaderboard()
            MANAGER.draw_ui(self.screen)
            self.screen.blit(self.new_cursor, pos)
            pygame.display.flip()
        pygame.quit()

# if __name__ == "__main__":
#     leaderboard_page = LeaderboardPage()
#     leaderboard_page.run()
