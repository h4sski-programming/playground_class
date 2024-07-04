import math

class Character:
    def __init__(self, name: str, hp: int, position: list[float] = [0, 0]) -> None:
        self.name = name
        self.hp = hp
        self.alive = True
        self.can_take_dmg = True
        self.position = position
    
    def take_dmg(self, dmg: float) -> None:
        if self.can_take_dmg:
            self.hp -= dmg
            self.alive = self.hp > 0
    
    def move(self, vector: list[int]) -> None:
        self.position = [self.position[i] + vector[i] for i in [0, 1]]
        
    def distance_to(self, target: list[int]) -> float:
        # c2 = a2 + b2
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        return math.sqrt( dx*dx + dy*dy )