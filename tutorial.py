import pygame

def Tutorial():
    statisticsBar = pygame.Rect(0, 0, 60, 640) 

    pygame.init()
    screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), statisticsBar)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()
    pygame.quit()