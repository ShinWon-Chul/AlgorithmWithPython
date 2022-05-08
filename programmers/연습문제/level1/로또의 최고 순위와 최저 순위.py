def solution(lottos, win_nums):
    answer = []
    correct = 0
    zero = 0
    dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for num in lottos:
        if num in win_nums:
            correct += 1
        elif num == 0:
            zero += 1
    answer.append(dict[correct + zero])
    answer.append(dict[correct])
    return answer