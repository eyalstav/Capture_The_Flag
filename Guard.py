from Consts import *
import random
class Guard:
    def __init__(self):
        self.h = 2
        self.w = 2
        self.row = random.randint(SOLDIER_WIDTH, GRID_ROWS - self.w*2)
        self.col = random.randint(0, GRID_COLS - self.h*2)
        self.img = pygame.transform.scale(pygame.image.load(GUARD_IMG),(self.w*CELL_SIZE[0]*4 ,self.h*CELL_SIZE[1]*2))
        self.d = 1
        self.sprite_sheet = pygame.image.load("bin/Slime/Run2.png")
        self.frame = 0
    def move(self):
        self.col += self.d
        if self.col >= GRID_COLS-1:
            self.col -= self.d
            self.d *= -1
            self.sprite_sheet = pygame.transform.flip(self.sprite_sheet,True,False)
        if self.col < 0:
            self.col -= self.d
            self.d *= -1
            self.sprite_sheet = pygame.transform.flip(self.sprite_sheet, True, False)


guard = Guard()