"""Class file for Robots

Each robot will have a name, health, and an active weapon they are
currently using to damage opponents in battle.
"""
from data_models.weapon import Weapon
from data_models.console_display import ConsoleDisplay

class Robot:
    """Represents a single robot that can participate in battles

    Instance Variables:
        name: string
            the name of the robot
        health: int
            the current health of the robot
        active_weapon: Weapon
            the weapon the robot is currently using
        available_weapons: list:Weapon
                a list of all available Weapon objects the robot can choose from

    Public Methods:
        attack(dinosaur: Dinosaur) : void
            lowers the health of the dinosaur by the value of the active weapon's attack power and displays the result
        set_active_weapon() : void
            sets the currently active weapon for the robot
    Private Methods:
        _set_available_weapons() : list:Weapon
            configures all weapons that are available to the robot
    """
    def __init__(self, name):
        """Constructs a robot

        Instance Variables from Parameters:
            name: string
                the name of the robot
        Instance Variables:
            health: int
                the current health of the robot
            active_weapon: Weapon
                the weapon the robot is currently using
            available_weapons: list:Weapon
                a list of all available Weapon objects the robot can choose from
        """
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('laser gun', 20)
        self.available_weapons = self._set_available_weapons()

    def _set_available_weapons(self):
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

    def attack(self, dinosaur):
        """Allows the robot to attack a dinosaur

        Args:
            dinosaur: Dinosaur
                the dinosaur to attack
        
        Effects:
            The current health of the dinosaur is reduced by the attack power of the active weapon
            Displays the new current health of the dinosaur to the console
        """
        dinosaur.health -= self.active_weapon.attack_power
        ConsoleDisplay.display_attack_result(self.name, dinosaur.name, dinosaur.health)