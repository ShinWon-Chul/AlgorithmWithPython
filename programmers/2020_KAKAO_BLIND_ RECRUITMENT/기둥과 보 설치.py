def solution(n, build_frame):
    result= []

    adx = [0, -1, +1, 0, 0, -1, -1, 1, 1]
    ady = [0, 0, 0, -1, 1, 1, -1, 1, -1]
    #보일 경우 조건
    def beam_condition(x, y):
        condition = False
        #아래 기둥이 있거나 양옆에 보가 있는경우
        if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
            condition = True
        return condition

    #기둥일 경우 조건
    def col_condition(x, y):
        condition = False
        #바닥이거나 보의 양 끝의 위거나 바로 아래 기둥이 있거나
        if y == 0 or [x-1, y, 1] in result or [x, y, 1] in result or [x, y-1, 0] in result:
            condition = True
        return condition

    for frame in build_frame:
        x, y, ob, ri = frame
        #설치할 경우
        if ri == 1:
            #기둥일 경우
            if ob == 0:
                if col_condition(x, y):
                    result.append([x, y, ob])
            #보일 경우
            elif ob == 1:
                if beam_condition(x, y):
                    result.append([x, y, ob])
        #제거일 경우
        else:
            #일단 제거하고 나서 인접 구조물이 안전한지 확인
            able = True
            result.remove([x, y, ob])
            #인접 구조물의 조건을 확인
            for i in range(9):
                if not able:
                    break
                ax = x + adx[i]
                ay = y + ady[i]
                for pframe in result:
                    #기존의 설치된 구조물
                    px, py, pob = pframe
                    if ax == px and ay == py:
                        #기존에 인접한 설치물이 기둥일 경우
                        if pob == 0:
                            able = able and col_condition(px, py)
                        #기존에 인접한 설치물이 보일 경우 
                        elif pob == 1:
                            able = able and beam_condition(px, py)
            #모든 구조물이 안전하다면 제거한 채로 다음단계 진행
            if able:
                continue
            #아니라면 무시하고 다음단계 진행
            else:
                result.append([x, y, ob])
    result.sort(key = lambda x : (x[0], x[1], x[2]))
    return result