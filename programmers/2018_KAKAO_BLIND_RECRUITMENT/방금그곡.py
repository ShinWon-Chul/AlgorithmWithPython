import re

def solution(m, musicinfos):
    for idx, music in enumerate(musicinfos):
        music = str(idx)+','+ music
        musicinfos[idx] = music

    musicinfos = list(map(lambda x : x.split(','), musicinfos))
    result = []

    for music in musicinfos:
        start = music[1].split(':')
        end = music[2].split(':')
        time = (int(end[0])*60+int(end[1])) - (int(start[0])*60+int(start[1]))
        length = len(music[-1].replace('#', ''))
        hearing = ''
        count = 0
        index = 0

        if time < length:
            while count<time:
                if music[-1][index] == '#':
                    hearing += music[-1][index]
                    index += 1
                else:
                    hearing += music[-1][index]
                    index += 1
                    count += 1
        elif time >= length:
            hearing += music[-1] * int(time/length)
            mod = time % length
            while count<mod:
                if music[-1][index] == '#':
                    hearing += music[-1][index]
                    index += 1
                else:
                    hearing += music[-1][index]
                    index += 1
                    count += 1

        find = re.findall(m+'#*', hearing)
        if m in find:
            result.append([time, music[0], music[3]])
            
    if len(result) == 0:
        return "(None)"
    else:
        result.sort(key = lambda x : (-x[0], x[1]))
        return result[0][-1]