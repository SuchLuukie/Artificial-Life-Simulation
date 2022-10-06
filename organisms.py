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
    class Consumer:
        pass

    class Eye:
        pass

    class Damager:
        pass

    class Shield:
        pass

    class Mover:
        pass