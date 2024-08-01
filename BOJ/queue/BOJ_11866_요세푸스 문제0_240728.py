from collections import deque

N, K = map(int, input().split())


arr = deque(range(1, N + 1))
result = []

while arr:
    arr.rotate(-(K - 1))
    result.append(arr.popleft())

res = '<' + ', '.join(map(str, result)) + '>'
print(res)

"""
N, K = 7, 3

while arr:
    arr.rotate(-(K - 1))

arr
deque([3, 4, 5, 6, 7, 1, 2])
deque([6, 7, 1, 2, 4, 5])
deque([2, 4, 5, 7, 1])
deque([7, 1, 4, 5])
deque([5, 1, 4])
deque([1, 4])
deque([4])

res = 
<3, 6, 2, 7, 5, 1, 4>

"""