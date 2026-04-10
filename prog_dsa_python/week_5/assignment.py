# Programming Assignment

# For this assignment, you have to write a complete Python program. Paste your code in the window below.

# You may define additional auxiliary functions as needed.
# There are some public test cases and some (hidden) private test cases.
# "Compile and run" will evaluate your submission against the public test cases
# "Submit" will evaluate your submission against the hidden private test cases. There are 6 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
# Ignore warnings about "Presentation errors".
# Here are some basic facts about tennis scoring: A tennis match is made up of sets. A set is made up of games.

# To win a set, a player has to win 6 games with a difference of 2 games. At 6-6, there is often a special tie-breaker. In some cases, players go on playing till one of them wins the set with a difference of two games.

# Tennis matches can be either 3 sets or 5 sets. The player who wins a majority of sets wins the match (i.e., 2 out 3 sets or 3 out of 5 sets) The score of a match lists out the games in each set, with the overall winner's score reported first for each set. Thus, if the score is 6-3, 5-7, 7-6 it means that the first player won the first set by 6 games to 3, lost the second one 5 games to 7 and won the third one 7 games to 6 (and hence won the overall match as well by 2 sets to 1).

# You will read input from the keyboard (standard input) containing the results of several tennis matches. Each match's score is recorded on a separate line with the following format:

# Winner:Loser:Set-1-score,...,Set-k-score, where 2 ≤ k ≤ 5

# For example, an input line of the form

# Jabeur:Swiatek:3-6,6-3,6-3
# indicates that Jabeur beat Swiatek 3-6, 6-3, 6-3 in a best of 3 set match.

# The input is terminated by a line consisting of the string "EOF".

# You have to write a Python program that reads information about all the matches and compile the following statistics for each player:

# Number of best-of-5 set matches won
# Number of best-of-3 set matches won
# Number of sets won
# Number of games won
# Number of sets lost
# Number of games lost
# You should print out to the screen (standard output) a summary in decreasing order of ranking, where the ranking is according to the criteria 1-6 in that order (compare item 1, if equal compare item 2, if equal compare item 3 etc, noting that for items 5 and 6 the comparison is reversed).

# For instance, given the following data

# Zverev:Alcaraz:2-6,6-7,7-6,6-3,6-1
# Swiatek:Jabeur:6-4,6-4
# Alcaraz:Zverev:6-3,6-3
# Jabeur:Swiatek:1-6,7-5,6-2
# Zverev:Alcaraz:6-0,7-6,6-3
# Jabeur:Swiatek:2-6,6-2,6-0
# Alcaraz:Zverev:6-3,4-6,6-3,6-4
# Swiatek:Jabeur:6-1,3-6,7-5
# Zverev:Alcaraz:7-6,4-6,7-6,2-6,6-2
# Jabeur:Swiatek:6-4,1-6,6-3
# Alcaraz:Zverev:7-5,7-5
# Jabeur:Swiatek:3-6,6-3,6-3
# EOF
# your program should print out the following

# Zverev 3 0 10 104 11 106
# Alcaraz 1 2 11 106 10 104
# Jabeur 0 4 9 76 8 74
# Swiatek 0 2 8 74 9 76
# You can assume that there are no spaces around the punctuation marks ":", "-" and ",". Each player's name will be spelled consistently and no two players have the same name.

# Sample Test Cases

# Test Case 1	
# Federer:Djokovic:2-6,6-7,7-6,6-3,6-1
# Djokovic:Federer:6-3,4-6,6-4,6-3
# Federer:Djokovic:6-0,7-6,6-7,6-3
# Djokovic:Federer:6-4,6-4
# Federer:Djokovic:2-6,6-2,6-0
# Djokovic:Federer:6-3,4-6,6-3,6-4
# Federer:Djokovic:7-6,4-6,7-6,2-6,6-2
# Djokovic:Federer:7-5,7-5
# Halep:Barty:3-6,6-3,6-3
# EOF
# Federer 3 1 13 142 16 143
# Djokovic 2 2 16 143 13 142
# Halep 0 1 2 15 1 12
# Barty 0 0 1 12 2 15

# Test Case 2	
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Williams:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Williams:7-5,7-5
# Halep:Williams:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Williams:Thiem:6-3,4-6,7-6,0-6,7-5
# EOF
# Halep 2 2 10 75 6 60
# Medvedev 2 0 11 122 16 139
# Williams 2 0 7 68 7 71
# Thiem 1 2 14 133 13 128

# Test Case 3	
# Djokovic:Zverev:2-6,6-7,7-6,6-3,6-1
# Zverev:Djokovic:6-3,4-6,6-4,6-3
# Djokovic:Zverev:6-0,7-6,6-7,6-3
# Zverev:Djokovic:6-4,6-4
# Djokovic:Zverev:2-6,6-2,6-0
# Zverev:Djokovic:6-3,4-6,6-3,6-4
# Djokovic:Zverev:7-6,4-6,7-6,2-6,6-2
# Zverev:Djokovic:7-5,7-5
# Williams:Muguruza:3-6,6-3,6-3
# Muguruza:Williams:6-4,6-4
# Williams:Muguruza:2-6,6-2,6-0
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# EOF
# Williams 3 2 16 160 16 146
# Muguruza 3 1 16 146 16 160
# Djokovic 3 1 13 142 16 143
# Zverev 2 2 16 143 13 142

