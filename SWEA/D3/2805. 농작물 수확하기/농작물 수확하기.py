T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, str(input()))) for _ in range(N)]
    mid = N // 2
    result = 0
    for i in range(N):
        start = abs(mid - i)
        end = N - start
        result += sum(arr[i][start : end])
    print(f"#{t + 1} {result}")