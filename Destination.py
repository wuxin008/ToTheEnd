from Environment import *

class Destination(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.surface = pygame.Surface(size=size)
        self.rect = self.surface.get_rect()
        self.rect.center = position
        self.surface.fill(YELLOW)

    def update(self):
        pass

    def changePos(self, position):
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
