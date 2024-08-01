answer = 0

def dfs(score, selected, ability, j):
    global answer
    if j == len(ability[0]):
        answer = max(answer, score)
        return

    for i in range(len(ability)):
        if i not in selected:
            selected.add(i)
            dfs(score + ability[i][j], selected, ability, j + 1)
            selected.remove(i)

def solution(ability):
    global answer
    answer = 0
    for i in range(len(ability)):
        dfs(ability[i][0], {i}, ability, 1)
    return answer