"""Class file for Dinosaurs

Each dinosaur will have a name, health, and attack power.
Dinosaurs can participate in battles against robots
"""
class Dinosaur:
    """Represents a single dinosaur that can participate in battles

    Instance Variables:
        name: string
            the name of the dinosaur
        attack_power: int
            the dinosaur's attack power that can damage opponents
        health: int
            the current health of the dinosaur

    Public Methods:
        attack(robot: Robot) : void
            lowers the health of the robot by the value of the dinosaur's attack power
    """
    def __init__(self, name, attack_power):
        """Constructs a dinosaur

        Instance Variables from Parameters:
            name: string
                the name of the dinosaur
            attack_power: int
                the dinosaur's attack power that can damage opponents
        Instance Variables:
            health: int
                the current health of the dinosaur
        """
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        """Allows the dinosaur to attack a robot

        Args:
            robot: Robot
                the robot to attack
        
        Effects:
            The current health of the robot is reduced by the value of the dinosaur's attack power
        """
        robot.health -= self.attack_power
        print(f'\n{self.name} attacks! {robot.name}\'s health is now {robot.health}')