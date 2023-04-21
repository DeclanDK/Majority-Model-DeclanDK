import networkx as nx
import numpy as np
import math
import graph_import as gi
import maj_model as mm
import matplotlib.pyplot as plt 

x_axis = [5,6,7,8,9]
y_axis = []

for k in range(5,10):
    count = 0
    for i in range(20):
        graph = gi.gen_graph('random', 1000)

        fin_graph = mm.maj_mod(graph, adv = True, k = k)

        # Add the final number  of blue nodes to the count variable
        count += sum([1 for node_id in fin_graph.nodes if fin_graph.nodes[node_id]["colour"] == 'blue'])

    y_axis.append(count//20)

plt.figure(figsize=(15,15))

ax = plt.axes()

plt.plot(x_axis, y_axis,'bo')
plt.xlabel("Budget - k")
plt.ylabel("Final # of Blue Nodes")
        
plt.title("Scatter plot")

plt.show()

#graph = gi.gen_graph('fb', 100)

#print("Number of Nodes: ", graph.order())
#print("Number of Edges: ", graph.number_of_edges())

#fin_graph = mm.maj_mod(graph, adv = True, k= 5)

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
