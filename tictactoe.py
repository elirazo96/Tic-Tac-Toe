import random
print("Welcome to the Tic Tac Toe Game")

# Objects:
# The Tic Tac Toe board
gameboard = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]
currentplayer = "X"
winner = None
game_in_progress  = True

# Printing the board
def game_board_print(gameboard):
    print(" " + gameboard[0][0] + " | " + gameboard[0][1] + " | " + gameboard[0][2])
    print("---+---+---")
    print(" " + gameboard[1][0] + " | " + gameboard[1][1] + " | " + gameboard[1][2])
    print("---+---+---")
    print(" " + gameboard[2][0] + " | " + gameboard[2][1] + " | " + gameboard[2][2])

# Player choose a position and mark on the board
def choose_position(gameboard, mark):
    if mark == "X":
        # The player enters input for choose and mark position
        while True:
            row = input("Enter row number (0-2): ")
            col = input("Enter column number (0-2): ")
            if not (col.isdigit() and row.isdigit()): # Checks that the user's values are valid
                print(f"Invalid value. Please enter row and col numbers again.")
            elif int(col) not in range(0, 3) or int(row) not in range(0, 3): # Checks that the user's values are valid
                print(f"Not in range. Please enter row and col numbers again")
            elif gameboard[int(row)][int(col)] == "_": # # Checks that the user's mark is available
                gameboard[int(row)][int(col)] = mark
                return
            else:
                print("Please choose another position.")
    else:
        # Random move for player O (through import random)
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        while gameboard[row][col] != "_":
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        gameboard[row][col] = mark

# Checks if there is a possible winner
def check_winner(gameboard):
    # check rows
    for row in gameboard:
        if row[0] == row[1] == row[2] != "_":
            return row[0]
    # check columns
    for c in range(3):
        if gameboard[0][c] == gameboard[1][c] == gameboard[2][c] != "_":
            return gameboard[0][c]
    # check horizontal
    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != "_":
        return gameboard[0][0]
    if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] != "_":
        return gameboard[0][2]
    # no winner
    return None

# Printing the board before the while loop (before the game start)
game_board_print(gameboard)

while game_in_progress :
    # Ask from the current player to mark a position
    choose_position(gameboard, currentplayer)

    # check if the game is over
    winner = check_winner(gameboard)
    if winner is not None:
        rematch = input(f"{winner} wins! Do you want to play again? (yes/no) ") # Offers rematch
        if rematch.lower() == "yes" or rematch.lower() == "y": # Checks the user's answer about the rematch
            gameboard = [["_", "_", "_"],
                          ["_", "_", "_"],
                          ["_", "_", "_"]]  # Set all positions to "_"

            currentplayer = "X"  # Specify the player
        else:
            game_in_progress  = False # Ends the game
            if rematch.lower() == "no" or rematch.lower() == "n":
                print("Goodbye!")

    elif "_" not in gameboard[0] and "_" not in gameboard[1] and "_" not in gameboard[2]: # Checks for a tie
        rematch = input("Tie! Do you want to play again? (yes/no) ")  # Offers rematch
        if rematch.lower() == "yes" or rematch.lower() == "y": # Checks the user's answer about the rematch
            gameboard = [["_", "_", "_"],
                          ["_", "_", "_"],
                          ["_", "_", "_"]]  # Set all positions to "_"
            currentplayer = "X"  # Specify the player
        else:
            game_in_progress  = False # Ends the game
            
            if rematch.lower() == "no" or rematch.lower() == "n":
                print("Goodbye!")

    # switching  player's turn
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

        # Printing the current board
        game_board_print(gameboard)











