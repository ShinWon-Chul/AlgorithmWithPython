#시간을 초로 바꾸는 메서드
def time_to_second(time):
    s_time = time.split(':')
    second = int(s_time[0])*3600 + int(s_time[1])*60 + int(s_time[2])
    return second

#초를 시간으로 바꾸는 메서드
def second_to_time(second):
    time_ = []   
    time_.append(str(int(second/3600))) 
    second = second%3600
    time_.append(str(int(second/60)))
    time_.append(str(second%60))
    time_ = list(map(lambda x : '0'+x if len(x) == 1 else x, time_))
    time_ = ':'.join(time_)
    return time_    

def solution(play_time, adv_time, logs):
    #동영상 시간과 광고시간을 초로 변경
    play_time = time_to_second(play_time)
    adv_time = time_to_second(adv_time)

    #누적합을 구하기 위한 dp 테이블 정의
    time = [0] * (play_time+1)
    length = len(time)
    n = len(logs)
    
    #dp테이블에 시청자 증가 감소수 표시
    for i in range(n):
        interval = list(map(lambda x : time_to_second(x), logs[i].split('-')))
        time[interval[0]] += 1
        if interval[1]<length:
            time[interval[1]] += -1
    
    #현 시점에서 시청자 수 기록
    for i in range(1, length):
        time[i] = time[i-1] + time[i]
    
    #누적합을 통해 현 시점에서 누적 시청 시간 기록
    prefix_sum = [0]
    sum_value = 0
    for i in range(length):
        sum_value += time[i]
        prefix_sum.append(sum_value)
    

    result = 0 #누적 시청시간 최대값을 기록하기 위한 변수
    answer = [] #최대 누적 시청시간과 광고 시작 시점을 기록할 리스트
    for i in range(adv_time, length+1):
        seeing_time = prefix_sum[i] - prefix_sum[i-adv_time]
        
        #현 시점에서의 누적 시청 시간이 전 시점에서 누적 시청시간 보다 크다면
        if result <= seeing_time:
            #최대 누적 시청시간 기록
            result = seeing_time
            answer.append([result,i-adv_time])
    #누적 시청 시간이 큰 순서대로, 시작 시간이 먼저인 순서대로 정렬
    answer.sort(key = lambda x : (-x[0], x[1]))
    
    #시작시간을 초에서 시간으로 변환하여 리턴
    return  second_to_time(answer[0][1])