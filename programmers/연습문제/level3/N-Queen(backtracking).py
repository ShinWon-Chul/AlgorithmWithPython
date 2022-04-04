answer = 0
def dfs(arr, count, n, cols):
    global answer

    if count == n:
        answer += 1
        return

    x = count
    for y in cols:
        if y not in arr:
            for old_x, old_y in enumerate(arr):
                if abs(old_x-x) == abs(old_y-y):
                    break
            else:
                arr.append(y)
                dfs(arr, count+1, n, cols)
                arr.remove(y)
                
def solution(n):
    arr = []
    cols = [i for i in range(n)]
    for col in range(n):
        arr.append(col)
        dfs(arr, 1, n, cols)
        arr.pop()    
    return answer