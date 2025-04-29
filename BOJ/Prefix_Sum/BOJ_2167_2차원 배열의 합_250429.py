N, M = list(map(int, input().split()))
matrix = [ list(map(int, input().split())) for _ in range(N)]
K = int(input())

matrix_prefix_sum = []
for y in range(N):
	summary = 0
	prefix_sum = [0]
	for x in range(M):
		summary += matrix[y][x]
		prefix_sum.append(summary)
	matrix_prefix_sum.append(prefix_sum)

for _ in range(K):
	answer = 0
	i, j, x, y = list(map(int, input().split()))
	for row in range(i-1, x, 1):
		answer += matrix_prefix_sum[row][y] - matrix_prefix_sum[row][j-1]
	print(answer)
