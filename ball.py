import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.x = 200
        self.y = 364
        self.r = 6
        self.speed = 2
        self.x_move = None
        self.y_move = -self.speed
        self.rect = pygame.Rect((self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))
        self.game = game
        self.colors = {0: (200, 200, 200), 1: (27, 245, 230)}
        self.booster = 0
        self.color = (200, 200, 200)
        self.plat_kd = 0
        self.killed = False

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color, (self.x, self.y), self.r)

    def update(self):
        if self.x_move is None:
            return
        self.plat_kd = self.plat_kd - 1 if self.plat_kd else 0
        self.x += self.x_move
        self.y += self.y_move
        self.rect.left += self.x_move
        self.rect.top += self.y_move
        self.color = self.colors[self.booster]
        self.check_move()

    def check_start(self, move):
        if self.x_move is None:
            self.x_move = move * self.speed

    def check_move(self):
        if self.x <= self.speed or self.x >= 400 - self.speed:
            self.x_move = -self.x_move
        if self.y <= 40 + self.speed:
            self.y_move = -self.y_move
        if self.y - self.r >= 400 and not self.killed:
            if self.game.two_balls:
                self.game.two_balls = False
                if self.game.ball is self:
                    self.game.ball = self.game.second_ball
                    self.game.second_ball = None
            else:
                self.game.stats.minus_hp()
            self.killed = True
        # if self.y + self.r >= 400:
        #     self.y_move = -self.y_move
        # if self.rect.colliderect(self.game.platform.rect_t) or self.rect.colliderect(self.game.platform.rect_b):
        #     self.y_move = -self.y_move
        # elif self.rect.colliderect(self.game.platform.rect_l) or self.rect.colliderect(self.game.platform.rect_r):
        #     self.x_move = -self.x_move
        if self.rect.colliderect(self.game.platform.visual_rect) and not self.plat_kd:
            self.y_move = -self.y_move
            self.plat_kd = 30


class Second_Ball(Ball):
    def __init__(self, game):
        super().__init__(game)
        self.x = game.ball.x
        self.y = game.ball.y
        self.x_move = -game.ball.x_move
        self.y_move = game.ball.y_move
        self.rect = pygame.Rect((self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))