import copy

def dfs(start, tickets, answer, result):
    if len(tickets) == 0:
        result.append(answer)
        return
    
    for ticket in tickets:
        if ticket[0] == start:
            new_tickets = copy.deepcopy(tickets)
            new_tickets.remove(ticket)
            new_answer = copy.deepcopy(answer)
            new_answer.append(ticket[1])
            dfs(ticket[1], new_tickets, new_answer, result)
            
def solution(tickets):
    result = []
    answer = ["ICN"]
    dfs("ICN", tickets, answer, result)
    result.sort()
    return result[0]