from heapq import heappush, heappop
"""최소 힙을 사용함으로써 가장 앞의 종료시간이 현재 강의중 가장 빨리 끝나는 시간임"""

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

result = []
l.sort()
heappush(result, l[0][1])
for s, t in l[1:]:
    #새로 들어온 강의의 시작시간이 가장 빨리 끝나는 시간보다 빠르다면
    if s < result[0]:
        #새로운 강의실 사용
        heappush(result, t)
    #새로 들어온 강의의 시작시간이 가장빨리 끝나는 시간보다 느리다면
    else:
        heappop(result) #기존의 종료 시간을 빼고
        heappush(result, t) #새로 들어온 강의의 종료시간으로 갱신
print(len(result))