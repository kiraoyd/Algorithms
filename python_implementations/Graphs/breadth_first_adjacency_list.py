#---------BFS TRAVERSAL - ADJACENCY LIST-------3

#Space complexity: O(V + E)
#Time complexity: O(V + E), visit each node once and explore neighbors, iteration increases as value of E increases (as we iterate over the Edge lists)
def bfs_list(adjacency_list, start_node, number):
    #start_node is the initial node we visit
    visited = [False] * (number+1)
    queue = []
    queue.append(start_node)
    visited[start_node] = True

    print(f"Our queue begins holding the starting node: {queue}, we consider {queue[0]} as having been visited.\n")
    while queue:
        #while there are nodes to explore
        current_node = queue.pop(0) #grab the first node in the queue
        print(f"\nFrom node {current_node}...(we just popped this off the queue)")

        #Get neighbors list for currrent_node
        neighbors = adjacency_list[current_node]
        size = len(neighbors)
        index = 0
        added_count = 0
        while index < size:
            neighbor = neighbors[index]
            #add each neighbor to the queue if it has not been visited
            if visited[neighbor] == False:
                queue.append(neighbor)
                visited[neighbor] = True #mark it as visited
                added_count += 1
                print(f"...we are visiting this node: {neighbor} (added to queue)")

            #print(queue)
            index = index + 1

        if added_count == 0 :
            print("All this nodes neighbors have been visited already.")
        print(f"Here is what we have in the queue to process: {queue}")
    #After all neighbors of this current node are added to the queue, the loop breaks

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
