from itertools import product

def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    dictionary = []
    for n in range(5):
        for i in product(arr, repeat = n+1):
            dictionary.append(''.join(i))
    dictionary.sort()
    
    return dictionary.index(word)+1
