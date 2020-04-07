class node():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getEucledianDistance(self,dest):
        return ( (self.x-dest.x)**2 + (self.y-dest.y)**2)**(0.5)#Euclidean distance

    def getDistances(self,dest):
        dx=(self.x-dest.x)
        dy=(self.y-dest.y)
        return dx,dy
    
    def getNeighbors(self):
        pass