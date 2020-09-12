import os

def LoadSave():
    if not (os.path.exists("SaveGame\Game_1")):
        SaveFile = open("SaveGame\Game_1", "w")
        SaveFile.write("gold: 0\nattack: 1\nlvl: 1\n")
        Gold = 0
        Attack = 1
        lvl = 1
        SaveFile.close()
    else:
        SaveFile = open("SaveGame\Game_1", "r")
        SaveTxt = SaveFile.readlines()
        Gold = int(SaveTxt[0][6:len(SaveTxt[0])-1])
        Attack = int(SaveTxt[1][8:len(SaveTxt[1])-1])
        lvl = int(SaveTxt[2][5:len(SaveTxt[1]) - 1])
        SaveFile.close()
    return Gold,Attack,lvl

def SaveRes(Gold,Attack,Lvl):
    SaveFile = open("SaveGame\Game_1", "w")
    SaveFile.write("gold: "+str(Gold)+"\nattack: "+str(Attack)+"\nLvl: "+str(Lvl))
    SaveFile.close()