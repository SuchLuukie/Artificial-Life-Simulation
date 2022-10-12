# Import libraries

class Components:
    # The way the positions of the components are stored in the genes, it will be as follows
    # First the letters of the specific components, then the direction of where it's placed
    # Then in that direction it will be placed like a cone

    # Example: Cn1
    # Translation: Consumer north position 1

    def __init__(self, local_position):
        self.local_position = local_position

    # be able to iterate over all the different components
    def __iter__(self):
        for subclass in Components.__subclasses__():
            yield subclass


class Consumer(Components):
    def __init__(self):
        self.gene_type = "C"

class Eye(Components):
    def __init__(self):
        self.gene_type = "E"

class Damager(Components):
    def __init__(self):
        self.gene_type = "D"

class Shield(Components):
    def __init__(self):
        self.gene_type = "S"

class Mover(Components):
    def __init__(self):
        self.gene_type = "M"

# Center of each organism
class Nucleas:
    def __init__(self) -> None:
        self.colour = (76, 168, 186)