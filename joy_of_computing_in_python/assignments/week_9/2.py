# Word Length Distribution Analyzer

# Problem Statement
# You are given a line of text through standard input.
# The text consists of words separated by spaces.
# Your task is to analyze the text and determine how many words occur for each word length.
# The length of a word is the number of characters it contains.

# Words are separated by one or more spaces.
# The result should show how many words exist for each length.

# Input Format
# A single line containing space-separated words

# Output Format
# Print a dictionary where:
# Key → word length
# Value → number of words of that length

# Constraints
# 1 ≤ number of words ≤ 10³
# Each word contains only lowercase English letters


dict = {}
s = input().strip().split()

for i in s:
  if len(i) not in dict:
    dict[len(i)] = 1
  else:
    dict[len(i)]+=1
    
print(dict, end="")