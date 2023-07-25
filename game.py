import Environment
from Environment import *
from Button import Button


class Start(object):
    def __init__(self, screen):
        self.screen = screen
        self.game_title = Font_48.render('To The End', True, RED)
        self.gt_rect = self.game_title.get_rect()
        self.gt_rect.center = (WIDTH / 2, HEIGHT / 100 * 20)
        self.play_button = Button('开始', RED, None, 350, centered_x=True)
        self.exit_button = Button('退出', BLACK, None, 400, centered_x=True)

        screen.blit(self.game_title, self.gt_rect)
        self.play_button.display(screen)
        self.exit_button.display(screen)
        pygame.display.update()

    def showStart(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.game_title, self.gt_rect)
        if self.play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('开始', RED, None, 350, centered_x=True)
        else:
            play_button = Button('开始', BLACK, None, 350, centered_x=True)
        if self.exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('退出', RED, None, 400, centered_x=True)
        else:
            exit_button = Button('退出', BLACK, None, 400, centered_x=True)
        play_button.display(self.screen)
        exit_button.display(self.screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                return Environment.PLAY
            if exit_button.check_click(pygame.mouse.get_pos()):
                return Environment.QUIT
        return 0


class Play(object):
    def __init__(self, screen, player, barriers, destination):
        self.screen = screen
        self.p = player
        self.e = barriers
        self.d = destination
        self.pGroup = pygame.sprite.Group()
        self.barriers_group = pygame.sprite.Group()
        self.all_group = pygame.sprite.Group()
        self.all_group.add(self.d)
        self.all_group.add(self.p)
        self.text = Font_48.render('游戏结束!', True, RED)
        for i in barriers:
            self.barriers_group.add(i)
            self.all_group.add(i)

    def setStage(self, p_state, b_state, d_state):
        self.p.changePos(p_state)
        for i in range(len(b_state)):
            self.e[i].changePos(b_state[i])
        self.d.changePos(d_state)
    def action(self):
        self.screen.fill(WHITE)
        for entity in self.all_group:
            self.screen.blit(entity.surface, entity.rect)
            entity.update()

        if pygame.sprite.spritecollideany(self.p, self.barriers_group):
            # print('碰撞检测！')
            # self.screen.fill(WHITE)
            # textcenter = self.text.get_rect()
            # textcenter.center = (HEIGHT / 2, WIDTH / 2)
            # self.screen.blit(self.text, textcenter)
            # for entity in self.all_group:
            #     entity.kill()
            # pygame.display.update()
            # time.sleep(2)
            return Environment.FAIL

        # print("self.p.rect", self.p.rect.top, self.p.rect.left, self.p.rect.bottom, self.p.rect.right)
        # print('self.d.rect', self.d.rect.top, self.d.rect.left, self.d.rect.bottom, self.d.rect.right)
        if self.p.rect.top >= self.d.rect.top and self.p.rect.bottom <= self.d.rect.bottom and self.p.rect.left >= self.d.rect.left and self.p.rect.right <= self.d.rect.right:
            return Environment.SUCCESS

        pygame.display.update()
        return 1


class Fail(object):
    def __init__(self, screen):
        self.screen = screen
        self.restart = Button('按space重新开始', BLACK, None, HEIGHT / 100 * 60, centered_x = WIDTH / 2)
        self.quit = Button('按esc退出游戏', BLACK, None, HEIGHT / 100 * 70, centered_x = WIDTH / 2)

    def showFail(self):
        self.screen.fill(WHITE)
        text1 = Font_48.render('你输了！', True, RED)
        text_rect1 = text1.get_rect()
        text_rect1.center = (WIDTH / 2, HEIGHT / 100 * 20)
        self.screen.blit(text1, text_rect1)
        self.restart.display(self.screen)
        self.quit.display(self.screen)
        if pygame.mouse.get_pressed()[0]:
            if self.restart.check_click(pygame.mouse.get_pos()):
                return Environment.START
            if self.quit.check_click(pygame.mouse.get_pos()):
                return Environment.QUIT
        pygame.display.update()
        if self.restart.check_click(pygame.mouse.get_pos()):
            play_button = Button('按space重新开始', RED, None, HEIGHT / 100 * 60, centered_x = WIDTH / 2)
        else:
            play_button = Button('按space重新开始', BLACK, None, HEIGHT / 100 * 60, centered_x = WIDTH / 2)
        if self.quit.check_click(pygame.mouse.get_pos()):
            exit_button = Button('按esc退出游戏', RED, None, HEIGHT / 100 * 70, centered_x = WIDTH / 2)
        else:
            exit_button = Button('按esc退出游戏', BLACK, None, HEIGHT / 100 * 70, centered_x = WIDTH / 2)
        play_button.display(self.screen)
        exit_button.display(self.screen)
        pygame.display.update()

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_SPACE]:
            return Environment.START
        if pressed_key[K_ESCAPE]:
            return Environment.QUIT
        return Environment.FAIL

class Success(object):
    def __init__(self, screen):
        self.screen = screen
        self.restart = Button('按space重新开始', BLACK, None, HEIGHT / 100 * 60, centered_x = WIDTH / 2)
        self.quit = Button('按esc退出游戏', BLACK, None, HEIGHT / 100 * 70, centered_x = WIDTH / 2)

    def showSuccess(self):
        self.screen.fill(WHITE)
        text1 = Font_48.render('你赢了！', True, RED)
        text_rect1 = text1.get_rect()
        text_rect1.center = (WIDTH / 2, HEIGHT / 100 * 20)
        self.screen.blit(text1, text_rect1)
        self.restart.display(self.screen)
        self.quit.display(self.screen)
        if pygame.mouse.get_pressed()[0]:
            if self.restart.check_click(pygame.mouse.get_pos()):
                return Environment.START
            if self.quit.check_click(pygame.mouse.get_pos()):
                return Environment.QUIT
        pygame.display.update()
        if self.restart.check_click(pygame.mouse.get_pos()):
            play_button = Button('按space重新开始', RED, None, HEIGHT / 100 * 60, centered_x=WIDTH / 2)
        else:
            play_button = Button('按space重新开始', BLACK, None, HEIGHT / 100 * 60, centered_x=WIDTH / 2)
        if self.quit.check_click(pygame.mouse.get_pos()):
            exit_button = Button('按esc退出游戏', RED, None, HEIGHT / 100 * 70, centered_x=WIDTH / 2)
        else:
            exit_button = Button('按esc退出游戏', BLACK, None, HEIGHT / 100 * 70, centered_x=WIDTH / 2)
        play_button.display(self.screen)
        exit_button.display(self.screen)
        pygame.display.update()

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_SPACE]:
            return Environment.START
        if pressed_key[K_ESCAPE]:
            return Environment.QUIT
        return Environment.SUCCESS
