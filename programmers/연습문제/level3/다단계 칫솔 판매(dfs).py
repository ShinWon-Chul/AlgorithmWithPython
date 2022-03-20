from collections import defaultdict

def solution(enroll, referral, seller, amount):
    
    answer = []
    revenue = defaultdict(lambda : 0)
    graph = defaultdict()

    for ref, en in zip(referral, enroll):
        graph[en] = ref

    def dfs(start, money):
        if start == '-':
            return

        dist_money = money // 10

        if dist_money == 0:
            revenue[start] += money
            return
        else :
            my_money = money - dist_money
            revenue[start] += my_money
            dfs(graph[start], dist_money)

    for sell, amt in zip(seller, amount):
        dfs(sell, amt*100)

    for person in enroll:
        answer.append(revenue[person])
        
    return answer