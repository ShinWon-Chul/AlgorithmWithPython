def solution(distance, rocks, n):
    rocks += [0, distance]
    rocks.sort()
    n_rocks = len(rocks)
    start = 1
    end = distance
    
    while start<=end:
        mid = int((start+end)/2)
        
        count = 0
        remain = 0
        dist = 0
        for i in range(1, n_rocks):
            dist = abs(rocks[remain]-rocks[i])
            if dist < mid:
                if i == n_rocks-1:
                    count += 1
                else:
                    count += 1
            else:
                dist = 0
                remain = i
                
        if count > n:
            end = mid - 1
            
        else:
            start = mid + 1
            result = mid
    
    return result