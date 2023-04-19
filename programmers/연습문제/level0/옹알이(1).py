answer = 0

def dfs(b, word):
    global answer
    # 종료 조건
    if b[:3] not in word and b[:2] not in word and len(b) !=0:
        return
    elif len(b) == 0:
        answer += 1
        return
    # 탐색 조건
    elif b[:2] in word:
        dfs(b[2:], word)
    elif b[:3] in word:
        dfs(b[3:], word)

def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        dfs(b, word)
    return answer