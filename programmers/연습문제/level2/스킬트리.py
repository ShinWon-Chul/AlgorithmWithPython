def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        temp = ''
        for s in skill_tree:
            if s in skill:
                temp += s
        length = len(temp)
        if temp[:length] == skill[:length]:
            answer += 1
    return answer