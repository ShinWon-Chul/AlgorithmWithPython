def solution(n):
    answer = []
    arr = []
    for i in range(1, n+1):
        arr.append([0]*i)
    x = -1
    y = 0
    flag = 0
    num = 1
    while n > 0:
        if flag % 3 == 0:
            for i in range(n):
                x += 1
                arr[x][y]= num
                num+=1
        elif flag % 3 == 1:
            for i in range(n):
                y += 1
                arr[x][y] = num
                num+=1
        else:
            for i in range(n):
                x -= 1
                y -= 1
                arr[x][y] = num
                num+=1
        flag += 1
        n -= 1
    for row in arr:
        for value in row:
            answer.append(value)
    return answer