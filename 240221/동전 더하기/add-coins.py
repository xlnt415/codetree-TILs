n, k = map(int, input().split())

count = 0

coins = [
    int(input())
    for _ in range(n)
]


coins.sort(reverse = True)

for coin in coins:
    count += k // coin
    k %= coin


print(count)