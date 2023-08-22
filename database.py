import Soldier,Game_Field

import pandas as pd
database = pd.read_csv("bin/database.csv")

def save(num):
    #should save
    #player X Y
    #mines, grass
    database["x"][num] = Soldier.soldier.x
    database["y"][num] = Soldier.soldier.x
    database["field"][num] = Game_Field.field
    database.to_csv("bin/database.csv")

def load(num):
    pass
print(database)
f = database["field"][4].astype()
print()









