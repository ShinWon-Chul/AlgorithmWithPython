import math

def get_minimum_divisor(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return i # 해당 수를 return
    return x # 소수이므로 입력된 수를 return
        
def solution(n):
    answer = get_minimum_divisor(n-1)
    return answer