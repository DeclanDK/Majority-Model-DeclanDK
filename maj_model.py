import networkx as nx
import numpy as np
import math
import graph_import as gi
import graph_update as gu
import matplotlib.pyplot as plt 
import marketer

# Input: Graph
# Output: Stabilised Graph after running majority model

def maj_mod(G, adv = False, k = 5):
    if adv:
        G = marketer.greedy_adversary(G, k)

    old_G, new_G = gu.graph_update(G)
    iter = 1
    while True:
        older_G = old_G 

        old_G, new_G = gu.graph_update(G)
        iter += 1

        if nx.is_isomorphic(old_G, new_G,):
            print("Stab - # of Rounds: ", iter)
            return new_G
        
        elif nx.is_isomorphic(older_G, new_G):
            print("Alternating - # of Rounds: ", iter)
            return new_G