# Problem Statement

# You are given a sentence and a list of stopwords through standard input.

# Your task is to remove all occurrences of the stopwords from the given sentence and print the cleaned sentence.
# Words in the sentence are separated by spaces.
# Stopwords are also provided as space-separated words.
# The order of the remaining words must be preserved.
# If a word appears multiple times and is a stopword, all its occurrences must be removed.
# If all words are removed, print an empty line.

# Input Format
# First line contains a sentence consisting of space-separated words
# Second line contains space-separated stopwords

# Output Format
# Print the cleaned sentence after removing all stopwords
# If no words remain, print an empty line

# Constraints
# 0 ≤ number of words in the sentence ≤ 10³
# 0 ≤ number of stopwords ≤ 10³
# All words contain only lowercase English letters

sen = input().strip().split()
sw = input().strip().split()

res = ""
for i in sen:
  if i not in sw:
    res = res+" "+i

print(res.strip(), end = "")