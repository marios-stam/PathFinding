import  time
from  nodeClasses.spareNode import spareNode
from  nodeClasses.startNode import startNode
from  nodeClasses.wallNode  import wallNode
from  nodeClasses.goalNode  import goalNode



def algo(arr,start :startNode,goal :goalNode,gui):
    OPEN=[start]
    CLOSED=[]
    while True:
        curr_node= min(OPEN,key=lambda i:i.getFcost())
        if (curr_node in CLOSED):
            print('PROSOXI RE MALAKAAAAAAAAAAA')
            OPEN.remove(curr_node)
            continue
        try:
           print(f'Current node:{curr_node.x,curr_node.y} with parent at {curr_node.parent.x,curr_node.parent.y}')
        except Exception as e:
            print(e)    

        OPEN.remove(curr_node)
        
        CLOSED.append(curr_node)            
        curr_node.setStatus('current')

        if  isinstance(curr_node,goalNode):#reached to the goal
            break

        for neighbor in curr_node.getNeighbors(arr):

            if ( isinstance(neighbor,wallNode)) or (neighbor in CLOSED) :
                continue
            
            #check if there is shorter path to neighbor
            if(neighbor.parent!=None):
                old_f=neighbor.getFcost()
                old_parent=neighbor.parent
                neighbor.setParent(curr_node)
                shorter_path=neighbor.getFcost()<old_f
                if(not shorter_path):neighbor.setParent(old_parent)
            else:
                shorter_path=False

            if(shorter_path or (neighbor not  in CLOSED)):
                neighbor.setParent(curr_node)
                neighbor.getFcost()
                if(neighbor not in CLOSED):
                    neighbor.status='open'
                    OPEN.append(neighbor)
            #render changes for debugging
            gui.update()
            time.sleep(.2)
            curr_node.setStatus('closed')

    path_to_goal=[]
    while not isinstance(curr_node,startNode):
        path_to_goal.append(curr_node)
        curr_node=curr_node.parent
    
    path_to_goal[1:]
    for i in path_to_goal:
        print(i.x,i.y)
    
    gui.drawPath(path_to_goal)
    return path_to_goal
        
