T = int(input())

for t in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    total = sum(scores)
    dp = [False] * (total + 1)
    dp[0] = True
    for s in scores:
        for i in range(total, -1, -1):
            if dp[i]:
                dp[i + s] = True
    result = sum(dp)
    print(f"#{t + 1} {result}")