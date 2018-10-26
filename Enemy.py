import  pygame

import settings


class Enemy(pygame.sprite.Sprite):

    def __init__(self, width, height, x):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(settings.RED)

        self.rect = self.image.get_rect()
        self.rect.x = x


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
