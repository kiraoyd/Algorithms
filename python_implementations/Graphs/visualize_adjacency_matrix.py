#Code Sourced from: https://colab.research.google.com/drive/1ufc2FhEbO-6yK2EZ3W3CgkqSwvhjXUPl?usp=sharing#scrollTo=FnyZLBbeTfQN
#Original Author: Kunj J Joshi
#Adapted and comments added by Kira Klingenberg

#To get pythons networkx and matplotlib libraries locally:
#pip install networkx
#pip install matplotlib

import networkx as nx
import matplotlib.pyplot as plt
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




#---MAIN----
#Example matrix from class
matrix = [
    [0,0,0,0,0,0],
    [0,0,1,1,0,0],
    [0,1,0,1,1,0],
    [0,1,1,0,1,1],
    [0,0,1,1,0,0],
    [0,0,0,1,1,0]
]


#Social network matrix for HW
matrix2 = [
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

create_graph(matrix)