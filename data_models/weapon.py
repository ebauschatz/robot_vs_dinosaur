"""Class file for weapons

Each resulting object will represent a single weapon that can be
used in a battle to damage an opponent
"""
class Weapon:
    """Represents a single weapon that can be used by a robot to attack a foe

    Instance Variables:
        name: string
            represents the name of the weapon
        attack_power: int
            the attack power of the weapon
    """
    def __init__(self, name, attack_power):
        """Constructs a weapon instance

        Instance Variables from Parameters:
            name: string
                represents the name of the weapon
            attack_power: int
                the attack power of the weapon
        """
        self.name = name
        self.attack_power = attack_power