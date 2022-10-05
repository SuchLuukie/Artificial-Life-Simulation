# Import libraries
import pygame

class FPS_Counter:
    def __init__(self, screen) -> None:
        pygame.font.init()

        # Display variables
        self.screen = screen
        self.font = pygame.font.SysFont('Sans-Serif', 25, bold=True)
        self.colour = (255, 255, 255)

        # FPS variables
        self.clock = pygame.time.Clock()
        self.fps_history_range = 200
        self.fps_history = []
        self.fps = 0

        self.fps_display()


    # Calculates the average FPS over the last n frames
    def update_fps(self):
        self.clock.tick()
        self.fps_history.append(self.clock.get_fps())

        if len(self.fps_history) > self.fps_history_range:
            del self.fps_history[0]

        total = 0
        for i in self.fps_history:
            total += i
        
        avg = total / len(self.fps_history)
        self.fps = round(avg)

        self.fps_display()


    def fps_display(self):

        fps_text = self.font.render(str(self.fps), False, self.colour)
        self.screen.blit(fps_text, (5, 5))