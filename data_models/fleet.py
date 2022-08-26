"""Class file for fleets of robots

Describes a group of robots that are allied in battle
"""
from data_models.robot import Robot

class Fleet:
    """Represents a group of allied robots

    Instance Variables:
        robots: list:Robot
            a list of robots who join into a fleet

    Private Methods:
        __generate_fleet(): list:Robot
            generates a list of robots that constitute the fleet
    """
    def __init__(self):
        """Constructs a fleet

        Instance Variables:
            robots: list:Robot
                a list of robots who join into a fleet
        """
        self.robots = self.__generate_fleet()

    def __generate_fleet(self):
        """Generates a list of robots that constitute the fleet

        Returns:
            list of Robot objects
        """
        return [
            Robot('Zearth'),
            Robot('K2S0'),
            Robot('Marvin')
        ]