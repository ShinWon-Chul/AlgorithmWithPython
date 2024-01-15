from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    max_count = len(q1) * 4 # 큐가 한번 뒤바뀌었다가 다시 원래대로 돌아오는 횟수
    
    if (sum_q1 + sum_q2) %2 !=0: # 2로 나누어떨어지지 않는다면 두 큐의 합이 같을 수 없음 (시간 개선)
        return -1
    
    while True:
        if sum_q1 > sum_q2:
            n = q1.popleft()
            q2.append(n)
            sum_q1 -= n
            sum_q2 += n
            answer += 1
            
        elif sum_q1 < sum_q2:
            n = q2.popleft()
            q1.append(n)
            sum_q1 += n
            sum_q2 -= n
            answer += 1
            
        if sum_q1 == sum_q2:
            break
            
        if answer > max_count:
            answer = -1
            break
            
    return answer