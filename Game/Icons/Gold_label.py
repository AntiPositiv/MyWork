import pygame
#
def gold(Gold, txt_gold,screen,color):
    lab_gold = txt_gold.render("Gold:" + str(Gold), 1, color)
    screen.blit(lab_gold, (10, 50))
    pygame.display.update()