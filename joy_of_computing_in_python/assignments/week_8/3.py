# Problem Statement: Longest Common Prefix

# You are given N strings.
# Your task is to find the longest common prefix shared among all the given strings.

# A prefix is a sequence of characters that appears at the beginning of each string.
# If no common prefix exists, print an empty string "".

#  Input Format (Corrected)
# First line contains an integer N — the number of strings
# The next N lines each contain one string

# Output Format
# Print the longest common prefix
# If no common prefix exists, print an empty string ""

# Constraints
# 1 ≤ N ≤ 200
# 1 ≤ length of each string ≤ 200
# Strings contain only lowercase English letters


n = int(input().strip())

s = []
for i in range(n):
  k = input().strip()
  s.append(k)
  
def equality_check(ind,n,s):
  for j in range(1,n):
    if ind>=len(s[j]) or s[j][ind] != s[0][ind]:
      return False
  return True

p = ""
for i in range(len(s[0])):
  c = equality_check(i,n,s)
  if c:
    p+=s[0][i]
  else:
    break

if p:
  print(p, end="")
else:
  print('""', end="")