T = int(input())

for t in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        arr[i][0] = 1
        for j in range(1, i + 1):
            arr[i][j]  = arr[i - 1][j - 1] + arr[i - 1][j]
    print(f"#{t + 1}")
    for row in arr:
        row = [i for i in row if i != 0]
        print(*row)