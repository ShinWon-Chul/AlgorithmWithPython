import heapq
import copy
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

char_location1 = [ list(map(lambda x : int(x) -1, input().split())) for _ in range(5)]
char_location2 = copy.deepcopy(char_location1)
char_location2[0], char_location2[-1] = char_location2[-1], char_location2[0]

def dijkstra_shortest_path(cost_matrix, start, goal):
    rows = len(cost_matrix)
    cols = len(cost_matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동

    # 초기화
    start_x, start_y = start
    goal_x, goal_y = goal
    min_cost = [[float('inf')] * cols for _ in range(rows)]
    min_cost[start_x][start_y] = cost_matrix[start_x][start_y]

    # 우선순위 큐
    priority_queue = [(0, start_x, start_y)]

    while priority_queue:
        current_cost, x, y = heapq.heappop(priority_queue)
        
        # 목표 지점에 도달하면 종료
        if (x, y) == (goal_x, goal_y):
            return current_cost
        
        # 인접한 노드 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = current_cost + cost_matrix[nx][ny] + cost_matrix[x][y]
                
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(priority_queue, (new_cost, nx, ny))
        
    
    return -1  # 목표 지점에 도달할 수 없는 경우


# # 최단 경로 비용 계산
result1 = 0
result2 = 0

for i in range(5):
    # 처음 시작인 경우 0, 0 부터 시작
    if i == 0:
        start = [0, 0]
        goal1, goal2 = char_location1[i], char_location2[i]
        if start == goal1:
            result1 += 0
        else:
            result1 += dijkstra_shortest_path(graph, start, goal1)
        if start == goal2:
            result2 += 0
        else:
            result2 += dijkstra_shortest_path(graph, start, goal2)
    else:

        start1, start2 = char_location1[i-1], char_location2[i-1]
        goal1, goal2 = char_location1[i], char_location2[i]
        if start1 == goal1:
            result1 += 0
        else:
            result1 += dijkstra_shortest_path(graph, start1, goal1)

        if start2 == goal2:
            result2 += 0
        else:
            result2 += dijkstra_shortest_path(graph, start2, goal2)

print(min(result1, result2))
