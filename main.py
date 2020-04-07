import random
import time
import pygame
from colors import colors
from  nodeClasses.spareNode import spareNode
from  nodeClasses.startNode import startNode
from  nodeClasses.wallNode  import wallNode
from  nodeClasses.goalNode  import goalNode


WIN_LEN=500
WIN_HEIGHT=500
FPS=10

ROWS=20
COLS=20
SIDE_LENGTH=(WIN_LEN/ROWS)*0.9
SPACING_LENGTH=(WIN_LEN/ROWS)*0.1

# empty plane
arr = [[ spareNode(i,j) for j in range(COLS)] for i in range(ROWS)]


#generate walls
for i in range(0,10):
    arr[15-i][5+i]=wallNode(15-i,5+i)

#define start and finish pos
arr[5][5]=startNode(5,5)
arr[15][15]=goalNode(18,18)



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
                color=colors.matchColor(cell)
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