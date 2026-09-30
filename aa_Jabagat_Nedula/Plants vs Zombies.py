class Plant:
    def __init__(self, name, health, damage):
        self.name=name
        self.health=health
        self.damage=damage

    def attack(self, zombie):
        zombie.health=zombie.health-self.damage
        

    def take_damage(self, amount):
        self.health=self.health-amount

    def show_stats(self):
        print(f"Plant name: {self.name}, Plant health: {self.health}")


class Zombie:

    def __init__(self, name, health, damage, distance):
        self.name=name
        self.health=health
        self.damage=damage
        self.distance=distance

    def move(self):
        self.distance+=1

    def attack(self,plant):
        plant.health=plant.health-self.damage

    def take_damage(self, amount):
        self.health=self.health-amount

    def show_stats(self):
        print(f"Zombie name: {self.name}, Zombie health: {self.health}")


game="" #for turn system



plant1=Plant("Peashooter", 100, 10)
plant2=Plant("Fire Peashooter", 100, 15)
zombie=Zombie("Head Office Impgantuar", 100, 50,0)

while game != "end":
    print("PLANTS VS ZOMBIES. One lane only")
    turn=1
    print(f"turn number {turn}")
    while plant1.health>0:
        plant1.attack(zombie)
        plant2.attack(zombie)
        zombie.attack(plant1)
        plant1.show_stats()
        plant2.show_stats()
        zombie.show_stats()
        if zombie.health<=0:
            game="end"
        turn+=1
        zombie.distance+=1
    while plant2.health>0 or zombie.health>0:
        print(f"turn number: {turn}")
        zombie.take_damage(plant2.damage)
        plant2.take_damage(zombie.damage)
        plant2.show_stats()
        zombie.show_stats()
        if plant2.health<=0:
            print("zombie wins")
            game="end"
        elif zombie.health<=0:
            print("plants win")
            game="end"
        turn+=1
#Testing Checklist

#The two plants have different damage values: Plant 1 damage = 10, Plant 2 damage = 15, Zombie health = 75
#Plants defeat the Zombie: Zombie health = 0, Game ends
#Zombie reaches distance 0 and damages a plant = Plant 1 health = 100, Zombie distance = 0, Zombie damage = 50, Plant health = 50
#Zombie targets the second plant after the first plant is defeated: Zombie's initial distance (from nearest living plant)= 0, Zombie's new distance (from nearest living plant) = 2
#Game stops when the Zombie or both plants are defeated: Zombie health = 0, Game Ends
