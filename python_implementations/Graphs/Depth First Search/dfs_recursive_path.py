#--------------- RECURSIVE MAZE PATH FINDING--------------


#Wrapper function to start the recursion, and pass the matrix, the visited array and the path array to each call by reference
def dfs_path(matrix, start, target, total_nodes):
    visited = [False] * (total_nodes +1)
    path = []

    found = dfs_recursive(matrix, start, target, visited, path, total_nodes)
    if found:
        path.reverse() #the path was originally appended in reverse order
        print(f"The path from {start} to {target} using recursive Depth First Search is: {path}")
        print(f"To find this path we had to visit the following nodes: ")
        node = 0
        while node < len(visited):
            if visited[node]:
                print(f"Node {node}")
            node += 1
    else:
        print(f"No path found from {start} to {target}")



#Credit to Kevin Macdonald for suggesting in class we ONLY add a node to the path on the return if we hit the target node
#This strategy is a lot cleaner than my original idea of: add all visited nodes to the path and pop if not part of the target path
def dfs_recursive(matrix, current_node, target, visited, path, total_nodes):
    #Extra check just in case we try to visit a node that is out of bounds of the graph
    if current_node > total_nodes or current_node < 1:
        return

    visited[current_node] = True #mark this node as visited

    #check to see if the current_node is the target, if it is, we found our path and it's time to return True back up the callstack
    if current_node == target:
        path.append(target) #add the target to the path
        return True

    #otherwise, no target found yet so try to keep going deeper along the path
    neighbor = 1
    found = False #if any recursive call returns having found the target, we don't want to continue the neighbor checking loop below

    #Explore the current_nodes neighbors, each neighbor gets explored to it's path's max depth before we ever end up iterating again through the loop to check the NEXT neighbor
    while neighbor <= total_nodes:
        if matrix[current_node][neighbor] == 1 and not visited[neighbor]:
            found = dfs_recursive(matrix, neighbor, target, visited, path, total_nodes)  #this call pauses the loop, we will only return to the loop to continue checking the other neighbors (other possible paths) if we search as deeply as possible down this path and do NOT hit the target

            #any recursive call that has hit the target, will return 'True' back up the callstack, keep this going with the check below:
            if found:
                #we also want to add the current_node to the path, as we've found the path to the target
                path.append(current_node)
                return True #no need to explore further, just keep returning True up the callstack

        #otherwise, no target found along that neighbors path, so iterate and explore the next neighbors path to its maximum depth
        neighbor += 1

    return False # if none of this nodes neighbors hits the target, return False


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
dfs_path(matrix, start, target, total_nodes)