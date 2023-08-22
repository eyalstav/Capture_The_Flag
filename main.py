import pygame
pygame.init()
import Soldier
import Screen
import Game_Field

run = True

def handle_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                Soldier.soldier.direction = "left"
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Soldier.soldier.direction = 'right'
            if event.key == pygame.K_UP or event.key == ord('w'):
                Soldier.soldier.direction = 'up'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                Soldier.soldier.direction = 'down'
            if event.key == pygame.K_RETURN:
                Screen.draw_mines()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                Soldier.soldier.direction = None
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Soldier.soldier.direction = None
            if event.key == pygame.K_UP or event.key == ord('w'):
                Soldier.soldier.direction = None
            if event.key == pygame.K_DOWN or event.key == ord('s'):
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
        if flag.is_stepped_on(Soldier.soldier):
            Screen.draw_win_msg()
            break
        if not Soldier.soldier.alive:
            Screen.draw_lose_msg()
            break

        Screen.draw(field)
        clock.tick(15)
    pygame.quit()
    quit()



if __name__ == '__main__':
    main()

