import time

import pygame
pygame.init()
import Soldier
import Screen
import Game_Field
import Guard
import Teleport
import Consts
run = True



def handle_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in Consts.KEYBOARD_DICT.keys():
                Soldier.soldier.direction = Consts.KEYBOARD_DICT[event.key]
            elif event.key == pygame.K_RETURN:
                Screen.draw_mines()
        if event.type == pygame.KEYUP and event.key in Consts.KEYBOARD_DICT.keys():
            Soldier.soldier.direction = None



def main():
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



if __name__ == '__main__':
    main()

