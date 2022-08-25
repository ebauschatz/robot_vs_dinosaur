"""Class file for battlefields

A battlefield encompasses the logic for a contest between a robot and
a dinosaur. Messages will be displayed for the beginning of a game and
the resulting victor.
"""
from data_models.robot import Robot
from data_models.dinosaur import Dinosaur
from data_models.console_display import ConsoleDisplay

class Battlefield:
    """Represents a battlefield where the game takes place

    Instance Variables:
        robot: Robot
            the robot that will take part in the battle
        dinosaur: Dinosaur
            the dinosaur that will take part in the battle

    Public Methods:
        run_game() : void
            This will run all game-related logic and initiate the battle
        determine_winner() : void
            This will display the results of the battle to the user
        battle_phase() : void
            This performs all battle logic between participants
    """
    def __init__(self):
        """Constructs a battlefield for the game to take place in

        Instance Variables:
            robot: Robot
                the robot that will take part in the battle
            dinosaur: Dinosaur
                the dinosaur that will take part in the battle
        """
        self.robot = Robot('Zearth')
        self.dinosaur = Dinosaur('Rosie', 25)

    def run_game(self):
        """Performs all game logic

        Effects:
            Displays a welcome message
            Performs the battle between all participants
            Displays a message declaring the winner of the game
        """
        ConsoleDisplay.display_welcome()
        self.battle_phase()
        self.display_winner()

    def battle_phase(self):
        """Performs logic for the battle

        Effects:
            The health of participants will be reduced until one or more is not greater than zero
        """
        while self.dinosaur.health > 0 and self.robot.health > 0:
            #simulate simultaneous attacks instead of turn-based
            self.dinosaur.attack(self.robot)
            self.robot.set_active_weapon()
            self.robot.attack(self.dinosaur)
    
    def determine_winner(self):
        """Displays the winner of the battle

        Effects:
            The winner and associated message will be displayed to the console
        """
        if self.robot.health > 0 and self.dinosaur.health <= 0:
            ConsoleDisplay.display_winner('\nRobots are the best!', self.robot.name)
        elif self.dinosaur.health > 0 and self.robot.health <= 0:
            ConsoleDisplay.display_winner('\nObviously dinosaurs are superior!', self.dinosaur.name)
        else:
            ConsoleDisplay.display_no_winner(self.dinosaur.name, self.robot.name)