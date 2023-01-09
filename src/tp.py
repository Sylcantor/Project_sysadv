import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

import multiprocessing as mp

#function who print number of nodes, edges and connected components of a graph of a graph
def print_graph_info(G,name):
    number_of_nodes = G.number_of_nodes()
    number_of_edges = G.number_of_edges()
    print("Number of nodes : ", number_of_nodes, " of graph ", name)
    print("Number of edges : ", number_of_edges, " of graph ", name)

    #write in a file the number of nodes and edges of the graph
    file = open("graph_info.txt", "a")
    file.write("Number of nodes : " + str(number_of_nodes) + " of graph " + name + " \n")
    file.write("Number of edges : " + str(number_of_edges) + " of graph " + name + " \n")
    file.close()
    

#function who print the density of a graph
def print_density(G,name):
    density = nx.density(G)
    print("Density : ", density, " of graph ", name)
    file = open("graph_info.txt", "a")
    file.write("Density : " + str(density) + " of graph " + name + " \n")
    file.close()

#function who print the average degree of a graph
def print_average_degree(G,name):
    average_degree = sum(dict(G.degree()).values())/len(dict(G.degree()).values())
    print("Average degree : ", average_degree, " of graph ", name)
    file = open("graph_info.txt", "a")
    file.write("Average degree : " + str(average_degree) + " of graph " + name + " \n")
    file.close()

#function who print the average distance between two nodes in a graph
def print_average_distance(G,name):
    average_distance = nx.average_shortest_path_length(G)
    print("Average distance : ", average_distance, " of graph ", name)
    file = open("graph_info.txt", "a")
    file.write("Average distance : " + str(average_distance) + " of graph " + name + " \n")
    file.close()

#function who print the diameter of a graph
def print_diameter(G,name):
    diameter = nx.diameter(G)
    print("Diameter : ", diameter, " of graph ", name)
    file = open("graph_info.txt", "a")
    file.write("Diameter : " + str(diameter) + " of graph " + name + " \n")
    file.close()

#function who print the degree distribution of a graph
def print_degree_distribution(G,name):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    print("Degree sequence", degree_sequence, " of graph ", name)
    file = open("graph_info.txt", "a")
    file.write("Degree sequence " + str(degree_sequence) + " of graph " + name + " \n")
    file.close()

#function who print the largest connected component of a graph
def get_largest_connected_component(G):
    largest = max(nx.connected_components(G), key=len)
    #print(len(largest))
    S = G.subgraph(largest)
    return S

#function who write a graph to a file
def write_graph_to_file(G, path):
    nx.write_edgelist(G, path, delimiter=" ", data=False)

#function who print the number total of triangles in a graph
def print_number_of_triangles(G,name):
    triangles = nx.triangles(G)
    triangles = sum(triangles.values()) / 3
    print("Number of triangles in graph ", name, " : " + str(triangles))
    file = open("graph_info.txt", "a")
    file.write("Number of triangles in graph " + name + " : " + str(triangles) + " \n")
    file.close()

#function who print the global clustering coefficient of a graph
def print_global_clustering_coefficient(G,name):
    global_clustering = nx.transitivity(G)
    print("Global clustering coefficient in graph ", name, " : ")
    print(global_clustering)
    file = open("graph_info.txt", "a")
    file.write("Global clustering coefficient in graph " + name + " : " + str(global_clustering) + " \n")
    file.close()

#function who print the local clustering coefficient of a graph
def print_local_clustering_coefficient(G,name):
    local_clustering = nx.average_clustering(G)
    print("Local clustering coefficient in graph ", name, " : ")
    print(local_clustering)
    file = open("graph_info.txt", "a")
    file.write("Local clustering coefficient in graph " + name + " : " + str(local_clustering) + " \n")
    file.close()

