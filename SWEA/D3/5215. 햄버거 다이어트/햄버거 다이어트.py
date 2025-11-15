T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    result = [0] * (L + 1)
    arr = [list(map(int, input().split())) for _ in range(N)]
    for score, cal in arr:
        for i in range(L, cal - 1, -1):
            result[i] = max(result[i], result[i - cal] + score)
    max_ = max(result)
    print(f"#{t + 1} {max_}")