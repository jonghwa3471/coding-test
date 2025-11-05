T = int(input())

for t in range(T):
    N = int(input())
    arr = [0, 0, 0, 0, 0]
    division = [2, 3, 5, 7, 11]
    for i in range(5):
        while N % division[i] == 0:
            N //= division[i]
            arr[i] += 1
    print(f"#{t + 1}", *arr)