T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    arr = []
    dp = [0] * (L + 1)
    for n in range(N):
        T, K = map(int, input().split())
        arr.append((T, K))
    for taste, cal in arr:
        for c in range(L, cal - 1, -1):
            dp[c] = max(dp[c], dp[c - cal] + taste)
    result = max(dp)
    print(f"#{t + 1} {result}")