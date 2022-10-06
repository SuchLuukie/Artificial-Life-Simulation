# Import libraries
import numpy as np


class Organisms:
    def __init__(self) -> None:
        self.movement_directions = {
            0: [-1, 0], # Up
            1: [0, 1],  # Right
            2: [1, 0],  # Down
            3: [0, -1]  # Left
        }

    class BasicFlyer:
        pass


class Components:
    # The way the positions are stored in the genes will be as follows
    # First the letters of the specific components, then the direction of where it's placed
    # Then in that direction it will be placed like a cone

    # Example: Cn1
    # Translation: Consumer north position 1

    # C in the genetics
    class Consumer:
        pass

    # E in the genetics
    class Eye:
        pass

    # D in the genetics
    class Damager:
        pass

    # S in the genetics
    class Shield:
        pass

    # M in the genetics
    class Mover:
        pass