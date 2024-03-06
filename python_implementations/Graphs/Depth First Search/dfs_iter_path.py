#----------------ITERATIVE MAZE PATH FINDING---------------#

#-----track the parent of each node visited, then use that parent array to reconstruct the path----#
def dfs_maze(matrix, start, target, total_nodes):
    visited = [False] * (total_nodes + 1)
    parent = [0] * (total_nodes + 1) #will keep track of the parent nodes of each node in a path (each index represents a node, and the value stored at that index is the parent to that node)
    stack = [] #will hold nodes we have not yet visited in the levels above where we are currently exploring

    stack.append(start) #add start node to the stack

    #as long as we have nodes in the stack that might have neighbors, pop that node and explore it's neighbors
    while stack:
        #pop the node at the top of the stack
        current_node = stack.pop()

        #Right away, if we reached the target, we are done, no more exploring needed
        if current_node == target:
            #construct path from parent array
            path = []
            path.append(target) #add the target node to the path

            #working backwords from the current, target node
            node = target #we want to find the parent node, of 'node'
            while node != start:
                path.append(parent[node]) #add the parent of 'node' to the path
                node = parent[node] #the new 'node' we want to find the parent of, will be the parent we just added to the path

            path.reverse() #the path was appended backwards, so reverse the list
            print(f"The path from {start} to {target} found with DFS is: {path}") #show the path
            return path

        #visit the current_node
        if visited[current_node] == False:
            visited[current_node] = True #visit a node when we pop it from the stack

            neighbor = 1
            #walk across the column for the current_nodes row, find this current nodes unvisted neighbors
            #To construct the path later, keep track of the parent nodes to the nodes we push to the stack
            while neighbor <= total_nodes:
                #if the current node has a neighbor, and that neighbor has not yet been visited...
                if matrix[current_node][neighbor] == 1 and visited[neighbor] == False:
                    stack.append(neighbor) #add this neighbor to the stack
                    parent[neighbor] = current_node #record the current node as this neighbor-nodes parent
                neighbor += 1

#---------MAIN CALLING ROUTINE--------#
matrix = [
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

total_nodes = 10
start = 7
target = 8
dfs_maze(matrix, start, target, total_nodes)