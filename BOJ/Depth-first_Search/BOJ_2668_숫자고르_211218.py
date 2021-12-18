n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
graph = [[] for _ in range(n+1)]
for i in range(n):
    graph[nums[i]].append(i+1)
result = []
def dfs(start):
    visited.append(start)
    for node in graph[start]:
        if node in visited:
            result.append(start)
        else:
            visited.append(node)
            dfs(node)
            
for start in range(1, n+1):
    visited = []
    dfs(start)
result = list(set(result))
result.sort()
print(len(result))
for num in result:
    print(num)