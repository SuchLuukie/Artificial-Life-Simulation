# Import libraries
import numpy as np


class Organism:
    def __init__(self, position) -> None:
        # Positioning and movement variables
        self.position = position
        self.movement_direction = 0
        self.movement_directions = {
            0: [-1, 0], # Up
            1: [0, 1],  # Right
            2: [1, 0],  # Down
            3: [0, -1]  # Left
        }


class TestOrganism(Organism):
    def __init__(self):
        pass