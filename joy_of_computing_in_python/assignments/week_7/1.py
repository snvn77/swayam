# Unique Element Extractor

# Problem Statement
# Data cleaning pipelines often require the removal of duplicate entries while preserving only unique values.

# You are required to write a Python function as described below.
# unique_elements(L)

# Input
# A list L containing elements of any data type.

# Output
# Return a list containing all unique elements from the list L.

# Notes
# Each element should appear exactly once in the output.
# The order of elements must be the same as their first occurrence in the input list.
# The output must be a list.
# Sets must NOT be used in the final output.

# Example Behaviour (for clarity)
# unique_elements([1,2,2,3]) → [1, 2, 3]
# unique_elements([5,5,5])   → [5]
# unique_elements([])        → []
# unique_elements([1,'a',1]) → [1, 'a']

def unique_elements(L):
  lst = []
  for i in L:
    if i not in lst:
      lst.append(i)
  
  return lst