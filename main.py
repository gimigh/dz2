import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.mood = 70
        self.energy = 100

    def eat(self):
        self.hunger = max(0, self.hunger - 20)
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} is eating,please wait")

    def play(self):
        self.energy = max(0, self.energy - 30)
        self.hunger = min(100, self.hunger + 10)
        self.thirst = min(100, self.thirst + 10)
        print(f"{self.name} is playing")