from sys import stdin

n = int(input())
solution = list(map(int, stdin.readline().rstrip().split()))
solution.sort()
answer = 2e9+1 # 기준값
left = 0
right = n - 1
while left < right:
    
    total = solution[left] + solution[right]
    
    if abs(total) < answer:
        answer = abs(total)
        result = [solution[left], solution[right]]
    
    if total < 0:
        left += 1
    else:
        right -= 1
print(result[0], result[1])