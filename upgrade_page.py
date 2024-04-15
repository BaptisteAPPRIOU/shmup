import pygame
import pygame_gui
from game_manager import GameManager

FPS = 60

class UpgradePage:
    def __init__(self, parent_screen, username, total_score, health,life):
        self.parent_screen = parent_screen  
        self.overlay_surface = pygame.Surface((640, 1000), pygame.SRCALPHA)  
        self.running = True  
        self.overlay_surface.set_alpha(58)
        self.font = pygame.font.Font("Fonts/Minecraft.ttf", 25)
        self.disabled_button = None
        self.username = username
        self.total_score = total_score
        self.health = health
        self.life = life

        self.game_over = pygame.image.load("images/upgrades.png").convert_alpha() 
        pygame.mouse.set_visible(True)

    def run(self):
        clock = pygame.time.Clock()
        MANAGER = pygame_gui.UIManager(self.parent_screen.get_size(), "theme.json")
        
        # Create buttons
        quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 580), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="quit_button")
        confirm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 535), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="confirm_button")
        self.speed_upgrade_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((140, 400), (100, 100)),
            text="",
            manager=MANAGER,
            object_id="speed_upgrade_button")
        self.damage_upgrade_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((270, 400), (100, 100)),
            text="",
            manager=MANAGER,
            object_id="damage_upgrade_button")
        self.health_upgrade_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((400, 400), (100, 100)),
            text="",
            manager=MANAGER,
            object_id="health_upgrade_button")
        
        # Create labels
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((135, 170), (350, 200)),
            text="After each victorious battle",
            manager=MANAGER,
            object_id="label")
        self.label_2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((135, 190), (370, 200)),
            text="choose wisely from a selection of upgrades to",
            manager=MANAGER,
            object_id="label")
        self.label_3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((125, 210), (390, 200)),
            text="enhance your firepower and fortify your defenses.",
            manager=MANAGER,
            object_id="label")
        self.label_5 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((110, 230), (410, 200)),
            text="Every upgrade brings you one step closer to victory.",
            manager=MANAGER,
            object_id="label")
        self.label_4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((120, 270), (400, 200)),
            text="Choose wisely, for the Dead Tide grows stronger.",
            manager=MANAGER,
            object_id="label")
        
        game_manager = GameManager() 

        while self.running:  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False  
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == quit_button:
                            game_manager.show_landing_page()
                        elif event.ui_element == confirm_button:
                            game_manager.show_level2_page(self.username, self.total_score, self.health, self.life, self.disabled_button)
                        elif event.ui_element == self.speed_upgrade_button:
                            self.disabled_button = "speed_upgrade"
                            self.speed_upgrade_button.disable()
                            self.health_upgrade_button.enable()
                            self.damage_upgrade_button.enable()
                        elif event.ui_element == self.damage_upgrade_button:
                            self.disabled_button = "damage_upgrade"
                            self.damage_upgrade_button.disable()
                            self.speed_upgrade_button.enable()
                            self.health_upgrade_button.enable()
                        elif event.ui_element == self.health_upgrade_button:
                            self.disabled_button = "health_upgrade"
                            self.health_upgrade_button.disable()
                            self.speed_upgrade_button.enable()
                            self.damage_upgrade_button.enable()

                MANAGER.process_events(event)
            MANAGER.update(clock.tick(FPS))
            self.overlay_surface.blit(self.game_over, (95, 170))
            MANAGER.draw_ui(self.overlay_surface)  
            self.parent_screen.blit(self.overlay_surface, (0, 0))  

            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
    upgrade_page = UpgradePage(screen)
    upgrade_page.run()