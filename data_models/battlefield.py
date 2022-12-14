"""Class file for battlefields

A battlefield encompasses the logic for a contest between a robot and
a dinosaur. Messages will be displayed for the beginning of a game and
the resulting victor.
"""
import random
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
            This determines the winner of the battle based on remaining health
        battle_phase() : void
            This performs all battle logic between participants
        get_random_list_element(all_options: list:Any) : Any
            Returns a randomly selected element from a list of any type
        run_group_attack(attackers: list:Combatant, targets: list:Combatant) : void
            Performs an attack for all attackers against random targets
        run_single_attack(attacker: Combatant, target: Combatant)
            Performs an attack from a single attacker against a single target
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
        winner = self.determine_winner()
        if winner != '':
            ConsoleDisplay.display_winner(winner)
        else:
            ConsoleDisplay.display_no_winner()

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
            attackers: list:Combatant
                a list of all attacking entities
            targets: list:Combatant
                a list of all available target entities
        
        Effects:
            The health of selected targets will be reduced for each successful attack
        """
        for attacker in attackers:
            if attacker.health <= 0:
                continue
            remaining_targets = [t for t in targets if t.health > 0]
            if len(remaining_targets) > 0:
                target = self.get_random_list_element(remaining_targets)
                self.run_single_attack(attacker, target)
            else:
                break

    def run_single_attack(self, attacker, target):
        """Perform an attack against a single target

        Args:
            attacker: Combatant
                the attacking entity
            target: Combatant
                the target of the attack
        
        Effects:
            If the attack is successful the health of selected target will be reduced
            Displays attack message to the console
        """
        attack_succeeds = self.get_random_list_element([True, False])
        if attack_succeeds:
            current_attack_power = attacker.get_attack_power()
            attacker.attack(current_attack_power, target)
        else:
            ConsoleDisplay.display_attack_missed(attacker.name, target.name)

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
        """Determines the winner of the battle based on remaining health

        Returns:
            String representing the winning group
        """
        if len([x for x in self.fleet.robots if x.health > 0]) > 0 and len([x for x in self.herd.dinosaurs if x.health > 0]) == 0:
            return 'Robots'
        elif len([x for x in self.fleet.robots if x.health > 0]) == 0 and len([x for x in self.herd.dinosaurs if x.health > 0]) > 0:
            return 'Dinosaurs'
        else:
            return ''