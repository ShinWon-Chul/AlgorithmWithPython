from sys import stdin
N, C = list(map(int, stdin.readline().rstrip().split()))

house = []
for _ in range(N):
    house.append(int(stdin.readline().strip()))
house = sorted(house)

start = 1
end = house[-1]-house[0]
result = 0

while start <= end:
    count = 1
    mid = (start+end)//2
    current = house[0]
    for i in range(1, N):
        if house[i] >= current+mid:
            count += 1
            current = house[i]
    
    if count < C:
        end = mid-1
    else:
        result = mid
        start = mid +1
print(result)