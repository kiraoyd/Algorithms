
#We "visit" a node when we pop it from the stack
#No path tracking yet, just node exploration here
def dfs(matrix, start, total_nodes):
    visited = [False] * (total_nodes + 1)
    stack = []
    stack.append(start)

    #visit nodes in the stack
    while stack:
        #pop the node at the top of the stack
        current_node = stack.pop()

        if not visited[current_node]:
            visited[current_node] = True #visit the node if it is unvisited

            #If the node is unvisited, we want to push its neighbors to the stack
            neighbor = 1
            while neighbor <= total_nodes:
                if matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
                neighbor += 1

        print(stack)
        #Since we push and pop to the top of the stack, we bury unvisited neighbors from earlier levels
        #So we end up traversing as far down as we can, before backtracking back up to the last unvisited neighbor of some node above

    #Once there are no more unvisited neighbors on the stack, we are done and have visited every node
    print(visited) #View the visited array to see all nodes have been visited (except the non-existent 0-node)


#---MAIN CALLING ROUTINE---#

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

start = 5
total_nodes = 10
dfs(matrix, start, total_nodes)