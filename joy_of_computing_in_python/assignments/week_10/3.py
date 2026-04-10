# Automated Message Counter

# Problem Statement
# You are given a collection of text messages and a keyword through standard input.
# Your task is to count how many messages contain the given keyword as a substring.
# A message is counted if the keyword appears anywhere inside it.
# Matching is case-sensitive.
# Each message is checked independently.
# Finally, print the total count.

# Input Format
# First line contains an integer n — number of messages
# Next n lines each contain one message (string)
# Last line contains the keyword

# Output Format
# Print a single integer representing the number of messages that contain the keyword

# Constraints
# 1 ≤ n ≤ 10³
# Each message contains printable characters
# Keyword is a non-empty string

n = int(input())

msgs = [input() for _ in range(n)]

key_word = input()

msg_count = [1 if key_word in msg else 0 for msg in msgs]

print(sum(msg_count), end = "")