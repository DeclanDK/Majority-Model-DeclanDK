# Greedy Adversarial function trying to make blue win 
def greedy_adversary(G, k):
    red_nodes = [(node, degree) for node, degree in G.degree if G.nodes[node]["colour"] == 'red' ]

    # Get the k highest-degree red nodes from G
    red_sorted_nodes = sorted(red_nodes, key = lambda x : x[1], reverse = True)[:k]
    #for node in sorted_nodes:
    #    print(node)

    for node, _ in red_sorted_nodes:
        G.nodes[node]["colour"] = 'blue'

    return G  