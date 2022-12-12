import networkx as nx

G = nx.read_edgelist('/home/guiblin/Master/Systemadv/data/out.moreno_names_names_filtered.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)


print(nx.number_connected_components(G))

largest = max(nx.connected_components(G), key=len)
#print(len(largest))


print(G.number_of_nodes())
print(G.number_of_edges())


S = G.subgraph(largest)
print(S.number_of_nodes())
print(S.number_of_edges())

print(nx.density(S))

#write the largest connected component to a file
#nx.write_edgelist(S, "/home/guiblin/Master/Systemadv/data/out.moreno_names_names_filtered-largest.txt", delimiter=" ", data=False)
