T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bugs = 0
    for i in range(N - M + 1):
        for j in range(len(arr[0]) - M + 1):
            sum_ = 0
            for k in range(i, i + M):
                sum_ += sum(arr[k][j : j + M])
                if bugs < sum_:
                	bugs = sum_
    print(f"#{t + 1} {bugs}")