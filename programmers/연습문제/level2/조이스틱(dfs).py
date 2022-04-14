min_cnt = int(1e9)

def solution(name):
    visited = [0 if i != 'A' else 1 for i in name]
    global min_cnt
    
    def dfs(visited, cnt, cur):
        global min_cnt
        if 0 not in visited:
            min_cnt = min(min_cnt, cnt)
            return
        
        if cnt > 20:
            return
        
        if cur < 0:
            cur = len(visited)-1
        elif cur > len(visited)-1:
            cur = 0

        if visited[cur] == 0:
            visited[cur] = 1
            dfs(visited, cnt+1, cur+1)
            dfs(visited, cnt+1, cur-1)
            visited[cur] = 0
        else:
            dfs(visited, cnt+1, cur+1)
            dfs(visited, cnt+1, cur-1)
            
    dfs(visited, 0, 0)

    count = 0
    for char in name:
        move_up_down = ord(char)-ord("A")
        if move_up_down <= 13 :
            count += move_up_down
        else:
            count += 26-move_up_down
    if min_cnt == 0:
        min_cnt=1
    return count+min_cnt-1