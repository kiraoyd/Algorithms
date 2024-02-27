#Code Sourced from: https://colab.research.google.com/drive/1ufc2FhEbO-6yK2EZ3W3CgkqSwvhjXUPl?usp=sharing#scrollTo=FnyZLBbeTfQN
#Original Author: Kunj J Joshi
#Adapted and comments added by Kira Klingenberg

#To get pythons networkx and matplotlib libraries locally:
#pip install networkx
#pip install matplotlib


import networkx as nx
import matplotlib.pyplot as plt

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

    #display an image of the graph to verify
    G=nx.Graph()
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()

    #actual matrix is returned to be used
    return adj_matrix


vertices=[1,2,3,4,5,6]
edges=[[1,2],[2,4],[1,5],[3,5],[4,5],[1,3],[5,3],[5,1],[5,6]]

matrix = create_adjacency_matrix(vertices,edges)
print(matrix)