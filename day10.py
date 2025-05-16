with open("day10.txt") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)

# Define the directions for moving in the grid
dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def in_grid(i, j):
    rows = len(grid)  # Number of rows
    cols = len(grid[0]) if rows > 0 else 0  # Number of columns
    return (0 <= i < rows) and (0 <= j < cols)

def score(i, j):
    if grid[i][j] != "0":  # Start only from cells with "0"
        return 0
    
    visited = set()
    stack = [(i, j)]
    ans = 0

    while stack:
        curi, curj = stack.pop()
        if (curi, curj) in visited:
            continue
        visited.add((curi, curj))

        cur = int(grid[curi][curj])
        if cur == 9:
            ans += 1
            continue

        for di, dj in dd:
            ii, jj = curi + di, curj + dj
            if in_grid(ii, jj) and (ii, jj) not in visited:
                nbr = int(grid[ii][jj])
                if nbr == cur + 1:  # Look for consecutive values
                    stack.append((ii, jj))
    
    return ans

ans = 0
for i in range(n):
    for j in range(n):
        ans += score(i, j)

print(ans)
