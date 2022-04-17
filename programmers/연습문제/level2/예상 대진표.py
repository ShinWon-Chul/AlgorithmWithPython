import math

def solution(n,a,b):
    answer = 1 
    while True:
        if math.ceil(a/2) == math.ceil(b/2):
            break
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
    return answer