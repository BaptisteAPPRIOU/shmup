import pygame
import pygame_gui
from game_manager import GameManager

FPS = 60

class ExitPage:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen  # Reference to the screen of the calling page
        self.overlay_surface = pygame.Surface((500, 500), pygame.SRCALPHA)  # Create a transparent surface for the overlay page
        self.running = True  # Flag to control the running state of the exit page
        self.overlay_surface.set_alpha(58)  # Set the transparency of the overlay surface
        self.exit_sign = pygame.image.load("images/exit_sign.png").convert_alpha()  # Load the exit sign image

    def run(self):
        clock = pygame.time.Clock()
        MANAGER = pygame_gui.UIManager(self.parent_screen.get_size(), "theme.json")

        button_yes = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 375), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="yes_button")
        
        button_no = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((222, 425), (196, 36)),
            text="",
            manager=MANAGER,
            object_id="no_button")
        
        game_manager = GameManager() 

        while self.running:  # Run the exit page while the running flag is True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Stop running if the window is closed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False  # Stop running if ESC key is pressed
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_yes:
                            print("Yes button clicked")
                            game_manager.show_landing_page() 
                        elif event.ui_element == button_no:
                            print("No button clicked")
                            self.running = False  # Close the exit page

                MANAGER.process_events(event)
            MANAGER.update(clock.tick(FPS))
            # self.overlay_surface.fill((255, 255, 255, 8))  # Fill the overlay surface with semi-transparent black color
            # self.rectangle = pygame.draw.rect(self.overlay_surface, (255, 255, 255), self.rectangle)
            self.overlay_surface.blit(self.exit_sign, (170, 250))
            MANAGER.draw_ui(self.overlay_surface)  # Draw UI elements on the overlay surface
            self.parent_screen.blit(self.overlay_surface, (0, 0))  # Draw the overlay surface on the parent screen
            pygame.display.flip()

        # After the loop, clear the overlay surface
        # self.overlay_surface.fill((255, 255, 255, 8))
        # self.parent_screen.blit(self.overlay_surface, (0, 0))  # Draw the transparent surface to clear the overlay
        # pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 1000), pygame.NOFRAME)
    exit_page = ExitPage(screen)
    exit_page.run()