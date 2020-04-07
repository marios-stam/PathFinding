import random
import time
import pygame
from colors import  colors

WIN_LEN=500
WIN_HEIGHT=500
FPS=10

ROWS=50
COLS=50
SIDE_LENGTH=(WIN_LEN/ROWS)*0.9
SPACING_LENGTH=(WIN_LEN/ROWS)*0.1

# empty plane
arr = [[0 for _ in range(ROWS)] for _ in range(COLS)]

#generate walls
for i in range(0,20):
    arr[34-i][14+i]=3

#define start and finish pos
arr[5][5]=1
arr[40][40]=2

screen = pygame.display.set_mode((WIN_LEN, WIN_HEIGHT))


def draw_matrix(matrix):
    '''
    Function to draw the plane given the matrix
    '''

    # fills the screen with black
    screen.fill(colors.black)

    # walks through the plane drawing its cells
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell!=0:
                color=colors.matchColor[cell]
                
                pygame.draw.rect(
                    screen, color, ((SIDE_LENGTH+SPACING_LENGTH)*c, (SIDE_LENGTH+SPACING_LENGTH)*r, SIDE_LENGTH, SIDE_LENGTH)
                )




# draws the initial state of the seed
draw_matrix(arr)

pygame.display.flip()

# waits one second so we can see the initial state before
# starting the interaction loop
time.sleep(1)

while True:
    # INPUT PROCESSING
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        # quits the program if clicked to close the window
        break
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        # quits the program on pressing ESC
        break

    # GAME UPDATE



    # DRAWING

    # draws the new generation at the screen
    draw_matrix(arr)

    pygame.display.flip()

    # waits a brief moment until going to the next generation
    time.sleep(1/FPS)