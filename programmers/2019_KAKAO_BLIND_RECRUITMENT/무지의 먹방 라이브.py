import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    h = []
    for i, v in enumerate(food_times):
        heapq.heappush(h, (v, i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)
    left_time = k

    h.sort(key = lambda x : x[0])
    while sum_value + (h[0][0]-previous) * length <= k :
        now = heapq.heappop(h)[0]
        sum_value += ((now-previous) * length)
        length -= 1
        previous = now


    left_time -= sum_value    
    next_food = left_time%length
    h.sort(key=lambda x : x[1])
    return h[next_food][1]