import pygame
import math

from character import Character
from settings import *


class Player(Character):
    def __init__(self, name: str, hp: int, ) -> None:
        self.color = 'red'
        super().__init__(name, hp)
        
    def draw(self, surface) -> None:
        
        rect = pygame.Rect(self.position, (20,20))
        pygame.draw.rect(surface=surface, rect=rect, color='red')
        pygame.draw.circle(surface, color=self.color, center=(self.position[0]+MAP_GRID_SIZE/2, self.position[1]+MAP_GRID_SIZE/2), radius=200, width=2)
        text = pygame.font.SysFont('Comic Sans MS', 20).render('P', False, 'black')
        surface.blit(text, self.position)
        hp_text = pygame.font.SysFont('Comic Sans MS', 20).render(f'{self.hp}', False, 'black')
        surface.blit(hp_text, (self.position[0], self.position[1]+10))
    
    def move_down(self):
        self.position[1] += 1
    def move_up(self):
        self.position[1] -= 1
    def move_left(self):
        self.position[0] -= 1
    def move_right(self):
        self.position[0] += 1


class Player2(Character):
    def __init__(self, name: str, hp: int, position: list[float] = [10,10]) -> None:
        super().__init__(name, hp, position)
        self.color = 'red'
        self.angle = 0
        self.velocity = 0.3
        
    def draw(self, surface) -> None:
        rect = pygame.Rect(self.position, (10,10))
        pygame.draw.rect(surface=surface, rect=rect, color=self.color)
        pygame.draw.circle(surface, color=self.color, center=(self.position[0]+MAP_GRID_SIZE/2, self.position[1]+MAP_GRID_SIZE/2), radius=200, width=2)
        text = pygame.font.SysFont('Comic Sans MS', 20).render('P', False, 'black')
        surface.blit(text, self.position)
        hp_text = pygame.font.SysFont('Comic Sans MS', 20).render(f'{self.hp}', False, 'black')
        surface.blit(hp_text, (self.position[0], self.position[1]+10))
    
    def update(self):
        self.position[0] += self.velocity * math.cos(self.angle)
        self.position[1] += self.velocity * math.sin(self.angle)
    
    def turn_left(self):
        self.angle -= 0.05
    def turn_right(self):
        self.angle += 0.05