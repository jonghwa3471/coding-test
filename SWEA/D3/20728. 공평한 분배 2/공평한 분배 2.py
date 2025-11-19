T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = float("inf")
    for i in range(N - K + 1):
        if arr[i + K -1] - arr[i] < result:
            result = arr[i + K - 1] - arr[i]
    print(f"#{t + 1} {result}")