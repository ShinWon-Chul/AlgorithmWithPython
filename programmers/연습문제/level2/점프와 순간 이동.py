def solution(n):
    answer = 1
    while n>2:
        if n % 2 == 0 :
            n = int(n/2)
        else:
            n -= 1
            answer += 1
    
    return answer