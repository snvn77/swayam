# A Month of Chance—Simulating a Lottery Strategy

# Background
# Ravi, a college student interested in probability and data analysis, wants to understand whether playing a simple lottery-style game every day can be profitable in the long run. Instead of relying on intuition or anecdotes, he decides to simulate the experience using Python.

# Ravi chooses a very straightforward strategy:
# Every day, he selects one fixed number between 1 and 10 as his bet.
# A system randomly draws a number between 1 and 10.
# If his chosen number matches the draw, he earns a large reward.
# If it doesn’t, he incurs a small loss.

# He repeats this experiment once per day for 30 days, representing a month of consistent participation.

# --------------------------------------------------------------------------------------------------------------------------------------

# Objective of the Study

# The purpose of this case study is to:
# Observe how randomness affects outcomes over time
# Track profit and loss trends instead of isolated wins
# Visually analyze whether consistency in betting leads to gains or losses

# Rather than focusing on a single lucky or unlucky day, Ravi wants to see the overall trajectory of his account balance.

# --------------------------------------------------------------------------------------------------------------------------------------- 

# Experimental Setup
# Ravi starts with an account balance of ₹0
# He plays the game once per day for 30 days
# Each day’s result updates his account balance
# The balance is recorded daily to study trends over time

# To make the results more intuitive, Ravi plots:
# Days (1–30) on the x-axis
# Account balance on the y-axis

# This allows him to clearly see fluctuations, streaks of loss, occasional jumps, and the final outcome.

# ---------------------------------------------------------------------------------------------------------------------------------------

#  Given Code for Analysis

#  Students are provided with the following Python code and are expected to analyze its behavior, output, and implications based on the case study above:
import random
import matplotlib.pyplot as plt

# User Input
bet = int(input("Enter your bet from 1 to 10: "))

# Account Initialization
account = 0

# Simulation loop for one month (30 days)
x = [] # Days
y = [] # Account Balances

for day in range(30):
    lucky_draw = random.randint(1,10)

    if bet == lucky_draw:
        account+=900
    else:
        account-=100

    x.append(day+1)
    y.append(account)

# Visualization
plt.plot(x,y)
plt.xlabel("Days")
plt.ylabel("Account Balance")
plt.title("Lottery Simulation - Profit or Loss")
plt.show()

# Questions: 

# What does the variable bet represent in the simulation?
#  The amount of money invested each day
#  The randomly generated lucky number
#  The fixed number chosen by the user for the entire month     (Right Answer)
#  The number of days the simulation runs



# How many times is the lottery game simulated in the program?
#  10
#  30      (Right Answer)
#  Until the user wins
#  Depends on the bet value



# What happens to the account balance when the bet does NOT match the lucky draw?
#  It remains unchanged
#  It increases by 100
#  It decreases by 900
#  It decreases by 100      (Right Answer)



# Which Python library is responsible for generating randomness in the simulation?
#  matplotlib
#  random      (Right Answer)
#  pyplot
#  math



# What do the lists x and y store respectively?
#  Account balances and days
#  Bets and lucky numbers
#  Days and account balances      (Right Answer)
#  Wins and losses



# If the user never wins even once during the 30 days, what will be the final account balance?
#  −3000      (Right Answer)
#  −900
#  −100
#  0



# What is the probability of winning on any single day?
#  1/30
#  1/100
#  1/10      (Right Answer)
#  Depends on previous days



# Why does the account balance graph typically show long downward trends with occasional sharp upward jumps?
#  Because the bet value changes daily
#  Because losses are frequent and wins are rare but large      (Right Answer)
#  Because matplotlib smooths the curve
#  Because account balance is averaged



# Which change would make the simulation more statistically reliable without changing the game rules?
#  Increasing the win amount
#  Running the simulation for more days      (Right Answer)
#  Changing the bet every day
#  Removing the plot



# Despite a high winning reward (₹900), why does the simulation still tend to show losses over time?
#  Because the plotting scale is incorrect
#  Because the probability of winning is too low compared to the loss frequency      (Right Answer)
#  Because Python integers overflow
#  Because the account starts at zero