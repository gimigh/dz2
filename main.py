import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.mood = 70
        self.energy = 100

    def eat(self):
        self.hunger -= 30
        self.energy += 10
        print(f"{self.name} is eating")

    def play(self):
        self.energy -= 30
        self.hunger += 10
        self.mood += 40
        print(f"{self.name} is playing")

    def sleep(self):
        self.hunger += 10
        self.mood -= 5
        self.energy +=50
        print(f"{self.name} is sleeping")

        if self.hunger >= 10 or self.happiness <= 0:
            self.is_alive = False

    def __str__(self):
        return f"{self.name}: mood {self.mood}, hunger {self.hunger}, energy {self.energy}"

cat = Cat("myay")