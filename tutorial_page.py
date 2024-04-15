import pygame
import pygame_gui
from pirate_tutorial import Pirate
from game_manager import GameManager

class TutorialPage():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/tutorial.png").convert_alpha()
        self.new_cursor = pygame.image.load("images/mouse_cursor.png").convert_alpha()
        pygame.mouse.set_visible(False)

    def run(self):
        clock = pygame.time.Clock()
        self.screen.blit(self.background, (0, 0))
        self.MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")

        # Create buttons
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
        # Create labels
        label_tutorial_text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 40), (600, 400)),
            text="Take control of the mighty cannon and defend the village harbor from the ",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 60), (600, 400)),
            text="relentless onslaught of zombie pirates.Use 'Q' and 'D' or '←' and '→'",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 80), (600, 400)),
            text="to aim your cannon and fend off the undead horde.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_5 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 100), (600, 400)),
            text="As enemy ships approach, they'll unleash waves of undead pirates",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_6 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 120), (600, 400)),
            text="hell-bent on reaching the village gates. ",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_7 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 160), (600, 400)),
            text="Blast them to bits with the 'SPACE BAR' before they breach the walls!",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_8 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 180), (600, 400)),
            text="and unleash chaos upon the unsuspecting villagers.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_9 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 220), (600, 400)),
            text="After each victorious battle, choose wisely from a selection of upgrades.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_10 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 240), (600, 400)),
            text="Upgrade your cannon's damage, speed, and health to face the zombie pirates.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_11 = pygame_gui.elements.UILabel(  
            relative_rect=pygame.Rect((20, 260), (620, 400)),
            text="Test yourself against other daring captains and etch your name in the annals",
            manager=self.MANAGER,
            object_id="label")
        
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        pirate = Pirate(all_sprites, bullets, 640, 800)
        all_sprites.add(pirate)

        game_manager = GameManager()  

        running = True
        while running:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_manager.show_exit_page(self.screen)
                    if event.key == pygame.K_SPACE:
                        pirate.shoot()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == continue_button:
                            game_manager.show_user_creation_page()
                        if event.ui_element == back_button:
                            game_manager.show_landing_page()

                self.MANAGER.process_events(event)
            self.MANAGER.update(clock.tick(60))
            self.screen.blit(self.background, (0, 0))
            all_sprites.update()
            all_sprites.draw(self.screen)
            self.MANAGER.draw_ui(self.screen)
            self.screen.blit(self.new_cursor, pos)

            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    tutorial_page = TutorialPage()
    tutorial_page.run()