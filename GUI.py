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




class GUI():
    

    def __init__(self,arr):
        self.arr=arr

        self.screen = pygame.display.set_mode((WIN_LEN, WIN_HEIGHT))
    
    def update(self):
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            # quits the program if clicked to close the window
            exit()
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # quits the program on pressing ESC
            exit()

        self.draw_matrix()
        pygame.display.flip()

    def draw_matrix(self):
        # fills the screen with black
        self.screen.fill(colors.black)

        # walks through the plane drawing its cells
        for r, row in enumerate(self.arr):
            for c, cell in enumerate(row):
                if cell!=0:
                    color=colors.matchColor(cell)
                    pygame.draw.rect(
                        self.screen, color, ((SIDE_LENGTH+SPACING_LENGTH)*c, (SIDE_LENGTH+SPACING_LENGTH)*r, SIDE_LENGTH, SIDE_LENGTH)
                    )
    def drawPath(self,path):
        for i in path:
            #print('drawing path at:'i.x,i.y)
            color=(0,0,255)
            pygame.draw.rect(
                        self.screen, color, ((SIDE_LENGTH+SPACING_LENGTH)*i.y, (SIDE_LENGTH+SPACING_LENGTH)*i.x, SIDE_LENGTH, SIDE_LENGTH)
                    )
        pygame.display.flip()