from game import *
import Environment
from Environment import *
from Player import Player
from Barrier import Barrier
from Destination import Destination

DISPLAYSURF = pygame.display.set_mode((HEIGHT, WIDTH), pygame.RESIZABLE)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("ToTheEnd")

FPS = 60
FramePerSec = pygame.time.Clock()

Font = pygame.font.SysFont('方正粗黑宋简体', 24, False, False)

p1 = Player(size=(60, 60), position=(30, 30))
b1 = Barrier((125, 25), (125, 175), 1)
b2 = Barrier((225, 175), (225, 25), 1)
b3 = Barrier((325, 25), (325, 175), 1)
b4 = Barrier((425, 175), (425, 25), 1)
b5 = Barrier((525, 25), (525, 175), 1)
b6 = Barrier((25, 425), (25, 575), 1)
b7 = Barrier((125, 575), (125, 425), 1)
b8 = Barrier((225, 425), (225, 575), 1)
b9 = Barrier((325, 575), (325, 425), 1)
b10 = Barrier((425, 425), (425, 575), 1)
b11 = Barrier((25, 300), (275, 300), 1)
b12 = Barrier((325, 300), (575, 300), 1)
d1 = Destination((100, 100), (WIDTH - 50, HEIGHT - 50))
start = Start(DISPLAYSURF)
play = Play(DISPLAYSURF, p1, [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12], d1)
fail = Fail(DISPLAYSURF)
success = Success(DISPLAYSURF)

Done = False
state = 0
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            Done = True
            break
    match state:
        case Environment.START:
            state = start.showStart()
        case Environment.PLAY:
            state = play.action()
        case Environment.FAIL:
            play.setStage(p_state=(25, 25), b_state=[(100, 100), (200, 5), (300, 200)], d_state=(WIDTH - 25, HEIGHT - 25))
            state = fail.showFail()
        case Environment.SUCCESS:
            play.setStage(p_state=(25, 25), b_state=[(100, 100), (200, 5), (300, 200)],
                          d_state=(WIDTH - 25, HEIGHT - 25))
            state = success.showSuccess()
        case Environment.QUIT:
            Done = True
            break
    FramePerSec.tick(FPS)
pygame.quit()

# Done = False
# while not Done:
#     for event in pygame.event.get():
#         if (event.type == QUIT):
#             Done = True
#             break
#
#     DISPLAYSURF.fill(WHITE)
#     for entity in all_sprites:
#         DISPLAYSURF.blit(entity.surface, entity.rect)
#         entity.update()
#
#     if pygame.sprite.spritecollideany(p1, enemies):
#         DISPLAYSURF.fill(WHITE)
#         textcenter = text1.get_rect()
#         textcenter.center = (HEIGHT / 2, WIDTH / 2)
#         DISPLAYSURF.blit(text1, textcenter)
#         for entity in all_sprites:
#             entity.kill()
#         pygame.display.update()
#         time.sleep(2)
#         Done = True
#
#     pygame.display.update()
#     FramePerSec.tick(FPS)
# pygame.quit()
