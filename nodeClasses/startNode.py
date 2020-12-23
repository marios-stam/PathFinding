from  nodeClasses.node import node 

class startNode(node):
    def __init__(self,x,y):
        node.__init__(self,x,y)
       
    def getFcost(self):
        return 0
