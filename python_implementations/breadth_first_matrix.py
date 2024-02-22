
#---------BFS TRAVERSAL - ADJACENCY MATRIX-------3
#space complexity, O(V^2), Vertices are both rows and columns
#Time complexity:  O(V + E), we consider E because the work of the inner loop increases as E increases, because the work is nested in the condition that triggers only if an Edge exists (noted by a 1 in our matrix)

def bfs_matrix (matrix, start_node, total_nodes):
    #Start_node is the initial node we visit
    #create a list of visited nodes, initialize them all to False
    #This list should be of size total_nodes + 1, as we don't have a 0-node in this example
    visited = [False] * (total_nodes + 1)
    visited[0] = True #there's no 0-node, so mark it True by default
    queue = [] #create the queue, empty at first

    #push the start_node to the queue
    queue.append(start_node)
    #mark node as visited
    visited[start_node] = True
    #Why mark as we append? The queue holds nodes whose neighbors we might need to explore. This ordering also prevents us from double adding a node to the queue in the case of a cycle

    print(f"Our queue begins holding the starting node: {queue}, we consider {queue[0]} as having been visited.\n")

    #while there is something in the queue to consider
    while queue:
        #visit the first node in the queue
        current_node = queue.pop(0) #queue.pop() pops the LAST item in a list, so we need to specify '0' to pop the first thing
        print(f"\n From node {current_node}... (we just popped this off the queue)")


        #Iterate over the row in the matrix that represents the current_node
        neighbor  = 1
        added_count = 0 #for better output
        while neighbor <= total_nodes:
            #looks for neighbors to current_node that have not been visited
            if matrix[current_node][neighbor] == 1 and visited[neighbor] == False:
                #the neighbor to the current_node is unvisited, add it to the queue
                queue.append(neighbor)
                visited[neighbor] = True #mark this neighbor as visited
                added_count += 1 #for better output
                print(f"We are visiting this node: {neighbor}, (we added it to the queue)")
            neighbor += 1  #Increment neighbor count after check
        #When the inner loop breaks, w ehave finished processing the row for the current_node and pushed all its neighbors to the queue
        #So now it's time to pop the next node in the queue and run the inner loop again on IT's row, jump back to the while loop on line 16

        if added_count == 0: #use added_count for better output
            print("All this nodes neighbors have already been visited.")

        print(f"Here is what we have in the queue at this point: {queue}")

    print(visited) #show that we visited all nodes
    return visited



#MAIN CALLING ROUTINE
adjacency_matrix = [
    [0,0,0,0,0,0],
    [0,0,1,1,0,0],
    [0,1,0,1,1,0],
    [0,1,1,0,1,1],
    [0,0,1,1,0,0],
    [0,0,0,1,1,0]
]

bfs_matrix(adjacency_matrix, 2, 5)