from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    max_value = max(q)
    
    while q:
        p = q.popleft()
        if p == max_value and location == 0:
            answer += 1
            return answer            
        elif p == max_value:
            answer += 1
            location -= 1
            if location == -1:
                location = len(q)-1
            max_value = max(q)
        else:
            location -= 1
            q.append(p)
            if location == -1:
                location = len(q)-1
            
    return answer