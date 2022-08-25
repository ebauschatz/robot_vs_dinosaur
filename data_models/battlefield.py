"""Class file for battlefields

A battlefield encompasses the logic for a contest between a robot and
a dinosaur. Messages will be displayed for the beginning of a game and
the resulting victor.
"""
from data_models.robot import Robot
from data_models.dinosaur import Dinosaur

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
        display_welcome() : void
            This will dispay the initial startup welcome message to the user
        display_winner() : void
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
        self.display_welcome()
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
            self.robot.attack(self.dinosaur)
    
    def display_welcome(self):
        """Display a welcome message for the game

        Effects:
            Displays a game welcome message to the console
        """
        print('\nWelcome to the battlefield, where a robot and a dinosaur will battle for ultimate supremacy!')

    def display_winner(self):
        """Displays the winner of the battle

        Effects:
            The winner and associated message will be displayed to the console
        """
        if self.robot.health > 0 and self.dinosaur.health <= 0:
            print(f'\nRobots are the best! {self.robot.name} has triumphed!')
        elif self.dinosaur.health > 0 and self.robot.health <= 0:
            print(f'\nObviously dinosaurs are superior! {self.dinosaur.name} is the victor!')
        else:
            print(f'\nThere was no clear winner between {self.dinosaur.name} and {self.robot.name}.')