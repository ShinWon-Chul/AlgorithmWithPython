def solution(queries):
    answer = []
    beans = ['RR', 'Rr', 'Rr', 'rr']
    for n, p in queries:
        if n == 1:
            answer.append('Rr')
            continue
        if n == 2:
            answer.append(beans[p-1])
            continue
        else:
            parents = []
            
            for i in range(n-2):
                parent = int((p-1)/4)
                child = p % 4

                if child == 0:
                    child = 4

                parents.append(child)
                p = parent+1
                if i == n-3:
                    parents.append(p)

            # 부모부터 내려오면서 찾아주는 과정
            for i in range(len(parents)-1, -1, -1):
                # print(i)
                if parents[i] == 1:
                    answer.append("RR")
                    break
                elif parents[i] == 4:
                    answer.append("rr")
                    break
            else:
                answer.append(beans[parents[i]-1])
    return answer