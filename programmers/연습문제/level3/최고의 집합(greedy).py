def solution(n, s):
    num = n
    answer = []
    
    if int(s/n) == 0:
        return [-1]
    
    for i in range(n):
        answer.append(int(s/num))
        s -= int(s/num)
        num -= 1
        
    return answer