T = int(input())

for t in range(T):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    deg90 = [[""] * N for _ in range(N)]
    deg180 = [[""] * N for _ in range(N)]
    deg270 = [[""] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            deg90[i][j] = arr[N - 1 - j][i]
            deg180[i][j] = arr[N - 1 - i][N - 1 - j]
            deg270[i][j] = arr[j][N - 1 - i]
    print(f"#{t + 1}")
    for i in range(N):
        deg90_row = "".join(deg90[i])
        deg180_row = "".join(deg180[i])
        deg270_row = "".join(deg270[i])
        print(deg90_row, deg180_row, deg270_row)