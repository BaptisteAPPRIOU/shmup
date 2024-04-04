import pygame
from map_game import mapGame
from lifeboat import Lifeboat
from sloop import Sloop
from ship import Ship
from galion import Galion
import random

def main():
    map_game = mapGame()
    max_lifeboats = 10
    max_sloops = 4
    max_ships = 2
    vessels = {'lifeboats': [], 'sloops': [], 'ships': [], 'galion': None}                                  # Create a dictionary to store all vessels
    cooldown = 0                                                                                            # Cooldown for spawning new vessels      

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

        if cooldown <= 0:                                                                                   # Check if cooldown is over       
            if len(vessels['lifeboats']) < max_lifeboats:                                                   # Check if number of lifeboats is less than the maximum   
                if random.random() < 0.05:                                                                  # Randomly spawn a lifeboat   
                    new_lifeboat = Lifeboat(map_game.screen, hit_points=100, damage=10, speed=2, value=10)
                    while new_lifeboat.check_overlap(vessels['lifeboats']):                                 # Check if lifeboat overlaps with other lifeboats
                        new_lifeboat.spawn()
                    vessels['lifeboats'].append(new_lifeboat)
                    cooldown = random.randint(10, 90)
                    print("Number of lifeboats:", len(vessels['lifeboats']))

            if len(vessels['lifeboats']) >= max_lifeboats - max_sloops and len(vessels['sloops']) < max_sloops:                 
                if random.random() < 0.05:
                    new_sloop = Sloop(map_game.screen, hit_points=100, damage=10, speed=1.5, value=20)
                    while new_sloop.check_overlap(vessels['lifeboats'] + vessels['sloops']):
                        new_sloop.spawn()
                    vessels['sloops'].append(new_sloop)
                    cooldown = random.randint(10, 90)
                    print("Number of sloops:", len(vessels['sloops']))

            if len(vessels['sloops']) >= max_sloops - max_ships and len(vessels['ships']) < max_ships:
                if random.random() < 0.05:
                    new_ship = Ship(map_game.screen, hit_points=100, damage=10, speed=1, value=30)
                    while new_ship.check_overlap(vessels['lifeboats'] + vessels['sloops'] + vessels['ships']):
                        new_ship.spawn()
                    vessels['ships'].append(new_ship)
                    cooldown = random.randint(10, 90)
                    print("Number of ships:", len(vessels['ships']))

            if len(vessels['ships']) == max_ships and vessels['galion'] is None:
                if random.random() < 0.05:
                    galion = Galion(map_game.screen, hit_points=100, damage=10, speed=0.5, value=50)
                    galion.spawn()
                    vessels['galion'] = galion
                    cooldown = random.randint(10, 90)
                    print("Galion spawned")

        for vessel_type in vessels.values():                                                                # Iterate through all vessels      
            if isinstance(vessel_type, list):                                                               # Check if vessel is a list        
                for vessel in vessel_type:                                                                  # Iterate through each vessel in the list     
                    vessel.move()
                    vessel.draw()
            elif isinstance(vessel_type, Galion) and vessel_type is not None:                               # Check if vessel is a Galion and not None
                vessel_type.move()
                vessel_type.draw()

        cooldown -= 1
        map_game.update_display() 
        
    map_game.quit()

if __name__ == "__main__":
    main()
