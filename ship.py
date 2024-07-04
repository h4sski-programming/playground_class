import pygame

from character import Character
from settings import *

class Ship(Character):
    def __init__(self, name: str, hp: int, position: list[int], 
                 country: str, speed_max: float, momentum: float, course: float, 
                 canons_max: int, canons: int, canons_range :float, reload_time: float, 
                 ship_type: str) -> None:
        self.country = country          # list['spain', 'french', 'england', 'netherland'] or in short list['s', 'f', 'e', 'n']
        self.speed_max = speed_max
        self.speed = 0
        self.momentum = momentum
        self.course = course      # degrees 0~360
        self.direction = self.course
        self.canons_max = canons_max
        self.canons = canons
        self.canons_range = canons_range
        self.reload_time = reload_time
        self.ship_type = ship_type
        self.color = ''
        
        super().__init__(name, hp, position)
        self.assign_color()
    
    def assign_color(self) -> None:
        if self.country == 'spain':
            self.color = 'yellow'
        elif self.country == 'french':
            self.color = 'violet'
        elif self.country == 'netherland':
            self.color = 'orange'
        elif self.country == 'england':
            self.color = 'white'
        else:
            self.color = 'blue'
        
    def draw(self, surface) -> None:
        
        rect = pygame.Rect(self.position, (20,20))
        pygame.draw.rect(surface=surface, rect=rect, color=self.color)
        pygame.draw.circle(surface, color=self.color, center=(self.position[0]+MAP_GRID_SIZE/2, self.position[1]+MAP_GRID_SIZE/2), radius=self.canons_range, width=2)
        text = pygame.font.SysFont('Comic Sans MS', 30).render(self.ship_type, False, 'black')
        surface.blit(text, self.position)
        

class Galeon_ship(Ship):
    def __init__(self, name: str, hp: int, position: list[int], country: str, course: float, canons: int) -> None:
        super().__init__(name, hp, position, country=country, speed_max=4, momentum=12, course=course, 
                         canons_max=240, canons=canons, canons_range=110, reload_time=2.4, ship_type='g')


class Frigate_ship(Ship):
    def __init__(self, name: str, hp: int, position: list[int], country: str, course: float, canons: int) -> None:
        super().__init__(name, hp, position, country=country, speed_max=6, momentum=10, course=course, 
                         canons_max=300, canons=canons, canons_range=130, reload_time=2, ship_type='f')


class Brigantine_ship(Ship):
    def __init__(self, name: str, hp: int, position: list[int], country: str, course: float, canons: int) -> None:
        super().__init__(name, hp, position, country=country, speed_max=10, momentum=6, course=course, 
                         canons_max=160, canons=canons, canons_range=80, reload_time=1.3, ship_type='b')
        
        
class Sloop_ship(Ship):
    def __init__(self, name: str, hp: int, position: list[int], country: str, course: float, canons: int) -> None:
        super().__init__(name, hp, position, country=country, speed_max=18, momentum=3, course=course, 
                         canons_max=60, canons=canons, canons_range=50, reload_time=0.4, ship_type='s')