def solution(sticker):

    if len(sticker) == 1:
        return sticker[0]
    dp = [0 for _ in range(len(sticker))]  # use first sticker
    dp2 = [0 for _ in range(len(sticker))]  # unused first sticker

    dp[0] = sticker[0]
    dp[1] = sticker[0]

    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])

    value_1 = max(dp)

    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    value_2 = max(dp2)

    answer = max(value_1,value_2)
    return answer
