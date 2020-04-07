from  nodeClasses.node import node 
from  nodeClasses.startNode import startNode 

class spareNode(node):
    def __init__(self,x,y,goal=None):
        node.__init__(self,x,y)
        self.GOAL=goal

    
    def setGoal(self,goal):
        self.GOAL=goal
    
    def setParent(self,parent):
        self.parent=parent
    
    """
     -g(n) is the cost of the path from the start node to n
     -h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal. 
    """
    def getGcost(self):
        g=0
        child=self
        while( type(child.parent)!=startNode  ):#irate every parent until start
            g+=1#TODO:check if diagonallly and make it 14
            child=child.parent

        self.g=g
        return g
            
    
    def getHcost(self):
        self.h=self.getEucledianDistance(self.GOAL)
        return self.h
    
    def getFcost(self):
        f=self.f= self.getGcost() + self.getHcost() 
        return f

