def solution(a, b):
    dictionary = {0:0, 1 : 31, 2:60, 3:91, 4:121, 5:152, 6:182, 7:213, 8:244, 9:274, 10:305, 11:335, 12:366}
    day = dictionary[a-1]+b
    Day_of_the_week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    answer = Day_of_the_week[day%7-1]
    return answer