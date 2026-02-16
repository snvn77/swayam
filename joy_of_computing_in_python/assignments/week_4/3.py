# Problem Statement
# Data validation systems often need to detect duplicate values in datasets to ensure data integrity.

# Write a function has_duplicates(L) that:
# - Accepts a list L
# - Returns True if any element appears more than once
# - Returns False if all elements are unique

# Constraints:
# - L may be empty
# - Elements can be integers or strings


def has_duplicates(L):
  if L:
    d = []
    for i in L:
      if i in d:
        return True
      else:
        d.append(i)
    return False
  else:
    return False