"""Application entry point

This will set up a new battlefield and run the game on that battlefield
"""
from data_models.battlefield import Battlefield

def main():
    """Application entry point

    Effects:
        Runs a game on a new battlefield
    """
    battlefield = Battlefield()
    battlefield.run_game()

if __name__ == '__main__':
    main()