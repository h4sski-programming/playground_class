import pygame

from settings import Settings
from map import Map
from player import Player, Player2
from ship import Sloop_ship, Brigantine_ship, Frigate_ship, Galeon_ship

class Game:
    def __init__(self) -> None:
        pass
        # pygame setup
        pygame.init()
        # pygame.key.set_repeat(interval=10)
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = Map(self)
        self.player = Player('player', 10)
        self.player2 = Player2(name='player2', hp=10)
        self.enemys = [
            Sloop_ship('e1', 10, [600,400], 'england', 270, 20),
            Brigantine_ship('s1', 10, [640,360], 'netherland', 270, 20),
            Frigate_ship('f1', 10, [800,240], 'france', 270, 20),
            Galeon_ship('g1', 10, [740,120], 'spain', 270, 20),
            ]

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.player.move_down()
        if keys[pygame.K_UP]:
            self.player.move_up()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        
        
        if keys[pygame.K_a]:
            self.player2.turn_left()
        if keys[pygame.K_d]:
            self.player2.turn_right()

    
    def update(self):
        self.player2.update()

    def draw(self):
        self.screen.fill((80, 80, 80))
        
        self.top_bar = pygame.Surface((self.settings.resolution[0], self.settings.top_bar_height))
        self.middle_surface = pygame.Surface((self.settings.resolution[0], self.settings.resolution[1] - (self.settings.top_bar_height + self.settings.bottom_bar_height)))
        self.bottom_bar = pygame.Surface((self.settings.resolution[0], self.settings.bottom_bar_height))
        
        self.top_bar.fill((80, 80, 80))
        
        self.map.draw(self.middle_surface)
        self.player.draw(self.middle_surface)
        self.player2.draw(self.middle_surface)
        for enemy in self.enemys:
            enemy.draw(self.middle_surface)
        
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