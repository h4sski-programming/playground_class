import pygame

from settings import Settings
from map import Map
from player import Player

class Game:
    def __init__(self) -> None:
        pass
        # pygame setup
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = Map(self)
        self.player = Player('player', 10)

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
    
    def update(self):
        pass

    def draw(self):
        self.screen.fill((80, 80, 80))
        
        self.top_bar = pygame.Surface((self.settings.resolution[0], self.settings.top_bar_height))
        self.middle_surface = pygame.Surface((self.settings.resolution[0], self.settings.resolution[1] - (self.settings.top_bar_height + self.settings.bottom_bar_height)))
        self.bottom_bar = pygame.Surface((self.settings.resolution[0], self.settings.bottom_bar_height))
        
        self.top_bar.fill((80, 80, 80))
        
        self.map.draw(self.middle_surface)
        self.player.draw(self.middle_surface)
        
        self.screen.blit(self.top_bar, (0, 0))
        self.screen.blit(self.middle_surface, (0, self.settings.top_bar_height))
        self.screen.blit(self.bottom_bar, (0, self.settings.resolution[1] - self.settings.bottom_bar_height))
        
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()