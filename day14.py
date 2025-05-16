with open("day14.txt") as fin:
    lines = fin.read().strip().split("\n")


n = 103
m = 101


p = []
v = []

for line in lines:
    a, b = line.split(" ")
    p.append(list(map(int, a.split("=")[1].split(","))))
    v.append(tuple(map(int, b.split("=")[1].split(","))))

    p[-1] = [p[-1][1], p[-1][0]]
    v[-1] = [v[-1][1], v[-1][0]]

N = len(p)

def update():
    global p, v
    for i in range(N):
        p[i][0] = (p[i][0] + v[i][0] + n) % n
        p[i][1] = (p[i][1] + v[i][1] + m) % m


def count_robots(i0, i1, j0, j1):
    ans = 0
    for i in range(i0, i1):
        for j in range(j0, j1):
            for ii, jj in p:
                if i == ii and j == jj:
                    ans += 1
    return ans

seen = {}
step=0
while True:
    print(f"Step {step}")
    picture = [[" "] * (m//2+1) for _ in range(n//4+1)]
    for i, j in p:
        picture[i//4][j//2]="#"
    picture = ("\n".join([" ".join(line) for line in picture]))
    if picture in seen:
        print(f"Saw this picture at step {seen[picture]}, stooping--- " )
        break
    seen[picture] = seen
    print()
    print(picture)
    update()

q0 = count_robots(0, n//2, 0, m//2)
q1 = count_robots(n//2+1, n, 0, m//2)
q2 = count_robots(0, n//2, m//2+1, m)
q3 = count_robots(n//2+1, n, m//2+1, m)

print(q0, q1, q2, q3)
print(q0 * q1 * q2 * q3)