import pandas as pd
database = pd.read_csv("bin/database.cvs")

def save(num):
    database[num] = {"player":{"x":8}}
    database.to_csv("bin/database.cvs")

def load(num):
    pass

save(3)










