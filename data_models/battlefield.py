"""Class file for battlefields

A battlefield encompasses the logic for a contest between a robot and
a dinosaur. Messages will be displayed for the beginning of a game and
the resulting victor.
"""
import random
from secrets import randbits
from tokenize import group
from data_models.fleet import Fleet
from data_models.herd import Herd
from data_models.console_display import ConsoleDisplay

class Battlefield:
    """Represents a battlefield where the game takes place

    Instance Variables:
        fleet: Fleet
            the fleet of robots that will take part in the battle
        herd: Herd
            the herd of dinosaurs that will take part in the battle

    Public Methods:
        run_game() : void
            This will run all game-related logic and initiate the battle
        determine_winner() : void
            This will display the results of the battle to the user
        battle_phase() : void
            This performs all battle logic between participants
        get_random_list_element(all_options: list:Any) : Any
            Returns a randomly selected element from a list of any type
        run_group_attack(attackers: list:(Dinosaur or Robot), targets: list:(Dinosaur or Robot)) : void
            Performs an attack for all attackers against random targets
    """
    def __init__(self):
        """Constructs a battlefield for the game to take place in

        Instance Variables:
            fleet: Fleet
                the fleet of robots that will take part in the battle
            herd: Herd
                the herd of dinosaurs that will take part in the battle
        """
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        """Performs all game logic

        Effects:
            Displays a welcome message
            Performs the battle between all participants
            Displays a message declaring the winner of the game
        """
        ConsoleDisplay.display_welcome()
        self.battle_phase()
        #self.determine_winner()

    def battle_phase(self):
        """Performs logic for the battle

        Effects:
            The health of participants will be reduced until one or more groups has no members with health greater than zero
        """
        participating_groups = ['robots', 'dinosaurs']
        while len([x for x in self.fleet.robots if x.health > 0]) > 0 and len([x for x in self.herd.dinosaurs if x.health > 0]) > 0:
            group_to_attack_first = self.get_random_list_element(participating_groups)
            if group_to_attack_first == 'dinosaurs':
                self.run_group_attack(self.herd.dinosaurs, self.fleet.robots)
                self.run_group_attack(self.fleet.robots, self.herd.dinosaurs)
            elif group_to_attack_first == 'robots':
                self.run_group_attack(self.fleet.robots, self.herd.dinosaurs)
                self.run_group_attack(self.herd.dinosaurs, self.fleet.robots)

    def run_group_attack(self, attackers, targets):
        """Perform attacks against a random target for all attackers

        Args:
            attackers: list:(Dinosaur or Robot)
                a list of all attacking entities
            targets: list:(Dinosaur or Robot)
                a list of all available target entities
        
        Effects:
            The health of selected targets will be reduced
        """
        for attacker in attackers:
            if attacker.health <= 0:
                continue
            remaining_targets = [t for t in targets if t.health > 0]
            if len(remaining_targets) > 0:
                target = self.get_random_list_element(remaining_targets)
                attacker.attack(target)
            else:
                break

    def get_random_list_element(self, all_options):
        """Determines a random element from a list

        Args:
            all_options: list
                a list of all options to choose from

        Returns:
            a randomly chosen element of the list
        """
        return random.choice(all_options)
    
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