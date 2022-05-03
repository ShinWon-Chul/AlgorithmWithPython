zero = 0
one = 0
def dfs(arr):
    n = int(len(arr)/2)
    dx = [[0, 0], [0, n], [n, 0], [n, n]]
    global zero
    global one
    if len(arr) == 1:
        if arr[0] == 0:
            zero += 1
            return
        else:
            one += 1
            return
    summ = 0
    for row in arr:
        summ += sum(row)
    if summ == len(arr)**2:
        dfs([1])
    elif summ == 0:
        dfs([0])
    else:
        for i in range(4):
            new_arr = []
            x, y = dx[i]
            for j in range(n):
                new_arr.append(arr[x][y:y+n])
                x += 1
            if len(new_arr) == 1:
                new_arr = new_arr[0]
            dfs(new_arr)
            
def solution(arr):
    dfs(arr)
    return [zero, one]