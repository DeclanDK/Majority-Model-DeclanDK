
import numpy as np
import networkx as nx
import graph_import

def node_update(graph, node_id):
    #print(graph.nodes[node_id])
    blue_neighbors = sum([1 for neighbour_id in graph.neighbors(node_id) if graph.nodes[neighbour_id]["colour"] == 'blue'])
    red_neighbours = sum([1 for neighbour_id in graph.neighbors(node_id) if graph.nodes[neighbour_id]["colour"] == 'red'])

    if blue_neighbors == red_neighbours:
        return str(graph.nodes[node_id]["colour"])
    elif blue_neighbors > red_neighbours:
        return 'blue'
    else:
        return 'red'

def graph_update(old_graph):
    new_graph = old_graph.copy()

    for node_id in new_graph.nodes():
        new_graph.nodes[node_id]["colour"] = node_update(old_graph, node_id)

    return old_graph, new_graph 