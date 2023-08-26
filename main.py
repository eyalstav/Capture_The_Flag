import pygame
import time
pygame.init()

import Intro, Consts

if __name__ == "__main__":
    Intro.play_intro()
    Consts.SOLDIER_FOLDER = f"bin/{Consts.current_hero}/"

import Soldier, Game_Field, Guard, Teleport
import Screen
import Consts
#import Database
pressed = time.time()

def handle_events():
    global run, pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in Consts.KEYBOARD_DICT.keys():
                Soldier.soldier.direction = Consts.KEYBOARD_DICT[event.key]
            elif event.key == pygame.K_RETURN:
                Screen.draw_mines()
            if event.key in range(ord('0'), ord('9') + 1):
                pressed = time.time()
        if event.type == pygame.KEYUP:
            if event.key in Consts.KEYBOARD_DICT.keys():
                Soldier.soldier.direction = None
            if event.key in range(ord('0'), ord('9') + 1):
                game_state = int(chr(event.key))
                if time.time()-pressed < 1:
                    #Database.load(game_state)
                    pass
                else:
                    pass
                    #Database.save(game_state, Game_Field.field, [Soldier.soldier.x, Soldier.soldier.y])

def main():
    print(Consts.SOLDIER_FOLDER, Consts.current_hero)
    run = True
    clock = pygame.time.Clock()
    field = Game_Field.field
    Screen.draw(field)
    Screen.draw_start_msg()
    flag = Game_Field.flag
    while run:
        handle_events()
        Soldier.soldier.move()
        Soldier.soldier.check_dead()
        Guard.guard.move()
        for tp in Teleport.tps:
            tp.check_tp()
        if flag.is_stepped_on(Soldier.soldier):
            Screen.draw_win_msg()
            break
        if not Soldier.soldier.alive:
            Screen.draw_lose_msg()
            break


        Screen.draw(field)
        clock.tick(Consts.TICK_LENGTH)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()

