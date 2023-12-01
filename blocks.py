import pygame
from random import choice, sample


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.x = x
        self.y = y
        self.width = 40
        self.height = 12
        self.visual_rect = pygame.Rect((x, y, self.width, self.height))
        self.rect_l = pygame.Rect((x, y, 1, self.height))
        self.rect_r = pygame.Rect((x - 1 + self.width, y, 1, self.height))
        self.rect_t = pygame.Rect((x, y, self.width, 1))
        self.rect_b = pygame.Rect((x, y - 1 + self.height, self.width, 1))
        self.color = choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.visual_rect)

    def update(self):
        flag = False
        balls = [self.game.ball, self.game.second_ball] if self.game.second_ball else [self.game.ball]
        for ball in balls:
            if ball.rect.colliderect(self.rect_l) or ball.rect.colliderect(self.rect_r):
                ball.x_move = -ball.x_move
                flag = True
            elif ball.rect.colliderect(self.rect_t) or ball.rect.colliderect(self.rect_b):
                ball.y_move = -ball.y_move
                flag = True
        if flag:
            self.game.stats.update_score()
            self.kill()
            if self.game.ball.booster == 1:
                self.lightning()

    def lightning(self):
        ln = len(self.game.blocks)
        num = ln if ln < 5 else 5
        indexes = sample(range(ln), num)
        for i, obj in enumerate(self.game.blocks):
            if i in indexes:
                obj.kill()
                self.game.stats.update_score()
        self.game.ball.booster = 0
        if self.game.second_ball:
            self.game.second_ball.booster = 0

