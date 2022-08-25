from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('laser gun', 20)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power