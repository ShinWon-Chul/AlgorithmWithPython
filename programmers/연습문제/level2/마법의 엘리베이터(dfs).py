res = 1e9

def dfs(arr, cnt):
    global res
    
    if len(arr) == 1:
        if arr[0] < 6:
            res = min(res, cnt + arr[0])
        else:
            res = min(res, cnt + (10-arr[0])+1)
        return
    
    num = arr[-1]
    
    # 빼는 경우
    dfs(arr[:-1], cnt + num)
    # 더하는 경우
    ns = int(''.join([str(n) for n in arr[:-1]])) + 1
    dfs([int(x) for x in str(ns)], cnt +(10-num))
    
    
def solution(storey):
    arr = [int(x) for x in str(storey)]
    dfs(arr, 0)
    
    return res