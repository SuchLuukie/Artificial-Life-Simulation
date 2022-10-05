# Import libraries
import pygame
import pygame.camera
from pygame.locals import *
from math import ceil
import numpy as np


class Enviroment:
    def __init__(self) -> None:

        # Display settings
        self.grid_line_width = 1
        self.grid_size = 100
        self.grid_padding = 10

        self.screen_size = (round(1920 * 0.7), round(1080 * 0.8))
        self.screen_name = "Artificial Life Simulation"

        # Simulation settings
        self.is_active = False
        self.map = np.zeros((ceil(self.screen_size[0] / (self.grid_size+self.grid_line_width)), ceil(self.screen_size[1] / (self.grid_size+self.grid_line_width))))

        # Graphics settings
        self.colour_dictionary = {
            'background': (24, 25, 26),
            'grid_colour': (58, 59, 60),
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
        self.screen = pygame.display.set_mode(self.screen_size)
        
        # Set the caption and logo
        pygame.display.set_caption(self.screen_name)

        # Begin the display loop
        self.display_loop()


    # Main loop that will update the display every frame
    def display_loop(self):
        while self.is_active:
            # Check all the events
            self.events_checker()

            # Set the background colour
            self.screen.fill(self.colour_dictionary['background'])

            # Draw the grid
            self.draw_grid()
            self.draw_grid_cells()

            # Flip the display
            pygame.display.flip()

    
    def events_checker(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_active = False


    def draw_grid(self):
        # First draw the horizontal lines for the grid every grid length
        for px in range(0, self.screen_size[1], self.grid_size):
            # Draw line from 0 to the screen width to start drawing the grid
            # We take px as the Y to get the correct spacing for the grid
            pygame.draw.line(self.screen, self.colour_dictionary['grid_colour'], (0, px+1), (self.screen_size[0], px), self.grid_line_width)

        # Now we draw the vertical lines to finish the grid
        for px in range(0, self.screen_size[0], self.grid_size):
            # Draw line from 0 to the screen height to finish drawing the grid
            # We take px as the X to get the correct spacing for the grid
            pygame.draw.line(self.screen, self.colour_dictionary['grid_colour'], (px, 0), (px, self.screen_size[1]), self.grid_line_width)
    

    def draw_grid_cells(self):
        map = self.map.tolist()

        for y, row in enumerate(map):
            for x, cell in enumerate(row):
                if cell <= 0:
                    continue

                # If it's not blank get the colour and the rectangle locations to draw the cell
                colour = self.colour_dictionary[cell]
                rect = (
                    self.grid_size * x + self.grid_line_width + self.grid_padding,
                    self.grid_size * y + self.grid_line_width + self.grid_padding,
                    self.grid_size - self.grid_line_width - self.grid_padding*2,
                    self.grid_size - self.grid_line_width - self.grid_padding*2
                )

                # Then draw the rectangle
                pygame.draw.rect(self.screen, color=colour, rect=rect)