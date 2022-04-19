from collections import deque
import copy

def solution(s):
    answer = 0
    q = deque(s)
    close = [')', ']', '}']
    open = ['(', '[', '{']
    
    for _ in range(len(s)):
        c = q.popleft()
        q.append(c)
        new_q = copy.deepcopy(q)
        arr = []
        while new_q:
            # 올바른 괄호 조건에 맞는지 판별
            if new_q[0] in close:
                if len(arr) == 0:
                    break
                if arr[-1] == open[close.index(new_q[0])]:
                    new_q.popleft()
                    arr.pop()
                else:
                    break
            elif new_q[0] in open:
                char = new_q.popleft()
                arr.append(char)
        # 큐와 스텍이 모두 비었다면 올바른 괄호이므로 answer 1증가     
        if len(arr) == 0 and len(new_q) == 0:
            answer += 1
            
    return answer