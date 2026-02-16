# The Shortest Codeword of Lexicon City
# Problem Statement
# In Lexicon City, encrypted messages are stored as comma-separated words.You are required to identify a special word based on the following rules:
# Accept a comma-separated list of words as input.
# Find the word with the minimum length.
# If multiple words share the same minimum length, print the rightmost such word.

# Input Format
# A single line containing comma-separated words.

# Output Format
# Print the required word.

# Private Test cases used for evaluation	    Input	   Expected Output
# Test Case 1	                                x,y,z             z
# Test Case 2	                            red,blue,green       red
# Test Case 3	                              one,two,ten        ten

l_str = input().split(',')

# l_len = []
# for i in l_str:
#   l_len.append(len(i))

# least = min(l_len)
# for i in range(len(l_len)-1,-1,-1):
#   if l_len[i]==least:
#     print(l_str[i])
#     break

short = l_str[0]
least = len(l_str[0])
for word in l_str:
    if len(word.strip())<=least:
        least = len(word.strip())
        short = word.strip()

print(short)
