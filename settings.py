
RESOLUTION = (1280, 720)
TOP_BAR_HEIGHT = 40
BOTTOM_BAR_HEIGHT = 20
MAP_GRID_SIZE = 20


class Settings:
    def __init__(self) -> None:
        self.resolution = RESOLUTION
        self.top_bar_height = TOP_BAR_HEIGHT
        self.bottom_bar_height = BOTTOM_BAR_HEIGHT
        self.middle_window_height = self.resolution[1] - self.top_bar_height - self.bottom_bar_height
        self.map_grid_size = MAP_GRID_SIZE
        self.map_grid = (self.resolution[0] // self.map_grid_size, self.middle_window_height // self.map_grid_size)
        
        # print(f'{self.map_grid = }\n{self.middle_window_height = }')
        # print(f'{self.map_grid = }')
