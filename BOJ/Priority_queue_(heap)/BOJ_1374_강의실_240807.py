"""N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다. 
이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.

물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 
한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다. 
필요한 최소 강의실의 수를 출력하는 프로그램을 작성하시오.

첫째 줄에 강의의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에 걸쳐 각 줄마다 세 개의 정수가 주어지는데, 
순서대로 강의 번호, 강의 시작 시간, 강의 종료 시간

입력
8
6 15 21
7 20 25
1 3 8
3 2 14
8 6 27
2 7 13
4 12 18
5 6 20

"""
from heapq import heappop, heappush
n = int(input())
lecture = [ list(map(int, input().split())) for _ in range(n)]

# 강의를 시작 시간순으로 정렬
lecture.sort(key = lambda x : x[1])
h = []

# 최소 하나의 강의실은 반드시 필요함
answer = 1
for lec in lecture:
    # 힙이 비어있지 않음(강의실을 사용중)
    if h:
        while h:
            # 힙의 처음 값이 가장 빨리 끝나는 시간이므로 시작시간 보다 작거나 같은 값을 힙에서 pop
            if h[0] <= lec[1]:
                heappop(h)
            else:
                break
        # 새로 들어온 강의의 종료시간을 힙에 push
        heappush(h, (lec[-1]))
        # 힙의 길이의 최대값 계산(사용중인 강의실의 최대 갯수)
        answer = max(answer, len(h))
    # 힙이 비어있는 경우 처음 강의의 종료시간을 힙에 푸시
    else:
        heappush(h, lec[-1])
print(answer)