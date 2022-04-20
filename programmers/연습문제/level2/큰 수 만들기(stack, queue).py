from collections import deque

def solution(number, k):
    arr = [number[0]]
    q = deque(number[1:])
    
    while q:
        num = q.popleft()
        if arr[-1] < num and k > 0:
            while len(arr) != 0 and arr[-1]<num:
                arr.pop()
                k -= 1
                if k == 0:
                    break
            arr.append(num)
        else:
            arr.append(num)
            
    result = ''.join(arr)
    if k != 0 :
        result = result[:-k]
        
    return result