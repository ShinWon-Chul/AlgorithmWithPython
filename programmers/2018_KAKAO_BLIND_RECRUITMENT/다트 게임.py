import re

def solution(dartResult):
    options = re.split('\d+', dartResult)[1:]
    score = list(map(int, re.split('\D+', dartResult)[:-1]))
    total_score = []
    for i in range(3):
        option = options[i]
        #S D T만 있는 경우
        if len(option) == 1:
            if option == 'S':
                total_score.append(score[i])
            elif option == 'D':
                total_score.append(score[i]**2)
            else:
                total_score.append(score[i]**3)
        #* 과 #이 있는 경우
        else:
            if option[0] == 'S':
                if option[1] == '*':
                    if i > 0 :
                        total_score[i-1] *= 2
                    total_score.append(score[i]*2)
                else:
                    total_score.append(score[i]* -1)

            elif option[0] == 'D':
                if option[1] == '*':
                    if i > 0:
                        total_score[i-1] *= 2
                    total_score.append((score[i]**2)*2)
                else:
                    total_score.append((score[i]**2)* -1)

            else :
                if option[1] == '*':
                    if i > 0:
                        total_score[i-1] *= 2
                    total_score.append((score[i]**3)*2)
                else:
                    total_score.append((score[i]**3)* -1)
    return sum(total_score)