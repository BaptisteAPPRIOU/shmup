import pygame
import pygame_gui
from pirate_tutorial import Pirate
from game_manager import GameManager

class TutorialPage():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/tutorial.png").convert_alpha()

    def run(self):
        clock = pygame.time.Clock()
        self.screen.blit(self.background, (0, 0))
        self.MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")

        continue_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 890), (196, 36)),
            text="",
            manager=self.MANAGER,
            object_id="continue_button")
        
        back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 930), (196, 36)),
            text="",
            manager=self.MANAGER,
            object_id="back_button")
        
        label_tutorial = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 20), (500, 400)),
            text="TUTORIAL",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 60), (500, 400)),
            text="This is a tutorial on how to play the game.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 100), (500, 400)),
            text="Use the keys 'q' and 'd' or '←'and '→' to move the pirate",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 120), (500, 400)),
            text="Press the space key to shoot the pirate's cannon.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_5 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 140), (500, 400)),
            text="Press the escape key to quit the game.",
            manager=self.MANAGER,
            object_id="label")
        
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        pirate = Pirate(all_sprites, bullets, 640, 800)
        all_sprites.add(pirate)

        game_manager = GameManager()  

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_manager.show_exit_page(self.screen)
                        # running = False
                    if event.key == pygame.K_SPACE:
                        pirate.shoot()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == continue_button:
                            print("Start button clicked")
                            game_manager.show_level1_page()
                            # running = False
                        if event.ui_element == back_button:
                            print("Back button clicked")
                            game_manager.show_landing_page()

                self.MANAGER.process_events(event)
            self.MANAGER.update(clock.tick(60))
            self.screen.blit(self.background, (0, 0))
            all_sprites.update()
            all_sprites.draw(self.screen)
            self.MANAGER.draw_ui(self.screen)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    tutorial_page = TutorialPage()
    tutorial_page.run()

