from itertools import permutations
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    n = len(numbers)
    nums = set()
    for i in range(1, n+1):
        for x in permutations(numbers, i):
            num = int(''.join(list(x)))
            if num in [1, 0]:
                continue
            if is_prime_number(num):
                nums.add(num)
    answer = len(nums)
    return answer