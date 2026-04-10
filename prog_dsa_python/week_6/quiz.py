# Quiz

# All questions carry equal weightage. All Python code is assumed to be executed using Python3. You may submit as many times as you like within the deadline. Your final submission will be graded.

# Note:
# If the question asks about a value of type string, remember to enclose your answer in single or double quotes.
# If the question asks about a value of type list, remember to enclose your answer in square brackets and use commas to separate list items.



# Suppose u and v both denote sets in Python. Under what condition can we guarantee that u-(v-u) == u?
#  The sets u and v should be disjoint.
#  The set u should be a subset of the set v
#  The set v should be a subset of the set u
#  This is true for any u and v.

# Feedback:
# v-u has no elements from u, so u-(v-u) removes nothing from u and is hence always equal to u.
# Accepted Answers:
# This is true for any u and v.




# Suppose u and v both denote sets in Python. and u|v != u^v. What can we conclude about u and v?
#  The sets u and v should overlap.
#  The set v should be a subset of the set u.
#  The set u should be a subset of the set v.
#  This is true for any u and v.

# Feedback:
# If the two sets were disjoint, we would have u|v == u^v. Since the two expressoins are not equal, it must be that the sets overlap.
# Accepted Answers:
# The sets u and v should overlap.




# Which of the following does not correspond to a min-heap on the list of values [19,97,83,45,72,55,31,28,31,29].
#  [19, 28, 72, 31, 29, 83, 97, 55, 45, 31]
#  [19, 31, 28, 45, 31, 97, 29, 72, 55, 83]
#  [19, 28, 29, 31, 31, 45, 55, 72, 83, 97]
#  [19, 28, 29, 31, 45, 83, 97, 55, 72, 31]

# Feedback:
# In [19, 28, 29, 31, 45, 83, 97, 55, 72, 31], value 45 has left child 31.
# Accepted Answers:
# [19, 28, 29, 31, 45, 83, 97, 55, 72, 31]




# Consider the min-heap [19, 28, 31, 31, 29, 83, 55, 97, 45, 72]. Suppose we apply the operation delete_min() to this min-heap. The resulting min-heap is:
#  [28, 29, 31, 31, 97, 83, 55, 72, 45]
#  [28, 29, 31, 31, 72, 83, 55, 97, 45]
#  [28, 29, 31, 31, 83, 72, 55, 97, 45]
#  [28, 29, 31, 31, 55, 83, 72, 97, 45]
# Feedback:
# Execute delete_min and check.
# Accepted Answers:
# [28, 29, 31, 31, 72, 83, 55, 97, 45]