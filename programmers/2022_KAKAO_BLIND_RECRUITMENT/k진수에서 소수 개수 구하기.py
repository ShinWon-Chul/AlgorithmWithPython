import math

"""num을 nonation진법으로 변환하는 메서드"""
def int_to_nonation(num, nonation):
    d_ = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    arr = ''
    while True:
        if num < nonation:
            if num > 9:
                num = d_[num]
                arr = num + arr
                break
            else:
                arr = str(num) + arr
                break
        mode = num%nonation
        if mode > 9:
            mode = d_[mode]
            arr = mode + arr 
        else:
            arr = str(mode) + arr 
        num = int(num/nonation)
    return arr

'''하나의 수가 소수인지 판별 메서드'''
def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    count = 0
    k_nonation = int_to_nonation(n, k)
    arr = k_nonation.split('0')
    for i in arr:
        if len(i) > 0:
            if int(i) != 1 and is_prime_number(int(i)):
                count += 1
    return count