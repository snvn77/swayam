# Character Frequency Mapper
# Problem Statement
# Text processing systems often analyze strings to study repetition patterns of characters.
# You are required to write a Python function that computes the frequency of each character in a given string.

# Function Specification
# char_frequency(s)

# Input:
# A string s (may be empty).
# The string may contain letters, digits, symbols, or spaces.

# Output:
# Return a dictionary where:
# each key is a character from the string,
# each value is the number of times that character appears in the string.

# Rules and Clarifications
# Character comparison is case-sensitive ('a' and 'A' are different).
# The function must return a dictionary.
# If the input string is empty, return an empty dictionary {}.
# Dictionary keys should appear in the order of first occurrence of characters in the string
# (this matches Python’s dictionary behavior in py3).

# Example Behaviour (for clarity)
# "aab"   → {'a': 2, 'b': 1}
# "abc"   → {'a': 1, 'b': 1, 'c': 1}
# ""      → {}
# "xyx"   → {'x': 2, 'y': 1}


def char_frequency(s):
  d = {}
  for i in s:
    d[i] = s.count(i)
  return d