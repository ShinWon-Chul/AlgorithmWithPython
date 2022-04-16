from collections import deque

def solution(n, words):
    answer = []
    occur = [words[0]]
    number = 1
    count = 1
    q = deque(words[1:])
    while q:
        word = q.popleft()
        if word not in occur and word[0] == occur[-1][-1]:
            occur.append(word)
            number += 1
        else:
            number += 1
            return [number, count]
        if number == n:
            number = 0
            count += 1
            
    return [0, 0]