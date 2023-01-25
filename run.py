import random
import pyfiglet

# Add values for ships & game grid

ships_length = [2, 3, 4, 5]
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





# Function ensuring ship placements fit within set grid





# Function allowing user to select grid to target





# Function to check if user hit a ship





# End display functions for if user wins or loses




