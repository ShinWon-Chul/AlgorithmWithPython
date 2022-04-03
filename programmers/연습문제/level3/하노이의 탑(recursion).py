def solution(n):
    arr = []
    def move(start, to, arr):
        arr.append([start, to])
        
    def hanoi(N, start, to, via, arr):
        if N == 1:
            move(start, to, arr)
        else:
            hanoi(N-1, start, via, to, arr)
            move(start, to, arr)
            hanoi(N-1, via, to, start, arr)
            
    hanoi(n, 1, 3, 2, arr)
    return arr