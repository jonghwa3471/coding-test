T = int(input())

for t in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    r, c = 0, 0
    for i in range(1, (N * N) + 1):
        arr[r][c] = i
        nr, nc = r + dirs[d][0], c + dirs[d][1]
        if not (0 <= nr < N and 0 <= nc < N) or arr[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + dirs[d][0], c + dirs[d][1]
        r, c = nr, nc
    print(f"#{t + 1}")
    for row in arr:
        print(*row)