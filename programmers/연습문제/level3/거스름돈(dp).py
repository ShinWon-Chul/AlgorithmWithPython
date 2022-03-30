def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    for currency in money:
        for i in range(currency, n+1):
            dp[i] += dp[i-currency]
    return dp[-1]%1000000007