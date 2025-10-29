T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    result = 0
    max_price = 0
    for price in reversed(arr):
        if max_price <= price:
            max_price = price
       	else:
            result += max_price - price
    print(f"#{i + 1} {result}")