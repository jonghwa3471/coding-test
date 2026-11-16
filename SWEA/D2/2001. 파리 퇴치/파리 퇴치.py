T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            grid = 0
            for k in range(i, i + M):
                row = sum(arr[k][j:j+M])
                grid += row
            if grid > result:
                result = grid
    print(f"#{t + 1} {result}")