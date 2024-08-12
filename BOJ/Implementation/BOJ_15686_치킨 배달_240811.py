import itertools
inf = int(1e9)
n, m = list(map(int, input().split()))
grid = [[0]*(n+1)]
for _ in range(n):
    grid.append([0] + list(map(int, input().split())))

def distance(c, h):
    dist = abs(c[0]-h[0])+abs(c[1]-h[1])
    return dist

chickens = []
houses = []
for ix, row in enumerate(grid):
    for iy, col in enumerate(row):
        if grid[ix][iy] == 2:
            chickens.append([ix,iy])
        elif grid[ix][iy] == 1:
            houses.append([ix, iy])

result = inf
remains = list(itertools.combinations(chickens, m))
for remain in remains:
    total_dist = 0
    for h in houses:
        local_dist = inf
        for c in remain:
            local_dist = min(local_dist, distance(c, h))
        total_dist += local_dist
    result = min(result, total_dist)
print(result)

# cCm * h * m