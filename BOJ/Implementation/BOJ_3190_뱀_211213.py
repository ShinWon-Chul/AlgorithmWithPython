n = int(input())
k = int(input())
grid = [[0]*(n+1) for _ in range(n+1)]
apples = []
for _ in range(k):
    x, y = list(map(int, input().split()))
    grid[x][y] = 1
l = int(input())
directions = {}
for _ in range(l):
    k, v = list(input().split())
    directions[int(k)] = v

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
head = [1,1]
tail = [1,1]
grid[1][1] = 2
for x, y in apples:
    grid[x][y] = 1

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0
    return direction

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

count = 0
moved = []
while True:
    if count in directions.keys():
        if directions[count] == 'D':
            turn_right()
        else:
            turn_left()
    count += 1
    x, y = head
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx <= n and 1 <= ny <= n:
        if grid[nx][ny] == 1:
            grid[nx][ny] = 2
            head = [nx,ny]
            moved.append(head)
        elif grid[nx][ny] == 0:
            grid[nx][ny] = 2
            head = [nx,ny]
            grid[tail[0]][tail[1]] = 0
            moved.append(head)
            tail = moved[0]
            moved = moved[1:]
        else:
            break
    else:
        break
print(count)