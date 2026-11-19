T = int(input())

for t in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = 0
    for i in range(N):
        mid = N // 2
        start = abs(mid - i)
        end = N - start
        result += sum(map(int, arr[i][start : end]))
    print(f"#{t + 1} {result}")