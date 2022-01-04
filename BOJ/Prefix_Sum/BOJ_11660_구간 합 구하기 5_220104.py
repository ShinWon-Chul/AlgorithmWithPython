from sys import stdin
n, m = map(int, input().split()) # 행렬 크기, 구해야 하는 수

arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().rstrip().split())))
t = []
for _ in range(m):
    t.append(list(map(int, stdin.readline().rstrip().split())))

for idx, row in enumerate(arr):
    sum_value = 0
    prefix_sum = [0]
    for value in row:
        sum_value += value
        prefix_sum.append(sum_value)
    arr[idx] = prefix_sum
    
for x1, y1, x2, y2 in t:
    if x1 == x2:
        print(arr[x1-1][y2] - arr[x2-1][y1-1])
    else:
        result = 0
        for i in range(x1-1, x2):
            summ = arr[i][y2] - arr[i][y1-1]
            result += summ
        print(result)