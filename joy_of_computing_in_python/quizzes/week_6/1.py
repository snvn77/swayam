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