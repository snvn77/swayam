# Detecting Pattern Consistency Between Two Strings

# Background
# A software team working on a text pattern–matching system needs to verify whether two given strings follow the same structural pattern. This requirement arises in areas such as:
# Data normalization
# Search indexing
# Language processing
# Pattern validation in user input

# The focus is not on object-oriented design, but purely on string processing and logical consistency.

# ------------------------------------------------------------------------------------------------------------------------------

# Problem Scenario

# Two strings are given:
# String S represents an original pattern
# String T represents a transformed version

# The task is to determine whether:
# Each character in S consistently maps to one unique character in T
# The mapping is one-to-one and reversible
# The relative structure of both strings remains identical

# For example:
# "egg" and "add" follow the same pattern
#  "foo" and "bar" do not

# -----------------------------------------------------------------------------------------------------------------------------------

# Constraints of the Study
# Both strings must be of equal length
# A character cannot map to multiple different characters
# Two different characters cannot map to the same character
# The comparison is performed position by position

# Learners are given the following code to analyze and answer questions based on the case study:
def isomorphicString(s, t):
    if len(s) != len(t):
        return False
    
    s_map = {}
    t_map = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if (char_s in s_map and s_map[char_s] != char_t) or (char_t in t_map and t_map[char_t] != char_s):
            return False
        
        s_map[char_s] = char_t
        t_map[char_t] = char_s
    
    return True

# -----------------------------------------------------------------------------------------------------------------------------------

# Questions:

# What will the function return for s = "egg" and t = "add"?
#  True      (Right Answer)
#  False
#  Depends on dictionary insertion order
#  Raises an error



# What is the first condition that can cause the function to return False?
#  Duplicate characters in s
#  Conflicting mappings in dictionaries
#  Repeated characters at adjacent positions
#  Length mismatch between the two strings       (Right Answer)



# What will the function return for s = "ab" and t = "cc"?
#  False       (Right Answer)
#  True
#  Only the forward mapping fails
#  Depends on loop iteration



# Why is the condition checking both s_map and t_map necessary?
#  To reduce memory usage
#  To avoid nested loops
#  To speed up execution
#  To enforce a one-to-one and reversible character mapping       (Right Answer)



# Which of the following best describes what the algorithm is verifying?
#  Structural equivalence between two strings       (Right Answer)
#  Lexicographical ordering
#  Equality of character frequencies
#  Whether both strings are permutations