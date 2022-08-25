from data_models.robot import Robot
from data_models.dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('Zearth')
        self.dinosaur = Dinosaur('Rosie', '25')

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to the battlefield, where a robot and a dinosaur will battle for ultimate supremacy!')

    def battle_phase(self):
        pass

    def display_winner(self):
        if self.robot.health > 0 and self.dinosaur.health <= 0:
            print(f'\nRobots are the best! {self.robot.name} has triumphed!')
        elif self.dinosaur.health > 0 and self.robot.health <= 0:
            print(f'\nObviously dinosaurs are superior! {self.robot.name} is the victor!')
        else:
            print(f'\nThere was no clear winner between {self.dinosaur.name} and {self.robot.name}.')