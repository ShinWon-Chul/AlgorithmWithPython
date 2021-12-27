import itertools

def solution(relation):
    total_num = len(relation)
    len_col = len(relation[0])
    cols = []
    result = []
    for i in range(len_col):
        cols.append(i)
    for i in range(1, len_col+1):
        for x in itertools.combinations(cols, i):
            temp_set = set()
            for r in relation:
                temp_list = []
                for j in x:
                    temp_list.append(r[j])
                temp_set.add(tuple(temp_list))

            if len(x) == 1:
                #유일성을 만족하는지 검사
                if len(temp_set) == total_num :
                    result.append(list(x))
            else:
                #유일성 을 만족하는지 검사
                if len(temp_set) == total_num :
                    #최소성을 만족하는지 검사
                    minimality = True
                    for nx in itertools.combinations(x, len(x)-1):
                        t_temp_set = set()
                        for r in relation:
                            t_temp_list = []
                            for j in nx:
                                t_temp_list.append(r[j])
                            t_temp_set.add(tuple(t_temp_list))
                        if len(t_temp_set) == total_num :
                            minimality = False
                    if minimality:
                        result.append(list(x))
    answer = len(result)
    return answer