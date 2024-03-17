"""
#-------HOMEWORK #5 SOLUTION: INFORMATION SPREAD--------------------#
assume we have a connected graph (no bipartate graph) so there will always be a path from some node to some other node.
# The graph is represented by an adjacency matrix where there is no 0-node and nodes are a sequence of numbers from 1 to nodes_visited.
# Determine how quickly information can spread from some start_node to a certain number of other nodes (spread_goal)
# Speed of spread is represented in levels of connection.
# A faster spread happens with fewer levels of connection that must be traversed to reach the spread_goal.
"""
def bfs_spread_matrix (matrix, start_node, total_nodes, spread_goal):
    #Start_node is the initial node we visit
    visited = [False] * (total_nodes + 1)
    visited[0] = True #there's no 0-node, so mark it True by default
    queue = [] #create the queue, empty at first

    #We are already at the starting node
    queue.append(start_node)
    visited[start_node] = True

    nodes_visited = 0
    level = 0 #start with the source, level will represent the level we just finished visiting

    #keep going until we have reached 10 people
    while queue and nodes_visited < spread_goal:
        #check the number of items in the queue at this level
        nodes_in_level = len(queue)
        count = 0
        #pop all nodes at this level and visit their neighbors
        while count < nodes_in_level and nodes_visited < spread_goal:
            current_node = queue.pop(0)
            #Iterate over the row in the matrix that represents the current_node
            neighbor  = 1
            while neighbor <= total_nodes and nodes_visited < spread_goal: #nodes_visited is row length
                #looks for neighbors to current_node that have not been visited
                if matrix[current_node][neighbor] == 1 and visited[neighbor] == False:
                    #the neighbor to the current_node is unvisited, add it to the queue
                    queue.append(neighbor)
                    visited[neighbor] = True #mark this neighbor as visited
                    nodes_visited += 1 #tally up person as reached
                neighbor += 1  #Increment neighbor count after check
            count += 1

        level += 1 #level holds the level we just finished "visiting"


    print(f"Information spread to {nodes_visited} people in {level} levels of connection from the source") #show that we visited all nodes
    return level

"""
#-------SAME CODE AS ABOVE BUT WITH ADDED PRINT STATEMENTS TO HELP VISUALIZE IN THE OUTPUT-----#
"""
def bfs_spread_matrix_trace (matrix, start_node, total_nodes, spread_goal):
    #Start_node is the initial node we visit
    visited = [False] * (total_nodes + 1)
    visited[0] = True #there's no 0-node, so mark it True by default
    queue = [] #create the queue, empty at first

    queue.append(start_node)
    visited[start_node] = True

    print(f"\nBegining the Traced version of the solution....")
    print(f"Our queue begins holding the starting node: {queue}, we consider {queue[0]} as having been visited.\n")

    nodes_visited = 0
    level = 0 #start with the source,
    #keep going until we have reached 10 people
    while queue and nodes_visited < spread_goal:
        #check the number of items in the queue at this level
        nodes_in_level = len(queue)
        count = 0
        #don't increase the level until we've popped all nodes at this level and visited their neighbors
        while count < nodes_in_level and nodes_visited < spread_goal:

            current_node = queue.pop(0)
            print(f"\n From node {current_node}... (we just popped this off the queue)")

            #Iterate over the row in the matrix that represents the current_node
            neighbor  = 1
            added_count = 0 #for better output
            while neighbor <= total_nodes and nodes_visited < spread_goal: #nodes_visited is row length
                #looks for neighbors to current_node that have not been visited
                if matrix[current_node][neighbor] == 1 and visited[neighbor] == False:
                    #the neighbor to the current_node is unvisited, add it to the queue
                    queue.append(neighbor)
                    visited[neighbor] = True #mark this neighbor as visited
                    added_count += 1 #for better output
                    nodes_visited += 1 #tally up person as reached
                    print(f"...we are visiting this node: {neighbor}, (we added it to the queue)")
                neighbor += 1  #Increment neighbor count after check


            if added_count == 0: #use added_count for better output
                print("All this nodes neighbors have already been visited.")

            if nodes_visited < spread_goal:
                print(f" We have visited a total of {nodes_visited} nodes at this point.")
            else:
                print(f" We have visited a total of {nodes_visited} nodes at this point, we've reached the goal!")
            print(f"Here is what we have in the queue at this point: {queue}")
            count += 1

        level += 1 #level holds the level we just finished "visiting"
        print(f"\n------We just finished visiting the nodes at level {level}...")
        if nodes_visited < spread_goal:
            print(f"...time to move on to the next. ")
        else:
            print(f".....this is the last level we need to visit, so our traversal stops at level {level}")

    print(f"\n RESULTS: Information spread to {nodes_visited} people in {level} levels of connection from the source") #show that we visited all nodes
    return level


#----------MAIN CALLING ROUTINE------------

case1 = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,0,1,0,0,0],
    [0,1,0,1,0,1,1,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,1,1,0],
    [0,1,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1,0]
]

case2 = [
    [0,0,0,0,0,0],
    [0,0,1,1,0,0],
    [0,1,0,1,1,0],
    [0,1,1,0,1,1],
    [0,0,1,1,0,0],
    [0,0,0,1,1,0]
]

"""
#Uncomment this blcok to run case1 without an output trace
start = 2
total_nodes = 10
spread_goal = 8
bfs_spread_matrix(case1, start, total_nodes, spread_goal)
"""


#Run case 2 with an output trace
start = 1
total_nodes = 5
spread_goal = 3
bfs_spread_matrix_trace(case2, start, total_nodes, spread_goal)

