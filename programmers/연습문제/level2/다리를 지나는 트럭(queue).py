from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = [[t, 1] for t in truck_weights]
    b = deque([truck_weights[0]])
    trucks = deque(truck_weights[1:])
    while b:
        # 다리에 올라가 있는 트럭의 무게 계산
        w = 0
        for truck, time in b:
            w += truck
            
        # 트럭이 더 올라갈 수 있다면
        if len(trucks)>0 and w+trucks[0][0] <= weight:
            answer += 1
            # 기존에 올라와있던 트럭들의 진행 시간을 1증가
            for i in range(len(b)):
                b[i][1] += 1
            # 새 트럭을 다리에 추가
            t = trucks.popleft()
            b.append(t)
            # 다리를 다 지난 트럭이있다면 다리에서 제거
            if b[0][1] > bridge_length:
                b.popleft()
                
        # 트럭을 더 올릴 수 없다면
        else:
            answer += 1
            # 기존에 올라와있던 트럭들의 진행 시간을 1증가
            for i in range(len(b)):
                b[i][1] += 1
            # 다리를 다 지난 트럭을 다리에서 제거
            if b[0][1] > bridge_length:
                b.popleft()
            # 다리에서 트럭이 나간후 올라갈 수 있는 트럭이 있는지 확인
            w = 0
            for truck, time in b:
                w += truck
            if len(trucks)>0 and w+trucks[0][0] <= weight:
                t = trucks.popleft()
                b.append(t)
        
    return answer