def solution(num, total):
    answer = []
    if total != 0:
        if num % 2 == 0:
            mid = int(total/num)
            front = [ mid-i for i in range(1, int(num/2))]
            back = [ mid+i for i in range(1, int(num/2)+1)]
            answer = front + [mid] + back

        else:
            mid = int(total/num)
            front = [ mid-i for i in range(1, int((num-1)/2)+1)]
            back = [ mid+i for i in range(1, int((num-1)/2)+1)]
            answer = front + [mid] + back
    else:
        if num % 2 == 0:
            mid = 0
            front = [ mid-i for i in range(1, int(num/2))]
            back = [ mid+i for i in range(1, int(num/2)+1)]
            answer = front + [mid] + back

        else:
            mid = 0
            front = [ mid-i for i in range(1, int((num-1)/2)+1)]
            back = [ mid+i for i in range(1, int((num-1)/2)+1)]
            answer = front + [mid] + back
            
    answer.sort()
    return answer