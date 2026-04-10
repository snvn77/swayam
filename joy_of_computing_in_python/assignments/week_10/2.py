# Pixel Intensity Quantizer

# Problem Statement
# You are given a set of pixel intensity values through standard input.
# Each pixel intensity is an integer between 0 and 255.

# Your task is to group these values into 8 discrete buckets based on the following rule:
# 0–31 → bucket 0
# 32–63 → bucket 1
# 64–95 → bucket 2
# 96–127 → bucket 3
# 128–159 → bucket 4
# 160–191 → bucket 5
# 192–223 → bucket 6
# 224–255 → bucket 7

# For each input value, determine its bucket and print the resulting list.

# Input Format
# First line contains an integer n — number of intensity values
# Second line contains n space-separated integers representing pixel intensities

# Output Format
# Print a list of integers representing the bucket value for each input intensity
# The order of elements must be preserved

# Constraints
# 1 ≤ n ≤ 10⁵
# 0 ≤ intensity value ≤ 255

n = int(input())

p = input().strip().split()

# b = []
# for i in p:
#   if 0<=int(i)<=31:
#     b.append(0)
#   elif 32<=int(i)<=63:
#     b.append(1)
#   elif 64<=int(i)<=95:
#     b.append(2)
#   elif 96<=int(i)<=127:
#     b.append(3)
#   elif 128<=int(i)<=159:
#     b.append(4)
#   elif 160<=int(i)<=191:
#     b.append(5)
#   elif 192<=int(i)<=223:
#     b.append(6)
#   else:
#     b.append(7)

b = [int(i)//32 for i in p]
    
print(b, end="")