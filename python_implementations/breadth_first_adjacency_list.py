#---------BFS TRAVERSAL - ADJACENCY MATRIX-------3
#space complexity, O(V^2), Vertices are both rows and columns
#Time complexity: also O(V + E), we consider E because the work of the inner loop increases as E increases, because the work is nested in the condition that triggers only if an Edge exists (is a 1)
def bfs_matrix(graph, start_node, number):
    #Start_node is the initial node we visit
    #create a list of visited nodes, initialize them all to False
    #This list should be of size number + 1
    visited = [False] * (number+1)
    #create a queue, empty
    queue = []
    #push the start_node to the queue
    queue.append(start_node)
    #mark the start_node as visited
    # Any node added to the queue is marked as visited
    visited[start_node] = True
    #Why as we append? So we don't double add during the if graph[curent_node][neighbor] == 1 and visited[neighbor] == False check down below, in the event there is a cycle in the graph

    print(f"Our queue begins holding the starting node: {queue}, we consider {queue[0]} as having been visited.\n")

    #As long as we have something in the queue...
    while queue:
        #Visit the node at the front of the queue
        current_node = queue.pop(0) #queue.pop() pops the LAST item in a list
        print(f"\nFrom node {current_node}...(we just popped this off the queue)")


        #Iterate over the row for the current_node
        neighbor = 1
        added_count = 0
        while neighbor <= number:
            #If we have a connection and it is to a vertex NOT yet visited
            if graph[current_node][neighbor] == 1 and visited[neighbor] == False:
                #This neighbor to the current node is unvisited, add it to the queue
                queue.append(neighbor)
                visited[neighbor] = True #Mark as visited
                added_count += 1
                print(f"...we are visiting this node: {neighbor} (added to queue)")

            neighbor += 1 #Increment neighbor count after check
        #When the inner loop breaks, we have finished processing the row for the current_node and pushed all its neighbors to the queue
        #So now it's time to pop the next node in the queue and run the inner loop again on IT's row, jump back to the while loop on line 16
        if added_count == 0 :
            print("All this nodes neighbors have been visited already.")
        print(f"Here is what we have in the queue to process: {queue}")
    return visited



#----MAIN CALLING ROUTINE----#
adjacency = {
    1: [2,3],
    2: [1,3,4],
    3: [1,2,4,5],
    4: [2,3,5],
    5: [3,4]
}

number = 5
visited = bfs_list(adjacency, 1, number)
print(f"\nThrough BFS run on an adjacency list, we visited all the verticies, where the index value of the list represents the vertex: {visited}")
