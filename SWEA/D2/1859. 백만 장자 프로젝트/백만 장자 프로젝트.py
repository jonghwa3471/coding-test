T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    profit = 0
    max_price = 0
    for price in arr[::-1]:
        if price > max_price:
            max_price = price
        profit += max_price - price
    print(f"#{t + 1} {profit}")