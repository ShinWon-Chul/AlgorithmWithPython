from sys import stdin
n, m = list(map(int, input().split()))
arr = list(map(int, stdin.readline().rstrip().split()))

start = 1
end = m* max(arr)

while start <= end:
    mid = int((start + end) / 2)
    balloon = 0
    for i in arr:
        balloon += int(mid/i)

    if balloon < m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)