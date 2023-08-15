import sys, pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Main class to manage assets and behaviour"""

    def __init__(self) -> None:
        
        pygame.init() # initialize pygame

        pygame.display.set_caption('Alien Invasion')
        self.settings = Settings()

        self.clock = pygame.time.Clock()

        width, height = self.settings.screen_width, self.settings.screen_height

        self.screen = pygame.display.set_mode((width, height))
        
        self.ship = Ship(self)

    def run_game(self) -> None:
        """Start the game loop"""
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Create the game instance
    ai = AlienInvasion()
    ai.run_game()