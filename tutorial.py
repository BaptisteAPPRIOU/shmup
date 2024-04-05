import pygame
import pygame_gui
from pirate import Pirate

def Tutorial():
    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
    screen.fill((255, 255, 255))
    MANAGER = pygame_gui.UIManager((540, 640), "theme.json")
    button_start = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((220, 560), (100, 40)),
        text="START",
        manager=MANAGER,
        object_id="button",
        tool_tip_text="Start the game")
    label_tutorial = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 20), (500, 400)),
        text="Tutorial",
        manager=MANAGER,
        object_id="label")
    label_tutorial_text = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 60), (500, 400)),
        text="This is a tutorial on how to play the game.",
        manager=MANAGER,
        object_id="label")
    label_tutorial_text_2 = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 80), (500, 400)),
        text="Press the start button to start the game.",
        manager=MANAGER,
        object_id="label")
    label_tutorial_text_3 = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 120), (500, 400)),
        text="Use the keys 'q' and 'd' or '←'and '→' to move the pirate",
        manager=MANAGER,
        object_id="label")
    label_tutorial_text_4 = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 100), (500, 400)),
        text="Press the space key to shoot the pirate's cannon.",
        manager=MANAGER,
        object_id="label")
    label_tutorial_text_5 = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 140), (500, 400)),
        text="Press the escape key to quit the game.",
        manager=MANAGER,
        object_id="label")
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    pirate = Pirate(all_sprites, bullets, 540, 480)
    all_sprites.add(pirate)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    pirate.shoot()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_start:
                        print("Start button clicked")
                        running = False
            MANAGER.process_events(event)
        MANAGER.update(clock.tick(60))
        screen.fill((255, 255, 255))
        all_sprites.update()
        all_sprites.draw(screen)
        MANAGER.draw_ui(screen)
        pygame.display.flip()
    pygame.quit()