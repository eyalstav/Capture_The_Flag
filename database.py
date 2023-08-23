import pandas as pd
import Game_Field
import Soldier
import Consts
from os.path import exists
import ast
def ensure_db_existence():
    '''
    this method creates db in case it doesn't exist
    '''
    if not exists(Consts.DB_PATH):
        db = pd.DataFrame(Consts.BLANK_GAME_STATES)
        db.to_csv(Consts.DB_PATH, encoding='utf-8')


def save(num, feild, location):
    '''
    this method saves the game's state
    :param num: the id number of the game state 0-9 wanted to be saved
    :return:
    '''
    database = pd.read_csv(Consts.DB_PATH)
    database.at[num, 'board'] = feild
    database.at[num, 'player_loc'] = location
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
    database = pd.read_csv(Consts.DB_PATH)
    Game_Field.field = ast.literal_eval(database.at[num, 'board'])
    Soldier.soldier.x = ast.literal_eval(database.at[num, 'player_loc'])[Consts.X_INDEX]
    Soldier.soldier.y = ast.literal_eval(database.at[num, 'player_loc'])[Consts.Y_INDEX]
    #make game state in the num state id empty
    save(num, [[]], [])








