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

    def place_organism(self, map, organism, coords):
        map[coords] = organism()
        return map


    class Empty(object):
        def __init__(self) -> None:
            self.colour = (24, 25, 26)
            self.food_worth = 0
            self.health = 0

    
    class Food(object):
        def __init__(self) -> None:
            self.colour = (91, 95, 217)
            self.food_worth = 10
            self.health = 0

    class Frog(object):
        def __init__(self) -> None:
            self.colour = (86, 214, 99)
            self.food_worth = 5
            self.health = 10

            # Movement variables
            self.direction = 0

        def move(self):
            pass
            # Frog's signature move is hopping over things
