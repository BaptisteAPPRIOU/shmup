import pygame
import pygame_gui
from game_manager import GameManager

FPS = 60

class CreditsPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
        self.background = pygame.image.load("images/tutorial.png").convert_alpha()
        self.surface = pygame.Surface((640, 1000), pygame.SRCALPHA)
        self.rectangle = pygame.Rect((0, 0), (500, 800))
        self.new_cursor = pygame.image.load("images/mouse_cursor.png").convert_alpha()
        pygame.mouse.set_visible(False)

    def draw_statistics_bar(self, surface):
        pygame.draw.rect(surface, (255, 255, 255, 100), (70, 150, 500, 750))

    def run(self):
        clock = pygame.time.Clock()
        MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")
        
        button_back = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 930), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="back_button")
        
        creators_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 20), (500, 350)),
            text="Creators of Dead Tide:",
            manager=MANAGER,
            object_id="label")
        
        baptiste_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 60), (500, 400)),
            text="Baptiste APPRIOU - Captain of creativity and code",
            manager=MANAGER,
            object_id="label")
        
        baptiste_text_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 80), (500, 400)),
            text="With your resilience, we sailed through stormy code",
            manager=MANAGER,
            object_id="label")
        baptiste_text_label_2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 100), (500, 400)),
            text="and reached the shores of a successful game.",
            manager=MANAGER,
            object_id="label")
        
        oussema_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 140), (500, 400)),
            text="Oussema FATNASSI - Master of design and detail",
            manager=MANAGER,
            object_id="label")
        
        oussema_text_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 160), (500, 400)),
            text="Your artistic vision shaped the world of Dead Tide",
            manager=MANAGER,
            object_id="label")
        oussema_text_label_2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 180), (500, 400)),
            text="and gave it depth and beauty.",
            manager=MANAGER,
            object_id="label")
        
        ali_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 220), (500, 400)),
            text="Abakar ISSA ALI - Navigator of narrative and nuance",
            manager=MANAGER,
            object_id="label")
        ali_text_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 240), (500, 400)),
            text="Your storytelling skills crafted the lore of Dead Tide,",
            manager=MANAGER,
            object_id="label")
        ali_text_label_2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 260), (500, 400)),
            text="making it a world worth saving.",
            manager=MANAGER,
            object_id="label")
        
        fellow_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 550), (500, 400)),
            text="Fellow sailors:",
            manager=MANAGER,
            object_id="label")
        fellow_text_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 570), (500, 400)),
            text="Thank you for joining us on this epic adventure.",
            manager=MANAGER,
            object_id="label")
        fellow_text_label_2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 590), (500, 400)),
            text="Together, we stood against the zombie pirate horde and won",
            manager=MANAGER,
            object_id="label")
        fellow_text_label_3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 610), (500, 400)),
            text="May your sails stay full and your cannons stay loaded!",
            manager=MANAGER,
            object_id="label")
        special_thanks_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 350), (500, 400)),
            text="Special thanks to:",
            manager=MANAGER,
            object_id="label")
        special_thanks_text_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((70, 370), (500, 400)),
            text="Professors, and fellow adventurers who supported us",
            manager=MANAGER,
            object_id="label")
        
        game_manager = GameManager()  

        
        running = True
        while running:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_back:
                            print("Back button clicked")
                            game_manager.show_landing_page()

                MANAGER.process_events(event)
                
            MANAGER.update(clock.tick(FPS))
            self.screen.blit(self.background, (0, 0))
            self.surface.fill((255, 255, 255, 50))  
            self.draw_statistics_bar(self.surface)  
            self.screen.blit(self.surface, (0, 0))
            MANAGER.draw_ui(self.screen)
            self.screen.blit(self.new_cursor, pos) 
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    credits_page = CreditsPage()
    credits_page.run()
