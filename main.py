import networkx as nx
import numpy as np
import math
import graph_import


def main():
    # Import fb graph
    graph = graph_import.gen_graph('yt')

    print("Number of Nodes: ", graph.order())
    print("Number of Edges: ", graph.number_of_edges())

    return "hello"

string = main()
print("hello world")