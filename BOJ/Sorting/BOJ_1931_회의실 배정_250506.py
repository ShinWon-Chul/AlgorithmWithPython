# 입력을 받아 정렬하고(최소 힙을 사용하겟습니다.)(힙을 먼저 정렬 하겠습니다.)
# 순회하면서 끝나는 시간이 가장 짧은 회의를 선택하면 될것같습니다.

# 먼저 입력을 받겠습니다.
import sys
import heapq

input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
	heapq.heappush(h, list(map(int, input().split()))) # 이렇게 하면 정렬 시간을 최적화 할. 수 있습니다.

h.sort(key = lambda x : (x[1], x[0]))
# 끝나는 시간이 빠른 순으로 정렬합니다. 끝나는 시간이 같다면 시작시간이 빠른 순으로 정렬합니다.

answer = 0
prev_end = 0
for s, e in h:
	if prev_end <= s:
		answer += 1
		prev_end = e
		# print(s, e)
print(answer)

# answer  = 0
# end = 0
# start = 0
# while h:
# 	# 회의를 pop하면서 이전 끝나는 시간과 시작시간을 비교하겠습니다.
# 	s, e = heapq.heappop(h)
# 	if end <= s:

	# 이전 끝나는 시간과 시작시간을 비교하면서 시작시간이 같은 경우
	# 끝나는 시간이 가장 짧은 시간으로 선택하는 로직을 추가합니다.
