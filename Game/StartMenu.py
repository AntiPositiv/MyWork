import os

def LoadSave():
    if not (os.path.exists("SaveGame\Game_1")):
        SaveFile = open("SaveGame\Game_1", "w")
        SaveFile.write("gold: 0")
        Gold = 0
        SaveFile.close()
    else:
        SaveFile = open("SaveGame\Game_1", "r")
        SaveTxt = SaveFile.read()
        Gold = int(SaveTxt[6:])
        SaveFile.close()
    return Gold

def SaveRes(Gold):
    SaveFile = open("SaveGame\Game_1", "w")
    SaveFile.write("gold: "+str(Gold))
    SaveFile.close()