from sys import stdin
n, m = map(int, input().split()) # 수의 개수, 구해야 하는 횟수
arr = list(map(int, stdin.readline().rstrip().split()))
ij = []
for _ in range(m):
    ij.append(map(int, input().split()))
sum_value = 0
prefix_sum = [0]
for i in arr:
    sum_value += i
    prefix_sum.append(sum_value)
for i, j in ij:
    print(prefix_sum[j] - prefix_sum[i-1])