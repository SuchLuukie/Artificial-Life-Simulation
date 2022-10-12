# Import libraries
import numpy as np
from random import randint


# Import the components
from components import Components, Nucleas


class Genetics:
    def __init__(self) -> None:
        self.components = Components()


        # Settings for the component placement
        self.component_amount_range = [1, 10]
        self.placement_locations = range(0, 6)
        self.placement_directions = [
            "n",
            "e",
            "s",
            "w"
        ]
        self.random_gene()

        # The genetics will hold the information of the organisms
        # They will determine the indiviual components that the organisms are made out of
        # Aswell as their positions


    # Generates a random gene for an organism
    def random_gene(self):
        component_amount = randint(*self.component_amount_range)
        
        for new_component in range(component_amount):
            pass

    
    def translate_genes(self):
        return


    def mutate_gene(self):
        return

Genetics()