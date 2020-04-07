from  nodeClasses.node import node 
from  nodeClasses.startNode import startNode 
from  nodeClasses.wallNode import wallNode 

class spareNode(node):
    def __init__(self,x,y,goal=None):
        node.__init__(self,x,y)
        self.GOAL=goal
        self.setParent(None)
        self.setStatus(None)
    
    def setGoal(self,goal):
        self.GOAL=goal
    
    def setParent(self,parent):
        self.parent=parent
    def getNeighbors(self,arr):
        neighbors=super(spareNode, self).getNeighbors(arr)
        for i in neighbors:
            if isinstance(i,wallNode):
                pass
                #neighbors.remove(i)
        return neighbors

    """
     -g(n) is the cost of the path from the start node to n
     -h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal. 
    """
    def getGcost(self):
        g=0
        child=self
        #print(type(child)!=startNode)
        while( type(child)!=startNode and type(child.parent)!=startNode ):#irate every parent until start
            distance=1.4 if (child.x!=child.parent.x and child.y!=child.parent.y) else 1#if diagonally add 1.4=(2)^(0.5)           
            g+=distance
            child=child.parent

        self.g=g
        return g
            
    
    def getHcost(self):
        self.h=self.getEucledianDistance(self.GOAL)
        return self.h
    
    def getFcost(self):
        self.f= self.getGcost() + self.getHcost() 
        return self.f

