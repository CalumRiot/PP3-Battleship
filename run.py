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


# Function for placing ships onto board with either vertical or horizontal axis
# Computer ships are placed at random while user is prompted to input there own


def place_ships(board, length_of_ships):
    for ship_length in length_of_ships:
        if board == computer_display_grid:
            while True:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_ship_fit(ship_length, row, column, orientation) and not ship_overlaps(board, row, column, orientation, ship_length):
                    for i in range(column, column + ship_length) if orientation == "H" else range(row, row + ship_length):
                        board[row if orientation == "V" else i][column if orientation == "V" else i] = "X"
                    break
        else:
            place_ship = True
            print('Place the ship with a length of ' + str(ship_length))
            row, column, orientation = user_input(place_ship)
            if check_ship_fit(ship_length, row, column, orientation) and not ship_overlaps(board, row, column, orientation, ship_length):
                for i in range(column, column + ship_length) if orientation == "H" else range(row, row + ship_length):
                    board[row if orientation == "V" else i][column if orientation == "V" else i] = "X"
                print_board(player_display_grid)


# Functions to ensure ships don't overlap when placed and to ensure
# that ships are also placed within the defined grid size 

def check_ship_fit(ship_length, row, column, orientation):
    if orientation == "H":
        return column + ship_length <= 8
    else:
        return row + ship_length <= 8

def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        return any(board[row][i] == "X" for i in range(column, column + ship_length))
    else:
        return any(board[i][column] == "X" for i in range(row, row + ship_length))


# Function allowing user to select grid to target





# Function to check if user hit a ship





# End display functions for if user wins or loses




