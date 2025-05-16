def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal Up-Left
        (-1, 1)   # Diagonal Up-Right
    ]

    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, dx, dy):
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy):
                    count += 1

    return count

# Read the input from the file
with open("day4.txt", "r") as file:
    lines = file.readlines()

# Convert the input into a grid format
grid = [line.strip() for line in lines]

# Define the word to search for
word = "XMAS"

# Count occurrences of the word in the grid
result = count_word_occurrences(grid, word)

# Print the result
print("Total occurrences of '{}':".format(word), result)