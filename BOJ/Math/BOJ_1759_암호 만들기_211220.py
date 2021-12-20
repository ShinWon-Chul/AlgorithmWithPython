import itertools

l, c = map(int, input().split())
chars = input().split()
vowel = []#사용 가능한 모음
consonant = [] #사용 가능한 자음
candidat_vowel = ['a', 'e', 'i', 'o', 'u']
for i in chars:
    if i in candidat_vowel:
        vowel.append(i)
    else:
        consonant.append(i)
total_result = []
for i in range(1, l-1):
    for vow in itertools.combinations(vowel, i):
        cv = list(vow)
        for con in itertools.combinations(consonant, l-i):
            cc = list(con)
            result = ''.join(sorted(cv+cc))
            total_result.append(result)
total_result.sort()
for password in total_result:
    print(password)