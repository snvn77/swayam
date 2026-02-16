# Searching for a Book ID in a Digital Library

# A college library maintains a sorted list of book IDs.
# Each time a student requests a book, the system must search for the book ID and also measure how many checks (iterations) were needed to find it.

# Two interns, Aarav and Neel, suggest two different approaches:
# Aarav uses Linear Search
# Neel uses Binary Search

# The librarian wants to understand:
# 1. How each method works
# 2. How many iterations each method takes
# 3. Which method is more efficient and why

# Part 1: Linear Search Case Study

# Idea Behind Linear Search
# Linear search works exactly like checking books one by one on a shelf, starting from the first book until the required one is found.
# No assumptions about sorting
# Simple and intuitive
# Works for any list
def linear_search(a,x):
    count = 0

    for i in range(len(a)):
        count+=1
        if a[i] == x:
            print(f"Element found at position {i}.")
            return count
    print("Number is not found")
    return count    

# Sample Scenario
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = 7
# We are searching for the element 7 in the list:
# The algorithm starts from the first index (0) and moves forward one element at a time.

# 1. First iteration
# The element at index 0 is 1.
# It does not match 7, so the counter increases and the search continues.

# 2. Second iteration
# The element at index 1 is 2.
# Still not a match.The algorithm moves ahead.

# 3. Third iteration
# The element at index 2 is 3.
# Again, no match.

# 4. Fourth iteration
# The element at index 3 is 4.
# The search continues.

# 5. Fifth iteration
# The element at index 4 is 5.
# No match yet. 6.

# 6. Sixth iteration
# The element at index 5 is 6.
# The algorithm proceeds further.

# 7. Seventh iteration
# The element at index 6 is 7.
# This time, the element matches the target.

# Why the iteration count is 7
# The counter increases before checking each element, and the algorithm must visit every position from index 0 to index 6. 
# So, even though the element is at position 6, it takes 7 checks to find it.

# Part 2: Binary Search Case Study

# Idea Behind Binary Search
# Binary search is like opening a dictionary:
# You don’t start from page 1
# You open the middle, then decide left or right

# Important Requirement:
# The list must be sorted
def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    flag = 0
    count = 0

    while first_pos <= last_pos and flag==0:
        count+=1
        mid = (first_pos+last_pos)//2

        if x[mid]==a:
            flag = 1
            print(f"Element found at position {mid}")
            return count
        
        elif x<mid:
            last_pos = mid
        
        else:
            first_pos = mid

    print("Number is not found")
    return count

# Same Scenario, Different Strategy
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = 7
# Binary search works by eliminating half of the list after every comparison.

# 1. First iteration
# The middle element of the list is calculated.
# The value at the middle position is 5.
# Since 7 is greater than 5, the algorithm ignores the left half and continues with the right half.

# 2. Second iteration
# A new middle is calculated in the remaining right portion.
# The value now checked is 8.
# Since 7 is smaller than 8, the algorithm moves left.

# 3. Third iteration
# The middle is recalculated again.
# The value checked is 6.
# Since 7 is greater than 6, the algorithm shifts right.

# 4. Fourth iteration
# The middle position now contains 7.
# The target is found, and the search stops.

# Why the iteration count is only 4
# Each step removes half of the remaining elements, drastically reducing the number of comparisons.
# This is why binary search grows logarithmically and is much faster for large datasets. 


# A list contains 10 sorted elements. The target element is located at index 6.
# Using the linear search code from the case study, how many iterations will be counted?
#  10
#  6
#  7     (Right Answer)
#  5

# In the binary search implementation, what primarily causes the number of iterations to reduce compared to linear search?
#  The use of a flag variable
#  The loop runs fewer times due to index jumps      (Right Answer)
#  The list length is fixed
#  Elements are compared sequentially

# If the searched element is not present in the list of 10 elements,which statement is true regarding the iteration count?
#  Linear search will stop after half the list
#  Binary search will always run exactly 10 times
#  Binary search cannot handle missing elements
#  Linear search will check all elements      (Right Answer)

# If the number of elements increases from 10 to 1,000, which graph best represents the growth of iterations for binary search?
#  A slowly rising curve
#  A flat horizontal line
#  A zig-zag pattern
#  A steep straight line         (Right Answer)

# In the binary search code, what would happen if the list were unsorted but the same logic was applied?
#  The algorithm would still work but slower
#  The iteration count would double
#  Python would raise a runtime error
#  The element may not be found even if present      (Right Answer)