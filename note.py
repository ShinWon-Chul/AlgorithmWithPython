'''주어진 두 범위의 값 사이에 있는 원소의 개수를 구하는 메서드'''
from bisect import bisect_left, bisect_right
 
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    result = right_index - left_index
    return result

'''2차원 리스트(행렬)응 90도 회전하는 메서드'''
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])
    
    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length-1-r] = a[r][c]
    
    return res

#사용 예시
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
print(rotate_a_matrix_by_90_degree(a))