# Test Case 4	
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Barty:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Barty:7-5,7-5
# Halep:Barty:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Barty:Thiem:6-3,4-6,7-6,0-6,7-5
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Barty:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Barty:7-5,7-5
# Halep:Barty:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Barty:Thiem:6-3,4-6,7-6,0-6,7-5
# EOF
# Halep 4 4 20 150 12 120
# Medvedev 4 0 22 244 32 278
# Barty 4 0 14 136 14 142
# Thiem 2 4 28 266 26 256

# Test Case 5	
# Djokovic:Zverev:2-6,6-7,7-6,6-3,6-1
# Zverev:Djokovic:6-3,4-6,6-4,6-3
# Djokovic:Zverev:6-0,7-6,6-7,6-3
# Zverev:Djokovic:6-4,6-4
# Djokovic:Zverev:2-6,6-2,6-0
# Zverev:Djokovic:6-3,4-6,6-3,6-4
# Djokovic:Zverev:7-6,4-6,7-6,2-6,6-2
# Zverev:Djokovic:7-5,7-5
# Williams:Muguruza:3-6,6-3,6-3
# Muguruza:Williams:6-4,6-4
# Williams:Muguruza:2-6,6-2,6-0
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Kerber:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Kerber:7-5,7-5
# Halep:Kerber:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Kerber:Thiem:6-3,4-6,7-6,0-6,7-5
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Kerber:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Kerber:7-5,7-5
# Halep:Kerber:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Kerber:Thiem:6-3,4-6,7-6,0-6,7-5
# EOF
# Halep 4 4 20 150 12 120
# Medvedev 4 0 22 244 32 278
# Kerber 4 0 14 136 14 142
# Williams 3 2 16 160 16 146
# Muguruza 3 1 16 146 16 160
# Djokovic 3 1 13 142 16 143
# Thiem 2 4 28 266 26 256
# Zverev 2 2 16 143 13 142

# Test Case 6	
# Djokovic:Zverev:2-6,6-7,7-6,6-3,6-1
# Zverev:Djokovic:6-3,4-6,6-4,6-3
# Djokovic:Zverev:6-0,7-6,6-7,6-3
# Zverev:Djokovic:6-4,6-4
# Djokovic:Zverev:2-6,6-2,6-0
# Zverev:Djokovic:6-3,4-6,6-3,6-4
# Djokovic:Zverev:7-6,4-6,7-6,2-6,6-2
# Zverev:Djokovic:7-5,7-5
# Williams:Muguruza:3-6,6-3,6-3
# Muguruza:Williams:6-4,6-4
# Williams:Muguruza:2-6,6-2,6-0
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Barty:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Barty:7-5,7-5
# Halep:Barty:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Barty:Thiem:6-3,4-6,7-6,0-6,7-5
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Barty:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Barty:7-5,7-5
# Halep:Barty:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Barty:Thiem:6-3,4-6,7-6,0-6,7-5
# Djokovic:Zverev:2-6,6-7,7-6,6-3,6-1
# Zverev:Djokovic:6-3,4-6,6-4,6-3
# Djokovic:Zverev:6-0,7-6,6-7,6-3
# Zverev:Djokovic:6-4,6-4
# Djokovic:Zverev:2-6,6-2,6-0
# Zverev:Djokovic:6-3,4-6,6-3,6-4
# Djokovic:Zverev:7-6,4-6,7-6,2-6,6-2
# Zverev:Djokovic:7-5,7-5
# Williams:Muguruza:3-6,6-3,6-3
# Muguruza:Williams:6-4,6-4
# Williams:Muguruza:2-6,6-2,6-0
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Barty:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Barty:7-5,7-5
# Halep:Barty:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Barty:Thiem:6-3,4-6,7-6,0-6,7-5
# Halep:Medvedev:2-6,6-7,7-6,6-3,6-1
# Barty:Medvedev:6-3,4-6,6-4,6-3
# Medvedev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Medvedev:6-4,6-4
# Halep:Medvedev:2-6,6-2,6-0
# Thiem:Medvedev:6-3,4-6,6-3,6-4
# Medvedev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Barty:7-5,7-5
# Halep:Barty:3-6,6-3,6-3
# Halep:Thiem:0-6,0-6,6-0,6-0,7-5
# Barty:Thiem:6-3,4-6,7-6,0-6,7-5
# EOF
# Halep 8 8 40 300 24 240
# Medvedev 8 0 44 488 64 556
# Barty 8 0 28 272 28 284
# Williams 6 4 32 320 32 292
# Muguruza 6 2 32 292 32 320
# Djokovic 6 2 26 284 32 286
# Thiem 4 8 56 532 52 512
# Zverev 4 4 32 286 26 284

