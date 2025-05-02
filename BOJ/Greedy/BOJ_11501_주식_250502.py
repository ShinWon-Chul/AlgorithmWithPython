# 상수 조건이 어떻게 되나요?
# 테스트 케이스 별로 N의 복잡도를 갖습니다. O(T*N)

#입력 T를 받겠습니다.
# T = int(input())


# # 다음가격이 동일하거나, 오르는 한 계속 산다. 
# # 주식을 가지고 있다면 마지막 날에는 반드시 판다.
# # 떨어지기 직전에 판다
# stock = []
# for _ in range(T):
#     benefit = 0
#     N = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(N):
#         # print('i', i)
#         if i+1 < N: 
#             if arr[i] <= arr[i+1]:
#                 stock.append(arr[i])
#             else:
#                 if stock:
#             # elif arr[i] > arr[i-1] and stock:
#                     for s in stock:
#                         benefit += arr[i] - s  
#                     stock = []              
#         if i == N -1 and stock:
#             for s in stock:
#                 benefit += arr[i] - s
#         # print('stock', stock)
#         # print('benefit', benefit)
#     stock = []
#     print(benefit)

T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_price = 0
    benefit = 0
    
    # 뒤에서부터 순회
    for i in range(N - 1, -1, -1):
        # 새로운 맥스 프라이스가 나올때까지 이전에 계속 사야 하니 계속 이익을 올리는 방식
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            benefit += max_price - prices[i]
    
    print(benefit)