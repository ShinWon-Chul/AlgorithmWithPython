from collections import deque

def solution(s):
    q = deque(s)
    new_s = []
    while True:
        count = 0
        while q:
            char = q.popleft()
            if len(new_s) > 0 and char == new_s[-1]:
                count += 1
                new_s.pop()
            else:
                new_s.append(char)
        q = deque(new_s)
        new_s = []
        if count == 0 and len(q)>0:
            return 0
        elif count == 0 and len(q)==0:
            return 1