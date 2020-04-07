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
    
    def setStatus(self,status):
        self.status=status
    
    def getNeighbors(self,matrix):
        neighbors=[]
        
        x_start=0 if self.x==0 else -1
        x_end=0 if self.x==len(matrix[0]) else 1

        y_start=0 if self.y==0 else -1
        y_end=0 if self.y==len(matrix) else 1

        for i in range(x_start,x_end+1):     #adding 1 because of the range mechanism
            for j in range(y_start,y_end+1): #adding 1 because of the range mechanism
                if (i,j)==(0,0):#it is the node itself
                    continue
                neighbor=matrix[self.x+i][self.y+j]
                neighbors.append(neighbor)
        """
        up=matrix[self.x][self.y+1]
        down=matrix[self.x][self.y-1]
        right=matrix[self.x+1][self.y]
        left=matrix[self.x-1][self.y]
        neighbors+=[up,down,right,left]
        """
        return neighbors