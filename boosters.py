import pygame
from random import randint
from ball import Second_Ball


class Booster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/images/unknown_booster.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = randint(5, 374)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.top += 1
        if self.rect.colliderect(self.game.platform.visual_rect):
            self.kill()
            self.boost()
        if self.rect.top > 400:
            self.kill()

    def boost(self):
        pass


class B_Extra_Life(Booster):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load("assets/images/EL_booster.png")

    def boost(self):
        self.game.stats.hp += 1


class B_Lightning(Booster):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load("assets/images/Light_booster.png")

    def boost(self):
        self.game.ball.booster = 1
        if self.game.second_ball:
            self.game.second_ball.booster = 1


class B_Double_Ball(Booster):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load("assets/images/Double_booster.png")

    def boost(self):
        self.game.two_balls = True
        self.game.second_ball = Second_Ball(self.game)