# Test Case 7	
# Zverev:Alcaraz:2-6,6-7,7-6,6-3,6-1
# Swiatek:Jabeur:6-4,6-4
# Alcaraz:Zverev:6-3,6-3
# Jabeur:Swiatek:1-6,7-5,6-2
# Zverev:Alcaraz:6-0,7-6,6-3
# Jabeur:Swiatek:2-6,6-2,6-0
# Alcaraz:Zverev:6-3,4-6,6-3,6-4
# Swiatek:Jabeur:6-1,3-6,7-5
# Zverev:Alcaraz:7-6,4-6,7-6,2-6,6-2
# Jabeur:Swiatek:6-4,1-6,6-3
# Alcaraz:Zverev:7-5,7-5
# Jabeur:Swiatek:3-6,6-3,6-3
# EOF
# Zverev 3 0 10 104 11 106
# Alcaraz 1 2 11 106 10 104
# Jabeur 0 4 9 76 8 74
# Swiatek 0 2 8 74 9 76

# Test Case 8	
# Gauff:Zverev:2-6,6-7,7-6,6-3,6-1
# Tsitsipas:Zverev:6-3,4-6,6-4,6-3
# Zverev:Thiem:6-0,7-6,6-7,6-3
# Thiem:Zverev:6-4,6-4
# Gauff:Zverev:2-6,6-2,6-0
# Thiem:Zverev:6-3,4-6,6-3,6-4
# Zverev:Thiem:7-6,4-6,7-6,2-6,6-2
# Thiem:Tsitsipas:7-5,7-5
# Gauff:Tsitsipas:3-6,6-3,6-3
# Gauff:Thiem:0-6,0-6,6-0,6-0,7-5
# Tsitsipas:Thiem:6-3,4-6,7-6,0-6,7-5
# EOF
# Gauff 2 2 10 75 6 60
# Zverev 2 0 11 122 16 139
# Tsitsipas 2 0 7 68 7 71
# Thiem 1 2 14 133 13 128

# Test Case 9	
# Djokovic:Nadal:2-6,6-7,7-6,6-3,6-1
# Nadal:Djokovic:6-3,4-6,6-4,6-3
# Djokovic:Nadal:6-0,7-6,6-7,6-3
# Nadal:Djokovic:6-4,6-4
# Djokovic:Nadal:2-6,6-2,6-0
# Nadal:Djokovic:6-3,4-6,6-3,6-4
# Djokovic:Nadal:7-6,4-6,7-6,2-6,6-2
# Nadal:Djokovic:7-5,7-5
# Williams:Muguruza:3-6,6-3,6-3
# Muguruza:Williams:6-4,6-4
# Williams:Muguruza:2-6,6-2,6-0
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# Muguruza:Williams:6-3,4-6,6-4,6-3
# Williams:Muguruza:6-0,7-6,6-7,6-3
# EOF
# Williams 3 2 16 160 16 146
# Muguruza 3 1 16 146 16 160
# Djokovic 3 1 13 142 16 143
# Nadal 2 2 16 143 13 142

# Statistics will be stored as a dictionary
# Each key is a player name, each value is a list of 6 integers 
# representing 
#   Best of 5 set matches won,
#   Best of 3 set matches won,
#   Sets won
#   Games won
#   Sets lost (store as negative number for comparison)
#   Games lost (store as negative number for comparison)
stats = {}   

# Read a line of input
line = input().strip()
while line != "EOF":
  # Keep track of sets/games won and lost in this match
  # with respect to winner of the match
  (wsets,lsets,wgames,lgames) = (0,0,0,0)

  # Extract winner, loser and string of setscores
  (winner,loser,setscores) = line.strip().split(':',2)
  
  # Extract sequence of sets from setscores
  sets = setscores.split(',')

  for set in sets:
    # Process each set
    (winstr,losestr) = set.split('-')
    win = int(winstr)
    lose = int(losestr)
    wgames = wgames + win
    lgames = lgames + lose
    if win > lose:
      wsets = wsets + 1
    else:
      lsets = lsets + 1

  # Update statistics for each of the players

  for player in [winner,loser]:
    try:
      stats[player]
    except KeyError:
      stats[player] = [0,0,0,0,0,0]

  if wsets >= 3:
    stats[winner][0] = stats[winner][0] + 1
  else:
    stats[winner][1] = stats[winner][1] + 1

  stats[winner][2] = stats[winner][2] + wsets
  stats[winner][3] = stats[winner][3] + wgames
  stats[winner][4] = stats[winner][4] - lsets
  stats[winner][5] = stats[winner][5] - lgames

  stats[loser][2] = stats[loser][2] + lsets
  stats[loser][3] = stats[loser][3] + lgames
  stats[loser][4] = stats[loser][4] - wsets
  stats[loser][5] = stats[loser][5] - wgames

  line = input().strip()

# Collect each player's stats as a tuple, name last    
statlist = [(stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],name) for name in stats.keys() for stat in [stats[name]]]

# Sort the statistics in descending order
# Losing games are stored negatively for sorting correctly
statlist.sort(reverse = True)

# Print
for entry in statlist:
    print(entry[6],entry[0],entry[1],entry[2],entry[3], -entry[4], -entry[5])