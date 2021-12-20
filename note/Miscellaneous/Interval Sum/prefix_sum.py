n = 5
data = [10, 20, 30, 40, 50]

''' Make prefix sum array '''
summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)

''' Get interval sum '''
left = 2 #2번째 수부터
right = 4 #4번째 수까지
print(prefix_sum[right] - prefix_sum[left - 1]) #구간합 구하기