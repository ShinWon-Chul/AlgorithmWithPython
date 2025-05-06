# # 1~6만큼 커지면서 너비 우선탐색으로 그래프 탐색을 진행하겠습니다.

# # 입력을 받겠습니다.
# from collections import deque
# N, M = list(map(int, input().split()))
# #뱀을 타는것은 해를 구하는데 사용할 의미가 없으므로 사용하지 않겠습니다.
# graph = {}
# for i in range(N + M):
#     s, e = list(map(int, input().split()))
#     # 뱀도 포함
#     graph[s] = e

# # print(graph)
# start = 1
# INF = int(1e9)
# # visited 배열을 선언하여 도달한 지점의 최소 값을 저장하겠습니다.
# visited = [INF] * (101)
# def bfs(start):
#     q = deque([[start, 0]])

#     while q:
#         loc, cnt = q.popleft()
#         for i in range(1, 7):
#             n_loc = loc+i
#             #만약 n_loc이 100보다 크다면 100에 기록합니다.
#             if n_loc > 100:
#                 visited[100] = min(visited[100], cnt+1)
#                 continue 
#             # 이전에 방문하면서 굴렸던 수가 현재 굴린 수보다 작다면 수행합니다.
#             # print(n_loc)
#             if visited[n_loc] > cnt+1:
#                 # visited[n_loc] = cnt+1
#                 # 만약 사다리가 있다면 다음 경로를 사다리 경로로 저장합니다.
#                 if n_loc in graph:
#                     n_loc = graph[n_loc]
#                     # 사다리를 타고 올라간 최종 거리에도 수를기록 합니다.
#                     # if visited[n_loc] > cnt+1:
#                     visited[n_loc] = cnt+1
#                     q.append([n_loc, cnt+1])

#                 else:
#                     visited[n_loc] = cnt+1
#                     q.append([n_loc, cnt+1])

# bfs(1)
# print(visited[100])


from collections import deque

N, M = map(int, input().split())
graph = {i: i for i in range(1, 101)}  # 초기에는 자기 자신

# 사다리 + 뱀 정보 업데이트
for _ in range(N + M):
    s, e = map(int, input().split())
    graph[s] = e

visited = [False] * 101

def bfs():
    q = deque()
    q.append((1, 0))  # (위치, 주사위 횟수)
    visited[1] = True

    while q:
        pos, cnt = q.popleft()

        if pos == 100:
            return cnt

        for dice in range(1, 7):
            next_pos = pos + dice
            if next_pos > 100:
                continue

            move_pos = graph[next_pos]  # 사다리/뱀 타기
            if not visited[move_pos]:
                visited[move_pos] = True
                q.append((move_pos, cnt + 1))

print(bfs())
