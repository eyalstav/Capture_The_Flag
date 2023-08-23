import pygame
pygame.init()
from Screen import screen


def play_intro():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        bg_img = pygame.image.load("bin/startimg.png")
        screen.blit(bg_img,(0,0))
        pygame.display.flip()




if __name__ == '__main__':
    play_intro()