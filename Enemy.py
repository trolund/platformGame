import pygame

import settings

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x):

        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(settings.BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = x

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        self.HP = 100

    def update(self):
        # Gravity
        self.calc_grav()

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= settings.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = settings.SCREEN_HEIGHT - self.rect.height

        self.rect.y += self.change_y