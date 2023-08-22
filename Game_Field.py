import random
from Consts import *

def create_field():
    output = []
    for row in range(GRID_ROWS):
        r = []
        for col in range(GRID_COLS):
            r.append({"type": random.choice(["normal","grass"]),"mine":bool(random.getrandbits(1)),"soldier":False})

        output.append(r)
    return output


field = create_field()




