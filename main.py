import networkx as nx
import numpy as np
import math
import graph_import as gi
import maj_model as mm
import matplotlib.pyplot as plt 

graph = gi.gen_graph('random', 100)

print("Number of Nodes: ", graph.order())
print("Number of Edges: ", graph.number_of_edges())

fin_graph = mm.maj_mod(graph, adv = True)

# Draw graphs
# fig, axs = plt.subplots(ncols=2)
# colours1 = [graph.nodes[node_id]["colour"] for node_id in graph.nodes()]
# nx.draw(graph, ax = axs[0], with_labels = True, node_color = colours1)

# colours2 = [fin_graph.nodes[node_id]["colour"] for node_id in fin_graph.nodes()]
# nx.draw(fin_graph, ax = axs[1], with_labels = True, node_color = colours2)

# # #print("1st Iter")
# # #print("Blue nodes: ", sum([1 for node_id in graph.nodes() if graph.nodes[node_id]['colour'] == 'blue']))
# # #print("Red nodes: ", sum([1 for node_id in graph.nodes() if graph.nodes[node_id]['colour'] == 'red']))

# # #print("2nd Iter")
# # #print("Blue nodes: ", sum([1 for node_id in graph2.nodes() if graph2.nodes[node_id]['colour'] == 'blue']))
# # #print("Red nodes: ", sum([1 for node_id in graph2.nodes() if graph2.nodes[node_id]['colour'] == 'red']))
# plt.show()
