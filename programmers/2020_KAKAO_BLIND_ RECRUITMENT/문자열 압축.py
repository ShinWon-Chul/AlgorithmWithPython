def solution(s):
    if len(s) == 1:
        return (1)

    result = int(10e9)
    for term in range(1, len(s)):
        char = []
        count_num = 1
        count_char = 1
        for i in range(0, len(s), term):
            if i+term > len(s)-1:
                char.append(s[i:])
                break
            char.append(s[i: i+term])    
        temp_c = char[0]
        total_length = 0
        for i in range(1, len(char)):
            if char[i] == temp_c:
                count_num += 1
            else:
                if count_num == 1:
                    length = len(char[i-1])
                else:
                    length = len(str(count_num)) + len(char[i-1])
                total_length += length
                count_num = 1
                temp_c = char[i]

            if i == len(char)-1:
                if count_num == 1:
                    length = len(char[i])
                else:
                    length = len(str(count_num)) + len(char[i-1])
                total_length += length
        result = min(result, total_length)
    
    return result