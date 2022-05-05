def solution(dirs):
    load_dict = {'U':[0, 0.5], 'D':[0, -0.5], 'R':[0.5, 0], 'L':[-0.5, 0]}
    loc_dict = {'U':[0, 1], 'D':[0, -1], 'R':[1, 0], 'L':[-1, 0]}
    loc = [5, 5]
    visited = set()
    for dir in dirs:
        x, y = loc
        dx = x + loc_dict[dir][0]
        dy = y + loc_dict[dir][1]
        if 0 <= dx <= 10 and 0 <= dy <= 10:
            visited.add((x+load_dict[dir][0], y+load_dict[dir][1]))
            loc = [dx, dy]
    answer = len(visited)
    return answer