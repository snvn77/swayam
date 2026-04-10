# Understanding PageRank Through Code-Based Simulation

# In the lectures, we discussed a Python program that simulates a simplified version of the PageRank algorithm using point distribution. The program creates a directed graph, assigns points to nodes, redistributes those points according to outgoing edges, and compares the results with NetworkX’s built-in PageRank function.

# 1. Graph Creation
# A directed graph (DiGraph) with 10 nodes (numbered 0 to 9) is created using NetworkX.

# 2. Random Edge Generation
# The function responsible for adding edges loops over all pairs of distinct nodes (s, t) and adds a directed edge from s to t with a 50% probability. Self-loops are avoided by checking that s != t.

import random
import networkx as nx
import matplotlib.pyplot as plt


def create_graph(n=10, prob=0.5): # We are creating 10 node bi-directional graph and using 0.5 so that the edges are neither too dense nor too sparse
    G = nx.DiGraph()
    G.add_nodes_from(range(n))

    # 2. Random Edge Generation
    for s in range(n):
        for t in range(n):
            # Avoiding self loops and
            # also random.random gives values 0-1. So there is 50% chance of getting '< prob' which is 0.5. It can also be '> prob' only if it is 0.5
            if s != t and random.random() < prob:                 
                G.add_edge(s, t)

    return G



# 3. Initial Point Assignment
# Every node starts with 100 points. These points are stored in a list where the index corresponds to the node number.

# 4. Point Distribution Logic
# During redistribution:

# If a node has no outgoing edges, it keeps all its points.
# If a node has outgoing edges, its points are split equally among them.

# 5. Iterative Redistribution
# The program repeatedly redistributes points over multiple rounds. After each round, the new distribution is printed. The user can stop the process by typing #.



def distribute_points(G, points): # Similar to assignment 2 in week_12
    n = len(points)
    new_points = [0.0] * n

    for node in G.nodes:
        outgoing = list(G.successors(node))

        if not outgoing:
            # No outgoing edges → keep points
            new_points[node] += points[node]
        else:
            share = points[node] / len(outgoing)
            for neighbor in outgoing:
                new_points[neighbor] += share

    return new_points


def simulate(G, max_iter=20):
    n = len(G.nodes)
    points = [100.0] * n  # Initial points

    print("\nInitial Points:")
    print(points)

    for i in range(max_iter):
        user_input = input(f"\nPress Enter for iteration {i+1} (or # to stop): ")
        if user_input.strip() == "#":
            break

        points = distribute_points(G, points)
        print(f"After iteration {i+1}:")
        print([round(p, 2) for p in points])

    return points



# 6. Graph Visualization
# The graph structure, including nodes and edges, is displayed using matplotlib.

def visualize_graph(G):
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G) # Location of each node
    nx.draw(G, pos, with_labels=True, node_size=800)
    plt.title("Directed Graph")
    plt.show()


# 7. Ranking Nodes by Points
# At the end, a ranking function stores final points in a dictionary {node: points} and sorts them in ascending order to find which nodes have the lowest and highest scores.

def rank_nodes(points):
    score_dict = {i: p for i, p in enumerate(points)}
    ranked = sorted(score_dict.items(), key=lambda x: x[1])

    print("\nNode Ranking (Low → High):")
    for node, score in ranked:
        print(f"Node {node}: {round(score, 4)}")

    return ranked


# 8. Comparison with PageRank
# The program also calls NetworkX’s built-in pagerank() function to compute the official PageRank values for the same graph and prints them for comparison with the manual simulation.

def compare_with_pagerank(G):
    pr = nx.pagerank(G)

    print("\nNetworkX PageRank:")
    for node, score in sorted(pr.items(), key=lambda x: x[1]):
        print(f"Node {node}: {round(score, 6)}")


# This simulation helps visualize how importance flows through a network and how PageRank emerges as a stable distribution of scores when point redistribution is repeated many times.


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    G = create_graph(n=10, prob=0.5)

    final_points = simulate(G, max_iter=20)

    rank_nodes(final_points)

    visualize_graph(G)

    compare_with_pagerank(G)



# 1) Why is a directed graph mandatory for implementing PageRank in the given code?

# Because PageRank depends on the direction of influence between nodes       (Right Answer)
# Because undirected graphs cannot be read from files
# Because NetworkX only supports directed graphs
# Because visualization requires arrows

# 2) Why are all nodes initially assigned equal points before distribution begins?

# To speed up execution
# To remove any initial bias in importance      (Right Answer)
# To match NetworkX’s internal implementation
# To simplify graph drawing

# 3) If a node has many outgoing edges, how does it affect its contribution?

# It gains more points
# It distributes more total points
# Its influence is divided among its neighbors      (Right Answer)
# It stops participating after one iteration

# 4) Why does the case study include a manual Excel-style simulation?

# To replace Python computation
# To compute final PageRank values
# To reduce graph complexity
# To help visualize a single iteration clearly       (Right Answer)

# 5) Why is the PageRank process iterative?

# Because sorting requires multiple passes
# Because convergence happens gradually       (Right Answer)
# Because graph size keeps changing
# Because visualization depends on iteration count

# 6) What is the main purpose of converting the points list into a dictionary?

# To improve numerical accuracy
# To reduce memory usage
# To speed up sorting
# To preserve node–score association       (Right Answer)

# 7) Which type of node can create issues in PageRank distribution?

# Nodes with self-loops
# Nodes with no incoming edges
# Nodes with no outgoing edges       (Right Answer)
# Nodes with high degree

# 8) Why is sorting performed after computing final point values?

# To normalize the graph
# To rank nodes by importance      (Right Answer)
# To check convergence
# To reduce floating-point error

# 9) What happens if the user stops the iteration process too early?

# Results remain accurate
# Values become random
# Convergence still occurs
# Rankings may be misleading       (Right Answer)

# 10) Why is nx.pagerank() used at the end of the case study?

# To replace the manual approach
# To speed up execution
# To visualize the graph
# To validate the conceptual simulation      (Right Answer)

# 11) What property of PageRank guarantees reliable results?

# Use of sorting
# Deterministic initialization
# Mathematical convergence       (Right Answer)
# Absence of cycles

# 12) Which factor most strongly increases a node’s PageRank score?

# Number of outgoing edges
# Random initialization
# Links from already important nodes      (Right Answer)
# Graph visualization

# 13) Why is a random graph generated in the later part of the code?

# To replace real datasets
# To test scalability and behavior       (Right Answer)
# To guarantee convergence
# To reduce computation time

# 14) Why does PageRank still work even if initial points are changed?

# Because initial values are ignored
# Because points are normalized instantly
# Because sorting removes bias
# Because the algorithm converges to the same distribution       (Right Answer)

# 15) Which statement best summarizes the PageRank idea demonstrated in the casestudy?

# Popular nodes are those with many outgoing edges
# Importance is random but stabilizes
# Every node eventually gets qual rank
# A node is important if the important nodes point to it       (Right Answer)