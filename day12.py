from collections import deque

# Input file
infile = "day12.txt"

# Parse grid
with open(infile) as f:
    G = f.read().strip().split('\n')

R, C = len(G), len(G[0])
SEEN = set()
p1, p2 = 0, 0
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

for r in range(R):
    for c in range(C):
        if (r, c) in SEEN:
            continue
        Q = deque([(r, c)])
        area = 0
        perimeter = 0
        
        while Q:
            r2, c2 = Q.popleft()
            if (r2, c2) in SEEN:
                continue
            SEEN.add((r2, c2))
            area += 1
            for dr, dc in DIRS:
                rr, cc = r2 + dr, c2 + dc
                if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r][c]:
                    Q.append((rr, cc))
                else:
                    perimeter += 1

        p1 += area * perimeter

print("P1:", p1)
