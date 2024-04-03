import pygame
from map_game import mapGame
from lifeboat import Lifeboat
from sloop import Sloop
from ship import Ship
import random

def main():
    map_game = mapGame()
    max_lifeboats = 10
    max_sloops = 4
    max_ships = 2
    lifeboats = []
    sloops = []
    ships = []  # Create a new list for ships
    cooldown = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        map_game.screen.fill((255, 255, 255))  
        map_game.draw()  

        if cooldown <= 0:
            if len(lifeboats) < max_lifeboats:
                if random.random() < 0.05:
                    new_lifeboat = Lifeboat(map_game.screen, hit_points=100, damage=10, speed=2, value=10)
                    while new_lifeboat.check_overlap(lifeboats):
                        new_lifeboat.spawn()
                    lifeboats.append(new_lifeboat)
                    cooldown = random.randint(10, 90)
                    print("Number of lifeboats:", len(lifeboats))

            if len(lifeboats) >= max_lifeboats - max_sloops and len(sloops) < max_sloops:
                if random.random() < 0.05:
                    new_sloop = Sloop(map_game.screen, hit_points=100, damage=10, speed=1.5, value=20)
                    while new_sloop.check_overlap(lifeboats + sloops):
                        new_sloop.spawn()
                    sloops.append(new_sloop)
                    cooldown = random.randint(10, 90)
                    print("Number of sloops:", len(sloops))

            if len(sloops) >= max_sloops - max_ships and len(ships) < max_ships:
                if random.random() < 0.05:
                    new_ship = Ship(map_game.screen, hit_points=100, damage=10, speed=1, value=30)
                    while new_ship.check_overlap(lifeboats + sloops + ships):
                        new_ship.spawn()
                    ships.append(new_ship)
                    cooldown = random.randint(10, 90)
                    print("Number of ships:", len(ships))

        for boat in lifeboats:
            boat.move()
            boat.draw()
        for sloop in sloops:
            sloop.move()
            sloop.draw()
        for ship in ships:
            ship.move()
            ship.draw()

        cooldown -= 1
        map_game.update_display() 
        
    map_game.quit()

if __name__ == "__main__":
    main()

