import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(bullet1,position):
        pygame.sprite.Sprite.__init__(bullet1)

        bullet1.image = pygame.image.load("images/bullet1.png").convert_alpha()
        bullet1.rect = bullet1.image.get_rect()
        bullet1.rect.left,bullet1.rect.top = position
        bullet1.speed = 10
        bullet1.active = True
        bullet1.mask = pygame.mask.from_surface(bullet1.image)

    def move(bullet1):
        bullet1.rect.top -= bullet1.speed

        if bullet1.rect.top < 0:
            bullet1.active = False

    def reset(bullet1,position):
        bullet1.rect.left,bullet1.rect.top = position
        bullet1.active = True
