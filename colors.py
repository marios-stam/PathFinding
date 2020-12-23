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
    orange=(255,140,0)
    yellow=(255,255,51)


    matchColorDict={  
                    startNode:blue,#Start
                    goalNode:red,#finish
                    wallNode:white#wall
                }
    spareNodedict={
                    None:black,
                    'current':yellow,
                    'closed':orange,
                    'open':green
        }
        

    @classmethod
    def matchColor(self,obj):
        kind=type(obj)
        if(kind!=spareNode):
            color=colors.matchColorDict[kind]
            return color
        
        return colors.spareNodedict[obj.status]



if __name__ == "__main__":
    
    e=goalNode(2,3)
    print(colors.matchColor(e))