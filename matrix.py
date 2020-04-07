from colors import colors
from  nodeClasses.spareNode import spareNode
from  nodeClasses.startNode import startNode
from  nodeClasses.wallNode  import wallNode
from  nodeClasses.goalNode  import goalNode


class matrix():
    def __init__(self,rows,cols):
        self.ROWS=rows
        self.COLS=cols
        
        self.generateMap()
        self.setStart(5,5)
        self.setGoal(18,18)
        self.manualWallsPlacement()
        self.fillSpareNodes()

    def generateMap(self):
        self.arr=[[ None for j in range(self.COLS)] for i in range(self.ROWS)]

    def setStart(self,x,y):
        self.start=startNode(x,y)
        self.arr[x][y]=self.start

    def setGoal(self,x,y):
        self.goal=goalNode(x,y)
        self.arr[x][y]=self.goal
        
    
    def setWalls(self,x,y):
        self.arr[x][y]=wallNode(x,y)

    def manualWallsPlacement(self):
        for i in range(0,10):
            self.setWalls(15-i,5+i)
            self.setWalls(16-i,5+i)

        #self.setWalls(5,14)

    def fillSpareNodes(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.arr[i][j]==None:
                    self.arr[i][j]=spareNode(i,j,self.goal)

    