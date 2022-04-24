from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        price = q.popleft()
        count = 0
        if len(q) != 0:
            for p in q:
                count += 1
                if price > p:
                    break
        answer.append(count)

    return answer