# Character Reduction Game

# Problem Statement
# You are given two strings through standard input.
# Your task is to remove all common characters between the two strings by applying the following rule:
# If a character appears in both strings, remove one occurrence of that character from each string.
# This process continues until no common characters remain.
# After all possible removals, count the total number of remaining characters in both strings.
# Finally, print this total count.

# Input Format
# First line contains string s1
# Second line contains string s2

# Output Format
# Print a single integer representing the total number of remaining characters

# Constraints
# 1 ≤ length of each string ≤ 10³
# Strings contain only lowercase English letters


s1 = list(input())
s2 = list(input())
s2_ref = s2[:]

for i in s2_ref:
  if i in s1:
    s1.remove(i)
    s2.remove(i)    

print(len(s1)+len(s2))