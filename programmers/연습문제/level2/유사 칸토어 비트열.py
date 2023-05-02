def solution(n, l, r):
    answer = 0

    # n 에 대한 칸토어 비트열 만들기
    dict1 = { '1' : '11011',
              '0' : '00000'}
    arr = '11011'
    if n == 1:
        arr = '11011'
    else:
        for _ in range(n-1):
            temp_arr = ''
            for i in range(0, len(arr), int(len(arr)/5)):
                temp_arr += dict1[arr[i : i+int(len(arr)/5)]]

            dict1[arr] = temp_arr
            new_z = temp_arr[int(len(temp_arr)/5) * 2:int(len(temp_arr)/5) * 3]
            dict1[new_z] = new_z*5
            arr = temp_arr

    new_arr = [ int(i) for i in arr[l-1 : r]]

    return sum(new_arr)