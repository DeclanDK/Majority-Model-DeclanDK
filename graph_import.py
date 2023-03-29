"""Module to import datasets"""

"""Libraries necessary to import the graphs"""
import networkx as nx

""" Set filepath strings to callable variables """
fb = "./datasets/facebook-links.txt"
sd = "./datasets/soc-Slashdot0902.txt"
tw = "./datasets/twitter_combined.txt"
yt = "./datasets/youtube-links.txt"

""" Function to generate graphs of datasets using networkx """

def gen_graph(ds):
    if (ds == 'fb'):
        graph = nx.Graph()
    
        # Read in graph from Facebook dataset
        with open(fb, 'rb') as f:
            for line in f:
        
                x, y, _ = line.split()

                graph.add_edge(int(x), int(y))
        return graph
    
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

    else:
        raise ValueError("Invalid dataset, must be 'fb', 'sd', 'tw' or 'yt'")
    
    return graph

