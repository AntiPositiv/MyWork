import pygame


def monster(x, y, screen, color):
    pygame.draw.rect(screen, color, (x, y, 76, 100))


class Poring_1:
    def __init__(self, Hp):
        self.Hp = Hp

    def __del__(self):
        print("Mob dead")