#function who return an erdos-renyi graph with the same parameters as G
def get_erdos_renyi_graph(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    p = 2 * m / (n * (n - 1))
    er = nx.erdos_renyi_graph(n, p)
    return er

#function who return a random graph with the same parameters as G
def generate_random_graph(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    p = 2 * m / (n * (n - 1))
    rg = nx.gnp_random_graph(n, p)
    return rg

def plot_distribution_degre_log(G):
    degrees = nx.degree(G)
    degree_count = {}
    for node, degree in degrees:
        if degree not in degree_count:
            degree_count[degree] = 1
        else:
            degree_count[degree] += 1

    # Récupérer les degrés et le nombre de noeuds de chaque degré dans des listes
    degrees = list(degree_count.keys())
    counts = list(degree_count.values())

    # Tracer la distribution des degrés avec une échelle lin-lin
    plt.plot(degrees, counts, 'bo')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Degré')
    plt.ylabel('Nombre de noeuds')
    plt.show()


def plot_distribution_degre_lin(G):
    degrees = nx.degree(G)
    degree_count = {}
    for node, degree in degrees:
        if degree not in degree_count:
            degree_count[degree] = 1
        else:
            degree_count[degree] += 1

    # Récupérer les degrés et le nombre de noeuds de chaque degré dans des listes
    degrees = list(degree_count.keys())
    counts = list(degree_count.values())

    # Tracer la distribution des degrés avec une échelle lin-lin
    plt.plot(degrees, counts, 'bo')
    plt.xscale('linear')
    plt.yscale('linear')
    plt.xlabel('Degré')
    plt.ylabel('Nombre de noeuds')
    plt.show()


#function main
def main():
    #DO YOUR STUFF HERE

    #G_small = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.opsahl-powergrid_filtered-largest.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)
    #G_big = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.flickrEdges_filtered-largest.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)
    #G_er_small = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.erdos-renyi-small.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)
    #G_random_small = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.random-small.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)
    #G_er_big = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.erdos-renyi-big.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)
    #G_random_big = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.random-big.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)
    

    #plot_distribution_degre_log(G_random_big)
    #plot_distribution_degre_lin(G_random_big)


    #SOME MULTIPROCESS STUFF :
    '''
    print("start process")
    p1 = mp.Process(target=generate_and_write_big_graph_erdos_renyi, args=(G_big,))
    p1.start()

    print("start process")
    p2 = mp.Process(target=generate_and_write_big_graph_random, args=(G_big,))
    p2.start()

    print("join process")
    p1.join()
    p2.join()
    
    print("process 1 & 2 done")
    G_er_big = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.erdos-renyi-big.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)
    G_random_big = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.random-big.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)

    print("start process for G_er_big and G_random_big")
    proccesses1 = [
        mp.Process(target=print_graph_info, args=(G_er_big,"G_er_big")),
        mp.Process(target=print_density, args=(G_er_big,"G_er_big")),
        mp.Process(target=print_average_degree, args=(G_er_big,"G_er_big")),
        mp.Process(target=print_average_distance, args=(G_er_big,"G_er_big")),
        mp.Process(target=print_diameter, args=(G_er_big,"G_er_big")),
        mp.Process(target=print_number_of_triangles, args=(G_er_big,"G_er_big")),
        mp.Process(target=print_global_clustering_coefficient, args=(G_er_big,"G_er_big")),
        mp.Process(target=print_local_clustering_coefficient, args=(G_er_big,"G_er_big")),
    ]

    for p in proccesses1:
        p.start()
    
    proccesses2 = [
        mp.Process(target=print_graph_info, args=(G_random_big,"G_random_big")),
        mp.Process(target=print_density, args=(G_random_big,"G_random_big")),
        mp.Process(target=print_average_degree, args=(G_random_big,"G_random_big")),
        mp.Process(target=print_average_distance, args=(G_random_big,"G_random_big")),
        mp.Process(target=print_diameter, args=(G_random_big,"G_random_big")),
        mp.Process(target=print_number_of_triangles, args=(G_random_big,"G_random_big")),
        mp.Process(target=print_global_clustering_coefficient, args=(G_random_big,"G_random_big")),
        mp.Process(target=print_local_clustering_coefficient, args=(G_random_big,"G_random_big")),
    ]

    for p in proccesses2:
        p.start()

    for p in proccesses1:
        p.join()


    for p in proccesses2:
        p.join()
    
    '''

#Call main
if __name__ == "__main__":
    main()