def solution(lines):
    def time_processing(line):
        arr = []
        end_time = end_time_convert(line[0])
        interval_time = interval_convert(line[1])
        arr.append(end_time - interval_time + 1)
        arr.append(end_time)
        return arr

    def end_time_convert(end_time):
        new_time = end_time.split(':')
        second = new_time[2].split('.')
        milli_second = int(new_time[0])*3600000 + int(new_time[1])*60000 + int(second[0])*1000 + int(second[1])
        return milli_second

    def interval_convert(interval):
        interval = interval.replace('s', '').split('.')
        if len(interval) == 2:
            milli_interval = int(interval[0])*1000 + int(interval[1])
        else :
            milli_interval = int(interval[0])*1000
        return milli_interval
    
    result = 0
    lines = list(map(lambda x : time_processing(x.split(' ')[1:]), lines))
    lines.sort(key = lambda x : x[-1])
    for times in lines:
        count = 0
        start_time = times[1]
        end_time = start_time + 999
        for i in lines : 
            if start_time <= i[1] and end_time >= i[0]:
                count += 1
        result = max(result, count)
    return result