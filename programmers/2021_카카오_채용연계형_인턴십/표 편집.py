from collections import deque

def solution(n, k, cmd):
    linked_list = {}
    for i in range(n):
        if i == 0:
            node = { 'data' : i, 'prev' : 'head', 'next' : i + 1 }
        elif i == n-1:
            node = { 'data' : i, 'prev' : i - 1, 'next' : 'tail'}
        else:
            node = { 'data' : i, 'prev' : i - 1, 'next' : i + 1}
        linked_list[i] = node
    result = ['O'] * n
    curr = k
    stack = []
    for c in cmd:
        if len(c) >= 3:
            c = c.split()
            if c[0] == 'D':
                for _ in range(int(c[1])):
                    next_node = linked_list[curr]['next']
                    curr = linked_list[next_node]['data']
            elif c[0] == 'U':
                for _ in range(int(c[1])):
                    prev_node = linked_list[curr]['prev']
                    curr = linked_list[prev_node]['data']
        else:
            
            if c == 'C':
                if linked_list[curr]['next'] == 'tail':
                    result[linked_list[curr]['data']] = 'X'
                    stack.append(linked_list[curr])
                    linked_list[linked_list[curr]['prev']]['next'] = 'tail'
                    curr = linked_list[linked_list[curr]['prev']]['data']
                elif linked_list[curr]['prev'] == 'head':
                    result[linked_list[curr]['data']] = 'X'
                    stack.append(linked_list[curr])
                    linked_list[linked_list[curr]['next']]['prev'] = 'head'
                    curr = linked_list[linked_list[curr]['next']]['data']
                else :
                    result[linked_list[curr]['data']] = 'X'
                    stack.append(linked_list[curr])
                    linked_list[linked_list[curr]['next']]['prev'] = linked_list[curr]['prev']
                    linked_list[linked_list[curr]['prev']]['next'] = linked_list[curr]['next']
                    curr = linked_list[linked_list[curr]['next']]['data']
            
            elif c == 'Z':
                node = stack.pop()
                if node['next'] == 'tail':
                    linked_list[node['prev']]['next'] = node['data']
                    result[node['data']] = 'O'
                elif node['prev'] == 'head':
                    linked_list[node['next']]['prev'] = node['data']
                    result[node['data']] = 'O'
                else:
                    linked_list[node['prev']]['next'] = node['data']
                    linked_list[node['next']]['prev'] = node['data']
                    result[node['data']] = 'O'

    return ''.join(result)