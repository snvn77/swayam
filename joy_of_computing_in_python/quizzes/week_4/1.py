# Building a Mini Dobble Game Using Python:
# In this activity, a learner designs a simplified version of the popular Dobble game using Python. The goal of the game is simple: two cards are generated such that exactly one symbol is common between them, and the player must correctly identify that common symbol.

# Step 1: Preparing the Symbol Set
# The game begins by importing two built-in Python modules:
# string → used to access alphabets easily
# random → used to generate randomness in the game
# Using string.ascii_letters, a list of symbols is created that contains:
# lowercase letters (a–z)
# uppercase letters (A–Z)
# This list becomes the symbol pool from which all card symbols are drawn.
# Once a symbol is used, it is removed from the pool to prevent duplication.

# Step 2: Deciding Positions on Cards
# Each card contains 5 positions, indexed from 0 to 4.
# Two random positions are generated:
# pos1 → where the common symbol will appear on Card 1
# pos2 → where the common symbol will appear on Card 2
# These positions are chosen randomly, which ensures that the common symbol does not always appear in the same place.

# Step 3: Selecting the Common Symbol
# One symbol is randomly selected from the symbol pool to act as the common symbol shared by both cards.
# Immediately after selecting it, the symbol is removed from the pool, ensuring:
# it cannot accidentally appear again
# uniqueness across the rest of the cards
# This guarantees the key rule of Dobble: only one symbol matches.

# Step 4: Creating the Cards
# Two lists are created:
# card1
# card2
# Each list has 5 empty slots, initialized with ZERO.
# These lists represent the two cards shown to the player.

# Step 5: Handling Common and Non-Common Positions
# If pos1 and pos2 are the same, the common symbol is placed at that index in both cards
# If they are different:
# The common symbol is placed at pos1 in Card 1
# The same symbol is placed at pos2 in Card 2
# Two different symbols are placed in the swapped positions to avoid accidental matching
# This logic ensures that:
# only one symbol is shared
# all other symbols differ across cards

# Step 6: Filling Remaining Positions Using a Loop
# A while loop runs from index 0 to 4.
# For every index except pos1 and pos2:
# one new symbol is picked for Card 1
# a different new symbol is picked for Card 2
# both symbols are removed from the pool
# This systematic filling ensures:
# no empty positions remain
# no duplicate symbols exist
# only one common symbol survives

# Step 7: Player Interaction
# The player is prompted with:
# Spot the common symbol:
# The input is stored in a variable and represents the player’s guess.
# This step introduces human interaction into the program, converting logic into a playable game.

# Step 8: Validating the Answer
# The program compares:
# the player’s input
# the actual common symbol
# If they match → "Right!" is displayed
# Otherwise → "Wrong!" is displayed
# This final comparison closes the game loop and gives instant feedback.


# What is the maximum number of unique symbols that can be safely used by this program without causing a runtime error?
#  26
#  Unlimited
#  10
#  52   (Right Answer)

# Which statement about pos1 and pos2 is logically correct?
#  They may or may not be equal   (Right Answer)
#  They are always different
#  They are fixed once generated
#  They cannot be equal

# Why is same_symbol removed from the symbol list immediately after selection?
#  To improve randomness
#  To reduce memory usage
#  To ensure it appears exactly once on each card   (Right Answer)
#  To simplify the loop condition

# What problem does the condition if pos1 == pos2 prevent?
#  Index out-of-range error
#  Logical conflict in symbol placement    (Right Answer)
#  Infinite looping
#  Input mismatch

# When pos1 ≠ pos2, how many times does the while loop assign symbols?
#  5
#  2    
#  4
#  3    (Right Answer)

# What is the most serious consequence if symbols are not removed inside the loop?
#  Cards become sorted automatically
#  Multiple common symbols may appear    (Right Answer)
#  Loop runs indefinitely
#  Cards become identical

# Which player input would be marked incorrect even if the symbol looks correct?
#  Input entered quickly
#  Input with correct spacing
#  Lowercase input for an uppercase symbol    (Right Answer)
#  Input after a delay

# Which statement is guaranteed true every time the program runs?
#  Symbols appear in alphabetical order
#  Both cards are mirror images
#  Cards share no symbols
#  Cards share exactly one symbol    (Right Answer)