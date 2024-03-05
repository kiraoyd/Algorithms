def dfs_wrapper(matrix, start, total_nodes):
    visited = [False] * (total_nodes +1)

    #Make the first call to "visit" the start node
    dfs_recursive(matrix, start, visited, total_nodes)
    print(visited)


#each call to dfs_recursive "visits" the current_node passed to it as an argument
#We will go deeper in level as we check and recursively call the function on one of the current_nodes neighbor
#The loop exploring neighbors will pause the current call on the first valid neighbor...
#...it will only restart once we return from the entire recursive DFS exploration of that neighbor, into another possible iteration of the loop
def dfs_recursive(matrix, current_node, visited, total_nodes):
    if current_node > total_nodes:
        return
    #This will mark each node we recurse to visit as visited, and add it to the path
    visited[current_node] = True

    neighbor = 1 #remember, the adjacency matrix is padded with the 0 row and 0 column

    #Explore the current_nodes neighbors to their max depth
    #The while loop represents going through all the direct adjacent neighbors of the current_node
    while neighbor <= total_nodes:
        if matrix[current_node][neighbor] == 1 and not visited[neighbor]:
            dfs_recursive(matrix, neighbor, visited, total_nodes) #The while loop pauses at each recursive call, allowing us tp traverse depth first
        neighbor += 1

