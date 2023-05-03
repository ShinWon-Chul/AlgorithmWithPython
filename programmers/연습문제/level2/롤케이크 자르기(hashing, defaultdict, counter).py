from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    a = defaultdict(lambda : 0)
    b = Counter(topping)
    
    for i in topping:
        a[i] += 1
        b[i] -= 1
        if b[i] == 0:
            b.pop(i)
        if len(b) == len(a):
            answer += 1
    
    return answer