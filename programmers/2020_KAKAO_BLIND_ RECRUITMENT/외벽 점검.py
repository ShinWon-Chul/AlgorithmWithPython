import itertools

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    count = 0
    for idx in range(length):
        for friends in itertools.permutations(dist, len(dist)):
            count += 1
            position = weak[idx] + friends[count -1]
            while position < weak[idx+length-1]:
                if count == len(friends):
                    count += 1
                    break
                else:
                    for i in range(len(weak[idx : idx+length])):
                        if weak[idx : idx+length][i] > position:
                            position = weak[idx : idx+length][i]
                            break
                    count += 1
                    position += friends[count-1]
            answer = min(answer, count)
            count = 0
    if answer == len(dist)+1 :
        return -1
    else:
        return answer