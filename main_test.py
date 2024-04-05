import pygame
from lifeboat_test import Lifeboat
from sloop_test import Sloop

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((540, 640), pygame.NOFRAME)
        self.statistics_bar = pygame.Rect(0, 0, 60, 640)
        self.beach = pygame.Rect(60, 550, 480, 90)
        self.vessels = pygame.sprite.Group()

    def spawn_sloop(self,numb_sloops):
        for _ in range(numb_sloops):
            sloop = Sloop(self.screen, self.vessels, speed=3)
            self.vessels.add(sloop)

    def run(self):
        for _ in range(10):
            lifeboat = Lifeboat(self.screen, self.vessels, speed=3)
            self.vessels.add(lifeboat)

            sloop = Sloop(self.screen, self.vessels, speed=3)
            self.vessels.add(sloop)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
 
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 0), self.statistics_bar)
            pygame.draw.rect(self.screen, "YELLOW", self.beach)

            for vessel in self.vessels:
                vessel.move()
                #print(vessel.rect.y)
                self.screen.blit(vessel.image, vessel.rect)

            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.quit()

if __name__ == "__main__":
    Main().run()
