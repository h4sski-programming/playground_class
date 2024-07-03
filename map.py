import pygame
import random

class Map:
    def __init__(self, game) -> None:
        self.cols = game.settings.map_grid[0]
        self.rows = game.settings.map_grid[1]
        self.x_size = (game.settings.resolution[0] // self.cols)
        self.y_size = (game.settings.resolution[1] // self.rows)
        self.grid = self.generate_grid()
        
    def draw(self, surface) -> None:
        self.x_size = surface.get_width() // self.cols
        self.y_size = surface.get_height() // self.rows
        # print(surface.get_width(), surface.get_height(), self.x_size, self.y_size)
        for x in range(self.cols):
            for y in range(self.rows):
                rect = pygame.Rect((x*self.x_size, y*self.y_size), (self.x_size-1, self.y_size-1))
                color = (0,100, 250) if self.grid[y][x] else 'green'
                pygame.draw.rect(surface=surface, rect=rect, color=color)
    
    def generate_grid(self) -> list[list[int]]:
        # [[1 if random.random() < 0.85 else 0 for _ in range(self.cols)] for _ in range(self.rows)]
        # yes, I can do it as coperhansion, but it's prepared for more advanced generation
        # to-do -> change it to more real generator.
        grid = []
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                row.append(1 if random.random() < 0.85 else 0)
            grid.append(row)
        return grid