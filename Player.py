from Environment import *


class Player(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.surface = pygame.Surface(size)
        self.surface.fill(RED)
        self.rect = self.surface.get_rect()
        self.rect.center = position

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT] | pressed_keys[K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP] | pressed_keys[K_w]:
                self.rect.move_ip(0, -5)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT] | pressed_keys[K_d]:
                self.rect.move_ip(5, 0)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[K_DOWN] | pressed_keys[K_s]:
                self.rect.move_ip(0, 5)

    def changePos(self, position):
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
