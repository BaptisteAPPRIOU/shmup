from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, hit_points, damage, speed, value):
        self.hitPoints = hit_points
        self.damage = damage
        self.speed = speed
        self.value = value

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self):
        pass