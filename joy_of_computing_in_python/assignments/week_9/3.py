# Graph Degree Analyzer
# Problem Statement
# You are given a graph through standard input.

# The graph is represented using adjacency information, where each node is followed by the nodes it is directly connected to.
# Your task is to compute the degree of each node.
# The degree of a node is the number of nodes directly connected to it.
# If a node has no adjacent nodes, its degree is 0.
# If a node has a self-loop (connected to itself), it is counted as one connection.

# Input Format
# First line contains an integer N — the number of nodes

# The next N lines contain:
# First value → node label
# Remaining values → adjacent nodes (space-separated)
# If a node has no neighbors, the line contains only the node label

# Output Format
# Print a dictionary where:

# Key → node
# Value → degree of that node

# Constraints
# 1 ≤ N ≤ 10³
# Node labels may be integers or lowercase letters

n = int(input().strip())

i_list = []
for _ in range(n):
  i = input().strip().split()
  i_list.append(i)

res = {}
for i in i_list:
  res[i[0]] = len(i) - 1
  
print(res, end = "")