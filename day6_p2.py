import sys

def pr(s):
    print(s)

# Set the recursion limit (rarely needed but might be helpful for large datasets)
sys.setrecursionlimit(10**6)

# Path to the input file
infile = 'day6.txt'  # Path to input.txt file

# Initialize part 2 answer
p2 = 0

# Read the entire input file and split it into lines
with open(infile, 'r') as file:
    D = file.read().strip()

# Split the input into grid G
G = D.split('\n')
R = len(G)
C = len(G[0])

# Find the starting position of the guard ('^', '>', 'v', '<')
for r in range(R):
    for c in range(C):
        if G[r][c] in '^>v<':
            sr, sc = r, c

# Simulate the guard's movement for part 2
for o_r in range(R):
    for o_c in range(C):
        # Skip invalid obstruction positions (the guard's starting position or existing obstacles)
        if (o_r == sr and o_c == sc) or G[o_r][o_c] != '.':
            continue

        # Initialize guard's starting position and direction
        r, c = sr, sc
        d = {'^': 0, '>': 1, 'v': 2, '<': 3}[G[sr][sc]]  # Map direction to 0=up, 1=right, 2=down, 3=left
        SEEN = set()

        while True:
            # If the guard revisits the same position and direction, a loop is detected
            if (r, c, d) in SEEN:
                p2 += 1
                break
            SEEN.add((r, c, d))

            # Move the guard in the current direction
            dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            rr, cc = r + dr, c + dc

            # Check if the next position is out of bounds
            if not (0 <= rr < R and 0 <= cc < C):
                break

            # If the guard encounters an obstacle or the hypothetical obstruction, turn right
            if G[rr][cc] == '#' or (rr == o_r and cc == o_c):
                d = (d + 1) % 4
            else:
                # Otherwise, move to the next position
                r, c = rr, cc

# Output the result for part 2
pr(p2)  # Part 2 result