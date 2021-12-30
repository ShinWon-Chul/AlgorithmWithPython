def solution(msg):
    dictionary = {}
    for i in range(65, 91):
        dictionary[chr(i)] = i-64

    result = []
    index = 0
    next_word_index = 27
    while True:
        max_length = 0
        #가장 긴 문자열 찾기
        for i in range(index, len(msg)+1):
            temp_w = msg[index:i]
            if temp_w in dictionary:
                if len(temp_w) > max_length:
                    max_length = len(temp_w)
                    w = temp_w
                    next_index = i

        #가장 긴 문자열이 w라면 w의 인덱스를 리스트에 넣고
        result.append(dictionary[w])
        #만약 w뒤에 처리되지 않은 글자가 있다면
        if next_index != len(msg):
            #w+c에 해당하는 단어를 사전에 등록한다.
            wc = msg[index:next_index+1]
            dictionary[wc] = next_word_index
            next_word_index += 1
        else:
            break
        index = next_index
    return result