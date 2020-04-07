from  nodeClasses.spareNode import spareNode
from  nodeClasses.startNode import startNode
from  nodeClasses.wallNode  import wallNode
from  nodeClasses.goalNode  import goalNode

class colors:
    
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)

    matchColorDict={    
                    spareNode:black, 
                    startNode:green,#Start
                    goalNode:red,#finish
                    wallNode:white#wall
                }

        

    @classmethod
    def matchColor(self,obj):
        kind=type(obj)
        color=colors.matchColorDict[kind]
        return color
    
if __name__ == "__main__":
    
    e=goalNode(2,3)
    print(colors.matchColor(e))