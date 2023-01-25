import random
import pyfiglet

# Add values for ships & game grid

ships_length = [2, 3, 4, 5]
player_display_grid = [[" "] * 8 for i in range(8)]
computer_display_grid = [[" "] * 8 for i in range(8)]
player_guess_grid = [[" "] * 8 for i in range(8)]
computer_guess_grid = [[" "] * 8 for i in range(8)]
grid_values = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

