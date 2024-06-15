def get_fastest_time(locations, mid, l):
    fastest = 0
    for loc in locations:
        if loc <= mid:
            fastest = max(fastest, loc)
        else:
            fastest = max(fastest, l-loc)
    return fastest

def get_slowest_time(locations, mid, l):
    slowest = 0
    for loc in locations:
        if loc <= mid:
            slowest = max(slowest, l-loc)
        else:
            slowest = max(slowest, loc)
    return slowest

t = int(input())
for _ in range(t):
    l,n = map(int, input().split())
    locations = [ int(input()) for _ in range(n)]
    mid = int(l/2)

    fastest = get_fastest_time(locations, mid, l)
    slowest = get_slowest_time(locations, mid, l)
    print(f'{fastest} {slowest}')