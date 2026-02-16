# When One List Becomes Many (But Isn’t)

# Context
# Ravi is maintaining student records in Python. Each record is stored as a list, and sometimes a list even contains another list (nested list). Ravi assumes that assigning one list to another creates a new copy. What actually happens surprises him.
# This case study walks through Ravi’s understanding step by step.

# Part 1: List Assignment — No Copy at All
# Ravi starts with a list of marks. 
marks = [70,80,90]
backup = marks
# Ravi thinks backup is a separate list.
# Now he modifies backup:  
backup[0] = 100
print(backup)
print(marks)
# What Actually Happens
# marks and backup refer to the same list
# No new list is created
# Any change through one name affects the other
# Output
# [100, 80, 90]
# [100, 80, 90]
# Key Insight:
# List assignment copies the reference, not the data.

# Part 2: Shallow Copy — New List, Same Inner Objects
# Ravi now learns about the copy() method.
marks = [[78,80],[90,95]]
backup = marks.copy()
# This time, Ravi updates an inner list:
backup[0][0] = 100
print(backup)
print(marks)
# What Happens Now
# marks and backup are different outer lists
# BUT the inner lists are shared
# Modifying a nested list affects both
# Output :
# [[100, 80], [90, 95]]
# [[100, 80], [90, 95]]
# Key Insight:
# Shallow copy copies the outer list only, not nested lists.

# Shallow Copy with Slice Notation
marks = [[1,2],[3,4]]
backup = marks[:]
backup[1][1]= 99

print(backup)
print(marks)
# Output :
# [[1, 2], [3, 99]]
# [[1, 2], [3, 99]]

# Deep Copy — Complete Independence
# Ravi now wants a fully independent copy.
import copy
marks = [[78,80],[90,95]]
backup = copy.deepcopy(marks)
# He modifies the nested list:  
backup[0][0] = 100
print(backup)
print(marks)
# What Happens Now
# Outer list is copied
# Inner lists are copied
# Changes do not affect the original
# Output:
# [[70, 80], [90, 95]]
# [[100, 80], [90, 95]]


# What will be printed?
a = [10,20,30]
b = a
b.append(40)
print(a)
#  [10, 20, 30]
#  [10, 20, 30, 40]   (Right Answer)
#  Error
#  [40]

# Choose the correct output.
a = [1,2,3]
b = a.copy()
b[0] = 99
print(a)
#  [1, 99, 3]
#  [99, 2, 3]
#  [1, 2, 3]    (Right Answer) 
#  Error

# What is printed?  
a = [[1,2],[3,4]]
b = a.copy()
b[0][1] = 99
print(a)
#  Error
#  [[1, 2], [3, 4]]
#  [[1, 2], [3, 99]]
#  [[1, 99], [3, 4]]   (Right Answer)

# Predict the output.
a = [[5,6],[7,8]]
b = a[:]
b[1] = [0,0]
print(a)
#  Error
#  [[5, 6], [7, 8]]     (Right Answer)
#  [[5, 6], [0, 0]]
#  [[0, 0], [7, 8]]

# Select the correct output.
a = [[5,6],[7,8]]
b = a[:]
b[1][0] = 100
print(a)
#  [[5, 6], [7, 8]]
#  Error
#  [[100, 6], [7, 8]]
#  [[5, 6], [100, 8]]     (Right Answer)

# Select the correct output.
import copy
a = [[1,2],[3,4]]
b = copy.deepcopy(a)
b[0][0] = 9
print(a)
#  [[9, 2], [3, 4]]
#  Error
#  [[1, 2], [3, 4]]    (Right Answer) 
#  [[1, 9], [3, 4]]

# What is the final output?
a = [[1,2],[3,4]]
b = a
c = a.copy()
d = copy.deepcopy(a)

b[0][0] = 10
c[1][1] = 20
d[0][1] = 30

print(a)
#  [[10, 30], [3, 20]]
#  [[10, 2], [3, 4]]
#  [[1, 2], [3, 4]]
#  [[10, 2], [3, 20]]   (Right Answer)