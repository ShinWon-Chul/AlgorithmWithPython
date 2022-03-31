import heapq

def solution(n, works):
    answer = 0
    works = [ -work for work in works]
    heapq.heapify(works)
    
    for _ in range(n):
        work = heapq.heappop(works)
        heapq.heappush(works, work+1)
    for i in works:
        if i < 0: answer += i*i
    
    return answer