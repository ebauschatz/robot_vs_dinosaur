"""Class file for Combatants

All participants in a battle should derive from the combatant parent class.
"""
from data_models.console_display import ConsoleDisplay

class Combatant:
    """Describes a single combatant

    Instance Variables:
        name: str
            the name of the combatant
        health: int
            the current health of the combatant

    Public Methods:
        attack(attack_power: int, target: Combatant)
            allows the combatant to attack another target combatant and do damage
        get_attack_power(): int
            returns the combatant's attack power
    """
    def __init__(self, name):
        """Constructs a combatant

        Instance Variables from Parameters:
            name: str
                the name of the combatant
        Instance Variables:
            health: int
                the current health of the combatant
        """
        self.name = name
        self.health = 100

    def attack(self, attack_power, target):
        """Allows the combatant to attack a target

        Args:
            attack_power: int
                the attack power of the current attack
            target: Combatant
                the target to attack
        
        Effects:
            The current health of the target is reduced by the value of the attack power
        """
        target.health -= attack_power
        ConsoleDisplay.display_attack_result(self.name, target.name, target.health)

    def get_attack_power(self):
        """Returns the attack power of the combattant for this attack

        Returns:
            int of the attack power
        """
        return 0