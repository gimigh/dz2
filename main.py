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




cat = Cat("myay")
for day in range(1, 31):

 action = random.choice(["eat", "play", "sleep"])

if action == "eat":
    cat.eat()
elif action == "play":
    cat.play()
else:
    cat.sleep()


