from collections import deque
def solution(cacheSize, cities):
    cities = list(map(lambda x : x.lower(), cities))

    time = 5
    q = deque([cities[0]])
    if cacheSize > 0:
        for city in cities[1:]:
            #캐시 힛인 경우
            if city in q:
                time += 1
                q.remove(city)
                q.append(city)
            #캐시 미스인 경우
            else:
                #캐시의 길이가 cacheSize보다 작은경우
                if len(q) < cacheSize:
                    time += 5
                    q.append(city)
                #캐시가 꽉 차있는경우
                else:
                    time += 5
                    q.popleft()
                    q.append(city)
    else:
        time = 5*len(cities)
    return time