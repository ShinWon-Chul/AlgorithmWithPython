N, K = list(map(int, input().split()))
temperature = list(map(int, input().split()))

summary = 0
prefix_sum = [0]

for i in range(N):
	summary += temperature[i]
	prefix_sum.append(summary)

sums = []
for j in range(0, N):
	if j+K < len(prefix_sum):
		temperature_sum = prefix_sum[j+K] - prefix_sum[j] 
		sums.append(temperature_sum)
print(max(sums))