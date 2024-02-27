import networkx as nx
import matplotlib.pyplot as plt


#----HELPER FUNCTION-----------
#Displays the adjacency matrix
def create_graph(adj_matrix):
    edges=[]
    total_vertices=len(adj_matrix)
    for mat in adj_matrix:
        if len(mat)>total_vertices or len(mat)<total_vertices:
            print("False Adjacency Matrix")
            return 0
    for i in range(len(adj_matrix)):
        mat=adj_matrix[i]
        for j in range(len(mat)):
            if mat[j]==1:
                temp=[i,j]
                edges.append(temp)

    #visualize graph
    G=nx.Graph()
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()
    vertices=[i for i in range(len(adj_matrix))]

    print(vertices, edges)
    return vertices,edges



#------Fewest Edges----------#
#We have a graph representing a social network, where each node representes a person and is a number from 1 to total_nodes.
# Pick a start_node to represent an influencer, and a destination_node to represent someone they want to reach.
# We'd like to know how quickly information can pass from the influencer to the person they want to reach, within this Social Network.
# Write a function to determine what the fewest edges we have to traverse across is to move from the start_node to the destination_node.
# This is a type of "shortest path" problem, for an unweighted graph.
# Return the fewest number of edges to get from the start_node to the destination_node.


def bfs_fewest_edge_matrix(matrix, start_node, destination, network_size):

    #Edge cases to consider:
    if destination > network_size or start_node > network_size:
        return -1


    #Tracks which nodes have been visited, to correctly map node-number to index, we need visited to be one size bigger than the total number of nodes
    #Example: 5 nodes, the visisted indicies will be: 0,1,2,3,4,5, size is 6
    visited = [False] * (network_size + 1)

    queue = []  #holds onto which nodes we still need to visit the neighbors of
    queue.append(start_node) #Start_node is the initial node we visit
    visited[start_node] = True #update the Visited list

    level = 0 #start with the source, level will represent the level we just finished visiting
    found = False #flag will change to True once any of the nodes we visit is the destination node

    #Keep popping nodes off the queue to visit their neighbors, as long as we haven't found the destination yet
    while queue and not found:
        #We want to track what level we are at, the innermost loop will always append to the queue the nodes that share a level
        #BUT without keeping track, it would be possible that multiple levels of nodes are represented in the queue at one time
        #So add this second loop, around the inner one, that maintains a level count
        nodes_in_level = len(queue) #If we only ever pop nodes one level at a time, then the queue will only ever contain the nodes for one level
        count = 0 #will let this loop run until all nodes at this level have been visited

        #pop all nodes at the current level and visit their neighbors
        while count < nodes_in_level and not found:
            current_node = queue.pop(0)
            neighbor = 1
            while neighbor <= network_size and not found:
                if matrix[current_node][neighbor] == 1 and visited[neighbor] == False:
                    #check to see if this neighbor is our destination
                    if neighbor == destination:
                        found = True
                    queue.append(neighbor)
                    visited[neighbor] = True

                neighbor += 1
            count += 1

        level += 1 #move to the next level

    print(f"We can get from {start_node} to {destination} in as few as {level} edges.")

    if found:
        return level
    else:
        return -1 #return a not-found error flag


#----MAIN CALLING ROUTINE-------

adjacency_matrix = [
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

#See the graph for this matrix
create_graph(adjacency_matrix)
#Program will pause here until you close the graphics window

#run the fewest edges code
#Change up the start and destination values to test this
start = 2
destination = 10
total = 10
result = bfs_fewest_edge_matrix(adjacency_matrix, start, destination, total)
if result == -1:
    print("something went wrong")