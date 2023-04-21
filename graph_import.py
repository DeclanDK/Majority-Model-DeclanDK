""" Module to import datasets """

""" Libraries necessary to import the graphs """
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

""" Set filepath strings to callable variables """
fb = "./datasets/facebook-links.txt"
sd = "./datasets/soc-Slashdot0902.txt"
tw = "./datasets/twitter_combined.txt"
yt = "./datasets/youtube-links.txt"

""" Function to generate graphs of datasets using networkx """

def gen_graph(ds, n = None):
    if (ds == 'fb'):
        graph = nx.Graph()
    
        # Read in graph from Facebook dataset
        with open(fb, 'rb') as f:
            for line in f:
        
                x, y, _ = line.split()

                graph.add_edge(int(x), int(y))
    
    elif (ds == 'sd'):
          graph = nx.Graph()
        
          # Read in graph from Slashdot dataset
          with open(sd, 'rb') as f:
            for line in f:

                x, y = line.split()

                graph.add_edge(int(x), int(y))

    elif (ds == 'tw'):
        graph = nx.Graph()

        # Read in graph from Twitter dataset
        with open(tw, 'rb') as f:
            for line in f:

                x, y = line.split()

                graph.add_edge(int(x), int(y))

    elif (ds == 'yt'):
        graph = nx.Graph()

        # Read in graph from Youtube dataset
        with open(yt, 'rb') as f:
            for line in f:

                x, y = line.split()

                graph.add_edge(int(x), int(y))
        # Generate a random graph, using n as number of nodes with random edges.
        # If n = None, create graph of n = 100
    elif (ds == 'random'):
        # Make sure n is correctly inputed if a value is given
        if (n != None and type(n) != int):
            raise ValueError("n must be an integer")
        
        # Generate n and m values for random graph

        if n == None:
            n = 100
            m = np.random.randint(1, 4950)
        else:
            m = np.random.randint(1, (n*(n-1)//2))
        
        graph = nx.gnm_random_graph(n, m)

    else:
        raise ValueError("Invalid dataset, must be 'fb', 'sd', 'tw', 'yt' or 'random'")
    
    # Assign colours to graph

    for node_id in graph.nodes():
        colour = 'red' if np.random.rand() < 0.5 else 'blue'
        graph.nodes[node_id]["colour"] = colour 

    return graph

