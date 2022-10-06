# Import libraries
import pygame
import pygame.camera
from pygame.locals import *
from math import ceil
import numpy as np

# Import files
from display_components.fps_counter import FPS_Counter
from organisms import Organisms


class Enviroment:
    def __init__(self) -> None:
        # Display settings
        self.cell_border_width = 0.5
        self.cell_size = 15

        self.screen_resolution = (round(1920 * 0.7), round(1080 * 0.8))
        self.screen_name = "Artificial Life Simulation"

        # Simulation settings
        self.organisms = Organisms()
        self.is_active = False
        self.step = 0

        # User interfacing variables
        self.current_selection = None

        # The map will be a bit larger to count for the future scrolling across the screen (3 cell padding)
        # Calculate the map size
        map_width = ceil(self.screen_resolution[0] / self.cell_size) + 6
        map_height = ceil(self.screen_resolution[1] / self.cell_size) + 6
        self.map = np.full((map_height, map_width), fill_value=None)

        # Graphics settings
        self.colour_dictionary = {
            'outline': (58, 59, 60),
            'background': (24, 25, 26)
        }


    # Start the enviroment
    def run_simulation(self):
        self.is_active = True
        self.display_init()


    # Step in the simulation
    def step_simulation(self):
        pass


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
            self.screen.fill(self.colour_dictionary['background'])

            # Draw the grid
            self.draw_cells()

            # Update the fps
            self.fps_counter.update_fps()

            # Flip the display
            pygame.display.flip()

    
    def events_checker(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_active = False

            if event.type == pygame.MOUSEMOTION:
                # If left click is pressed
                if event.buttons[0] == 1:
                    self.user_placing(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.user_placing(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.step_simulation()


    def draw_cells(self):
        # Turn the map into a iterable list
        map = self.map.tolist()

        # We enumerate over every single cell
        for y, row in enumerate(map):
            # Offset it by 3 for the map padding
            y -= 3

            for x, cell in enumerate(row):
                # Offset it by 3 for the map padding
                x -= 3

                if cell == None:
                    continue

                # The background is the outline colour
                # We draw a rectangle to display if the cell is empty with the background colour or any other type of cell
                colour = cell.colour
                rect_cords = (
                    x * self.cell_size + self.cell_border_width,
                    y * self.cell_size + self.cell_border_width,
                    self.cell_size - self.cell_border_width * 2,
                    self.cell_size - self.cell_border_width * 2
                )
                pygame.draw.rect(self.screen, color=colour, rect=rect_cords)
    

    def user_placing(self, pos):
        for oy, row in enumerate(self.map.tolist()):
            # oy = original y
            y = oy - 3
            for ox, cell in enumerate(row):
                # ox = original x
                x = ox - 3

                # Calculate the bounding box of the rectangles
                x1 = x * self.cell_size + self.cell_border_width
                y1 = y * self.cell_size + self.cell_border_width
                x2 = x1 + (self.cell_size - self.cell_border_width * 2)
                y2 = y1 + (self.cell_size - self.cell_border_width * 2)

                # Check if the event pos is inside the the bounding box of the rectangle
                if x1 < pos[0] < x2 and y1 < pos[1] < y2:
                    # Place the current selection
                    self.organisms.place_organism(self.map, self.current_selection, (oy, ox))