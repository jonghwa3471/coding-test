T = int(input())

for t in range(T):
    N = int(input())
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    pos = [0] * (N * N + 1)
    for r in range(N):
        for c in range(N):
            pos[arr[r][c]] = (r, c)
            
    dp = [0] * (N * N + 1)
    dp[N * N] = 1
    
    for num in range(N * N - 1, 0, -1):
        r, c = pos[num]
        nr, nc = pos[num + 1]
        if abs(r - nr) + abs(c - nc) == 1:
            dp[num] = dp[num + 1] + 1
        else:
            dp[num] = 1
    max_len = max(dp)
    start = dp.index(max_len)
    print(f"#{t + 1} {start} {max_len}")