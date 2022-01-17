'''주어진 두 범위의 값 사이에 있는 원소의 개수를 구하는 메서드'''
from bisect import bisect_left, bisect_right
 
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    result = right_index - left_index
    return result