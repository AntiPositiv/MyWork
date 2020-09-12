import pygame
# import os
#################
from Game.GameObj import Mob_1
from Game import StartMenu
from Game.Icons import Gold_label

##################
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
Gold, Attack, lvl = StartMenu.LoadSave()
###########
# Счетчик золота
txt_gold = pygame.font.SysFont('vladimirscript', 32)
Gold_label.gold(Gold, txt_gold, screen_1, White)
###########
# Апгрейды
wind_button_up = pygame.Surface([100,50])
wind_button_up.fill((255,255,255))
pygame.draw.rect(wind_button_up,White,[650,50,100,50])
screen_1.blit(wind_button_up,(650,50))
def Attack_Up(gold,lvl):
    cost = int(10 * lvl)
    if cost > gold:
        print("Недостаточно денег")
        attack_up = 0
        cost = 0
    else:
        #придумать в дальнейшем формулу
        attack_up = 1
        lvl += 1
        print('Upgrade')
    return cost,attack_up,lvl
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
                elif 650 <= event.pos[0] <= 750 and 50 <= event.pos[1] <= 100:
                    #Тригер апгрейда
                    buf_cost,buf_attack_up,lvl = Attack_Up(Gold,lvl)
                    Gold -= buf_cost
                    Attack += buf_attack_up
                    Gold_label.gold(Gold, txt_gold, screen_1, White)
        if event.type == pygame.QUIT:
            # Сохранение игры
            StartMenu.SaveRes(Gold,Attack,lvl)
            exit()

    clock.tick(FPS)
