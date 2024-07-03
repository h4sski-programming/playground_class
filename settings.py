class Settings:
    def __init__(self) -> None:
        self.resolution = (1280, 720)
        self.top_bar_height = 40
        self.bottom_bar_height = 20
        self.map_grid = (64, (self.resolution[1] - self.top_bar_height - self.bottom_bar_height) // 20)
        
        # print(f'{self.map_grid = }')