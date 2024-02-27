import networkx as nx
import matplotlib.pyplot as plt

#Helper function:
def create_adjacency_matrix(vertices,edges):
    total_vertices=len(vertices) + 1 #account for no 0-vertex
    adj_matrix=[]
    #create the rows
    while(len(adj_matrix)<total_vertices):
        temp=[]
        #Each row gets initialized with 0's
        for i in range(total_vertices):
            temp.append(0)
        adj_matrix.append(temp)

    #Set the edges
    for edge in edges:
        i=edge[0]
        j=edge[1]
        if i>=total_vertices or j>=total_vertices or i<0 or j<0:
            print(f"Not a Proper Input in Edge {i},{j}")
        else:
            adj_matrix[i][j]=1
            adj_matrix[j][i]=1

    #display an image of the graph to verify, doesn't work in REPL.it
    G=nx.Graph()
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()

    #actual matrix is returned to be used
    return adj_matrix



#-----PARRY INVITE PROBLEM -----Adjacency Matrix-----#
# Imagine we are in charge of throwing a party.
# Our host is a person who has a potentially vast and interconnected social network.
# We can have exactly party_size number of people at this party, including the host
# Use BFS traversal to invite exactly party_size number of people, prioritizing the hosts closest connections first
# Assume network is represented by an adjacency matrix, and all people are represented by nodes that are just numbers from 1 - n, where n is the network_size (there is no 0-node)
def bfs_party_matrix(network, host, party_size, network_size):
    #host is the source node here for this problem
    #social_network is a 2D matrix, rows and columns represent all nodes in the network

    invited = [] #tracks who we have invited so far
    #Note: You can solve this with JUST an invited list, or JUST a visited list as well.
    #This implementation will use both lists just for good measure

    #Edge Case:
    #If we try to invite more people than in the network, just invite EVERYONE
    if network_size <= party_size:
        count = 1
        while count <= party_size:
            invited.append(count)
            count += 1
        return invited

    #------------BFS Traversal code - over an Adjacency Matrix -----------

    #Tracks which nodes have been visited, to correctly map node-number to index, we need visited to be one size bigger than the total number of nodes
    #Example: 5 nodes, the visisted indicies will be: 0,1,2,3,4,5, size is 6
    visited = [False] * (network_size + 1)

    #Only nodes that have been visited already, get added to the queue
    queue = [] #holds onto which nodes we still need to visit the neighbors of
    queue.append(host) #The host is visited, as this is the node we start from, so we add it to the queue
    visited[host] = True #update the Visited list
    invited.append(host) #consider our host invited, it's their party after all

    #We will need to track how many people have been invited so far, so we can stop when we hit the party_size
    count = 1 #host has been invited, so start count at 1 to include them

    #We will always invite the people closest to host first
    #Keep traversing as long as we have nodes in the queue AND we still have party-spots to fill
    while queue and count < party_size:
        current_node = queue.pop(0) #grab the first node in the queue...
        #...visit the current_nodes neighbors

        #-----The following code block is specific to traversing an adjacency matrix------
        neighbor = 1 #we have no 0-node, so the first neighbor in the row to check is 1
        #iterate across columns over the current_nodes row
        while neighbor <= network_size and count < party_size:
            if network[current_node][neighbor] == 1 and visited[neighbor] == False:
                #visit this node if the current_node is connected to it by an edge, and it has not yet been visited
                queue.append(neighbor)
                visited[neighbor] = True
                invited.append(neighbor) #visiting a node, in this problem, means inviting that person
                count += 1 #tally up the total intited so far
            neighbor += 1 #move on to the next column

    return invited #Once the BFS traversal terminates, this will hold all the nodes / people we invited



#The party problem could translate from Social Networks to maps:
# --> find the 10 restaurants closest to your location
# --> Find the 5 uber cars closest to your location
# ...etc


#-----MAIN CALLING ROUTINE-----

#Create an adjacency matrix using the helper function (comment this out if you want to provide your own adjacency matrix)
vertices=[1,2,3,4,5,6,7,8,9,10]
edges=[[1,2],[1,7],[1,5],[2,3],[2,6],[3,6],[2,8],[2,5], [5,4], [8,4], [4,9], [9,10]]
matrix = create_adjacency_matrix(vertices,edges)
#If you are running this with the networkx and matplotlib library, the program will PAUSE here until you close the graphics window
print(matrix) #show the matrix

host = 2
party_size = 8
network_size = 10
invited = bfs_party_matrix(matrix, host, party_size, network_size)
print(f"\nIf people really were just numbers (LIES!), then these people are coming to the party: {invited}")