from character import Character



class Ship(Character):
    def __init__(self, name: str, hp: int, position: list[int], 
                 country: str, speed_max: float, momentum: float, course: float, 
                 canons_max: int, canons: int, canons_range :float, reload_time: float) -> None:
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
        
        super().__init__(name, hp, position)


class Galeon_ship(Ship):
    def __init__(self, name: str, hp: int, position: list[int], country: str, course: float, canons: int) -> None:
        super().__init__(name, hp, position, country=country, speed_max=4, momentum=12, course=course, 
                         canons_max=240, canons=canons, canons_range=400, reload_time=2.4)


class Frigate_ship(Ship):
    def __init__(self, name: str, hp: int, position: list[int], country: str, course: float, canons: int) -> None:
        super().__init__(name, hp, position, country=country, speed_max=6, momentum=10, course=course, 
                         canons_max=160, canons=canons, canons_range=330, reload_time=1.7)


class Slup_ship(Ship):
    def __init__(self, name: str, hp: int, position: list[int], country: str, course: float, canons: int) -> None:
        super().__init__(name, hp, position, country=country, speed_max=18, momentum=3, course=course, 
                         canons_max=20, canons=canons, canons_range=180, reload_time=0.4)