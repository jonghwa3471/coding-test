T = int(input())

for t in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        arr[i][0] = 1
        for j in range(1, i + 1):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    print(f"#{t + 1}")
    for row in arr:
        result = [item for item in row if item != 0]
        print(*result)