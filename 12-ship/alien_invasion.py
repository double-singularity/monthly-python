import sys, pygame

class AlienInvasion:
    """Main class to manage assets and behaviour"""

    def __init__(self) -> None:
        
        pygame.init() # initialize pygame

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

        self.clock = pygame.time.Clock()
        self.bg_color = (230, 230, 230)

    def run_game(self) -> None:
        """Start the game loop"""
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Create the game instance
    ai = AlienInvasion()
    ai.run_game()