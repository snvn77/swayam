# Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
# You may define additional auxiliary functions as needed.


# Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number. For instance:
# >>> remdup([3,1,3,5])
# [3, 1, 5]
# >>> remdup([7,3,-1,-5])
# [7, 3, -1, -5]
# >>> remdup([3,5,7,5,3,7,10])
# [3, 5, 7, 10]


# Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.
# Here are some examples to show how your function should work.
# >>> sumsquare([1,3,5])
# [35, 0]
# >>> sumsquare([2,4,6])
# [0, 56]
# >>> sumsquare([-1,-2,3,7])
# [59, 4]


# A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix
# 1  2  3  4
# 5  6  7  8
# would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].
# The transpose of a matrix converts each row into a column. The transpose of the matrix above is:
# 1  5
# 2  6
# 3  7
# 4  8
# which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].
# Write a Python function transpose(m) that takes as input a two dimensional matrix m and returns the transpose of m. The argument m should remain undisturbed by the function.
# Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.
# >>> transpose([[1,2,3],[4,5,6]])
# [[1, 4], [2, 5], [3, 6]]
# >>> transpose([[1],[2],[3]])
# [[1, 2, 3]]
# >>> transpose([[3]])
# [[3]]



# Private Test cases used for evaluation	           Input	                 Expected Output
# Test Case 1	                            remdup([5,5,5,5,1,1,5,5,5])             [5, 1]
# Test Case 2	                                 remdup([8,6,4,6,8])               [8, 6, 4]
# Test Case 3	                                     remdup([5])                      [5]
# Test Case 4	                                     remdup([])                       []
# Test Case 5	                               sumsquare([1,2,3,4,5,6])            [35, 56]
# Test Case 6	                          sumsquare([1,4,9,16,25,36,49,64])       [3108, 5664]
# Test Case 7	                           sumsquare([0,1,-1,0,2,-2,3,-3])           [20, 8]
# Test Case 8	                        transpose([[1,2,3],[4,5,6],[7,8,9]])    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# Test Case 9	                                 transpose([[1,2,3,4]])        [[1], [2], [3], [4]]
# Test Case 10	                       transpose([[1,0,0],[0,1,0],[0,0,1]])    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]




def remdup(l):
  r = []
  for i in l:
    if i not in r:
      r.append(i)      
  return r

def sumsquare(l):
  even = 0
  odd = 0
  for i in l:
    if i%2==0:
      even+=i*i
    else:
      odd+=i*i
  return [odd, even]

def transpose(l):
  t=[]
  for j in range(len(l[0])):
    e=[]
    for i in l:
      e.append(i[j])
    t.append(e)
  return t