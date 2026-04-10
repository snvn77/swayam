# Circular Elimination Game

# Problem Statement
# You are given a group of players arranged in a circle.
# Starting from the first player, every k-th player is eliminated in a circular manner.
# The elimination continues until only one player remains.

# Your task is to simulate this process using the given inputs and determine the position (1-indexed) of the last remaining player.

# Input Format
# First line contains an integer n — the number of players
# Second line contains an integer k — the step count for elimination

# Output Format
# Print a single integer representing the position of the last remaining player

# Constraints
# 1 ≤ n ≤ 10⁵
# 1 ≤ k ≤ 10⁵

# Inputs
n = int(input()) # No. of players
k = int(input()) # Step count for eliminations

N = list(range(1,n+1)) # List for number of players

p = 0 # Pointer

# Loop for continuous elimnation until one player is left
while len(N)>1:
  p = (p+(k-1))%len(N) # (k-1) Since it is 0 indexed; %len(N) to loop over the present no. of players 
  eliminate = N.pop(p) # Elimination
  
print(N[0],end="") # print player position; end argument to avoid presentation error