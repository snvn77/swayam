# Problem Statement: Valid Anagram

# You are given two strings s and t.
# Your task is to determine whether string t is an anagram of string s.

# Two strings are anagrams if:
# They contain the same characters
# Each character appears the same number of times in both strings
# The order of characters does not matter

# If t is an anagram of s, print true.
# Otherwise, print false.

# Input Format
# First line contains string s
# Second line contains string t

# Output Format
# Print true if t is an anagram of s
# Print false otherwise

# Constraints
# 1 ≤ length of s, t ≤ 5 × 10⁴
# Strings contain only lowercase English letters


s = input()
t = input()

s_set = set(s)
t_set = set(t)

if s_set == t_set and len(s) == len(t):
  for i in s_set:
    if s.count(i) != t.count(i):
      print('false', end = "")
      break
    else:
      continue
  
  print('true', end = "")
  
else:
  print('false', end = "")