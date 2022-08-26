"""Class file for Robots

Each robot will have a name, health, a list of available weapons, and an active weapon they are
currently using to damage opponents in battle.
"""
from data_models.weapon import Weapon
from data_models.console_display import ConsoleDisplay
from data_models.combatant import Combatant

class Robot(Combatant):
    """Represents a single robot that can participate in battles

    Inherited Instance Variables:
        name: string
            the name of the robot
        health: int
            the current health of the robot
    Instance Variables:
        active_weapon: Weapon
            the weapon the robot is currently using
        available_weapons: list:Weapon
                a list of all available Weapon objects the robot can choose from

    Inherited Public Methods:
        attack(attack_power: int, target: Combatant)
            allows the combatant to attack another target combatant and do damage
    Public Methods:
        set_active_weapon() : void
            sets the currently active weapon for the robot
        get_attack_power() : int
            returns the attack power of the active weapon
    Private Methods:
        __set_available_weapons() : list:Weapon
            configures all weapons that are available to the robot
    """
    def __init__(self, name):
        """Constructs a robot

        Instance Variables from Parameters:
            name: string
                the name of the robot
        Inherited Instance Variables:
            health: int
                the current health of the robot
        Instance Variables:
            active_weapon: Weapon
                the weapon the robot is currently using
            available_weapons: list:Weapon
                a list of all available Weapon objects the robot can choose from
        """
        Combatant.__init__(self, name)
        self.active_weapon = Weapon('laser gun', 20)
        self.available_weapons = self.__set_available_weapons()

    def __set_available_weapons(self):
        """Configures all weapons available to the robot for battle

        Returns:
            A list of Weapon objects
        """
        return [
            Weapon('Laser Gun', 20),
            Weapon('Poison Dart', 15),
            Weapon('Rocket', 25)
        ]

    def set_active_weapon(self):
        """Sets the robot's active weapon

        Effects:
            Sets the active_weapon attribute
        """
        ConsoleDisplay.display_prompt_weapon_choice(self.name)
        ConsoleDisplay.display_all_list_options([x.name for x in self.available_weapons])
        valid_choice = False
        while valid_choice is False:
            user_choice = input('Please enter the number of your selection: ')
            if user_choice.isnumeric():
                valid_choice = True
        self.active_weapon = self.available_weapons[int(user_choice) - 1]

    def get_attack_power(self):
        """Returns the robot's current attack power
        
        Effects:
            Sets the robot's active weapon

        Returns:
            int of the active weapon's attack power
        """
        self.set_active_weapon()
        return self.active_weapon.attack_power