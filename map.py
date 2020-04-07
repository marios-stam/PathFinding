from colors import colors
from  nodeClasses.spareNode import spareNode
from  nodeClasses.startNode import startNode
from  nodeClasses.wallNode  import wallNode
from  nodeClasses.goalNode  import goalNode


class map():
    def __init__(self,rows,cols,screen):
        self.ROWS=rows
        self.COLS=cols
        self.screen=screen
        self.generateMap()

    def run(self):
        self.setStart(5,5)
        self.setGoal(18,18)
        self.manualWallsPlacement()

    def generateMap(self):
        self.arr=[[ spareNode(i,j) for j in range(self.COLS)] for i in range(self.ROWS)]

    def setStart(self,x,y):
        self.arr[x][y]=startNode(x,y)

    def setGoal(self,x,y):
         self.arr[x][y]=goalNode(x,y)
    
    def setWalls(self,x,y):
        self.arr[x][y]=wallNode(x,y)

    def manualWallsPlacement(self):
        for i in range(0,10):
            self.setWalls(15-i,5+i)
    


    