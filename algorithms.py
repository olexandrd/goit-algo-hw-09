coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum: int, coins: list) -> dict:
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        if sum // coin > 0:
            result[coin] = sum // coin
        sum %= coin
    return result


def find_min_coins(sum: int, coins: list) -> dict:
    dp = {0: 0}

    for i in range(1, sum + 1):
        dp[i] = float("inf")

    for coin in coins:
        for i in range(coin, sum + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Reconstruct the coins dictionary
    result = {}
    for coin in reversed(coins):
        count = 0
        while sum >= coin and dp[sum] == dp[sum - coin] + 1:
            sum -= coin
            count += 1
        if count > 0:
            result[coin] = count

    return result


if __name__ == "__main__":
    print(find_coins_greedy(30417, coins))
    print(find_min_coins(30417, coins))
