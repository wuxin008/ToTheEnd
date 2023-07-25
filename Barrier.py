from pygame.math import Vector2

from Environment import *


class Barrier(pygame.sprite.Sprite):
    def __init__(self, start, end, speed):
        super().__init__()
        self.surface = pygame.Surface((50, 50))
        self.surface.fill(GREEN)
        self.rect = self.surface.get_rect()
        self.rect.center = start
        self.position = Vector2(start)
        self.start = Vector2(start)
        self.end = Vector2(end)
        self.speed = speed
        self.direction = Vector2(self.end - self.start).normalize()

    def update(self):
        if self.position.distance_to(self.start) <= 1:
            self.speed = abs(self.speed)
        if self.position.distance_to(self.end) <= 1:
            self.speed = -abs(self.speed)
        self.position = self.position + self.speed * self.direction
        self.rect.center = self.position

    def changePos(self, position):
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.surface, self.rect)