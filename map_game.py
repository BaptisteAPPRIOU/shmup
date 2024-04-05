import pygame
import time
import pygame_gui

class mapGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
        self.screen.fill((255, 255, 255))
        self.statistics_bar = pygame.Rect(0, 0, 60, 640)
        self.beach = pygame.Rect(60, 550, 480, 90)
        self.clock = pygame.time.Clock()
        pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (60, 30)), text='Quit', manager=pygame_gui.UIManager((540, 640)))

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
        pygame.draw.rect(self.screen, "YELLOW", self.beach)

    def update_display(self):
        pygame.display.flip()
        self.clock.tick(60)

    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    map_game = mapGame()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        map_game.screen.fill((255, 255, 255))  
        map_game.draw()  
        map_game.update_display() 
    map_game.quit()
