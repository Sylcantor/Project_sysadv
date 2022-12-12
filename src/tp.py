import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.read_edgelist('/home/guiblin/repos/Project_sysadv/data/out.opsahl-powergrid-filtered.txt',create_using=nx.Graph,delimiter=" ",nodetype=int)


print(nx.number_connected_components(G))

largest = max(nx.connected_components(G), key=len)
#print(len(largest))


print(G.number_of_nodes())
print(G.number_of_edges())


S = G.subgraph(largest)
print(S.number_of_nodes())
print(S.number_of_edges())

print(nx.density(S))

#print the degree average of the largest connected component
print(sum(dict(S.degree()).values())/len(dict(S.degree()).values()))

#print the average distance between two nodes in the largest connected component

#print(nx.average_shortest_path_length(S)) #print 18.9 Est ce une bonne valeur?

#print the diameter of the largest connected component
#print(nx.diameter(S)) #46

degree_sequence = sorted([d for n, d in S.degree()], reverse=True)  # degree sequence
#print("Degree sequence", degree_sequence)

#write the largest connected component to a file
#nx.write_edgelist(S, "/home/guiblin/Master/Systemadv/data/out.moreno_names_names_filtered-largest.txt", delimiter=" ", data=False)

#draw the degree distribution of the largest connected component
fig = plt.figure("Degree of a random graph", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

'''

ax0 = fig.add_subplot(axgrid[0:3, :])
Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(Gcc, seed=10396953)
nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=20)
nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
ax0.set_title("Connected components of G")
ax0.set_axis_off()
'''

ax1 = fig.add_subplot(axgrid[0:2, :2])
ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Degree Rank Plot")
ax1.set_ylabel("Degree")
ax1.set_xlabel("Rank")
ax1.set_xscale('log')
ax1.set_yscale('log')

ax2 = fig.add_subplot(axgrid[0:2, 2:])
ax2.bar(*np.unique(degree_sequence, return_counts=True))
ax2.set_title("Degree histogram")
ax2.set_xlabel("Degree")
ax2.set_ylabel("# of Nodes")

ax2.set_xscale('log')
ax2.set_yscale('log')

fig.tight_layout()
plt.show()