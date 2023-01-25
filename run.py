import random
import pyfiglet

# Add values for ships & game grid

length_of_ships = [2, 3, 4, 5]
player_display_grid = [[" "] * 8 for i in range(8)]
computer_display_grid = [[" "] * 8 for i in range(8)]
player_guess_grid = [[" "] * 8 for i in range(8)]
computer_guess_grid = [[" "] * 8 for i in range(8)]
grid_values = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

# Create Game board

def print_board(board):
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

# Create function to allow users to select ship placement

def place_ships(board, length_of_ships):
    for ship_length in length_of_ships:
        if board == computer_display_grid:
            while True:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_ship_fit(ship_length, row, column, orientation) and not ship_overlaps(board, row, column, orientation, ship_length):
                    for i in range(column, column + ship_length) if orientation == "H" else range(row, row + ship_length):
                        board[row if orientation == "V" else i][column if orientation == "V" else i] = "X"
                    break
        

# Function ensuring ship placements fit within set grid





# Function allowing user to select grid to target





# Function to check if user hit a ship





# End display functions for if user wins or loses




