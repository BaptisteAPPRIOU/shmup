import pygame
import pygame_gui

def UserChoice():

    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
    screen.fill((255, 255, 255))
    MANAGER = pygame_gui.UIManager((540, 640))

    Button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((125, 70), (290, 100)),
        text="PLAY",
        manager=MANAGER,
        object_id="button",
        tool_tip_text="Play"
    )

    #pygame_gui.UIManager.update(RefreshRate)
    #pygame_gui.UIManager.draw_ui((540, 640))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            MANAGER.process_events(event)
        
        MANAGER.update(clock.tick(60))
        screen.fill((255, 255, 255))
        MANAGER.draw_ui(screen)
        pygame.display.flip()
    pygame.quit()
    
UserChoice()