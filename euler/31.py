target = 200
coins = (1, 2, 5, 10, 20, 50, 100, 200)
ways = [0] * (target + 1)
ways[0] = 1

for coin in coins:
    for j in range(coin, target + 1):
        ways[j] += ways[j - coin]

print("Solution : "+ str(ways[-1]))