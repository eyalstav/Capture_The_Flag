import pygame
pygame.init()
import moviepy
from moviepy.editor import VideoFileClip
import Consts

screen = pygame.display.set_mode(Consts.WIN_SIZE)
pygame.display.set_caption("Capture The Flag")

def play_intro():
    intro_clip = VideoFileClip("bin/intro1.mp4")
    pygame.display.set_caption("Capture The Flag")
    intro_clip.preview()

    hero_amount = 5

    def change_hero(change):
        Consts.current_hero += change
        if Consts.current_hero >= hero_amount: Consts.current_hero = 0
        elif Consts.current_hero < 0: Consts.current_hero = hero_amount-1

    def play_hero_animation():
        frame = Consts.intro_frame
        sheet = pygame.image.load(f"bin/{Consts.current_hero}/Idle.png")
        image = pygame.Surface((128, 128)).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * 128), 128 / 4, 128, 128 * 3 / 4))
        image = pygame.transform.scale(image, (200,200))
        image.set_colorkey((0,0,0))
        screen.blit(image, (width/2-image.get_width()/2, height/2))

        Consts.intro_frame += 1
        if (sheet.get_width() / 128)-1 <= frame:
            Consts.intro_frame = 0


    width = screen.get_width()
    height = screen.get_height()
    bg_img = pygame.image.load("bin/intro.png")

    smallfont = pygame.font.SysFont('Corbel', 60,True)
    right_text = smallfont.render('>', True, (0,0,0))
    right_x = width / 2 + 150
    right_y = height / 2 + 50
    left_text = smallfont.render('<', True, (0, 0, 0))
    left_x = width / 2 - 150 - left_text.get_width()
    left_y = height / 2 + 50

    play_text = smallfont.render('Play Game', True, (0,0,0))
    play_x = width/2 - play_text.get_width()/2
    play_y = height - height/8

    clock = pygame.time.Clock()
    run = True
    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the
                # button the game is terminated
                if right_x <= mouse[0] <= right_x + right_text.get_width() and right_y <= mouse[1] <= right_y + right_text.get_height():
                    change_hero(1)
                elif left_x <= mouse[0] <= left_x + left_text.get_width() and left_y <= mouse[1] <= left_y + left_text.get_height():
                    change_hero(-1)
                elif play_x <= mouse[0] <= play_x + play_text.get_width() and play_y <= mouse[1] <= play_y + play_text.get_height():
                    print("Play")
                    run = False

        screen.blit(bg_img, (0,0))

        screen.blit(right_text, (right_x, right_y))
        screen.blit(left_text, (left_x, left_y))
        screen.blit(play_text, (play_x, play_y))

        play_hero_animation()


        pygame.display.flip()
        clock.tick(10)

if __name__ == '__main__':
    play_intro()