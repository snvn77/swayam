# Score Conservation Checker

# You are given a directed graph and an initial score for each node through standard input.
# Your task is to perform one step of influence distribution using the same rules as Problem 1, and then check whether the total influence is conserved.

# Rules for influence distribution:
# If a node has outgoing edges, it splits its score equally among its outgoing neighbors.
# If a node has no outgoing edges, it keeps its entire score.
# All incoming influence is accumulated.

# After performing one distribution step:
# Compute the sum of all node scores before distribution
# Compute the sum of all node scores after distribution
# Print True if the total score is conserved, otherwise print False

# Input Format
# First line contains integer N — number of nodes

# Next N lines:
# Node followed by outgoing neighbors

# Next N lines:
# Node followed by its score

# Output Format
# Print True if total score before and after distribution is the same
# Otherwise, print False



from fractions import Fraction

# Inputs
n = int(input())

nodes = {}
for i in range(n):
    s=input()
    s_list = s[2:].split()
    nodes[int(s[0])]=[int(j) for j in s_list]

scores_1 = {}
for i in range(n):
    s = input()
    scores_1[int(s[0])] = int(s[2:])

# Total scores before distribution 
total_scores_1 = sum(scores_1.values())

# New dictionary for scores after distribution
scores_2 = {key:0 for key in scores_1.keys()}

# Distributing the score
for key, value in nodes.items():
    if value:
        for i in value:
            scores_2[i] += Fraction(scores_1[key],len(value))
    else:
        scores_2[key] += scores_1[key]

# Total score after distribution
total_scores_2 = sum(scores_2.values())

# Checking if the total scores remain same
if total_scores_1==total_scores_2:
    print("True",end="")
else:
    print("False", end="")