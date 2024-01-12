from itertools import product

def solution(users, emoticons):
    answer = []
    discount_arr = [0.1, 0.2, 0.3, 0.4]
    num_emoticons = len(emoticons)
    final_count = 0
    final_price = 0
    for discounts in product(discount_arr, repeat=num_emoticons):
        current_count = 0
        current_price = 0
        
        for i, user in enumerate(users):
            rate = user[0] / 100
            price = user[1]

            x = 0#현재 유저가 구매할 가격

            for j, discount in enumerate(discounts):
                if discount >= rate:
                    x += emoticons[j] - emoticons[j] * discount
            if x >= price:
                current_count += 1
            else:
                current_price += x
        
        answer.append([current_count, int(current_price)])
    answer.sort(key = lambda x : (-x[0], -x[1]))
    return answer[0]