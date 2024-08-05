import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
nodes = [0, 1, 2, 3, 4]
G.add_nodes_from(nodes)

# Add edges
edges = [(0, 1), (1, 2), (1, 3), (1, 4), (3, 4)]
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='green', node_size=1000, font_color='white', font_size=15)
plt.show()
