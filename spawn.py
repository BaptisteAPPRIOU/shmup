from zombie import Zombie
from zombie2 import Zombie_2
import random



def SpawnZombie(co_x, co_y, zombies, zombie_type):
    if zombie_type == 1:  # Spawn zombie type 1
        zombie = Zombie(co_x, co_y, zombies)
        zombies.add(zombie)
    elif zombie_type == 2:  # Spawn zombie type 2
        zombie = Zombie_2(co_x, co_y, zombies)
        zombies.add(zombie)