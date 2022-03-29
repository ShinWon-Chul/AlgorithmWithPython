import heapq

def solution(A, B):
    a = [-i for i in A]
    b = [-i for i in B]
    heapq.heapify(a)
    heapq.heapify(b)
    count = 0
    while a and b:
        a_val = heapq.heappop(a)
        b_val = heapq.heappop(b)
        if -b_val > -a_val:
            count += 1
        else:
            heapq.heappush(b, b_val)
    return count