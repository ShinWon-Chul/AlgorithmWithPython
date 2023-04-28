def solution(wallpaper):
    answer = []
    x1, y1, x2, y2 = 1e9, 1e9, 0, 0
    
    for y, row in enumerate(wallpaper):
        for x, col in enumerate(row):
            if col == '#':
                x1 = min(x1, x)
                y1 = min(y1, y)
                x2 = max(x2, x)
                y2 = max(y2, y)
    answer = [y1, x1, y2+1, x2+1]
    return answer