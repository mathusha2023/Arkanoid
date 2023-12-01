import pygame


class Stats:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.hp = 3

    def print_score(self):
        font = pygame.font.SysFont("times new roman", 20)
        # font.bold = True
        txt = font.render(f"Score: {self.score}", True, (255, 255, 255))
        rect = txt.get_rect()
        rect.topleft = self.game.screen.get_rect().topleft
        self.game.screen.blit(txt, rect)

    def update_score(self):
        self.score += 10

    def minus_hp(self):
        self.hp -= 1
        if not self.hp:
            self.game.lose = True
        else:
            self.game.reborn()

    def print_hp(self):
        for i in range(self.hp):
            pygame.draw.circle(self.game.screen, (255, 255, 255), (388 - i * 18, 12), self.game.ball.r)
