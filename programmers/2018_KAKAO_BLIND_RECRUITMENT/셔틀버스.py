from collections import deque

def solution(n, t, m, timetable):
    first_bus = 540
    timetable = list(map(lambda x : (int(x.split(':')[0])*60)+(int(x.split(':')[1])), timetable))
    timetable.sort()
    q = deque(timetable)
    #버스 도착시간
    arr = []
    for i in range(n):
        #막차
        if i == n-1:
            arrive_time = first_bus+i*t
            for _ in range(m):
                if len(q) != 0:
                    if q[0] <= arrive_time:
                        arr.append(q.popleft())
            #막차에 타는 사람이 없다면
            if len(arr) == 0:
                answer = arrive_time
            #막차를 타는 사람이 제한 사람보다 적다면
            elif len(arr) < m:
                answer = arrive_time
            #막차가 꽉 찬다면
            else:
                answer = arr[-1]-1
        else:
            #도중에 큐가 전부 비어버린다면 그냥 막차 타면됨
            if len(q)<m:
                answer = first_bus+n*t
            else:
                arrive_time = first_bus+i*t
                for _ in range(m):
                    if q[0] <= arrive_time:
                        q.popleft()


    hour = str(int(answer/60))
    minuit = str(answer%60)
    if len(hour) < 2:
        hour = '0'+hour
    if len(minuit) < 2:
        minuit = '0'+minuit
    answer = f'{hour}:{minuit}'
    return answer