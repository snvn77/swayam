# In-Place Data Reversal in a Memory-Constrained System:

# Context
# A learning analytics platform maintains a list of numerical records representing student interaction order during an online examination.The records are stored in the sequence in which events occurred.
# For audit, debugging, and review purposes, the system occasionally needs to reverse the order of these records so that the most recent interactions appear first.
# However, the platform operates under strict memory constraints because it runs simultaneously for thousands of students.

# System Constraints
# The development team has imposed the following conditions:
# 1. The reversal must happen within the same list (no new list allowed).
# 2. The solution must be function-based, not written inline.
# 3. The team wants to explore non-iterative approaches as part of internal training.
# 4. The system should work correctly for:
#                 o Empty lists
#                 o Lists with odd number of elements
#                 o Lists with even number of elements

# Operational Requirement
# When a list such as:
# [10, 20, 30, 40, 50]
# is processed by the system, the same list object must be transformed into:
# [50, 40, 30, 20, 10]
# No additional list should be returned or constructed.

# The following implementation was submitted by a developer for review and analysis:

def reverseArray(nums):
    start = 0
    end = len(nums) - 1
    swap = 0
    return helper_reverse(start, end, nums, swap)

def helper_reverse(start, end, nums, swap):
    if start > end:
        return nums

    swap = nums[start]
    nums[start] = nums[end]
    nums[end] = swap

    return helper_reverse(start + 1, end - 1, nums, swap)



# 1) If the function reverseArray is called with the input:

# nums = [1, 2, 3, 4]

# What will be the final value of nums?

# [1, 2, 3, 4]
# [4, 3, 2, 1]         (Right Answer)
# [2, 1, 4, 3]
# [4, 2, 3, 1]


# 2) For which condition does the recursive process stop?

# When start == end
# When start > end       (Right Answer)
# When end == 0
# When swap becomes zero


# 3) What does the function reverseArray(nums) return?
# (X) The modified list nums

# ( ) None

# ( ) A new reversed list

# ( ) Only the last swapped value


# 4) What happens when the input list has an odd number of elements?
# ( ) The middle element is removed

# ( ) The program crashes

# (X) The middle element remains unchanged

# ( ) The middle element is swapped with itself twice


# 5) What is the output when reverseArray([]) is executed?
# ( ) Runtime error

# ( ) None

# ( ) [0]

# (x) []


# 6) What is the extra space complexity of this approach (excluding input list)?
# (X) O(n) due to recursion stack

# ( ) O(1) because no variables are used

# ( ) O(log n)

# ( ) O(n²)


# 7) What is the actual role of the variable swap?
# ( ) It stores recursion depth

# (x) It temporarily holds a value during exchange

# ( ) It controls termination

# ( ) It accumulates reversed values


# 8) For a list of length 6, how many recursive calls perform swaps?
# ( ) 6

# ( ) 4

# (x) 3

# ( ) 5


# 9) Which statement best describes the behavior of this function?
# ( ) It creates and returns a new list

# ( ) It modifies the list but returns nothing

# ( ) It uses iteration internally

# (x) It mutates the original list and returns it


# 10) If the final return helper_reverse(...) line is removed from helper_reverse, what happens?
# ( ) The list still gets reversed but None is returned

# ( ) The list is not reversed

# ( ) The program throws a syntax error

# (X) Only the first swap happens





def reverseArray(nums):
    start = 0
    end = len(nums)-1
    return helper_reverse(start,end,nums)

def helper_reverse(start,end,nums):
    if start>=end:
        return nums
    else:
        nums[start],nums[end] = nums[end],nums[start]
        return helper_reverse(start+1, end-1, nums)
    
# The function uses recursion, so the extra space comes from the call stack, not from any new data structures.

# For a list of size n:
# Each recursive call reduces the problem by moving:
# start + 1
# end - 1
# So the recursion continues roughly n/2 times.
# Each recursive call adds a new stack frame.

# Extra Space Complexity:
# Number of recursive calls ≈ n/2
# Each call uses constant space
# So the total extra space is: O(n)
# (We drop constants like 1/2 in Big-O notation.)

# If this were implemented iteratively (using a loop instead of recursion), the extra space would be O(1).
