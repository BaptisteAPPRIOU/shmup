import enemy_creator

class galeon(enemy_creator.Enemy):
    
    def __init__(self, hit_points, damage, speed, value):
        self.hitPoints = 1000
        self.damage = 100
        self.speed = 40
        self.value = 100

    def attack(self):
        pass

    def move(self):
        pass