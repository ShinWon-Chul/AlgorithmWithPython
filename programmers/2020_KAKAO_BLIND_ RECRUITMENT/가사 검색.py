from collections import defaultdict
from bisect import bisect_left, bisect_right
 
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    result = right_index - left_index
    return result

def solution(words, queries):
    new_words = defaultdict(list)
    reverse_new_words = defaultdict(list)
    for word in words:
        new_words[len(word)].append(word)
    for key in new_words.keys():
        new_words[key].sort()
    for word in words:
        reverse_new_words[len(word)].append(word[::-1])
    for key in reverse_new_words.keys():
        reverse_new_words[key].sort()
    result = []
    for q in queries:
        count = 0
        length = len(q)
        if q[0] == '?':
            res = count_by_range(reverse_new_words[length], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        else:
            res = count_by_range(new_words[length], q.replace('?', 'a'), q.replace('?', 'z'))
        result.append(res)
    return result