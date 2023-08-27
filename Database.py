import pandas as pd
import pygame.transform

import Game_Field
import Guard
import Soldier
import Consts
from os.path import exists
import ast
import Teleport
def ensure_db_existence():
    '''
    this method creates db in case it doesn't exist
    '''
    if not exists(Consts.DB_PATH):
        db = pd.DataFrame(Consts.BLANK_GAME_STATES)
        db.to_csv(Consts.DB_PATH, encoding='utf-8')


def save(num, feild, location, guard, teleports):
    '''
    this method saves the game's state
    :param num: the id number of the game state 0-9 wanted to be saved
    :return:
    '''
    ensure_db_existence()
    database = pd.read_csv(Consts.DB_PATH)
    database.at[num, 'board'] = feild
    database.at[num, 'player_loc'] = location
    database.at[num, 'teleports'] = [[[tp.x1, tp.y1], [tp.x2, tp.y2]] for tp in teleports]
    database.at[num, 'guard_dir_loc'] = [guard.d, guard.row, guard.col]
    database.to_csv(Consts.DB_PATH, encoding='utf-8')


def is_saved(num):
    '''
    checks if game state in game state id is empty
    :param num: game state id number
    :return: bool
    '''
    ensure_db_existence()
    database = pd.read_csv(Consts.DB_PATH)
    return len(ast.literal_eval(database.at[num, 'player_loc'])) > 0

def load(num):
    '''
    this method loads the game's state by id num to the screen
    :param num: the id number of the state 0-9
    '''
    if is_saved(num):
        database = pd.read_csv(Consts.DB_PATH)
        Game_Field.field = ast.literal_eval(database.at[num, 'board'])
        Soldier.soldier.x = ast.literal_eval(database.at[num, 'player_loc'])[Consts.X_INDEX]
        Soldier.soldier.y = ast.literal_eval(database.at[num, 'player_loc'])[Consts.Y_INDEX]
        Soldier.soldier.y = ast.literal_eval(database.at[num, 'player_loc'])[Consts.Y_INDEX]
        print(ast.literal_eval(database.at[num, 'guard_dir_loc']))
        old_direction_guard = Guard.guard.d
        Guard.guard.d, Guard.guard.row, Guard.guard.col = ast.literal_eval(database.at[num, 'guard_dir_loc'])
        if Guard.guard.d != old_direction_guard:
            Guard.guard.img = pygame.transform.flip(Guard.guard.img, 1, 0 )
        teleports_locations = ast.literal_eval(database.at[num, 'teleports'])
        #create all teleports in their locations:
        Teleport.tps = [Teleport.TP(locs[0], locs[1]) for locs in teleports_locations]