def solution(phone_book):
    answer = True
    prefix_dict = {}
    phone_book.sort()
    for p in phone_book:
        prefix_dict[p] = 0
    for phone in phone_book:
        for i in range(len(phone)):
            if phone[:i] in prefix_dict:
                return False
    return True