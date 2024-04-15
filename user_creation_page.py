import pygame
import pygame_gui
from game_manager import GameManager
import json

class UserCreationPage():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/tutorial.png").convert_alpha()

        self.new_cursor = pygame.image.load("images/mouse_cursor.png").convert_alpha()
        pygame.mouse.set_visible(False)
    
    def save_user(self, user_name):
        data = {"name": user_name}
        with open("user_data.json", "w") as file:
            json.dump(data, file)

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
        label_tutorial = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 30), (500, 400)),
            text="Join the captain's last stand against the tides of darkness ",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 50), (500, 400)),
            text="and become the hero the village deserves.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 90), (500, 400)),
            text="Will you emerge victorious against the zombie pirate scourge",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 110), (500, 400)),
            text="or will you be swallowed by the depths of the Dead Tide?",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_5 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 130), (500, 400)),
            text="Set sail and prepare for battle,",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_6 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 150), (500, 400)),
            text="for the fate of the village hangs in the balance!",
            manager=self.MANAGER,
            object_id="label")
        
        # Create text entry
        entry_name = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((120, 450), (400, 36)),
            manager=self.MANAGER,
            object_id="entry_name")
        
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
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == continue_button:
                            print("Start button clicked")
                            self.user_name = entry_name.get_text()
                            self.save_user(self.user_name)
                            game_manager.show_level1_page(self.user_name)
                            # running = False
                        if event.ui_element == back_button:
                            print("Back button clicked")
                            game_manager.show_tutorial_page()

                self.MANAGER.process_events(event)
            self.MANAGER.update(clock.tick(60))
            self.screen.blit(self.background, (0, 0))
            self.MANAGER.draw_ui(self.screen)
            self.screen.blit(self.new_cursor, pos)

            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    user_creation_page = UserCreationPage()
    user_creation_page.run()

