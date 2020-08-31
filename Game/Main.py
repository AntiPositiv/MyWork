import pygame
# import os
#################
from Game.GameObj import Mob_1
from Game import StartMenu
from Game.Icons import Gold_label

#################
# RGB цвета
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Gray = (125, 125, 125)
################
pygame.init()

w, h = 800, 600
screen_1 = pygame.display.set_mode([w, h])

FPS = 30
clock = pygame.time.Clock()
####################
# Флаги спавна монстра
MobOnScreen = False
SpawnTime = 17
DamageMob = False
####################
# Загрузка сохранения
Gold = StartMenu.LoadSave()
###########
# Счетчик золота
txt_gold = pygame.font.SysFont('vladimirscript', 32)
Gold_label.gold(Gold, txt_gold, screen_1, White)
###########

###########
while True:
    # Спавн монстра
    if not (MobOnScreen) and SpawnTime == 17:
        Mob_1.monster((w // 2) - 38, (h // 2) - 50, screen_1, Gray)
        Mob = Mob_1.Poring_1(5)
        print("Mob on screen", "hp =", Mob.Hp)
        pygame.display.update()
        MobOnScreen = True
        SpawnTime = 0
    elif not (MobOnScreen):
        SpawnTime += 1
    # Анимация атаки
    if not (DamageMob) and MobOnScreen:
        Mob_1.monster((w // 2) - 38, (h // 2) - 50, screen_1, Gray)
        pygame.display.update()
        DamageMob = True

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (w / 2) - 38 <= event.pos[0] <= (w // 2) + 38 and (h // 2) - 50 <= event.pos[1] <= (
                        h / 2) + 50 and MobOnScreen:
                    Mob_1.monster((w // 2) - 38, (h // 2) - 50, screen_1, Red)
                    pygame.display.update()
                    DamageMob = False
                    Mob.Hp -= 1
                    if Mob.Hp <= 0 and MobOnScreen:
                        MobOnScreen = False
                        Mob.__del__()
                        screen_1.fill(Black)
                        pygame.display.update()
                        #######################
                        Gold += 1
                        Gold_label.gold(Gold, txt_gold, screen_1, White)

        if event.type == pygame.QUIT:
            # Сохранение игры
            StartMenu.SaveRes(Gold)
            exit()

    clock.tick(FPS)
