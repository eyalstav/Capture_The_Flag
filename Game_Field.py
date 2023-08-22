import random
from Consts import *


def generate_mines():
    mine_locations = []
    for i in range(MINE_AMOUNT):
        while True:
            x = random.randint(0, int(GRID_COLS / 3)) * 3 - 1
            y =  random.randint(0, GRID_ROWS - 1)
            if x>=4 and y>=6:
                break
        mine_locations.append([y,x])
    return mine_locations
def create_field():
    output = []

    for row in range(GRID_ROWS):
        r = []
        for col in range(GRID_COLS):
            r.append({"type": random.choice(["normal","grass"]),"mine":False,"soldier":False, "draw_mine":False})
        output.append(r)

    for mine in mines:
        output[mine[0]][mine[1]]["draw_mine"] = True
        for i in range(3):
            output[mine[0]][mine[1]+i]["mine"] = True


    return output

mines = generate_mines()
field = create_field()




