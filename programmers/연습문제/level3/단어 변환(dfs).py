answer = int(1e9)
def dfs(begin, count, words, target):
    global answer
    if begin == target:
        answer = min(count, answer)
        return

    for word in words:
        same_char = 0
        for idx, char in enumerate(word):
            if char == begin[idx]:
                same_char += 1

        if same_char == len(begin) - 1:
            words.remove(word)
            dfs(word, count + 1, words, target)
            words.append(word)
def solution(begin, target, words):
    count = 0   
    if target in words:
        dfs(begin, count, words, target)
        return answer
    else:
        return 0