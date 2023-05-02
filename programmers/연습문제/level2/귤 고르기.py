from collections import Counter

def solution(k, tangerine):
    answer = 0
    n = 0
    dict_ = Counter(tangerine)
    arr = [[v, k] for k, v in dict_.items()] 
    arr.sort(reverse=True)
    for v, _ in arr:
        
        n += v
        answer += 1
        if n >= k:
            break
            
    return answer