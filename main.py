import pygame

import Soldier

pygame.init()
import Screen
import Game_Field

run = True

def handle_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                Soldier.soldier.move("left")
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Soldier.soldier.move('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                Soldier.soldier.move('up')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                Soldier.soldier.move('down')

def main():
    clock = pygame.time.Clock()
    field = Game_Field.field
    while run:
        handle_events()

        Screen.draw(field)
        clock.tick(60)
    pygame.quit()
    quit()



if __name__ == '__main__':
    main()

