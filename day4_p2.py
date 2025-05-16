def is_valid_mas_diagonal(grid, r, c, dr1, dc1, dr2, dc2):
    """
    Checks if the diagonals starting from (r, c) form valid MAS sequences.
    dr1, dc1: directions for the first diagonal (e.g., top-left to bottom-right).
    dr2, dc2: directions for the second diagonal (e.g., top-right to bottom-left).
    """
    try:
        # First diagonal (MAS or SAM)
        diagonal_1 = grid[r + dr1][c + dc1] + grid[r][c] + grid[r - dr1][c - dc1]
        valid_diag_1 = diagonal_1 in ("MAS", "SAM")
        
        # Second diagonal (MAS or SAM)
        diagonal_2 = grid[r + dr2][c + dc2] + grid[r][c] + grid[r - dr2][c - dc2]
        valid_diag_2 = diagonal_2 in ("MAS", "SAM")
        
        return valid_diag_1 and valid_diag_2
    except IndexError:
        # If any check goes out of bounds, it's invalid
        return False


def count_x_mas_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Iterate through each potential center of the X
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A':  # The center of the "X-MAS" pattern
                # Check diagonals: Forward (top-left to bottom-right) and Backward (top-right to bottom-left)
                if is_valid_mas_diagonal(grid, r, c, -1, -1, -1, 1):
                    count += 1

    return count


# Load the input from the file
input_file_path = 'day4.txt'
with open(input_file_path, 'r') as file:
    grid = [line.strip() for line in file]

# Calculate the total number of X-MAS patterns
result = count_x_mas_patterns(grid)

# Print the result
print(f"Total X-MAS patterns found: {result}")