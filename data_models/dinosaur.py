"""Class file for Dinosaurs

Each dinosaur will have a name, health, and attack power.
Dinosaurs can participate in battles against robots
"""
from data_models.combatant import Combatant

class Dinosaur(Combatant):
    """Represents a single dinosaur that can participate in battles

    Inherited Instance Variables:
        name: string
            the name of the dinosaur
        health: int
            the current health of the dinosaur
    Instance Variables:
        attack_power: int
            the dinosaur's attack power that can damage opponents

    Inherited Public Methods:
        attack(attack_power: int, target: Combatant)
            allows the combatant to attack another target combatant and do damage
    Public Methods:
        get_attack_power(): int
            returns the attack power of the dinosaur
    """
    def __init__(self, name, attack_power):
        """Constructs a dinosaur

        Instance Variables from Parameters:
            name: string
                the name of the dinosaur
            attack_power: int
                the dinosaur's attack power that can damage opponents
        Inherited Instance Variables:
            health: int
                the current health of the dinosaur
        """
        Combatant.__init__(self, name)
        self.attack_power = attack_power

    def get_attack_power(self):
        """Returns the dinosaur's current attack power

        Returns:
            int of the current attack power
        """
        return self.attack_power