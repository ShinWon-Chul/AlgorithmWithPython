answer = 0
def solution(numbers, target):
    num = 0
    n = 0
    
    def dfs(num, n):
        global answer
        if n == len(numbers) :
            if num == target:
                answer += 1
            return
        for i in range(2):
            if i == 0:
                num += numbers[n]
                dfs(num, n+1)
                num -= numbers[n]
            else:
                num -= numbers[n]
                dfs(num, n+1)
                num += numbers[n]
    dfs(0, 0)
    return answer