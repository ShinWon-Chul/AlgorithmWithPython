def solution(nums):
    answer = 0
    n = int(len(nums)/2)
    nums = set(nums)
    if len(nums) >= n:
        return n
    else:
        return len(nums)