"""Class file for herds of dinosaurs

Describes a group of dinosaurs that are allied in battle
"""
from data_models.dinosaur import Dinosaur

class Herd:
    """Represents a group of allied dinosaurs

    Instance Variables:
        dinosaurs: list:Dinosaur
            a list of dinosaurs who join into a herd

    Private Methods:
        _generate_herd(): list:Dinosaur
            generates a list of dinosaurs that constitute the herd
    """
    def __init__(self):
        """Constructs a herd

        Instance Variables:
            dinosaurs: list:Dinosaur
                a list of dinosaurs who join into a herd
        """
        self.dinosaurs = self._generate_herd()

    def _generate_herd(self):
        """Generates a list of dinosaurs that constitute the herd

        Returns:
            list of Dinosaur objects
        """
        return [
            Dinosaur('Rosie', 25),
            Dinosaur('Littlefoot', 25),
            Dinosaur('Bob', 20)
        ]