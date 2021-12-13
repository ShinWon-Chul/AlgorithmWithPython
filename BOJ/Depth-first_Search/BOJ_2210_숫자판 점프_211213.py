from sys import setrecursionlimit 
setrecursionlimit(10**9)
grid=[]
for _ in range(5):
    grid.append(list(map(int, input().split())))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
nums = []

def dfs(x, y, num):
    if len(num) == 6:
        if num not in nums:
            nums.append(num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <len(grid) and 0<= ny < len(grid[0]):
            dfs(nx, ny, num + str(grid[nx][ny])) # 중요!

for i in range(len(grid)):
    for j in range(len(grid[0])):
        dfs(i,j, str(grid[i][j]))
print(len(set(nums)))