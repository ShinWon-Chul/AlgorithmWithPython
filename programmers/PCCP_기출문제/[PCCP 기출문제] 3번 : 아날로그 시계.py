def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    starttime = h1* 3600 + m1 * 60 + s1
    endtime = h2 * 3600 + m2 * 60 + s2
    
    if starttime == 0 or starttime == 3600*12:
        answer += 1
    
    while starttime < endtime:
        changle = starttime/120 % 360
        cmangle = starttime/10 % 360
        csangle = starttime*6 % 360
        
        nhangle = 360 if (starttime+1)/120 % 360 == 0 else (starttime+1)/120 % 360
        nmangle = 360 if (starttime+1)/10 % 360 == 0 else (starttime+1)/10 % 360
        nsangle = 360 if (starttime+1)*6 % 360 == 0 else (starttime+1)*6 % 360
            
        # 시침
        if csangle < changle and nsangle >= nhangle:
            answer += 1
            # print('houre', answer)
        # 분침
        if csangle < cmangle and nsangle >= nmangle:
            # print('min', answer)
            answer += 1
        # 두번 더해지는것을 방지해야함
        if nhangle == nmangle == nsangle:
            answer -= 1
        
        starttime += 1
    return answer