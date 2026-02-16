# Student Performance Analyzer
# Ravi is a Teaching Assistant who is preparing a small Python utility to analyze student scores collected from a programming lab. The data comes in raw lists, but the final processed results must be immutable, so Ravi uses tuples.

# Step 1: Raw Student Marks (List)
# Ravi starts with a list of marks obtained by students:
marks = [35,78,92,45,60,88,49,100]
# This list is mutable, meaning values can change.

# Step 2: Filtering Passed Students (List Comprehension)
# Only students scoring 50 or more are considered passed. 
passed = [m for m in marks if m>=50]
# The expression m for m in marks generates values
# The condition if m >= 50 filters values
# The result is a new list, not modifying the original
# Result:
# passed = [78, 92, 60, 88, 100]

# Step 3: Adding Bonus Marks (List Comprehension)
# Each passed student gets 5 bonus marks, but the total should not exceed 100.
bonus_marks = [min(m+5,100) for m in passed]
# min(m + 5, 100) ensures marks do not exceed 100
# This still produces a list
# Result:
# bonus_marks = [83, 97, 65, 93, 100]

# Step 4: Converting List to Tuple
# Ravi wants to freeze the final results so they cannot be changed accidentally
final_scores = tuple(bonus_marks)
# Result:
# final_scores = (83, 97, 65, 93, 100)

# Step 5: Creating Score–Index Pairs :
# Ravi now wants to tag each score with its index position. 
indexed_scores = [(i, final_scores[i]) for i in range(len(final_scores))]
# Result:
# indexed_scores = [(0, 83), (1, 97), (2, 65), (3, 93), (4, 100)]
# Each element is a tuple inside a list.


# What is the value of passed?
marks = [35,78,92,45,60,88,49,100]
passes = [m for m in marks if m>=50]
#  [35, 78, 92, 45, 60, 88, 49, 100]
#  [78, 92, 60, 88, 100]  (Right Answer)
#  (78, 92, 60, 88, 100) 
#  [50, 60, 88, 100]

# What does bonus_marks contain?
passed = [78, 92, 60, 88, 100]
bonus_marks = [min(m+5,100) for m in marks]
#  [83, 97, 65, 93, 105]
#  [78, 92, 60, 88, 100]
#  [83, 97, 65, 93, 100]   (Right Answer)
#  (83, 97, 65, 93, 100)

# What is the type of final_scores?
final_scores = tuple(bonus_marks)
#  List
#  Set
#  Dictionary
#  Tuple    (Right Answer)

# What is the output of:
indexed_scores = [(i, final_scores[i]) for i in range(len(final_scores))]
print(indexed_scores[2])
#  (2, 97) 
#  (1, 97)
#  (2, 65)   (Right Answer)
#  65

# What happens if the following line is executed?
final_scores[0] = 90
#  The value updates successfully
#  The tuple converts into a list
#  A runtime error occurs     (Right Answer)
#  Only the first element changes