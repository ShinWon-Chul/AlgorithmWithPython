def int_to_nonation(num, nonation):
    arr = ''
    while True:
        if num < nonation:
            arr = str(num) + arr
            break
        mode = num%nonation

        arr = str(mode) + arr 
        num = int(num/nonation)
    return arr
    
def solution(n):
    answer = 0
    num = int_to_nonation(n, 3)
    for i, v in enumerate(num):
        if v != 0:
            answer += int(v) * (3**i)
    return answer