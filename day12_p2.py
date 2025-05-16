import sys
from collections import deque
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

# Read the input file name or use default
infile = sys.argv[1] if len(sys.argv) >= 2 else 'day12.txt'

# Read the grid data from the file
try:
    with open(infile, 'r') as f:
        G = f.read().strip().split('\n')
except FileNotFoundError:
    print(f"Error: File '{infile}' not found.")
    sys.exit(1)

# Validate grid data
if not G or any(len(row) != len(G[0]) for row in G):
    print("Error: Invalid grid format in the input file.")
    sys.exit(1)

R = len(G)
C = len(G[0])

p1 = 0
p2 = 0
SEEN = set()

for r in range(R):
    for c in range(C):
        if (r, c) in SEEN:
            continue
        Q = deque([(r, c)])
        area = 0
        perim = 0
        PERIM = dict()

        while Q:
            r2, c2 = Q.popleft()
            if (r2, c2) in SEEN:
                continue
            SEEN.add((r2, c2))
            area += 1
            for dr, dc in DIRS:
                rr = r2 + dr
                cc = c2 + dc
                if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r2][c2]:
                    Q.append((rr, cc))
                else:
                    perim += 1
                    if (dr, dc) not in PERIM:
                        PERIM[(dr, dc)] = set()
                    PERIM[(dr, dc)].add((r2, c2))

        sides = 0
        for k, vs in PERIM.items():
            SEEN_PERIM = set()
            for (pr, pc) in vs:
                if (pr, pc) not in SEEN_PERIM:
                    sides += 1
                    Q = deque([(pr, pc)])
                    while Q:
                        r2, c2 = Q.popleft()
                        if (r2, c2) in SEEN_PERIM:
                            continue
                        SEEN_PERIM.add((r2, c2))
                        for dr, dc in DIRS:
                            rr, cc = r2 + dr, c2 + dc
                            if (rr, cc) in vs:
                                Q.append((rr, cc))

        p1 += area * perim
        p2 += area * sides

# Print results
print("P1:", p1)
print("P2:", p2)
