import pygame.sprite
from platform import Platform
from ball import Ball
from blocks import Block
from stats import Stats
from boosters import *
from random import randint, choice


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Arkanoid")
        self.clock = pygame.time.Clock()
        self.create_all()

    def reborn(self):
        self.platform = Platform(self)
        self.ball = Ball(self)
        self.second_ball = None
        self.boosters = pygame.sprite.Group()
        self.two_balls = False

    def create_all(self):
        self.reborn()
        self.blocks = pygame.sprite.Group()
        self.stats = Stats(self)
        self.lose = False
        self.victory = False
        self.create_blocks()

    def maincicle(self):
        while True:
            self.check_events()
            if not (self.lose or self.victory):
                self.platform.update()
                self.boosters.update()
                self.ball.update()
                if self.second_ball:
                    self.second_ball.update()
                self.blocks.update()
                self.create_boosters()
                self.check_victory()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ball.check_start(-1)
                    self.platform.movement_l = True
                if event.key == pygame.K_RIGHT:
                    self.ball.check_start(1)
                    self.platform.movement_r = True
                if self.lose or self.victory:
                    self.create_all()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.platform.movement_l = False
                if event.key == pygame.K_RIGHT:
                    self.platform.movement_r = False

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.platform.draw()
        self.ball.draw()
        if self.second_ball:
            self.second_ball.draw()
        self.draw_blocks()
        self.draw_boosters()
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 400, 40))
        self.stats.print_score()
        self.stats.print_hp()
        if self.lose:
            self.create_lose_written()
        elif self.victory:
            self.create_win_written()
        pygame.display.flip()

    def create_blocks(self):
        for y in range(70, 203, 22):
            for x in range(4, 357, 44):
                block = Block(self, x, y)
                block.add(self.blocks)
        # for y in range(70, 71, 22):
        #     for x in range(4, 5, 44):
        #         block = Block(self, x, y)
        #         block.add(self.blocks)

    def draw_blocks(self):
        for block in self.blocks:
            block.draw()

    def create_lose_written(self):
        font = pygame.font.SysFont("times new roman", 40)
        font.bold = True
        txt = font.render("You lose!", True, (255, 255, 255))
        rect = txt.get_rect()
        rect.midbottom = self.screen.get_rect().center
        self.screen.blit(txt, rect)

    def create_win_written(self):
        font = pygame.font.SysFont("times new roman", 40)
        font.bold = True
        txt = font.render("You win!", True, (255, 255, 255))
        rect = txt.get_rect()
        rect.midbottom = self.screen.get_rect().center
        self.screen.blit(txt, rect)

    def check_victory(self):
        if not self.blocks:
            self.victory = True

    def create_boosters(self):
        if self.ball.x_move is None:
            return
        if self.stats.score >= 80:
            num = randint(1, 1201)
            if num == 1:
                boosters = (B_Extra_Life, B_Lightning) if self.second_ball else\
                    (B_Extra_Life, B_Lightning, B_Double_Ball)
                booster = choice(boosters)(self)
                booster.add(self.boosters)

    def draw_boosters(self):
        for booster in self.boosters:
            booster.draw()


game = Game()
game.maincicle()
