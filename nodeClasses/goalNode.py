from  nodeClasses.node import node 

class goalNode(node):
    def __init__(self,x,y):
        node.__init__(self,x,y)
        self.parent=None
    
    def setParent(self,parent):
        self.parent=parent
    
    def getFcost(self):
        return 0