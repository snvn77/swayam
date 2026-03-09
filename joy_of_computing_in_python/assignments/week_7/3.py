# Common Element Finder

# Problem Statement
# In data analysis, it is often necessary to identify elements that are common between two datasets.

# You are required to write a Python function that finds the common elements between two lists.
# common_elements(L1, L2)

# Input
# Two lists L1 and L2 containing elements of any data type.

# Output
# Return a list containing elements that are common to both lists.

# Notes
# Each common element should appear exactly once in the output.
# The order of elements in the output list must follow the order of first appearance in L1.
# The output must be a list.
# Sets must NOT be used in the final output.


# Example Behaviour (for clarity)
# common_elements([1,2,3],[2,3,4]) → [2, 3]
# common_elements([5,6],[7,8])     → []
# common_elements([1,1,2],[1,2,2]) → [1, 2]

def common_elements(L1,L2):
  L = []
  for i in L1:
    if (i in L2) and (i not in L):
      L.append(i)
  return L