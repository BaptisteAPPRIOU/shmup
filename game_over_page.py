import pygame
import pygame_gui
from game_manager import GameManager
from level1 import Level1
import json

FPS = 60

class GameOverPage:
    def __init__(self, parent_screen, total_score, username):
        self.parent_screen = parent_screen  
        self.overlay_surface = pygame.Surface((640, 1000), pygame.SRCALPHA)  
        self.running = True  
        self.overlay_surface.set_alpha(58)
        self.total_score = total_score
        self.username = username
        self.font = pygame.font.Font("Fonts/Minecraft.ttf", 25)

        self.leaderboard_file = "leaderboard.json"
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over.mp3")
        self.game_over_sound.play()       

        self.game_over = pygame.image.load("images/game_over.png").convert_alpha() 
        pygame.mouse.set_visible(True)
        self.coin_image = pygame.transform.scale(pygame.image.load("images/yellow_coin4.png").convert_alpha(), (40,40))

    def save_to_leaderboard(self):
        try:
            with open(self.leaderboard_file, "r") as file:
                leaderboard_data = json.load(file)
        except FileNotFoundError:
            leaderboard_data = []

        leaderboard_data.append({"username": self.username, "score": self.total_score})

        with open(self.leaderboard_file, "w") as file:
            json.dump(leaderboard_data, file)
    
    def run(self):
        clock = pygame.time.Clock()
        MANAGER = pygame_gui.UIManager(self.parent_screen.get_size(), "theme.json")
        
        quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 580), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="quit_button")
        
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((155, 270), (350, 200)),
            text="Swallowed by the depths of the Dead Tide",
            manager=MANAGER,
            object_id="label")
        
        self.label_2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((155, 290), (350, 200)),
            text="your valiant stand ends here.",
            manager=MANAGER,
            object_id="label")
        
        self.label_3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((145, 310), (370, 200)),
            text="The village mourns as darkness claims its hero.",
            manager=MANAGER,
            object_id="label")
        self.label_5 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((155, 330), (350, 200)),
            text="But fear not, for legends never truly die.",
            manager=MANAGER,
            object_id="label")
        self.label_4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((130, 350), (400, 200)),
            text="Take heed, captain, for your legacy sails eternal.",
            manager=MANAGER,
            object_id="label")
        
        game_manager = GameManager() 

        while self.running:  # Run the exit page while the running flag is True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Stop running if the window is closed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False  # Stop running if ESC key is pressed
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == quit_button:
                            print("Quit button clicked")
                            self.save_to_leaderboard()
                            game_manager.show_landing_page() 

                MANAGER.process_events(event)
            MANAGER.update(clock.tick(FPS))
            self.overlay_surface.blit(self.game_over, (110, 170))
            score_text = self.font.render(str(self.total_score), True, (255, 255, 255))
            username_text = self.font.render(self.username, True, (255, 255, 255))
            self.overlay_surface.blit(score_text, (222, 520))
            self.overlay_surface.blit(username_text, (222, 480))
            self.overlay_surface.blit(self.coin_image, (400, 510))
            MANAGER.draw_ui(self.overlay_surface)  
            self.parent_screen.blit(self.overlay_surface, (0, 0))  

            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
    game_over_page = GameOverPage(screen, 100, "John")
    game_over_page.run()