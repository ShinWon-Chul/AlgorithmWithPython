def solution(n):
    answer = 0
    nums = [ i for i in range(1, n+1)]
    start = 0
    end = 0
    while start < n:
        if sum(nums[start:end]) == n:
            end += 1
            start += 1
            answer += 1
        elif sum(nums[start:end]) < n:
            end += 1
        else:
            start += 1
    return answer