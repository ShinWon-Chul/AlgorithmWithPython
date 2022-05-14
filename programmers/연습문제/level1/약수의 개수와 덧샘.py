import math

def num_divisor(x):
    count = 0
    for i in range(1, x+1):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            count += 1
    if count % 2 == 0:
        return 'even'
    else:
        return 'odd'

def solution(left, right):
    answer = 0
    for num in range(left, right+1, 1):
        if num_divisor(num) == 'even':
            answer += num
        else:
            answer -= num
    return answer