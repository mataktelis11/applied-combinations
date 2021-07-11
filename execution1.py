import cliques
import randgraph
import networkx as nx
import matplotlib.pyplot as plt

#### USER INPUT ######
n = 20
k = 20
#####################




# create a random graph
G = nx.Graph()
G.add_nodes_from(list(range(1, n+1)))
G.add_edges_from(randgraph.createRandomGraph(n, k))

# find all cliques
cliques.findAllCliques(G)

# display the graph
plt.rcParams['toolbar'] = 'None'
nx.draw_networkx(G)
plt.show()


