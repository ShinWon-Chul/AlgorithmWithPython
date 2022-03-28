import math

def solution(n, stations, w):
    w_range = w*2+1
    count = 0
    start = 1
    for s in stations:
        
        end = s - w
        if end < 2:
            start = s + w + 1
        else:
            house = end-start
            count += math.ceil(house/w_range)
            start = s + w + 1
            
    if s + w  < n:
        start = s + w
        house = n -start
        count += math.ceil(house/w_range)

    return count