import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        for s in scoville:
            if s < K:
                break
        else:
            return answer 
        answer += 1
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        new_food = food1+food2*2
        heapq.heappush(scoville, new_food)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer