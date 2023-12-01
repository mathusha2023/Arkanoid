import pygame


# класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.x = 160
        self.y = 370
        self.width = 80
        self.height = 7
        self.visual_rect = pygame.Rect((self.x, self.y, self.width, self.height))
        self.game = game
        self.movement_l = False
        self.movement_r = False
        # self.rect_l = pygame.Rect((self.x, self.y, 1, self.height))
        # self.rect_r = pygame.Rect((self.x - 1 + self.width, self.y, 1, self.height))
        # self.rect_t = pygame.Rect((self.x, self.y, self.width, 1))
        # self.rect_b = pygame.Rect((self.x, self.y - 1 + self.height, self.width, 1))
        # self.rects = [self.visual_rect, self.rect_b, self.rect_r, self.rect_l, self.rect_t]

    def draw(self):
        pygame.draw.rect(self.game.screen, (200, 200, 200), self.visual_rect)

    def update(self):
        if self.x < 0 and self.movement_l or self.x > 320 and self.movement_r:
            return
        if self.movement_l:
            self.move_left()
        elif self.movement_r:
            self.move_right()

    def move_left(self):
        self.x -= 4
        # for rect in self.rects:
        #     rect.left -= 4
        self.visual_rect.left -= 4

    def move_right(self):
        self.x += 4
        # for rect in self.rects:
        #     rect.left += 4
        self.visual_rect.left += 4
