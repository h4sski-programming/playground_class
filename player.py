import pygame


from character import Character

class Player(Character):
    def __init__(self, name: str, hp: int, ) -> None:
        super().__init__(name, hp)
        
    def draw(self, surface) -> None:
        
        rect = pygame.Rect(self.position, (20,20))
        pygame.draw.rect(surface=surface, rect=rect, color='red')
        text = pygame.font.SysFont('Comic Sans MS', 30).render('P', False, 'black')
        surface.blit(text, self.position)