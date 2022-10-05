# Import libraries
import pygame
import pygame.camera
from pygame.locals import *
from math import ceil
import numpy as np

# Import files
from display_components.fps_counter import FPS_Counter


class Enviroment:
    def __init__(self) -> None:
        # Display settings
        self.cell_border_width = 0.5
        self.cell_size = 20

        self.screen_resolution = (round(1920 * 0.7), round(1080 * 0.8))
        self.screen_name = "Artificial Life Simulation"

        # Simulation settings
        self.is_active = False

        # The map will be a bit larger to count for the future scrolling across the screen (3 cell padding)
        # Calculate the map size
        map_width = ceil(self.screen_resolution[0] / self.cell_size) + 6
        map_height = ceil(self.screen_resolution[1] / self.cell_size) + 6
        self.map = np.zeros((map_height, map_width))

        # Graphics settings
        self.colour_dictionary = {
            'outline_colour': (58, 59, 60),
            0: (24, 25, 26),
            1: (91, 95, 217)
        }


    # Start the enviroment
    def run_simulation(self):
        self.is_active = True
        self.display_init()


    # Initial configuation of the display
    def display_init(self):
        # Make sure that the display should actually be initialised 
        if not self.is_active:
            return

        # Set screen parameters
        self.screen = pygame.display.set_mode(self.screen_resolution)

        # Create the FPS counter
        self.fps_counter = FPS_Counter(self.screen)
        
        # Set the caption and logo
        pygame.display.set_caption(self.screen_name)

        # Begin the display loop
        self.display_loop()


    # Main loop that will update the display every frame
    def display_loop(self):
        while self.is_active:
            # Check all the events
            self.events_checker()

            # Set the background colour with the cell outline colour
            self.screen.fill(self.colour_dictionary['outline_colour'])

            # Draw the grid
            self.draw_grid()

            # Update the fps
            self.fps_counter.update_fps()

            # Flip the display
            pygame.display.flip()

    
    def events_checker(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_active = False


    def draw_grid(self):
        # Turn the map into a iterable list
        map = self.map.tolist()

        # We enumerate over every single cell
        for y, row in enumerate(map):
            # Offset it by 3 for the map padding
            y -= 3

            for x, cell in enumerate(row):
                # Offset it by 3 for the map padding
                x -= 3

                # The background is the outline colour
                # We draw a rectangle to display if the cell is empty with the background colour or any other type of cell
                colour = self.colour_dictionary[cell]
                rect = (
                    x * self.cell_size + self.cell_border_width,
                    y * self.cell_size + self.cell_border_width,
                    self.cell_size - self.cell_border_width * 2,
                    self.cell_size - self.cell_border_width * 2
                )
                pygame.draw.rect(self.screen, color=colour, rect=rect)