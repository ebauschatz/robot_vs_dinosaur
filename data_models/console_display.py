"""Class file for console display

This class houses static methods for displaying messages to the console
"""
class ConsoleDisplay:
    """Represents cases where information needs to be presented to the user via console display

    Public Static Methods:
        display_attack_result(attacker_name: str, target_name: str, target_health: int) : void
            Displays the result of a single attack
        display_all_list_options(all_options: list:str) : void
            Displays all options from the list and their index + 1
        display_prompt_weapon_choice(name: str) : void
            Displays a weapon selection prompt
        display_welcome() : void
            Displays a welcome message for the game
        display_winner(victory_message: str, winner_name: str) : void
            Displays the winner's name and a message
        display_no_winner() : void
            Displays a message when no winner could be determined
    """
    @staticmethod
    def display_attack_result(attacker_name, target_name, target_health):
        """Displays the result of a single attack

        Args:
            attacker_name: str
                the name of the attacker
            target_name: str
                the name of the target
            target_health: int
                the current health of the target after the attack damage is taken

        Effects:
            Displays the attacker and target names, as well as the target health to the console
        """
        print(f'\n{attacker_name} attacks! {target_name}\'s health is now {target_health}')

    @staticmethod
    def display_all_list_options(all_options):
        """Displays all options from a list

        Args:
            all_options: list:str
                a list of strings to display

        Effects:
            Displays all options and their index to the console
        """
        for index, option in enumerate(all_options):
            print(str(index + 1) + ' - ' + option)

    @staticmethod
    def display_prompt_weapon_choice(name):
        """Displays weapon selection prompt

        Args:
            name: str
                the name of the entity who will use the weapon

        Effects:
            Displays the weapon selection prompt to the console
        """
        print(f'\nPlease choose a weapon for {name} to use on this attack:')

    @staticmethod
    def display_welcome():
        """Display a welcome message for the game

        Effects:
            Displays a game welcome message to the console
        """
        print('\nWelcome to the battlefield, where robots and dinosaurs will battle for ultimate supremacy!')

    @staticmethod
    def display_winner(winner_name):
        """Displays the winner of the battle
        
        Args:
            victory_message: str
                context message to display regarding the win
            winner_name: str
                the name of the battle winner

        Effects:
            The winner and associated message will be displayed to the console
        """
        print(f'\n{winner_name} won!')

    @staticmethod
    def display_no_winner():
        """Displays message when no winner could be determined

        Effects:
            Displays a message and the names to the console
        """
        print(f'\nThere was no clear winner.')