import pygame
import pygame_gui

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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_start:
                        print("Start button clicked")
            MANAGER.process_events(event)
        MANAGER.update(clock.tick(60))
        screen.fill((255, 255, 255))
        MANAGER.draw_ui(screen)
        pygame.display.flip()
    pygame.quit()
    
Tutorial()