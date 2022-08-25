"""Class file for Robots

Each robot will have a name, health, and an active weapon they are
currently using to damage opponents in battle.
"""
from data_models.weapon import Weapon

class Robot:
    """Represents a single robot that can participate in battles

    Instance Variables:
        name: string
            the name of the robot
        health: int
            the current health of the robot
        active_weapon: Weapon
            the weapon the robot is currently using

    Public Methods:
        attack(dinosaur: Dinosaur) : void
            lowers the health of the dinosaur by the value of the active weapon's attack power
    """
    def __init__(self, name):
        """Constructs a robot

        Instance Variables from Parameters:
            name: string
                the name of the robot
            active_weapon: Weapon
                the weapon the robot is currently using
        Instance Variables:
            health: int
                the current health of the robot
        """
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('laser gun', 20)

    def attack(self, dinosaur):
        """Allows the robot to attack a dinosaur

        Args:
            dinosaur: Dinosaur
                the dinosaur to attack
        
        Effects:
            The current health of the dinosaur is reduced by the attack power of the active weapon
        """
        dinosaur.health -= self.active_weapon.attack_power