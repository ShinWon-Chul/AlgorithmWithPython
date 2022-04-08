from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque([[i, x] for i, x in enumerate(progresses)])
    
    while q:
        count = 0
        n = len(q)
        for _ in range(n):
            i, progress = q.popleft()
            progress += speeds[i]
            q.append([i, progress])
            
        if q[0][1] > 99:
            for i in range(n):
                if q[i][1] > 99:
                    count += 1
                else:
                    break
            answer.append(count)
            
        for _ in range(count):
            q.popleft()
            
    return answer