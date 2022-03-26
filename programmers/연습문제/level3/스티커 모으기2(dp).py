def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    result = 0
    n = len(sticker)
    sticker *= 2
    for start in range(2):
        end = start + n
        dp = [0] * (n+3)
        new_sticker = sticker[start:end-1]
        new_sticker = [0, 0, 0] + new_sticker

        for i in range(3, n+2):
            dp[i] = max(new_sticker[i]+dp[i-2], new_sticker[i]+dp[i-3])
        max_value = max(dp)
        if max_value > result:
            result = max_value     

    return result