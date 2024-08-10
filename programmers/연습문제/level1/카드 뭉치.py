from collections import deque

def solution(cards1, cards2, goal):
    
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    while goal:
        if cards1 and goal[0] == cards1[0]:
            goal.popleft()
            cards1.popleft()
        elif cards2 and goal[0] == cards2[0]:
            goal.popleft()
            cards2.popleft()
        else:
            break
    if goal:
        return 'No'
    else:
        return 'Yes'