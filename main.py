import random
import time

import pygame

from algorithm import algo
from colors import colors
from GUI import COLS, FPS, GUI, ROWS
from matrix import matrix
from nodeClasses.goalNode import goalNode
from nodeClasses.spareNode import spareNode
from nodeClasses.startNode import startNode
from nodeClasses.wallNode import wallNode

matr=matrix(ROWS,COLS)
gui=GUI(matr.arr)


gui.update()

path=algo(matr.arr,matr.start,matr.goal,gui)

# waits one second so we can see the initial state before
# starting the interaction
time.sleep(15)

"""
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
    gui.update()

    # waits a brief moment until going to the next generation
    time.sleep(1/FPS)

    #time.sleep(500)
"""