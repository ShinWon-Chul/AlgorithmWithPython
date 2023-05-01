def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        dc = pc = cap

        while deliveries and deliveries[-1] == 0 :
            deliveries.pop()

        while pickups and pickups[-1] == 0:
            pickups.pop()

        answer += max(len(deliveries), len(pickups))*2
        
        # 배달
        while deliveries:
            if deliveries[-1] <= dc:
                dc -= deliveries.pop()
            else:
                deliveries[-1] -= dc
                break
            
        # 수거
        while pickups:
            if pickups[-1] <= pc:
                pc -= pickups.pop()
            else:
                pickups[-1] -= pc 
                break

    return answer