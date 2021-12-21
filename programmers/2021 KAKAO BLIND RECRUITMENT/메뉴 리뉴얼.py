import itertools

def solution(orders, course):
    answer = []

    all_course = [[] for _ in range(course[-1]+1)]
    course_list = [[] for _ in range(course[-1]+1)]
    num_of_course = [[] for _ in range(course[-1]+1)]

    for num_food in course:
        for order in orders:
            all_course[num_food] = all_course[num_food]+list(itertools.combinations(list(sorted(order)), num_food))

    #각 음식마다 갯수를 카운트 하여 course는 course_list에 append 갯수는 num_of_curese에 append
    for num_food in course:
        for ic, c in enumerate(all_course[num_food]):
            # 만약에 카운트 된적이 없다면
            if c not in course_list[num_food]:
                # 이전것은 카운트 되었으므로 제외하고 그 수를 num_of_course에 저장
    #             print(all_course[num_food][ic:].count(c))
                num_of_course[num_food].append(all_course[num_food][ic:].count(c))
                # course_list에 c 저장
                course_list[num_food].append(c)

    maximum_nums = [[] for _ in range(course[-1]+1)]
    for i, v in enumerate(num_of_course):
        if len(v) != 0:
            maximum_nums[i].append(max(v))
    maximum_nums

    for num_food, v in enumerate(maximum_nums):
        if len(v) != 0 and v[0]>1:
            for i, course in enumerate(course_list[num_food]):
                if num_of_course[num_food][i] == v[0]:
                    answer.append(''.join(course_list[num_food][i]))
    answer.sort()
    return answer