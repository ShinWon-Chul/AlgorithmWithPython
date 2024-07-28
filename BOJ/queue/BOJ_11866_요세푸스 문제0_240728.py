from collections import deque

N, K = map(int, input().split())


arr = deque(range(1, N + 1))
result = []

while arr:
    arr.rotate(-(K - 1))
    result.append(arr.popleft())

res = '<' + ', '.join(map(str, result)) + '>'
print(res)