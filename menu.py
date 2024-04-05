import pygame
import pygame_gui
from pygame.locals import *
from pygame_gui import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
    screen.fill((255, 255, 255))
    custom_font = pygame.font.Font("Fonts/Minecraft.ttf", 24)
    # statisticsBar = pygame.Rect(0, 0, 60, 640) 
    # pygame.draw.rect(screen, (0, 0, 0), statisticsBar)
    button_play = pygame.Rect(125, 70, 290, 100)
    button_leaderboard = pygame.Rect(170, 290, 200, 60)
    button_quit = pygame.Rect(195, 580, 150, 40)
    pygame.draw.rect(screen, "black", button_play)
    pygame.draw.rect(screen, "black", button_leaderboard)
    pygame.draw.rect(screen, "black", button_quit)
    button_play_text = custom_font.render("PLAY", True, (255, 255, 255))
    button_leaderboard_text = custom_font.render("LEADERBOARD", True, (255, 255, 255))
    button_quit_text = custom_font.render("QUIT", True, (255, 255, 255))
    screen.blit(button_play_text, (button_play.x + button_play.width // 2 - button_play_text.get_width() // 2, button_play.y + button_play.height // 2 - button_play_text.get_height() // 2)) 
    screen.blit(button_leaderboard_text, (button_leaderboard.x + button_leaderboard.width // 2 - button_leaderboard_text.get_width() // 2, button_leaderboard.y + button_leaderboard.height // 2 - button_leaderboard_text.get_height() // 2))
    screen.blit(button_quit_text, (button_quit.x + button_quit.width // 2 - button_quit_text.get_width() // 2, button_quit.y + button_quit.height // 2 - button_quit_text.get_height() // 2))
    
    
    # fond = pygame.image.load("Images/plage.png").convert()
    # pygame.transform.scale(fond, (540, 640))
    
    running = True
    while running == True:
        #screen.blit(fond, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_play.collidepoint(mouse_pos):
                        print("Play button clicked")
                    elif button_leaderboard.collidepoint(mouse_pos):
                        print("Leaderboard button clicked")
                    elif button_quit.collidepoint(mouse_pos):
                        print("Quit button clicked")
                        running = False
        pygame.display.flip()
    pygame.quit()
    
main()