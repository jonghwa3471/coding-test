T = int(input())

for t in range(T):
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money = int(input())
    for index, value in enumerate(arr):
        arr[index] = money // value
        money %= value
    print(f"#{t + 1}")
    print(*arr)