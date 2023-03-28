import pygame

class DroneSimulation:
    def __init__(self, grid_width, grid_height, drones):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.drones = drones

        # Initialize Pygame
        pygame.init()

        # Set the window size based on the grid size
        self.window_size = (grid_width * 50, grid_height * 50)
        self.screen = pygame.display.set_mode(self.window_size)

    def draw_grid(self):
        # Draw the grid lines
        for x in range(0, self.window_size[0], 50):
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.window_size[1]))
        for y in range(0, self.window_size[1], 50):
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (self.window_size[0], y))

    def draw_drones(self):
        # Draw each drone as a square
        for drone in self.drones:
            x, y = drone['position']
            pygame.draw.rect(self.screen, (0, 255, 0), (x*50, y*50, 50, 50))

    def run_simulation(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw the grid and drones
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_drones()

            # Update the display
            pygame.display.flip()

            # Delay for smooth animation
            clock.tick(10)

        pygame.quit()
