T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            bugs = 0
            for k in range(i, i + M):
                bugs += sum(arr[k][j : j + M])
            if bugs > result:
                result = bugs
    print(f"#{t + 1} {result}")