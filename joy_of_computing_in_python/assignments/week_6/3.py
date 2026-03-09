# Recursive Minimum Finder

# Problem Statement
# Recursive algorithms are often used to process lists when iteration is restricted.
# You are required to write a Python function as described below.

# recursive_min(L)

# Input:
# A non-empty list of integers L.

# Output:
# Return the minimum element present in the list.

# Notes:
# The solution must use recursion.
# Loops must NOT be used.
# The built-in min() function must NOT be used.

def recursive_min(L):
  if len(L)==1:
    return L[0]
  else:
    if L[-1]>L[-2]:
      return recursive_min(L[:len(L)-1])
    else:
      L[-1],L[-2] = L[-2],L[-1]
      return  recursive_min(L[:len(L)-1])