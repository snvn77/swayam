# Exploring Social Networks Using Shortest Paths

# Background

# A data analyst is interested in understanding how people are connected within a large online social network. To do this, the analyst works 
# with a real-world dataset representing friendships between users on a social media platform. Each user is modeled as a node, and each 
# friendship is modeled as an edge in a graph.

# The analyst chooses NetworkX, a Python library designed for creating, analyzing, and studying complex networks, to perform this analysis.

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Problem Context

# One of the most well-known ideas in social network analysis is the Six Degrees of Separation theory, which suggests that any person on 
# Earth is connected to any other person through a chain of no more than five or six acquaintances. Also known as the "small-world 
# experiment" or "six handshakes rule," this concept suggests a highly connected global network where the average path length between 
# strangers is surprisingly short.

# The analyst wants to verify whether this idea holds for the given social network dataset by answering the following questions:
# How closely connected are users on average?
# What is the shortest possible connection between any two users?
# What is the longest shortest path observed in the network?
# Does the network show properties that support the idea of six degrees of separation? 

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Data Description
# The dataset is stored in a text file (facebook_combined.txt).
# Each line represents a friendship between two users.
# The graph is undirected, meaning friendships work both ways.

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Analytical Approach

# Using the provided code, the analyst performs the following steps:

# 1. Network Construction
#        o The dataset is read and converted into a graph structure.
#        o All users (nodes) are extracted for analysis.

# 2. Shortest Path Computation
# 	o For every pair of distinct users, the shortest path length is calculated.
# 	o These values represent the minimum number of connections required to move from one user to another.

# 3. Statistical Analysis of Paths 
# 	o All shortest path lengths are stored.
# 	o The minimum, maximum, and average shortest path lengths are computed.

# 4. Interpretation of Results
#         o The minimum shortest path shows the closest possible connection between any two users.
#         o The maximum shortest path indicates the farthest distance between two users while still remaining connected.
#         o The average shortest path length serves as the most important metric for validating the Six Degrees of Separation theory.

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Key Observations
# If the average shortest path length is close to 6 (or lower), it supports the idea that people in the network are closely connected.
# A relatively small maximum shortest path length suggests that even the most distant users are not too far apart.
# These findings highlight how social networks enable rapid connectivity through indirect relationships. 

# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Conceptual Insights
# Six Degrees of Separation: The experiment demonstrates how short paths emerge naturally in large social networks.
# Exponential Growth of Connections: As each user has multiple friends, and each friend has their own friends, the number of reachable users grows exponentially with each step.
# Graph Theory in Practice: Abstract concepts like nodes, edges, and shortest paths directly translate into real-world social phenomena.

import networkx as nx

G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes)

shortest_path_length_list = []
for i in N:
    for j in N:
        if i!=j:
            l = nx.shortest_path_length(G, source=i, target=j)
            print(f"The shortest path length between {i} and {j} is: {l}")
            shortest_path_length_list.append(l)

print(f"The minimum shortest path length: {min(shortest_path_length_list)}")
print(f"The average shortest path length: {sum(shortest_path_length_list)/len(shortest_path_length_list)}")
print(f"The maximum shortest path length: {max(shortest_path_length_list)}")






# What is the primary purpose of using nx.read_edgelist("facebook_combined.txt") in the case study?
#  To create a graph where users are nodes and friendships are edges        (Right Answer)
#  To calculate shortest paths directly from the file
#  To store shortest path lengths in a list
#  To visualize the social network


# Why does the code check if u != v before computing the shortest path?
#  To prevent duplicate edges in the graph
#  To avoid self-loops that always have zero path length        (Right Answer)
#  To reduce memory usage
#  To ensure the graph remains undirected


# What does the list shortest_path_length_list primarily represent?
#  The degree of each node
#  The number of friends per user
#  All shortest path lengths between distinct pairs of nodes        (Right Answer)
#  Only the longest path in the network


# Which metric from the code is most relevant for validating the Six Degrees of Separation concept?
#  Minimum shortest path length
#  Maximum shortest path length
#  Number of nodes in the graph
#  Average shortest path length        (Right Answer)


# If the network is fully connected, what would most likely happen to the maximum shortest path length?
#  It would increase significantly
#  It would become zero
#  It would remain relatively small       (Right Answer)
#  It would become equal to the number of nodes


# Why does the case study mention exponential growth in connections?
#  Because shortest path lengths grow exponentially
#  Because the number of nodes doubles each iteration
#  Because friend-of-friend connections expand rapidly with each step        (Right Answer)
#  Because NetworkX uses exponential algorithms internally


# What is a computational limitation of the approach used in the code?
#  It cannot handle undirected graphs
#  It only works for weighted graphs
#  It ignores isolated nodes
#  It computes shortest paths for every node pair, which is expensive       (Right Answer)