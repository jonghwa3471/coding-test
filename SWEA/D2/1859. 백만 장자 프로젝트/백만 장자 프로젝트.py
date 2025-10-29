T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_ = 0
    profit = 0
    
    for price in reversed(arr):
        if max_ <= price:
            max_ = price
        else:
            profit += max_ - price
    print(f"#{t + 1} {profit}")