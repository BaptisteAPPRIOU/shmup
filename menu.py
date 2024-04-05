import pygame
import pygame_gui
from tutorial import Tutorial

def main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
    screen.fill((255, 255, 255))
    MANAGER = pygame_gui.UIManager((540, 640), "theme.json")
    # statisticsBar = pygame.Rect(0, 0, 60, 640) 
    # pygame.draw.rect(screen, (0, 0, 0), statisticsBar)
    button_play = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((125, 70), (290, 100)),
        text="PLAY",
        manager=MANAGER,
        object_id="button",
        tool_tip_text="Play")
    button_leaderboard = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((170, 290), (200, 60)),
        text="LEADERBOARD",
        manager=MANAGER,
        object_id="button",
        tool_tip_text="Leaderboard")
    button_quit = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((195, 580), (150, 40)),
        text="QUIT",
        manager=MANAGER,
        object_id="button",
        tool_tip_text="Quit")
    
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_play:
                        print("Play button clicked")
                        Tutorial()
                    elif event.ui_element == button_leaderboard:
                        print("Leaderboard button clicked")
                    elif event.ui_element == button_quit:
                        print("Quit button clicked")
                        running = False
            MANAGER.process_events(event)
        MANAGER.update(clock.tick(60))
        screen.fill((255, 255, 255))
        MANAGER.draw_ui(screen)
        pygame.display.flip()
    pygame.quit()
    
main()