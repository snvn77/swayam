# Terminal-Based Tic Tac Toe Game:

# Background
#  During a programming lab session, two students decide to recreate the classic Tic Tac Toe game using Python. Instead of using a graphical interface or mobile application, they choose a terminal-based approach, relying entirely on text input and output.
# The objective is to allow two players to play the game interactively while the system manages the board, validates moves, and determines the final result.

# Game Environment
# The game is executed in a Python environment where:
# The board consists of nine positions arranged in three rows and three columns
# Each position on the board can display:
#                o  An "X"
#                o  An "O"
#                o  Or remain empty
#  The board is shown to players after every move
# Players interact with the system by entering their choices through the keyboard.

# Player Interaction
# The game involves two players
# One player uses the symbol X, the other uses O
# Players enter their moves using row and column numbers
# Input is provided in a fixed format during every turn
# If an invalid entry is made, the system requests a new input without progressing the game

# Game Flow
# The game begins with a predefined starting player
# Players alternate turns throughout the match
# Each turn updates the visible board
# The game continues until a decisive outcome is reached
# No player is allowed to overwrite an existing move

# Game Completion
# The game ends in one of two ways:
# 1. A winner is declared
#             o One player successfully completes a valid winning pattern
#             o The game stops immediately once a winner is identified
# 2. A draw is declared
#            o All board positions are filled
#            o No player achieves a winning pattern
# In both cases, the final board state is displayed before the result is announced.

# The source code is presented in three sequential parts and must be read in the order provided as a single continuous program.


board = [[" " for _ in range(3)] for _ in range(3)]

def display_board():
    row_num = 0
    for row in board:
        print(" | ".join(row))
        row_num+=1
        if row_num<=2:
            print("---------")

def check_won(symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
        
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True
    
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    
    return False

current_player = "X"
turns = 0

while turns < 9:
    display_board()
    move=input(f"Player {current_player}, enter your move (row and column): ").split(",")

    if len(move)!=2:
        print("Invalid Input!")
        continue

    row, col = map(int, move)

    if row<1 or row>3 or col<1 or col>3:
        print("Invalid Position!")
        continue

    if board[row-1][col-1] != " ":
        print("Cell already occupied")
        continue

    board[row-1][col-1] = current_player
    turns+=1

    if check_won(current_player):
        display_board()
        print(f" Player {current_player} Wins!!")
        break

    current_player = "X" if current_player == "O" else "O"

display_board()
print("It's a draw!")