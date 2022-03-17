def solution(n):
    arr = ''
    while True:
        if n < 3:
            if n == 0:
                break
            else:
                arr = str(n) + arr
                break
        mode = n%3 
        if mode == 0:
            arr = str(4)+arr
            n = int(n/3) - 1
        else:
            arr = str(mode) + arr 
            n = int(n/3)
    return arr