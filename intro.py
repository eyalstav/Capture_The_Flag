import pygame
pygame.init()
from Screen import screen
import moviepy
from moviepy.editor import VideoFileClip

def play_intro():
    intro_clip = VideoFileClip("bin/intro1.mp4")
    intro_clip.preview()
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