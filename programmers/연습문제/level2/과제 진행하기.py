def convertor(time):
    new_time = list(map(int, time.split(':')))
    new_time = new_time[0]*60 + new_time[1]
    return new_time
    
def solution(plans):
    plans = [ [plan[0], convertor(plan[1]), int(plan[2])] for plan in plans]

    plans.sort(key = lambda x : x[1])
    answer = []
    stop = []
    time = plans[0][1]
    while plans:
        # 뒤에 과제가 더 남아 있다면
        if len(plans) > 1:
            c = plans[0]
            n = plans[1]
            # 현재 과제를 끝낼 수 있는경우
            if n[1] - c[1] >= c[2]:
                time += c[2]
                answer.append(plans.pop(0)[0])
                # 만약 stop 해놓은 과제가 있다면?
                if len(stop) > 0:
                    while time < plans[0][1] and len(stop) > 0:
                        # 스탑해놓은 과제를 끝낼 수 있는 경우
                        if time + stop[-1][2] <= plans[0][1]:
                            s = stop.pop(-1)
                            time += s[2]
                            answer.append(s[0])
                        
                        # 그렇지 못한 경우
                        else:
                            stop[-1][2] -= plans[0][1] - time
                            time = plans[0][1]
                            break

            # 현재 과제를 못끝내고 다음 과제를 시작해야 하는경우
            else:
                c = plans.pop(0)
                c[2] -= n[1] - c[1]
                time = n[1]
                stop.append(c)
                
        # 마지막 과제라면
        else:
            # 마지막 과제를 끝내고
            answer.append(plans.pop(0)[0])
            # 미뤄두었던 과제를 차례로 끝내면 된다.
            while stop:
                answer.append(stop.pop(-1)[0])
            
    return answer