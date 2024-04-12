import pygame
import pygame_gui
from pirate_tuto import Pirate

class Tutorial():
    
    def __init__(self, screen, gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
    
    def run(self):
        clock = pygame.time.Clock()
        self.screen.blit(pygame.image.load("images/splash_art.png").convert_alpha(), (0, 0))
        self.MANAGER = pygame_gui.UIManager((640, 1000), "theme.json")
        button_start = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((220, 560), (100, 40)),
            text="START",
            manager=self.MANAGER,
            object_id="button",
            tool_tip_text="Start the game")
        label_tutorial = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 20), (500, 400)),
            text="Tutorial",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 60), (500, 400)),
            text="This is a tutorial on how to play the game.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 80), (500, 400)),
            text="Press the start button to start the game.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 120), (500, 400)),
            text="Use the keys 'q' and 'd' or '←'and '→' to move the pirate",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 100), (500, 400)),
            text="Press the space key to shoot the pirate's cannon.",
            manager=self.MANAGER,
            object_id="label")
        label_tutorial_text_5 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 140), (500, 400)),
            text="Press the escape key to quit the game.",
            manager=self.MANAGER,
            object_id="label")
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        pirate = Pirate(all_sprites, bullets, 640, 1000)
        all_sprites.add(pirate)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                    if event.key == pygame.K_SPACE:
                        pirate.shoot()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_start:
                            print("Start button clicked")
                            self.gameStateManager.set_state('game')
                            running = False
                self.MANAGER.process_events(event)
            self.MANAGER.update(clock.tick(60))
            all_sprites.update()
            all_sprites.draw(self.screen)
            self.MANAGER.draw_ui(self.screen)
            pygame.display.flip()